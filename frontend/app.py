import streamlit as st
import requests


API_URL = "http://127.0.0.1:8000/predict"


st.set_page_config(
    page_title="Clasificador de Tickets Bancarios",
    page_icon="🏦",
    layout="centered"
)


st.title("🏦 Clasificador Inteligente de Tickets Bancarios")

st.write(
    "Introduce la descripción del incidente para obtener "
    "una clasificación automática."
)


texto_ticket = st.text_area(
    "Descripción del incidente",
    placeholder="Ejemplo: No reconozco una transferencia realizada desde mi cuenta.",
    height=150
)


if st.button("Analizar ticket"):

    if not texto_ticket.strip():

        st.warning("Introduce una descripción antes de analizar el ticket.")

    else:

        try:

            respuesta = requests.post(
                API_URL,
                json={"texto": texto_ticket},
                timeout=10
            )

            if respuesta.status_code == 200:

                resultado = respuesta.json()

                st.success("Ticket analizado correctamente")

                st.subheader("Resultado")

                st.write(
                    "**Categoría:**",
                    resultado["categoria"].replace("_", " ").title()
                )

                st.write(
                    "**Prioridad:**",
                    resultado["prioridad"]
                )

                st.write(
                    "**Área sugerida:**",
                    resultado["area"]
                )

                st.info(
                    "La clasificación es una recomendación automática. "
                    "Los casos sensibles deben ser revisados por un agente."
                )

            else:

                st.error(
                    f"La API devolvió un error: {respuesta.status_code}"
                )

        except requests.exceptions.RequestException:

            st.error(
                "No fue posible conectar con la API. "
                "Verifica que FastAPI esté ejecutándose."
            )