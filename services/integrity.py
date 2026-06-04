from datetime import datetime

from services.restaurant_service import listar_restaurantes
from services.client_service import listar_clientes
from services.menu_service import listar_menus
from services.order_service import listar_pedidos_cliente


# =========================
# HELPERS
# =========================
def safe_get(row, *keys):
    for k in keys:
        if k in row:
            return str(row.get(k, "")).strip()
    return ""


def is_empty(value):
    return value is None or str(value).strip() == ""


def to_float(value):
    try:
        return float(value)
    except:
        return None


def validate_date(value):
    try:
        return datetime.strptime(value, "%d-%m-%Y")
    except:
        return None


# =========================
# MAIN
# =========================
def run_integrity_check():

    issues = []

    # =========================================================
    # RESTAURANTES
    # =========================================================
    restaurantes = listar_restaurantes()

    nomes_r = set()
    nifs_r = set()

    for r in restaurantes:

        nome = safe_get(r, "Nome")
        nif = safe_get(r, "NIF")
        preco = to_float(r.get("Preco"))
        avaliacao = to_float(r.get("Avaliacao"))
        tipo = safe_get(r, "Tipo")
        rating = to_float(r.get("Rating"))
        lat = to_float(r.get("Lat"))
        lon = to_float(r.get("Lon"))

        if is_empty(nome):
            issues.append("❌ Restaurante sem Nome")

        if is_empty(nif):
            issues.append(f"❌ Restaurante sem NIF ({nome})")

        if nome in nomes_r:
            issues.append(f"⚠️ Restaurante duplicado: {nome}")
        nomes_r.add(nome)

        if nif in nifs_r:
            issues.append(f"⚠️ NIF duplicado: {nif}")
        nifs_r.add(nif)

        if preco is None or preco < 0:
            issues.append(f"❌ Preço inválido ({nome})")

        if avaliacao is None or not (0 <= avaliacao <= 10):
            issues.append(f"❌ Avaliação inválida ({nome})")

        if rating is None or not (0 <= rating <= 5):
            issues.append(f"❌ Rating inválido ({nome})")

        if lat is None or lon is None:
            issues.append(f"❌ Coordenadas inválidas ({nome})")

    # =========================================================
    # CLIENTES
    # =========================================================
    clientes = listar_clientes()

    clientes_seen = set()

    for c in clientes:

        nome = safe_get(c, "Nome")

        if is_empty(nome):
            issues.append("❌ Cliente sem Nome")

        if nome in clientes_seen:
            issues.append(f"⚠️ Cliente duplicado: {nome}")

        clientes_seen.add(nome)

    # =========================================================
    # MENUS (CORRIGIDO)
    # =========================================================
    menus = listar_menus()

    menus_seen = set()

    for m in menus:

        menu_id = safe_get(m, "id_menu")
        restaurante_nome = safe_get(m, "restaurante_nome")
        nome_item = safe_get(m, "nome_item")
        preco = to_float(m.get("preco"))

        # ID
        if is_empty(menu_id):
            issues.append("❌ Menu sem ID")

        if menu_id in menus_seen:
            issues.append(f"⚠️ Menu duplicado: {menu_id}")

        menus_seen.add(menu_id)

        # restaurante
        if is_empty(restaurante_nome):
            issues.append(f"❌ Menu sem restaurante ({menu_id})")

        # item
        if is_empty(nome_item):
            issues.append(f"❌ Menu sem nome de item ({menu_id})")

        # preço
        if preco is None:
            issues.append(f"❌ Preço inválido no menu ({menu_id})")
        elif preco < 0:
            issues.append(f"❌ Preço negativo no menu ({menu_id})")

    # =========================================================
    # PEDIDOS
    # =========================================================
    pedidos = listar_pedidos_cliente()

    pedidos_seen = set()

    for p in pedidos:

        cliente_id = safe_get(p, "Cliente_ID")
        cliente_nome = safe_get(p, "Cliente_Nome")
        restaurante_nif = safe_get(p, "Restaurante_NIF")
        restaurante_nome = safe_get(p, "Restaurante_Nome")
        menu_id = safe_get(p, "Menu_ID")
        item_nome = safe_get(p, "Item_Nome")
        preco = to_float(p.get("Preco"))
        data = validate_date(p.get("Data", ""))

        if is_empty(cliente_id):
            issues.append("❌ Pedido sem Cliente_ID")

        if is_empty(cliente_nome):
            issues.append("❌ Pedido sem Cliente_Nome")

        if is_empty(restaurante_nif):
            issues.append("❌ Pedido sem Restaurante_NIF")

        if is_empty(restaurante_nome):
            issues.append("❌ Pedido sem Restaurante_Nome")

        if is_empty(menu_id):
            issues.append("❌ Pedido sem Menu_ID")

        if is_empty(item_nome):
            issues.append("❌ Pedido sem Item_Nome")

        if preco is None or preco < 0:
            issues.append(f"❌ Preço inválido ({cliente_nome})")

        if data is None:
            issues.append(f"❌ Data inválida ({cliente_nome})")
        elif data > datetime.now():
            issues.append(f"⚠️ Data futura ({cliente_nome})")

        key = (cliente_id, restaurante_nif, menu_id, str(data))

        if key in pedidos_seen:
            issues.append(f"⚠️ Pedido duplicado ({cliente_nome})")

        pedidos_seen.add(key)

    # =========================================================
    # RESULTADO FINAL
    # =========================================================
    score = max(0, 100 - len(issues))

    return {
        "total_restaurantes": len(restaurantes),
        "total_clientes": len(clientes),
        "total_menus": len(menus),
        "total_pedidos": len(pedidos),
        "issues": issues,
        "status": "OK" if len(issues) == 0 else "WARNING",
        "score": score
    }