from sheets_service import get_sheet
from config import Config

def obter_analytics():

    sheet = get_sheet(
        Config.GOOGLE_SHEET_NAME,
        "restaurantes"
    )

    data = sheet.get_all_records()

    total = len(data)

    ratings = [float(r.get("Rating", 0)) for r in data if r.get("Rating")]
    precos = [float(r.get("Preco", 0)) for r in data if r.get("Preco")]

    analytics = {
        "total_restaurantes": total,
        "media_rating": round(sum(ratings) / len(ratings), 2) if ratings else 0,
        "media_preco": round(sum(precos) / len(precos), 2) if precos else 0
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

        try:
            rating = float(r.get("Rating", 0))
        except:
            continue

        if rating > 25 or rating < 18.5:
            criticos.append(r)

    return criticos