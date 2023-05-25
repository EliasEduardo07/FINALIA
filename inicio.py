import streamlit as st
import csv
import matplotlib.pyplot as plt

def calcular_imc(peso, altura):
    # Convertir peso a float
    peso = float(peso)

    # Convertir altura a metros
    altura = float(altura) / 100

    # Realizar cálculo del IMC
    imc = peso / (altura ** 2)
    return imc

def guardar_datos(nombre, apellidoP, edad, peso, altura_cm, imc):
    # Definir el nombre del archivo CSV
    archivo_csv = "datos_personas.csv"

    # Crear una lista con los datos a guardar
    datos = [nombre, apellidoP, edad, peso, altura_cm, imc]

    # Abrir el archivo CSV en modo de escritura y agregar los datos
    with open(archivo_csv, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(datos)

def app_inicio():
    # Título de la aplicación
    st.title("Nutria AI - Página de inicio")

    # Solicitar datos del usuario
    nombre = st.text_input("Nombre", max_chars=20, key="nombre_input")
    apellidoP = st.text_input("Apellido Paterno", max_chars=20, key="apellido_input")
    edad = st.number_input("Edad", min_value=0, key="edad_input")
    peso = st.number_input("Peso (kg)", min_value=0.0, key="peso_input")
    altura_cm = st.number_input("Altura (cm)", min_value=0.0, key="altura_input")

    # Comprobar si se han ingresado todos los datos
    datos_completos = nombre and apellidoP and edad and peso and altura_cm

    if datos_completos:
        # Calcular IMC
        altura = altura_cm
        imc = calcular_imc(peso, altura)

        # Definir rango de IMC ideal
        imc_ideal_min = 18.5
        imc_ideal_max = 24.9

        # Mostrar resultados
        st.write(f"Tu IMC es: {imc:.2f}")

        if imc > imc_ideal_max:
            st.warning("Tu IMC es alto. Por favor, visita a un médico.")
        elif imc < imc_ideal_min:
            st.warning("Tu IMC es bajo. Por favor, asiste a un médico.")
        else:
            st.success("Tu IMC está dentro del rango ideal.")

        # Crear gráfica de barras para comparar IMC
        fig, ax = plt.subplots()
        ax.bar(["Tu IMC"], [imc], label="Tu IMC")
        ax.bar(["IMC ideal"], [imc_ideal_max], label="IMC ideal")
        ax.set_ylabel("IMC")
        ax.set_title("Comparación de IMC")
        ax.legend()
        st.pyplot(fig)

        # Guardar datos en archivo CSV
        guardar_datos(nombre, apellidoP, edad, peso, altura_cm, imc)

    else:
        st.warning("Por favor, introduce todos los datos.")

if __name__ == "__main__":
    app_inicio()
