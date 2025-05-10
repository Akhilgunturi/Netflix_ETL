import pandas as pd

def clean_data(df):
    df = df.dropna(subset=['title', 'type', 'release_year'])
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
    return df

def explode_genres(df):
    df['listed_in'] = df['listed_in'].fillna('')
    df['listed_in'] = df['listed_in'].str.split(', ')
    df = df.explode('listed_in')
    df.rename(columns={'listed_in': 'genre'}, inplace=True)
    return df

def add_content_age(df):
    df['content_age'] = 2025 - df['release_year']
    return df