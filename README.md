# 📊 Análisis de Ventas Minoristas

Este repositorio contiene un estudio de caso de analítica de datos aplicado a un dataset de ventas minoristas.  
El análisis incluye estadísticas descriptivas, visualizaciones y resultados clave sobre rendimiento de ventas, comportamiento de clientes y eficiencia operativa.  

👉 [Tablero Interactivo en Streamlit](https://dashboard-ventas-minoristas.streamlit.app/)



---

## 📌 Resumen General

El análisis se realizó sobre el dataset **retail_sales_dataset**.  
Se aplicaron estadísticas descriptivas, gráficos (boxplots, histogramas, correlaciones) y visualizaciones que permiten responder preguntas clave de negocio.  

En general:
- Buen desempeño en ventas.
- Diferencias de rentabilidad por ciudad y línea de producto.
- Patrones de compra según género, tipo de cliente y método de pago.

---

## 🗂 Reconocimiento de los Datos

El dataset contiene información de ventas:  

| Columna       | Descripción |
|---------------|-------------|
| OrderID       | Identificador único de orden |
| OrderDate     | Fecha de la venta |
| Branch        | Código de sucursal |
| City          | Ciudad de la sucursal |
| CustomerType  | Cliente nuevo o recurrente |
| Gender        | Género del cliente |
| ProductLine   | Categoría de producto |
| UnitPrice     | Precio unitario |
| Quantity      | Unidades vendidas |
| Payment       | Método de pago |
| Total         | Total de la venta |
| COGS          | Costo de bienes vendidos |
| GrossIncome   | Ingreso bruto |
| GrossMargin%  | Margen de ganancia |
| Rating        | Satisfacción del cliente |

---

## 🔍 Análisis Exploratorio de Datos

- **Estadísticas descriptivas** → Distribución y dispersión de precios, ingresos y calificaciones.  


- **Boxplots (cajas y bigotes)** → Distribución simétrica sin outliers extremos.  
 
- **Histogramas** → Asimetría positiva en ventas, costos e ingresos.  

- **Matriz de Correlación** → Relaciones fuertes entre variables financieras, rating sin correlación con métricas económicas.  
 

---

## 📈 Resultados

### Rendimiento de Ventas
- **Producto más vendido por ciudad:**  
  - Guadalajara → Laptops  
  - Mexico City → Accessories  
  - Monterrey → Audio  
 

- **Ventas por día de la semana:**  
  - Mayor: Sábado  
  - Menor: Domingo  
 

- **Ventas por mes:**  
  - Pico en Enero  
  - Caída hasta Septiembre con repunte al final del año  


- **Ingresos por ciudad:**  
  - 1️⃣ Mexico City  
  - 2️⃣ Guadalajara  
  - 3️⃣ Monterrey  
 

---

### Análisis de Clientes
- **Tipo de cliente:**  
  - Nuevos generan más ingresos (52%) que recurrentes (48%).  


- **Compras por género:**  
  - Hombres gastan más en general.  
  - Mujeres destacan en **Laptops**.  
 
- **Métodos de pago:**  
  - Cash es el más utilizado en todas las ciudades.  
  - Credit Card es el menos usado.  
 
---

### Eficiencia Operativa
- **Margen bruto promedio:** Más alto en **Laptops** y **Accessories**.  
 

- **Rentabilidad:** Laptops, Accessories y Audio son los más rentables; Gaming y TV los menos.  


- **Ticket promedio:** Clientes nuevos gastan ligeramente más por transacción que recurrentes.  


---

## 📊 Visualizaciones

Además de este informe, se construyó un tablero interactivo en **Streamlit**:  
👉 [Ver Tablero](https://dashboard-ventas-minoristas.streamlit.app/)

---

## ✅ Conclusiones

- Identificación de productos más vendidos y ciudades con mayor ingreso.  
- Patrones de compra por género, ciudad y tipo de cliente.  
- Cash domina como método de pago.  
- Laptops y Accessories generan mayor rentabilidad.  
- Ticket promedio mayor en clientes nuevos.  

Estos hallazgos sirven como base para mejorar la estrategia de ventas, marketing y gestión de inventarios.

---

## 📚 Referencias

- IBM. CRISP-DM: metodología estándar para proyectos de minería de datos.  
- Microsoft (2025). *Análisis de ventas*.  
- Rojas, S. (2024). *Estrategias y planificación de ventas*. Corporación Universitaria de Asturias.  

---
