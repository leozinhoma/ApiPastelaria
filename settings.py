from urllib.parse import quote # por causa do @ na senha...
from dotenv import load_dotenv, find_dotenv
import os

# localiza o arquivo de .env
dotenv_file = find_dotenv()

#Carrega o arquivo .env
load_dotenv(".env")

#Configurações da API
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
RELOAD = os.getenv("RELOAD")

# Configurações Segurança da API
X_TOKEN = os.getenv("X_TOKEN")
X_KEY = os.getenv("X_KEY")

# Configurações banco de dados
DB_SGDB = os.getenv("DB_SGDB")
DB_NAME = os.getenv("DB_NAME")


# Ajusta STR_DATABASE conforme gerenciador escolhido
if DB_SGDB == 'sqlite': # SQLite
    STR_DATABASE = f"sqlite:///{DB_NAME}.db"
else: # SQLite
    STR_DATABASE = f"sqlite:///apiDatabase.db"