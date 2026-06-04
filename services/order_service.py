from sheets_service import get_sheet
from config import Config
from datetime import datetime

def listar_pedidos_cliente():

    sheet = get_sheet(
        Config.GOOGLE_SHEET_NAME,
        "pedidos"
    )

    return sheet.get_all_records()

def adicionar_pedido(data):

    sheet = get_sheet(
        Config.GOOGLE_SHEET_NAME,
        "pedidos"
    )

    row = [
        data["cliente_id"],
        data["cliente_nome"],
        data["restaurante_nif"],
        data["restaurante_nome"],
        data["menu_id"],
        data["item_nome"],
        data["preco"],
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ]

    sheet.append_row(row)
