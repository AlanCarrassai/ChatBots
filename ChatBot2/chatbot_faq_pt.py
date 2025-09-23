from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Criar o chatbot
chatbot = ChatBot(
    'FAQBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)

# Treinar com o corpus em português
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("corpus/portuguese/faq.yml")

# Loop de conversa
print("Olá! Digite 'sair' para encerrar.")
while True:
    pergunta = input("Você: ")
    if pergunta.lower() == 'sair':
        break
    resposta = chatbot.get_response(pergunta)
    print("Bot:", resposta)
