# Permitir execução de scripts no PowerShell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Criar o ambiente virtual com Python 3.10
py -3.10 -m venv env

# Ativar o ambiente virtual
.\env\Scripts\Activate.ps1

# Atualizar pip, setuptools e wheel
python.exe -m pip install --upgrade pip setuptools wheel

# Instalar todas as dependências do projeto
python -m pip install -r requirements.txt

# Baixar modelo do spaCy necessário para o ChatterBot
python -m spacy download en_core_web_sm

# Executar o chatbot
python chatbot_faq_pt.py

# Caso precise criar o env do zero
Remove-Item -Recurse -Force env