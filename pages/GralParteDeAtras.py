import streamlit as st

def main():
    st.set_page_config(page_title="Invenatrio Bodega General Parte de Atras", layout="wide")
    st.title("Bodega General - Parte de Atras")

    st.write("pendiente")

    st.markdown("---")
    st.page_link("main.py", label="⬅️ Volver al Inventario", icon="📦")

if __name__ == "__main__":
    main()
