import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.header("NO OLVIDEN MODIFICAR LA ESCALA DE COLOR DE PLOTLY")
st.sidebar.header("NO OLVIDEN MODIFICAR LA ESCALA DE COLOR DE PLOTLY")

st.header("Holi, soy una webapp en streamlit :)")
st.sidebar.header("Holi, soy un texto en el sidebar")
st.sidebar.markdown("---")
st.sidebar.write(":sunglasses: :sunglasses: :sunglasses:")


@st.cache
def cargar_datos(filename: str):
    return pd.read_csv(filename)


datos = cargar_datos("data.csv")


cargo_datos = st.sidebar.button("Cargar Datos")

if cargo_datos:
    st.write("Estoy cargando datos (pero no)")


digo_holi = st.sidebar.checkbox("Decir holi")
if digo_holi:
    st.markdown("# HOLI A TODOS")

radio_button = st.sidebar.radio(
    label="Opciones", options=["Decir Holi", "No decir Holi"]
)

if radio_button == "Decir Holi":
    st.markdown("# HOLI A TODOS")

else:
    st.markdown("Me dijeron que no dijera que dijera no decir holi")

datos_agrupados = datos.groupby(["salary", "sales"]).mean().reset_index().copy()

st.dataframe(datos_agrupados)
st.sidebar.markdown("---")

lista_sales_unicos = list(datos_agrupados["sales"].unique())
# st.write((lista_sales_unicos))
opcion_sales = st.sidebar.selectbox(
    label="Seleccione un valor de 'sales'", options=lista_sales_unicos
)
st.markdown("---")
st.dataframe(datos_agrupados[datos_agrupados["sales"] == opcion_sales])


otras_variables = list(datos_agrupados.columns)
otras_variables.pop(otras_variables.index("sales"))
otras_variables.pop(otras_variables.index("salary"))
st.write(otras_variables)
opcion_y = st.sidebar.selectbox(
    label="Seleccione una variable", options=otras_variables
)


@st.cache
def plot_simple(df, x, y, sales_filter):
    data = df.copy()
    data = data[data["sales"] == sales_filter]
    fig = px.bar(data, x=x, y=y)
    return fig, data


plot, d = plot_simple(datos_agrupados, "salary", opcion_y, opcion_sales)
st.plotly_chart(plot)
st.write(d)
st.header("NO OLVIDEN MODIFICAR LA ESCALA DE COLOR DE PLOTLY")
st.sidebar.header("NO OLVIDEN MODIFICAR LA ESCALA DE COLOR DE PLOTLY")
st.header("NO OLVIDEN MODIFICAR LA ESCALA DE COLOR DE PLOTLY")
st.header("NO OLVIDEN MODIFICAR LA ESCALA DE COLOR DE PLOTLY")
