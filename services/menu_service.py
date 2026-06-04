from sheets_service import get_sheet
from config import Config

def listar_menus():

    sheet = get_sheet(
        Config.GOOGLE_SHEET_NAME,
        "menus"
    )

    return sheet.get_all_records()

def adicionar_menu(data):

    sheet = get_sheet(
        Config.GOOGLE_SHEET_NAME,
        "menus"
    )

    row = [
        data["id_menu"],
        data["nome"]
    ]

    sheet.append_row(row)

def adicionar_item_menu(data):

    sheet = get_sheet(
        Config.GOOGLE_SHEET_NAME,
        "menu_items"
    )

    row = [
        data["id_menu"],
        data["nome_item"],
        data["preco"]
    ]

    sheet.append_row(row)
