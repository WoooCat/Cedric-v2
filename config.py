from dotenv import load_dotenv
import os


load_dotenv()


DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_CONNECTOR = os.getenv("DB_CONNECTOR", "asyncpg")

DATABASE_URL = f"postgresql+{DB_CONNECTOR}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


# DB_TABLES
CATEGORY_TABLE = os.getenv("CATEGORY_TABLE")
CATEGORY_RELATIONS_TABLE = os.getenv("CATEGORY_RELATIONS_TABLE")
PRODUCT_TABLE = os.getenv("PRODUCT_TABLE")
DISCOUNT_TABLE = os.getenv("DISCOUNT_TABLE")
PRODUCT_DISCOUNT_TABLE = os.getenv("PRODUCT_DISCOUNT_TABLE")
RESERVATION_TABLE = os.getenv("RESERVATION_TABLE")
SALE_TABLE = os.getenv("SALE_TABLE")