from dotenv import load_dotenv
import os

load_dotenv()  # Carga variables desde .env

DATABASE_URL = os.getenv("DATABASE_URL")
