from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

from flask import Flask, render_template, request

# ---Parte de Bot----

upmhBotsito = ChatBot('UPM_V2')

words = ['¿Donde esta la enfermeria?', 'La enfermaria se encuentra en el edificion LT1',
        '¿Con quien puedo consultar sobre becas?', 'Puedes consultar sobre Becas con la Lic. Elisa Acuña',
        'Necesito ayuda emocional', 'Puedes acudir con tu orientador. Tambien puedes agendar una cita con el psicologo del instituto',
        '¿Que becas de movilidad hay?', 'Solo hay una beca de movilidad esta dirigida a estudiantes de escasos recursos, que no cuenten con ningún otro apoyo en efectivo o en especie y que colaboren en un servicio administrativo u operativo dentro de la Universidad.']

trainer = ListTrainer(upmhBotsito)
trainer.train(words)


# ---PARTE DE LA PAGINA WEB---
app = Flask(__name__)

#Todo here

@app.route("/index", methods=["GET", "POST"])
def index():

    userMessage = request.form.get("usermessage")
    #Bot
    response = upmhBotsito.get_response(userMessage)
    #BotFin

    
    #Diccionario----
    data = {
        'titulo': 'UPMH',
        'response': response
    }
    #DiccionarioFIN---

    return render_template('index.html', data=data)

#Fin here

if __name__ == '__main__':
    app.run(debug=True)