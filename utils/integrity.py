from sheets_service import get_sheet
from config import Config
from utils.rating import calcular_rating

def testar_integridade():

    erros = []

    sheet = get_sheet(
        Config.GOOGLE_SHEET_NAME,
        "restaurantes"
    )

    restaurantes = sheet.get_all_records()

    for r in restaurantes:

        preco = float(r["Preco"])
        avaliacao = float(r["Avaliacao"])

        rating_calculado = calcular_rating(
            preco,
            avaliacao
        )

        rating_guardado = float(r["Rating"])

        if abs(rating_calculado - rating_guardado) > 0.1:

            erros.append(
                f"Rating inválido no restaurante {r['Nome']}"
            )

    return erros
