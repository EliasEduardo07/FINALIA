import streamlit as st
from inicio import app_inicio
from apriory import app_apriori
from metricas import app_metricas
from clustering import app_clustering 

def main():
    st.set_page_config(page_title="Aplicación de Nutrición", page_icon="🥦", layout="wide")

    # Menú de navegación
    menu = ["Inicio", "Apriori", "Métricas", "Clustering"]
    opcion = st.sidebar.selectbox("Selecciona una aplicación", menu)

    # Mostrar la aplicación correspondiente según la opción seleccionada
    if opcion == "Inicio":
        app_inicio()
    elif opcion == "Apriori":
        app_apriori()
    elif opcion == "Métricas":
        app_metricas()
    elif opcion == "Clustering":
        app_clustering()

if __name__ == "__main__":
    main()
