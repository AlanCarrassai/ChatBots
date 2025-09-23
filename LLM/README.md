# Criar o env para rodar esse chatterbot (windows/powershell/vscode)
```
Utilizei o Python 3.13.7
py -m venv env
env\Scripts\activate
python.exe -m pip install --upgrade pip setuptools wheel
py -m pip install -r requirements.txt
py -m spacy download en_core_web_sm
```

- Remover o env antigo, se necessário
```
Remove-Item -Recurse -Force env
```

# Principais diferenças
```
ChatBot Curto:
Corpus limitado (saudações e conversas básicas em português)

Respostas curtas e diretas

Threshold alto (0.95) para respostas mais confiáveis e previsíveis

Apenas BestMatch como logic adapter

ChatBot Criativo:
Corpus amplo (português, literatura, ciência, computadores)

Respostas abertas, criativas ou inesperadas

Threshold baixo (0.50) para respostas mais variadas

Vários logic adapters (BestMatch, MathematicalEvaluation, TimeLogicAdapter)
```
