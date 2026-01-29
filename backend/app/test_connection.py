from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, text

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

if not DATABASE_URL:
    raise RuntimeError('DATABASE_URL not set in environment')

def main():
    print(f'Trying to connect to: {DATABASE_URL}')
    engine = create_engine(DATABASE_URL)
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            print('Connection test OK, SELECT 1 ->', result.scalar())
    except Exception as e:
        print('Connection test failed:', e)

if __name__ == '__main__':
    main()
