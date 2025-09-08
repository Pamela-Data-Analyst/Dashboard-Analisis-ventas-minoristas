
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Set page configuration
st.set_page_config(layout="wide")

st.title("Dashboard de Análisis de Ventas de Tienda Minorista")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('retail_sales_dataset.csv')
    df['OrderDate'] = pd.to_datetime(df['OrderDate'])
    df['Month'] = df['OrderDate'].dt.month_name()
    df['DayOfWeek'] = df['OrderDate'].dt.day_name()
    return df

df = load_data()

st.sidebar.header("Filtros")

# City filter
selected_cities = st.sidebar.multiselect(
    "Selecciona Ciudades:",
    options=df['City'].unique(),
    default=df['City'].unique()
)

# Filter data based on selected cities
df_filtered = df[df['City'].isin(selected_cities)]

st.header("Rendimiento de Ventas")

st.subheader("Línea de Producto Más Vendida por Ciudad")
st.write("Este gráfico muestra la línea de producto con el mayor volumen de ventas en cada ciudad seleccionada.")
if not df_filtered.empty:
    product_sales_by_city = df_filtered.groupby(['City', 'ProductLine']).size().reset_index(name='SalesCount')
    most_sold_product_per_city = product_sales_by_city.loc[product_sales_by_city.groupby('City')['SalesCount'].idxmax()]
    fig_most_sold_product = px.bar(most_sold_product_per_city,
                 x='City',
                 y='SalesCount',
                 color='ProductLine',
                 title='Línea de Producto Más Vendida por Ciudad')
    st.plotly_chart(fig_most_sold_product, use_container_width=True)
else:
    st.warning("No hay datos para las ciudades seleccionadas.")


st.subheader("Volumen de Ventas por Mes y Día de la Semana")
st.write("Estos gráficos muestran la tendencia del volumen de ventas a lo largo de los meses y días de la semana para las ciudades seleccionadas.")
if not df_filtered.empty:
    col1, col2 = st.columns(2)

    with col1:
        monthly_sales = df_filtered.groupby('Month')['Total'].sum().reset_index()
        month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        monthly_sales['Month'] = pd.Categorical(monthly_sales['Month'], categories=month_order, ordered=True)
        monthly_sales = monthly_sales.sort_values('Month')
        fig_month = px.line(monthly_sales,
                           x='Month',
                           y='Total',
                           title='Tendencia de Volumen de Ventas por Mes')
        st.plotly_chart(fig_month, use_container_width=True)

    with col2:
        daily_sales = df_filtered.groupby('DayOfWeek')['Total'].sum().reset_index()
        day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        daily_sales['DayOfWeek'] = pd.Categorical(daily_sales['DayOfWeek'], categories=day_order, ordered=True)
        daily_sales = daily_sales.sort_values('DayOfWeek')
        fig_day = px.line(daily_sales,
                     x='DayOfWeek',
                     y='Total',
                     title='Tendencia de Volumen de Ventas por Día de la Semana')
        st.plotly_chart(fig_day, use_container_width=True)
else:
    st.warning("No hay datos para las ciudades seleccionadas.")


st.subheader("Ingresos Brutos por Ciudad")
st.write("Este gráfico muestra los ingresos brutos totales generados por cada ciudad seleccionada.")
if not df_filtered.empty:
    city_performance = df_filtered.groupby('City').agg(
        GrossIncomeTotal=('GrossIncome', 'sum'),
        GrossMarginAverage=('GrossMargin%', 'mean')
    ).reset_index()
    fig_income = px.bar(city_performance,
                        x='City',
                        y='GrossIncomeTotal',
                        title='Ingresos Brutos por Ciudad')
    st.plotly_chart(fig_income, use_container_width=True)
else:
    st.warning("No hay datos para las ciudades seleccionadas.")


st.header("Análisis de Clientes")

st.subheader("Total Compras por Perfil de Cliente")
st.write("Este gráfico de pastel muestra la distribución total de compras entre clientes nuevos y recurrentes en las ciudades seleccionadas.")
if not df_filtered.empty:
    customer_spending_type = df_filtered.groupby('CustomerType')['Total'].sum().reset_index()
    fig_customer_type_pie = px.pie(customer_spending_type,
                 values='Total',
                 names='CustomerType',
                 title='Total Compras por Perfil de Cliente')
    st.plotly_chart(fig_customer_type_pie, use_container_width=True)
else:
    st.warning("No hay datos para las ciudades seleccionadas.")

st.subheader("Total Compras por Perfil de Cliente por Ciudad")
st.write("Este gráfico de barras muestra el total de compras desglosado por perfil de cliente y ciudad para las ciudades seleccionadas.")
if not df_filtered.empty:
    customer_spending = df_filtered.groupby(['CustomerType', 'City'])['Total'].sum().reset_index()
    fig_customer_spending_city = px.bar(customer_spending,
                 x='CustomerType',
                 y='Total',
                 color='City',
                 title='Total Compras por Perfil de Cliente por Ciudad',
                 barmode='group')
    st.plotly_chart(fig_customer_spending_city, use_container_width=True)
