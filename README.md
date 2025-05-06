# 🤖 Bot WhatsApp com IA (Dialogflow) 🚀

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)
![License](https://img.shields.io/badge/License-Privado-lightgrey)

Este projeto é um **bot automatizado para WhatsApp**, desenvolvido em Python usando:

- **Flask** (para criar a API)
- **Twilio** (para integração com WhatsApp)
- **Dialogflow** (para inteligência artificial e NLP)

💬 **Funcionalidades:**

- Atende automaticamente clientes pelo WhatsApp
- Responde a perguntas frequentes (horários, localização, etc.)
- Usa inteligência artificial para interpretar e responder mensagens

## 🖼️ Exemplo do Bot em Ação

![Bot em ação](screenshot.png)

---

## 🚀 Tecnologias Utilizadas:

- Python
- Flask
- Twilio API
- Dialogflow (Google Cloud)

---

## 📦 Como Rodar Localmente:

1️⃣ Clone o repositório:

```bash
git clone https://github.com/FrancWash/whatsapp-bot-ia.git

2️⃣ Instale as dependências:
pip install -r requirements.txt

3️⃣ Configure a chave do Dialogflow:

Baixe sua chave JSON da Google Cloud.

Salve na raiz do projeto e configure no código.

4️⃣ Rode o bot localmente:
python bot_whatsapp.py

5️⃣ Exponha o bot usando Ngrok ou LocalTunnel:
ngrok http 5000

6️⃣ Configure o webhook no Twilio com a URL + /whatsapp

🛠️ Planos Futuros:
Hospedar o bot na nuvem (Render)

Melhorar as respostas usando LLMs mais avançados

Criar painel administrativo para monitorar interações

🙌 Autor
Franc Washington Vilela
🔗 LinkedIn

⚠️ Atenção
Este projeto é para fins educacionais e pode conter credenciais sensíveis. Use com cautela em produção.

