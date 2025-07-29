import streamlit as st
import pandas as pd
import qrcode
from io import BytesIO
import urllib.parse

st.page_link("Detalle.py", label="⬅️ Volver al Inicio", icon="📦")
st.markdown("---")

@st.cache_data
def cargar_inventariobodegeneral():
    archivo = 'QRBDGAGRL.xlsx'
    try:
        df = pd.read_excel(archivo)
        df.columns = df.columns.str.strip().str.lower()
        return df
    except Exception as e:
        st.error(f"Error al cargar el archivo: {e}")
        return pd.DataFrame()

def generar_qr_url(item, descripcion, ubicacion):
    base_url = "https://qrbodegageneral.streamlit.app/Detalle"
    params = {
        "item": item,
        "descripcion": descripcion,
        "ubicacion": ubicacion
    }
    full_url = f"{base_url}?{urllib.parse.urlencode(params)}"
    qr = qrcode.make(full_url)
    buf = BytesIO()
    qr.save(buf, format="PNG")
    buf.seek(0)
    return buf

def mostrar_inventario():
    df = cargar_inventariobodegeneral()
    if df.empty:
        st.warning("No hay datos disponibles.")
        return

    st.title("📦 Inventario de Bodega General")

    # Buscador por nombre de ítem
    busqueda = st.text_input("🔍 Buscar por id de ítem:")
    if busqueda:
        df = df[df['item'].str.contains(busqueda, case=False, na=False)]

    if df.empty:
        st.info("No se encontraron ítems que coincidan con la búsqueda.")
        return

    for _, row in df.iterrows():
        item = row['item']
        descripcion = row['descripcion']
        ubicacion = row['ubicacion']

        qr_img = generar_qr_url(item, descripcion, ubicacion)

        cols = st.columns([3, 4, 3, 2])
        cols[0].write(f"**Item:** {item}")
        cols[1].write(f"**Descripción:** {descripcion}")
        cols[2].write(f"**Ubicación:** {ubicacion}")
        cols[3].image(qr_img, use_container_width=True)

        st.download_button(
            label="📥 Descargar QR",
            data=qr_img,
            file_name=f"{item}_QR.png",
            mime="image/png"
        )

    df = cargar_inventariobodegeneral()
    if df.empty:
        st.warning("No hay datos disponibles.")
        return

    st.title("📦 Inventario de Bodega General")

    for _, row in df.iterrows():
        item = row['item']
        descripcion = row['descripcion']
        ubicacion = row['ubicacion']

        qr_img = generar_qr_url(item, descripcion, ubicacion)

        cols = st.columns([3, 4, 3, 2])
        cols[0].write(f"**Item:** {item}")
        cols[1].write(f"**Descripción:** {descripcion}")
        cols[2].write(f"**Ubicación:** {ubicacion}")
        cols[3].image(qr_img, use_container_width=True)

        # boton para decargar el QR
        st.download_button(
            label="Descargar QR",
            data=qr_img,
            file_name=f"{item}_QR.png",
            mime="image/png"
        )

def main():
    st.set_page_config(page_title="Bodega General", layout="wide")
    mostrar_inventario()

if __name__ == "__main__":
    main()
