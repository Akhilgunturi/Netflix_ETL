from sqlalchemy import create_engine
from config import POSTGRES_URI

def load_to_postgres(df):
    engine = create_engine(POSTGRES_URI)
    df.to_sql('netflix_titles', engine, if_exists='replace', index=False)