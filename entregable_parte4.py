import pandas as pd
import matplotlib.pyplot as plt
# ==================================================
# 2. Carga y Procesamiento de Datos
# ==================================================
# •	Leer el archivo CSV utilizando Pandas.
df = pd.read_csv("ventaspordepartamento.csv")


# ===================================================
# 4. Visualizacion de Datos
# ===================================================

# •	Gráfico de líneas: Evolución del precio promedio por categoría
precio_promedio_categoria = df.groupby("Categoria")["precio de venta S/"].mean()
plt.figure(figsize=(8,5))
plt.plot(precio_promedio_categoria.index, precio_promedio_categoria.values, marker='o', linestyle='-', color='b')
plt.xlabel("Categoría")
plt.ylabel("Precio Promedio (S/)")
plt.title("Evolución del Precio Promedio por Categoría")
plt.grid(True)
plt.show()

# •	Gráfico de barras: Total de ventas por tienda
ventas_tienda = df.groupby("Tienda")["precio de venta S/"].sum()
plt.figure(figsize=(8,5))
plt.bar(ventas_tienda.index, ventas_tienda.values, color=['blue', 'green'])
plt.xlabel("Tienda")
plt.ylabel("Total de Ventas (S/)")
plt.title("Total de Ventas por Tienda")
plt.show()

# •	Gráfico de torta: Distribución de productos por categoría
productos_categoria = df["Categoria"].value_counts()
plt.figure(figsize=(7,7))
plt.pie(productos_categoria, labels=productos_categoria.index, autopct='%1.1f%%', colors=['red', 'blue', 'green', 'yellow'])
plt.title("Distribución de Productos por Categoría")
plt.show()

# •	Histograma: Distribución de precios de venta
plt.figure(figsize=(8,5))
plt.hist(df["precio de venta S/"], bins=10, color='purple', edgecolor='black', alpha=0.7)
plt.xlabel("Precio de Venta (S/)")
plt.ylabel("Frecuencia")
plt.title("Distribución de Precios de Venta")
plt.show()


