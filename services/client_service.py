from sheets_service import get_sheet
from config import Config

def listar_clientes():

    sheet = get_sheet(
        Config.GOOGLE_SHEET_NAME,
        "clientes"
    )

    return sheet.get_all_records()

def adicionar_cliente(data):

    sheet = get_sheet(
        Config.GOOGLE_SHEET_NAME,
        "clientes"
    )

    row = [
        data["nome"],
        data["id_cliente"]
    ]

    sheet.append_row(row)
