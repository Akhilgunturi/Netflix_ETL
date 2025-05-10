import pandas as pd
from transformations import add_content_age

def test_add_content_age():
    df = pd.DataFrame({'release_year': [2020, 2000]})
    result = add_content_age(df)
    assert result['content_age'].tolist() == [5, 25]