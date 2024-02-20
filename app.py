from flask import Flask, render_template, request
import openai

app = Flask(__name__)
openai.api_key = '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'

conversations = []

## rutas

# ruta uso api
@app.route('/', methods=['GET', 'POST'])
def openai_api():
    if request.method == 'GET':
        return render_template('index.html', chat=conversations)
    
    if request.method == 'POST':
        question = request.form.get('question')

        if question:
            response = openai.ChatCompletion.create(
                model = 'gpt-3.5-turbo-0125',
                messages= [
                    {"role": "system", "content": ""},
                    {"role": "user", "content" : question}
                ],
                temperature = 0.5,
                max_tokens = 150,
                top_p = 1,
                frequency_penalty = 0,
                presence_penalty = 0.6
            )

            answer = 'AI: ' + str(response.choices[0].message.content)
            question = 'Yo: ' + question

            conversations.append(question)
            conversations.append(answer)

        return render_template('index.html', chat = conversations)

# ruta nosotros
@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

# bloque de prueba
if __name__ == '__main__':
    app.run(debug=True)