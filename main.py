from app.email_sender.senderEmail import sender_email
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'A API ESTÁ NO AR'

# @app.route('/authentication')
# def authentication():
#   usuario = request.args.get('usuario')
#   senha = request.args.get('senha')
#   authentication(usuario, senha)
#   if True:
#     return 'Logado com sucesso!'
#   else:
#     return 'Login ou senha iválidos!'

@app.route('/send-email-list')
def senderemail():
  # list_adrs = request.args.get('list_adrs')
  # sender_email(list_adrs)
  sender_email()
  if True:
    return 'Email enviado com sucesso!'
  else:
    return 'Email não enviado!'
  


if __name__ == '__main__':
    app.run()