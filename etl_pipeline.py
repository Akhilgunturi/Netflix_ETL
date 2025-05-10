import pandas as pd
from transformations import clean_data, explode_genres, add_content_age
from utils import load_to_postgres
from config import NETFLIX_CSV_PATH

def run_pipeline():
    # Extract
    print("Extracting data...")
    df = pd.read_csv("netflix_titles.csv")

    # Transform
    print("Transforming data...")
    df = clean_data(df)
    df = explode_genres(df)
    df = add_content_age(df)

    # Load
    print("Loading data into Postgres...")
    load_to_postgres(df)

    print("Pipeline execution completed.")

if __name__ == "__main__":
    run_pipeline()