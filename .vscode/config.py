# config.py

# -----------------------
# База даних
DATABASE_URL = "postgresql+psycopg2://postgres:sirenkyi2001as@localhost:5432/mydb"

# -----------------------
# JWT
SECRET_KEY = "mini_crm_super_secret_key_2026_do_not_share_987654321"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 120  # час життя токена в хвилинах

# -----------------------
# Інші налаштування
DEBUG = True  # або False для продакшн