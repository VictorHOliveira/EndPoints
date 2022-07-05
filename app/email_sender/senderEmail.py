import smtplib
from pathlib import Path
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.utils.credentials import host, port, user, password
from app.utils.banco_de_dados import conn_data_base

ROOT = Path(__file__).parents[1]

# Query para buscar email no banco para enviar email de convite

# def sender_email(list_adrs):
def sender_email():
    query_busca_email = 'SELECT emailConv FROM `emailConvidados` WHERE `dataUpdate` = "0000-00-00 00:00:00" ORDER BY `dataInsert` DESC'
    try:
        #Buscando email no banco
        print('Buscando e-mail no banco...')
        list_adrs = conn_data_base(query_busca_email)
        print(list_adrs)
        
        for i in range(len(list_adrs)):
            print('Email: ', list_adrs[i])
            email = list_adrs[i]
            # Criando objeto
            print('Criando objeto servidor...')
            server = smtplib.SMTP(host, port)
            # Login com servidor
            print('Login...')
            server.ehlo()
            server.starttls()
            server.login(user, password)
            # Criando mensagem
            message = message_builder("index_new.html")
            print('Criando mensagem...')
            email_msg = MIMEMultipart()
            email_msg['From'] = user
            email_msg['To'] = email[0]
            email_msg['Subject'] = '38° Franchising Fair | Convite'
            print('Adicionando texto...')
            email_msg.attach(MIMEText(message, "html", "utf-8"))
            # Enviando mensagem
            print('Enviando mensagem...')
            server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
            print('Email enviado com scuesso!!')
            server.quit()
            if i >= len(list_adrs):
                print('Passou no if ', i)
                break
        return True
    except:
        print('Email não enviado!!')
        return False
  
def message_builder(html_template):
    """Função respnsável por construir o corpo do e-mail de acordo com o template
    Args:
        html_template (string): Nome do template para construir o corpo do e-mail
        tag_list (string): Lista formatada em html
    Returns:
        string: Corpo do e-mail completo
    """
    html_template_path = f"{ROOT}/email_sender/template-email/{html_template}"
    try:
        with open(html_template_path, "r", encoding='utf-8') as file:
            message = file.read()
    except FileNotFoundError:
        print('ERROR - Falha ao encontrar o arquivo template!')
        print(f'{html_template_path}')
        return
    
    message = (
        message
        .replace('%logo_cliente', 'LOGO CLIENTE AQUI!')
        .replace('%qr_code', 'QR CODE AQUI!')
    )
    return message