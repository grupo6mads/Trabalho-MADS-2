import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    SECRET_KEY = os.getenv("SECRET_KEY")

    GOOGLE_SHEET_NAME = os.getenv("GOOGLE_SHEET_NAME")

    KEY_RESTAURANTES = os.getenv("KEY_RESTAURANTES")
    KEY_CLIENTES = os.getenv("KEY_CLIENTES")
    KEY_ADMIN = os.getenv("KEY_ADMIN")
    KEY_INTEGRITY=os.getenv("KEY_INTEGRITY")
