# Criar o env para rodar esse chatterbot (windows/powershell/vscode)
```
Utilizei o Python 3.17.3
py -m venv env
env\Scripts\activate
python.exe -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

- Remover o env antigo, se necessário
```
Remove-Item -Recurse -Force env
```
