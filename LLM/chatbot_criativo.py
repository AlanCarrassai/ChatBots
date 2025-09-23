from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Chatbot com foco em respostas mais abertas e criativas
chatbot_criativo = ChatBot(
    "BotCriativo",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database="database_criativo.sqlite",
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "default_response": "Não entendi o que você disse",
            "maximum_similarity_threshold": 0.50
        },
        {
            "import_path": "chatterbot.logic.MathematicalEvaluation"
        },
        {
            "import_path": "chatterbot.logic.TimeLogicAdapter"
        }
    ]
)

trainer = ChatterBotCorpusTrainer(chatbot_criativo)
trainer.train(
    "chatterbot.corpus.portuguese",
    "chatterbot.corpus.english",
    "chatterbot.corpus.english.literature",
    "chatterbot.corpus.english.computers",
    "chatterbot.corpus.english.science"
)

print("BotCriativo pronto! (digite 'sair' para encerrar)\n")

while True:
    pergunta = input("Você: ")
    if pergunta.lower() in ["sair", "exit", "quit"]:
        print("BotCriativo: Até logo!")
        break
    resposta = chatbot_criativo.get_response(pergunta)
    print("BotCriativo:", resposta)
