import base64
from email.message import EmailMessage

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def gmail_send_message(row):
  
  creds, _ = google.auth.default()

  try:
    service = build("gmail", "v1", credentials=creds)
    message = EmailMessage()

    #formateo mensaje
#Proceso 1 | observacion  2| tipo de riesgo 3| severidad 4| plan accion 5| Fecha compromiso 6| resonsabre 7| Area Res 8| correo Res  9| estado 10 -> -1

    date_com = row[5].value.strftime("%m/%d/%Y")
    message.set_content(f"Proceso: {row[0].value}\n Estado: {row[9].value}\n Observacion: {row[1].value}\n Fecha de Compormiso: {date_com}")

    #configuro mail
    message["To"] = "santycheco1@gmail.com"
    message["From"] = "mailparatestuno@gmail.com"
    message["Subject"] = "Proceso Atrasado"

    # encoded message
    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    create_message = {"raw": encoded_message}
    # pylint: disable=E1101
    send_message = (
        service.users()
        .messages()
        .send(userId="me", body=create_message)
        .execute()
    )
    print(f'Message Id: {send_message["id"]}')
  except HttpError as error:
    print(f"An error occurred: {error}")
    send_message = None
  


if __name__ == "__main__":
  gmail_send_message()