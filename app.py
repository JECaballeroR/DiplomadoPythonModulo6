import streamlit as st
import requests
import pandas as pd
import plotly.express as px

@st.cache
def cargar_datos(filename:str):
    return pd.read_csv(filename)

@st.cache
def plot_heatmap(df, x, y):
    data_heatmap=df.reset_index()[[x,y,'index']].groupby([x,y]).count().reset_index().pivot(x,y,'index').fillna(0)
    fig=px.imshow(data_heatmap, color_continuous_scale="Blues", aspect="auto", title=f'Heatmap {x} vs {y}')
    fig.update_traces(hovertemplate='<b><i>'+y+'</i></b>: %{y} <br><b><i>'
                            +x+'</i></b>: %{x} <br><b><i>Conteo interaccion variables</i></b>: %{z}<extra></extra>')
    return fig

datos=cargar_datos('data.csv')
# Sidebar
st.sidebar.markdown("# Selectores de datos")
st.sidebar.markdown("---")
satisfaction_level = st.sidebar.slider(label='satisfaction_level', min_value=0, max_value=100, value=50)
average_montly_hours = st.sidebar.slider(label='average_montly_hours', min_value=8, max_value=310, value=100)
salary_level = st.sidebar.selectbox(label='salary_level', options=['low', 'medium', 'high'])
request_data=[{
    'satisfaction_level':satisfaction_level/100,
    'average_montly_hours': average_montly_hours,
    'salary_level': salary_level
}]
url_api='http://127.0.0.1:8000/predict'
data = str(request_data).replace("'", '"')
prediccion= requests.post(url=url_api, data=data).text
st.sidebar.markdown("---")
opciones1=list(datos.columns)
eje_x_heatmap1=st.sidebar.selectbox(label='Heatmap X', options=opciones1)
opciones2=opciones1.copy()
opciones2.pop(opciones1.index(eje_x_heatmap1))
eje_y_heatmap1=st.sidebar.selectbox(label='Heatmap Y', options=opciones2)

#Main Body
st.header("Web app para el Diplomado de Python: Ejemplo Employee Turnover")
st.markdown("---")
col1, col2 = st.columns(2)
col1.metric(value=f'{100*pd.read_json(prediccion)["employee_left_proba"][0]} % ',
            label='Predicción probabilidad renuncia')
col2.write("Esto quedaría en la columna de la derecha")
st.markdown("---")
st.write(datos)
scatter_1=plot_heatmap(df=datos, x=eje_x_heatmap1, y=eje_y_heatmap1)

col1, col2 = st.columns(2)

col1.plotly_chart(scatter_1, use_container_width=True)

col2.plotly_chart( px.bar(datos.groupby(['left','salary']).count().reset_index().sort_values(by='satisfaction_level',
                                                                                             ascending=False),
                          x='salary', y='satisfaction_level', facet_col='left'),
                   use_container_width=True)