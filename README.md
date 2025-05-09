# 🤖 Bot WhatsApp com IA (Dialogflow) 🚀

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Status](https://img.shields.io/badge/Status-Estável-brightgreen)
![License](https://img.shields.io/badge/License-Privado-lightgrey)

Projeto concluído e funcional: bot automatizado para WhatsApp, capaz de atender clientes automaticamente, responder dúvidas frequentes e personalizar respostas usando inteligência artificial.

- **Flask** (para criar a API)
- **Twilio** (para integração com WhatsApp)
- **Dialogflow** (para inteligência artificial e NLP)

💬 **Funcionalidades:**

- Atende automaticamente clientes pelo WhatsApp
- Responde a perguntas frequentes (horários, localização, etc.)
- Usa inteligência artificial para interpretar e responder mensagens

## 🖼️ Exemplo do Bot em Ação

![Bot em ação](screenshot.png)

![Demonstração do chatbot funcionando](projeto_whatsapp_interaction_otimizado.gif)

---

## 🏋️‍♂️ Case de Uso – Academia

Imagine uma academia que recebe dezenas de mensagens no WhatsApp todos os dias com perguntas repetidas, como:

- Quais são os horários das aulas?
- Qual o valor dos planos?
- Vocês têm aula de funcional?
- Onde fica a academia?

Com o **Bot WhatsApp com IA**, é possível automatizar todas essas respostas, atendendo clientes 24h por dia sem depender de um atendente humano.

✅ O bot pode ser treinado para entender essas perguntas e responder automaticamente com as informações da academia.  
✅ Quando necessário, o bot também pode redirecionar a conversa para um atendente humano.

🎯 Benefícios para a academia:

- Redução de perguntas repetidas para a equipe
- Atendimento imediato, mesmo fora do horário comercial
- Melhora na experiência do cliente
- Mais tempo da equipe para focar em vendas presenciais ou atendimento avançado

Este é apenas um exemplo de como o bot pode ser aplicado para resolver um problema real de atendimento no WhatsApp, agregando valor a negócios locais.


---

## 🚀 Tecnologias Utilizadas:

- Python
- Flask
- Twilio API
- Dialogflow (Google Cloud)
- Railway (Deploy na Nuvem)

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

## 📈 Próximos Passos

- Customização para diferentes nichos (academias, igrejas, comércio local e etc...)
- Melhorias no NLP com modelos mais avançados
- Criação de interface para configuração das respostas
- Oferecer serviço como SaaS (Software as a Service)

🙌 Autor
Franc Washington Vilela

📩 E-mail: fvilela216@gmail.com  
📲 WhatsApp: +55 11 97847-4481  
🔗 LinkedIn: [Acesse meu perfil](https://www.linkedin.com/in/franc-washington-vilela-12446016a/)


⚠️ Aviso
Este projeto foi desenvolvido com fins educacionais e demonstração. Para uso em produção, recomenda-se validação adicional de segurança e escalabilidade.


