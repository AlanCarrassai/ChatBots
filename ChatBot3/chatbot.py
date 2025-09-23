from datasets import load_dataset
import difflib

# Carregar o dataset DailyDialog
print("Baixando dataset DailyDialog...")
dataset = load_dataset("daily_dialog", split="train", trust_remote_code=True)

# Criar pares de pergunta e resposta
pairs = []
for dialog in dataset["dialog"]:
    for i in range(len(dialog) - 1):
        pergunta = dialog[i].lower().strip()
        resposta = dialog[i + 1].strip()
        pairs.append((pergunta, resposta))

print(f"Total de pares carregados: {len(pairs)}")

# Função para responder
def responder(mensagem):
    mensagem = mensagem.lower().strip()
    perguntas = [p[0] for p in pairs]
    
    similar = difflib.get_close_matches(mensagem, perguntas, n=1, cutoff=0.5)
    
    if similar:
        for p, r in pairs:
            if p == similar[0]:
                return r
    return "Desculpe, não sei responder isso ainda."

# Loop de interação
print("\nChatbot DailyDialog pronto! Digite 'sair' para encerrar.\n")
while True:
    entrada = input("Você: ")
    if entrada.lower() in ["sair", "exit", "quit"]:
        print("Chatbot: Até mais!")
        break
    print("Chatbot:", responder(entrada))
