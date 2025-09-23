from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Chatbot com foco em respostas curtas e coerentes
chatbot_curto = ChatBot(
    "BotCurto",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database="database_curto.sqlite",
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "default_response": "Não entendi.",
            "maximum_similarity_threshold": 0.95
        }
    ]
)

trainer = ChatterBotCorpusTrainer(chatbot_curto)
trainer.train(
    "chatterbot.corpus.portuguese.greetings",
    "chatterbot.corpus.portuguese.conversations"
)

print("BotCurto pronto! (digite 'sair' para encerrar)\n")

while True:
    pergunta = input("Você: ")
    if pergunta.lower() in ["sair", "exit", "quit"]:
        print("BotCurto: Até logo!")
        break
    resposta = chatbot_curto.get_response(pergunta)
    print("BotCurto:", resposta)
