import streamlit as st

def main():
    st.set_page_config(page_title="inicio", layout="wide")

    # Leer parámetros de la URL
    query_params = st.query_params
    st.write("🔍 Parámetros recibidos:", query_params)  # Para depurar

    item = query_params.get("item", "")
    descripcion = query_params.get("descripcion", "")
    ubicacion = query_params.get("ubicacion", "")

    st.title("🔍 Detalle del Ítem Escaneado")
    st.markdown(f"**Item:** {item}")
    st.markdown(f"**Descripción:** {descripcion}")
    st.markdown(f"**Ubicación:** {ubicacion}")

    st.markdown("---")
    st.page_link("main.py", label="⬅️ Volver al Inventario", icon="📦")

if __name__ == "__main__":
    main()
