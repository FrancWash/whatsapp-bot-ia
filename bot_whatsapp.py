from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from google.cloud import dialogflow
import os

app = Flask(__name__)

import json
from google.oauth2 import service_account

# Lê o JSON da variável de ambiente
credentials_info = json.loads(os.environ["GOOGLE_APPLICATION_CREDENTIALS_JSON"])
credentials = service_account.Credentials.from_service_account_info(credentials_info)

DIALOGFLOW_PROJECT_ID = 'seu-project-id'  # coloque aqui o ID do seu projeto Dialogflow
DIALOGFLOW_LANGUAGE_CODE = 'pt-BR'
SESSION_ID = 'current-user-id'

def detect_intent_texts(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient(credentials=credentials)
    session = session_client.session_path(project_id, session_id)
    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = session_client.detect_intent(session=session, query_input=query_input)
    return response.query_result.fulfillment_text

@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()

    try:
        resposta = detect_intent_texts(DIALOGFLOW_PROJECT_ID, SESSION_ID, incoming_msg, DIALOGFLOW_LANGUAGE_CODE)
        if resposta.strip() == "":
            resposta = 'Desculpe, não entendi sua mensagem. Um atendente vai te ajudar em breve.'
    except Exception as e:
        print(f"Erro: {e}")
        resposta = 'Houve um problema ao processar sua mensagem. Tente novamente mais tarde.'

    msg.body(resposta)
    return str(resp)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)


