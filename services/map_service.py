from sheets_service import get_sheet
from config import Config
import folium


def gerar_mapa(zona=None):

    sheet = get_sheet(
        Config.GOOGLE_SHEET_NAME,
        "restaurantes"
    )

    restaurantes = sheet.get_all_records()

    mapa = folium.Map(
        location=[41.15, -8.61],
        zoom_start=12,
        tiles="CartoDB positron"
    )

    for r in restaurantes:

        localizacao = r.get("Localizacao")

        if localizacao is None:
            localizacao = ""

        localizacao = str(localizacao).strip()

        if zona:
            if localizacao.lower() != zona.strip().lower():
                continue

        try:
            lat = float(str(r.get("Lat", "")).strip())
            lon = float(str(r.get("Lon", "")).strip())
        except:
            continue

        nome = r.get("Nome", "Sem nome")
        rating = r.get("Rating", "N/A")
        tipo = r.get("Tipo", "")

        popup_html = f"""
        <b>{nome}</b><br>
        Tipo: {tipo}<br>
        Rating: {rating}
        """

        folium.Marker(
            location=[lat, lon],
            popup=popup_html,
            tooltip=nome
        ).add_to(mapa)

    return mapa._repr_html_()