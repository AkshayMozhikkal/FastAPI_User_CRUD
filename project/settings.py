from datetime import timedelta
import os


SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_DAYS = 7

access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
refresh_token_expires = timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)