import streamlit as st
import psycopg2

'''

# Crear una conexión a la base de datos PostgreSQL
conn = psycopg2.connect(
    host="tu_host",
    database="tu_base_de_datos",
    user="tu_usuario",
    password="tu_contraseña"
)

# Función para insertar datos en la base de datos
def insertar_transaccion(cantidad, descripcion):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO transacciones (cantidad, descripcion) VALUES (%s, %s)", (cantidad, descripcion))
    conn.commit()
    cursor.close()

'''

# Definir la aplicación de Streamlit
def main():
    st.title("Aplicación de Carga y Procesamiento de Datos")

    # Crear pestañas
    tabs = st.sidebar.radio("Seleccione una pestaña:", ("Carga de Transacción", "Procesamiento de Datos"))

    if tabs == "Carga de Transacción":
        st.header("Carga de Transacción")

        # Formulario para cargar transacción
        cantidad = st.number_input("Cantidad:")
        descripcion = st.text_area("Descripción:")
        if st.button("Guardar Transacción"):
            if cantidad and descripcion:
                #insertar_transaccion(cantidad, descripcion)
                #st.success("Transacción guardada con éxito.")

                st.write("PEPE")
            else:
                st.warning("Por favor, complete todos los campos.")

    elif tabs == "Procesamiento de Datos":
        st.header("Procesamiento de Datos")

        # Texto explicativo
        st.write("En esta sección, puede procesar los datos mediante un script de Python.")

        # Botón para procesar datos
        if st.button("Procesar Datos"):
            # Aquí puedes ejecutar tu script de procesamiento de datos
            st.info("El proceso de datos se ha completado.")

# Ejecutar la aplicación
if __name__ == "__main__":
    main()
