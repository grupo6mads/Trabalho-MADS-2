from sheets_service import get_sheet
from config import Config
import pandas as pd

def obter_analytics():

    sheet = get_sheet(
        Config.GOOGLE_SHEET_NAME,
        "restaurantes"
    )

    data = sheet.get_all_records()

    df = pd.DataFrame(data)

    analytics = {
        "total_restaurantes": len(df),
        "media_rating": round(df["Rating"].astype(float).mean(), 2),
        "media_preco": round(df["Preco"].astype(float).mean(), 2)
    }

    return analytics

def restaurantes_criticos():

    sheet = get_sheet(
        Config.GOOGLE_SHEET_NAME,
        "restaurantes"
    )

    data = sheet.get_all_records()

    criticos = []

    for r in data:

        rating = float(r["Rating"])

        if rating > 25 or rating < 18.5:
            criticos.append(r)

    return criticos