else:
    st.warning("No hay datos para las ciudades seleccionadas.")


st.subheader("Diferencias en Compras entre Géneros")
st.write("Estos gráficos analizan las diferencias en el total de compras entre hombres y mujeres, y cómo se distribuyen por línea de producto y ciudad en las ciudades seleccionadas.")
if not df_filtered.empty:
    col3, col4 = st.columns(2)

    with col3:
        gender_spending = df_filtered.groupby('Gender')['Total'].sum().reset_index()
        fig_gender_spending = px.bar(gender_spending,
                     x='Total',
                     y='Gender',
                     title='Total Compras por Género')
        st.plotly_chart(fig_gender_spending, use_container_width=True)

    with col4:
        gender_sales_by_city = df_filtered.groupby(['Gender', 'City'])['Total'].sum().reset_index()
        fig_gender_sales_city = px.bar(gender_sales_by_city,
                     x='City',
                     y='Total',
                     color='Gender',
                     title='Total Compras por Género por Ciudad',
                     barmode='group')
        st.plotly_chart(fig_gender_sales_city, use_container_width=True)

    st.write("Mapa de Calor de Ventas por Línea de Producto y Género:")
    sales_heatmap_data = df_filtered.groupby(['Gender', 'ProductLine'])['Total'].sum().reset_index()
    fig_gender_product_heatmap = go.Figure(data=go.Heatmap(
        x=sales_heatmap_data['ProductLine'],
        y=sales_heatmap_data['Gender'],
        z=sales_heatmap_data['Total'],
        colorscale='Viridis'))

    fig_gender_product_heatmap.update_layout(
        title='Total Ventas por Línea de Producto por Género',
        xaxis_title='Línea de Producto',
        yaxis_title='Género'
    )
    st.plotly_chart(fig_gender_product_heatmap, use_container_width=True)
else:
    st.warning("No hay datos para las ciudades seleccionadas.")


st.subheader("Método de Pago Más Utilizado por Ciudad")
st.write("Este gráfico muestra la frecuencia de uso de cada método de pago en las ciudades seleccionadas.")
if not df_filtered.empty:
    payment_method_by_city = df_filtered.groupby(['City', 'Payment']).size().reset_index(name='Count')
    fig_payment_method = px.bar(payment_method_by_city,
                 x='City',
                 y='Count',
                 color='Payment',
                 title='Método de Pago Más Utilizado por Ciudad',
                 barmode='group')
    st.plotly_chart(fig_payment_method, use_container_width=True)
else:
    st.warning("No hay datos para las ciudades seleccionadas.")


st.header("Eficiencia Operativa")

st.subheader("Margen Promedio por Producto y Ciudad")
st.write("Este gráfico muestra el margen bruto promedio generado por cada línea de producto en las ciudades seleccionadas.")
if not df_filtered.empty:
    product_average_margin_amount_by_city = df_filtered.groupby(['City', 'ProductLine'])['GrossIncome'].mean().reset_index()
    fig_average_margin = px.bar(product_average_margin_amount_by_city,
                 x='ProductLine',
                 y='GrossIncome',
                 color='City',
                 title='Margen Bruto Promedio por Línea de Producto y Ciudad',
                 barmode='group')
    st.plotly_chart(fig_average_margin, use_container_width=True)
else:
    st.warning("No hay datos para las ciudades seleccionadas.")


st.subheader("Líneas de Producto con Menor Rentabilidad")
st.write("Este gráfico de barras muestra la rentabilidad total (ingreso bruto total) de cada línea de producto en las ciudades seleccionadas, ordenadas de menor a mayor rentabilidad.")
if not df_filtered.empty:
    product_line_profitability = df_filtered.groupby('ProductLine')['GrossIncome'].sum().reset_index()
    product_line_profitability = product_line_profitability.sort_values('GrossIncome', ascending=True)
    fig_profitability = px.bar(product_line_profitability,
                 x='GrossIncome',
                 y='ProductLine',
                 title='Rentabilidad por Línea de Producto (Ingreso Bruto Total)')
    st.plotly_chart(fig_profitability, use_container_width=True)
else:
    st.warning("No hay datos para las ciudades seleccionadas.")

st.subheader("Ticket Promedio por Tipo de Cliente")
st.write("Este gráfico muestra el valor promedio de una transacción ('ticket promedio') para cada tipo de cliente en las ciudades seleccionadas.")
if not df_filtered.empty:
    average_ticket_by_customer_type = df_filtered.groupby('CustomerType')['Total'].mean().reset_index()
    fig_average_ticket = px.bar(average_ticket_by_customer_type,
                 x='CustomerType',
                 y='Total',
                 title='Ticket Promedio por Tipo de Cliente')
    st.plotly_chart(fig_average_ticket, use_container_width=True)
else:
    st.warning("No hay datos para las ciudades seleccionadas.")

