from sheets_service import get_sheet
from config import Config
from utils.rating import calcular_rating

def _clean_row(row):
    return {k.strip(): v for k, v in row.items()}

# =========================
# LISTAR RESTAURANTES
# =========================
def listar_restaurantes():

    sheet = get_sheet(
        Config.GOOGLE_SHEET_NAME,
        "restaurantes"
    )

    data = sheet.get_all_records()

    return [_clean_row(r) for r in data]


# =========================
# ADICIONAR RESTAURANTE
# =========================
def adicionar_restaurante(data):

    sheet = get_sheet(
        Config.GOOGLE_SHEET_NAME,
        "restaurantes"
    )

    preco = float(data.get("preco") or 0)
    avaliacao = float(data.get("avaliacao") or 0)

    rating = calcular_rating(preco, avaliacao)

    row = [
        data.get("nome"),
        data.get("nif"),
        preco,
        avaliacao,
        data.get("tipo"),
        rating,
        data.get("localizacao"),
        data.get("lat"),
        data.get("lon")
    ]

    sheet.append_row(row)


# =========================
# LISTAR POR RATING
# =========================
def listar_por_rating():

    restaurantes = listar_restaurantes()

    return sorted(
        restaurantes,
        key=lambda x: float(x.get("Rating") or 0),
        reverse=True
    )


# =========================
# TABELA PREÇOS
# =========================
def tabela_precos():

    restaurantes = listar_restaurantes()

    return [
        {
            "Nome": r.get("Nome"),
            "Preco": float(r.get("Preco") or 0)
        }
        for r in restaurantes
    ]


# =========================
# TABELA AVALIAÇÕES
# =========================
def tabela_avaliacoes():

    restaurantes = listar_restaurantes()

    return [
        {
            "Nome": r.get("Nome"),
            "Avaliacao": float(r.get("Avaliacao") or 0)
        }
        for r in restaurantes
    ]


# =========================
# HISTÓRICO RESTAURANTE
# =========================
def historico_restaurante(nif):

    sheet = get_sheet(
        Config.GOOGLE_SHEET_NAME,
        "historico_dados"
    )

    dados = sheet.get_all_records()

    return [
        d for d in dados
        if str(d.get("NIF", "")).strip() == str(nif).strip()
    ]