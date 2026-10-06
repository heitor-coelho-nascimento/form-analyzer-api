import pandas as pd


def analyze_data(df: pd.DataFrame):
    return {
        "total_respostas": len(df),
        "total_colunas": len(df.columns),
        "colunas": len(df.columns),
    }