import streamlit as st
import psycopg2
from PIL import Image
import pandas as pd

image = Image.open('logo1.jpg')

# Crear una conexión a la base de datos PostgreSQL
conn = psycopg2.connect(
    host="tempogym.cgxtpl6crtwg.us-east-2.rds.amazonaws.com",
    database="postgres",
    user="gym",
    password="consultora")



# Función para insertar datos en la base de datos
def insertar_transaccion(fecha_pago, tipo_operacion , tipo_suscripcion , medio_pago , precio_suscripcion , id_socio , dni , fecha_inicio_suscripcion , fecha_vencimiento_suscripcion, id_operacion):
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO operaciones (fecha_pago, tipo_operacion , tipo_suscripcion , medio_pago , precio_suscripcion , id_socio , dni , fecha_inicio_suscripcion , fecha_vencimiento_suscripcion, id_operacion) VALUES ({fecha_pago}, {tipo_operacion} , {tipo_suscripcion} , {medio_pago} , {precio_suscripcion} , {id_socio} , {dni} , {fecha_inicio_suscripcion} , {fecha_vencimiento_suscripcion}, {id_operacion})")
    conn.commit()
    cursor.close()


# Definir la aplicación de Streamlit
def main():
    st.title("Aplicación de Carga y Procesamiento de Datos")

    with st.sidebar:
        st.image(image)

    # Crear pestañas
    tabs = st.sidebar.radio("Seleccionar:", ("Carga de Transacción", "Procesamiento de Datos", "Tablero"))

    if tabs == "Carga de Transacción":

        
        st.header("Carga de Transacción")

        tab1, tab2 = st.tabs(["Nuevo Socio", "Socio Existente"])

        with tab1:
            st.header("Nuevo Socio")




        with tab2:
            st.header("Socio Existente / Individual") 

            fecha_pago = st.date_input( "Fecha de PAGO")
            fecha_pago = pd.to_datetime(fecha_pago)

            tipo_operacion = st.radio(
                "Tipo de OPERACION",
                options=["Clase Individual", "Renovación"])
            
            if tipo_operacion == "Clase Individual":

                tipo_suscripcion = "Clase Individual"

            if tipo_operacion == "Renovación":

                tipo_suscripcion = st.radio(
                    "Tipo de PLAN",
                    options=["Clase Individual","Plan 3 x Semana", "Plan Mensual"])
                
            medio_pago = st.radio(
                "Medio de PAGO",
                options=["Efectivo", "Transferencia"])
            
            if tipo_suscripcion == "Clase Individual":
                precio_suscripcion = st.number_input("Precio:",value = 500)

            if tipo_suscripcion == "Plan 3 x Semana":
                precio_suscripcion = st.number_input("Precio:",value = 4700)

            if tipo_suscripcion == "Plan Mensual":
                precio_suscripcion = st.number_input("Precio:",value = 5000)

            id_socio = st.number_input("Introducir ID SOCIO (0 si es Clase Individual):"
                                       #, format="%d"
                                       )

            dni = st.number_input("Introducir DNI del SOCIO:"
                                  #, format="%d"
                                  )

            fecha_inicio_suscripcion = st.date_input( "Fecha DESDE")
            fecha_inicio_suscripcion = pd.to_datetime(fecha_inicio_suscripcion)

            if fecha_inicio_suscripcion != None:

                fecha_vencimiento_suscripcion = st.date_input( "Fecha HASTA")
                fecha_vencimiento_suscripcion = pd.to_datetime(fecha_vencimiento_suscripcion)

            id_operacion = st.number_input("Introducir ID operacion"
                                  , format="%d"
                                  )
            
            pepe = f"INSERT INTO operaciones (fecha_pago, tipo_operacion , tipo_suscripcion , medio_pago , precio_suscripcion , id_socio , dni , fecha_inicio_suscripcion , fecha_vencimiento_suscripcion, id_operacion) VALUES ({fecha_pago}, {tipo_operacion} , {tipo_suscripcion} , {medio_pago} , {precio_suscripcion} , {id_socio} , {dni} , {fecha_inicio_suscripcion} , {fecha_vencimiento_suscripcion}, {id_operacion})"
            st.write(pepe)

            #st.write(fecha_pago)
            #st.write(type(fecha_pago))

            #fecha_nvo = pd.to_datetime(fecha_pago)
            #st.write(fecha_nvo)


            if st.button("Guardar Transacción"):
                if fecha_pago and tipo_operacion and tipo_suscripcion and medio_pago and precio_suscripcion and id_socio and dni and fecha_inicio_suscripcion and fecha_vencimiento_suscripcion and id_operacion:

                    insertar_transaccion(fecha_pago, tipo_operacion , tipo_suscripcion , medio_pago , precio_suscripcion , id_socio , dni , fecha_inicio_suscripcion , fecha_vencimiento_suscripcion, id_operacion)
                    st.success("Transacción guardada con éxito.")

                    st.write("PEPE")
                else:
                    st.warning("Por favor, complete todos los campos.")

    if tabs == "Tablero":

        st.markdown("Ir a Tablero ONLINE (INSERTAR ENLACE)")

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
