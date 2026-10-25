import pandas as pd
from app.main import profile_df, recommendations

def test_profile_counts_missing_duplicates():
    df = pd.DataFrame({"cantidad": [1, None, 1], "tipo": ["A", "B", "A"]})
    p = profile_df(df)
    assert p["rows"] == 3
    assert p["columns"] == 2
    assert p["missing"][0]["missing"] == 1
    assert p["duplicate_rows"] == 1

def test_recommendations_include_missing_and_duplicates():
    df = pd.DataFrame({"cantidad": [1, None, 1], "tipo": ["A", "B", "A"]})
    ids = [x["id"] for x in recommendations(df)]
    assert "missing:cantidad" in ids
    assert "duplicates:all" in ids
