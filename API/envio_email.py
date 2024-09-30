import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


remetente = "rafson@gmail.com"
destinatario = "@gmail.com"
senha = ""
assunto = "Assunto do Email"
corpo = "Este é o corpo do email enviado pelo Python!"


mensagem = MIMEMultipart()
mensagem['From'] = remetente
mensagem['To'] = destinatario
mensagem['Subject'] = assunto
mensagem.attach(MIMEText(corpo, 'plain'))


try:
    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    servidor.login(remetente, senha)
    texto = mensagem.as_string()
    servidor.sendmail(remetente, destinatario, texto)
    servidor.quit()
    print("Email enviado com sucesso!")
except Exception as e:
    print(f"Erro ao enviar email: {e}")
