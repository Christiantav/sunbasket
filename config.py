import os

# Would normally use .env for db creds.
user = os.environ.get('SUNBASKET_USER', 'USER not found')
password = os.environ.get('SUNBASKET_PASSWORD', 'PASSWORD not found')
host = os.environ.get('SUNBASKET_HOST', 'HOST not found')
port = os.environ.get('SUNBASKET_PORT', 'PORT not found')
database = os.environ.get('SUNBASKET_DATABASE', 'DATABASE not found')

SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
