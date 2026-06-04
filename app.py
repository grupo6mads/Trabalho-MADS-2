from flask import Flask, render_template, request, redirect, url_for, session, flash
from config import Config

from services.restaurant_service import (
    listar_restaurantes,
    adicionar_restaurante,
    listar_por_rating,
    tabela_precos,
    tabela_avaliacoes,
    historico_restaurante
)

from services.client_service import (
    listar_clientes,
    adicionar_cliente
)

from services.menu_service import (
    listar_menus,
    adicionar_menu,
    adicionar_item_menu
)

from services.order_service import (
    listar_pedidos_cliente,
    adicionar_pedido
)

from services.map_service import gerar_mapa

from utils.auth import login_required

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = app.config.get("SECRET_KEY", "dev_secret_key")

@app.route("/debug-sheet")
def debug_sheet():

    from sheets_service import get_sheet
    from config import Config

    sheet = get_sheet(Config.GOOGLE_SHEET_NAME, "restaurantes")

    print(sheet.row_values(1))

    return {"status": "ok", "message": "check terminal"}

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        access_key = request.form.get("access_key", "").strip()

        if access_key == app.config["KEY_RESTAURANTES"]:
            session["role"] = "restaurants"

        elif access_key == app.config["KEY_CLIENTES"]:
            session["role"] = "clients"

        elif access_key == app.config["KEY_ADMIN"]:
            session["role"] = "admin"

        elif access_key == app.config["KEY_INTEGRITY"]:
            session["role"] = "integrity"

        else:
            flash("Chave inválida", "danger")
            return redirect(url_for("index"))

        return redirect(url_for("dashboard"))

    return render_template("index.html")

from services.integrity import run_integrity_check

@app.route("/mapa", defaults={"zona": None})
@app.route("/mapa/<zona>")
def mapa(zona):

    mapa_html = gerar_mapa(zona)

    return render_template(
        "mapa.html",
        mapa=mapa_html
    )

@app.route("/integrity")
@login_required("integrity")
def integrity():

    result = run_integrity_check()

    return render_template(
        "integrity.html",
        result=result
    )

@app.route("/dashboard")
def dashboard():

    if "role" not in session:
        return redirect(url_for("index"))

    return render_template(
        "dashboard.html",
        role=session["role"]
    )

@app.route("/restaurantes")
@login_required("restaurants")
def restaurantes():

    restaurantes = listar_restaurantes()

    return render_template(
        "restaurantes.html",
        restaurantes=restaurantes
    )

@app.route("/restaurantes/add", methods=["POST"])
@login_required("restaurants")
def add_restaurante():

    adicionar_restaurante(request.form)

    flash("Restaurante adicionado", "success")

    return redirect(url_for("restaurantes"))

@app.route("/clientes")
@login_required("clients")
def clientes():

    clientes = listar_clientes()

    return render_template(
        "clientes.html",
        clientes=clientes
    )

@app.route("/clientes/add", methods=["POST"])
@login_required("clients")
def add_cliente():

    adicionar_cliente(request.form)

    flash("Cliente adicionado", "success")

    return redirect(url_for("clientes"))

@app.route("/menus")
@login_required("restaurants")
def menus():

    menus = listar_menus()

    return render_template(
        "menus.html",
        menus=menus
    )

@app.route("/menus/add", methods=["POST"])
@login_required("restaurants")
def add_menu_route():

    adicionar_menu(request.form)

    flash("Menu criado", "success")

    return redirect(url_for("menus"))

@app.route("/pedidos")
@login_required("restaurants")
def pedidos():

    pedidos = listar_pedidos_cliente()

    return render_template(
        "pedidos.html",
        pedidos=pedidos
    )

@app.route("/pedidos/add", methods=["POST"])
@login_required("restaurants")
def add_pedido_route():

    adicionar_pedido(request.form)

    flash("Pedido criado", "success")

    return redirect(url_for("pedidos"))

@app.route("/analytics")
@login_required("restaurants")
def analytics():

    ratings = tabela_avaliacoes()
    precos = tabela_precos()
    ranking = listar_por_rating()

    return render_template(
        "analytics.html",
        ratings=ratings,
        precos=precos,
        ranking=ranking
    )

@app.route("/historico/<nif>")
@login_required("restaurants")
def historico(nif):

    historico = historico_restaurante(nif)

    return render_template(
        "historico.html",
        historico=historico,
        nif=nif
    )

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
