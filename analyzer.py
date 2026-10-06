import pandas as pd


def analyzer_data(df: pd.DataFrame):
    return {
        "total_respostas": len(df),
        "total_colunas": len(df.columns),
        "colunas": len(df.columns),
    }