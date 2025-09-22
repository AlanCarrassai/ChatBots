from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import unicodedata

# Função para remover acentos e deixar minúsculo
def normalize_text(text):
    text = text.lower()
    text = ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')
    return text

# Caminho para o banco de dados
DB_FOLDER = "db"
DB_PATH = os.path.join(DB_FOLDER, "chatbot_pt.sqlite3")

# Cria a pasta db se não existir
if not os.path.exists(DB_FOLDER):
    os.makedirs(DB_FOLDER)

# Criação do chatbot
chatbot_pt = ChatBot(
    "MeuBotPT",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri=f"sqlite:///{DB_PATH}",
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace',
        'chatterbot.preprocessors.unescape_html',
        'chatterbot.preprocessors.convert_to_ascii'
    ],
    read_only=True,
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "default_response": "Desculpe, não entendi.",
            "maximum_similarity_threshold": 0.90
        }
    ]
)

trainer_pt = ListTrainer(chatbot_pt)

# Carrega base de conhecimento
faq_pt = []
with open("base_conhecimento.txt", "r", encoding="utf-8") as f:
    for linha in f:
        linha = linha.strip()
        if linha:
            faq_pt.append(linha)

# Treina o chatbot
trainer_pt.train(faq_pt)

# Loop de interação
print("Chatbot FAQ em português pronto! Digite 'sair' para encerrar.\n")

while True:
    entrada = input("Você: ")
    if entrada.lower() in ["sair", "exit", "quit"]:
        print("Chatbot: Até mais!")
        break

    # Normaliza a entrada do usuário
    entrada_normalized = normalize_text(entrada)
    
    # Pega a resposta
    resposta = chatbot_pt.get_response(entrada_normalized)
    print("Chatbot:", resposta)
