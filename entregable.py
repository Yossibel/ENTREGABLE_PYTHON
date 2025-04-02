# pip install seaborn

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# ==================================================
print("================ 2. Carga y Procesamiento de Datos =================")
# ==================================================
# •	Leer el archivo CSV utilizando Pandas.
df = pd.read_csv("ventaspordepartamento.csv")

# •	Explorar la estructura de los datos 
# Número de filas
num_filas = df.shape[0]  
print("Número de filas: ", num_filas)

# Número de columnas
num_columnas = df.shape[1]  
print("Número de columnas: ", num_columnas)

# Tipos de datos por columna
tipos_datos = df.dtypes  
print("Tipos de datos por columna: ", tipos_datos)

# •	Manejo de valores nulos y datos faltantes.
# Verificar valores nulos en cada columna
print("\nValores nulos por columna:")
print(df.isnull().sum())

# Filtrar las filas que contienen valores nulos
filas_con_nulos = df[df.isnull().any(axis=1)]
print("\nFilas con valores nulos antes de la limpieza:")
print(filas_con_nulos)

# Llenar valores nulos con un valor específico
df_filled = df.fillna({
    "Tipo": "Desconocido",
    "precio de venta S/": 0
})
# Verificar si aún hay valores nulos después de la limpieza
print("\nValores nulos después de la limpieza:")
print(df_filled.isnull().sum())

# Mostrar las filas que fueron modificadas
print("\nFilas después de la limpieza:")
print(df_filled.loc[filas_con_nulos.index])

# •	Aplicar operaciones con NumPy para transformar o calcular métricas sobre los datos.
# Convertir la columna "precio de venta S/" en un array de NumPy
precios = df["precio de venta S/"].to_numpy()

# Calcular métricas básicas
promedio_precio = np.nanmean(precios)
print("Promedio del precio: ", promedio_precio, " soles")

mediana_precio = np.nanmedian(precios)
print("Mediana del precio: ", mediana_precio, " soles")

desviacion_precio = np.nanstd(precios)
print("Desviación estándar del precio: ", desviacion_precio, " soles")

# Calcular la suma total de ventas por tienda
ventas_por_tienda = df.groupby("Tienda")["precio de venta S/"].sum()
print("\nSuma total de ventas por tienda:")
print(ventas_por_tienda)

# Encontrar el precio mínimo por categoría
precio_min_categoria = df.groupby("Categoria")["precio de venta S/"].min()
print("\nPrecio mínimo por categoría:")
print(precio_min_categoria)

# Encontrar el precio máximo por categoría
precio_max_categoria = df.groupby("Categoria")["precio de venta S/"].max()
print("\nPrecio máximo por categoría:")
print(precio_max_categoria)

# ==================================================
print("====================== 3. Analisis de Datos ======================")
# ==================================================
# •	Realizar análisis descriptivo utilizando estadísticas básicas (media, mediana, desviación estándar, etc.).
# Obtener estadísticas descriptivas generales
estadisticas_descriptivas = df.describe()
# Mostrar estadísticas generales
print("Análisis Descriptivo de los Datos:\n")
print(estadisticas_descriptivas)
#MEDIA DEL PRECIO DE VENTA
mean_precio = df['precio de venta S/'].mean()
print("MEDIA DEL PRECIO DE VENTA: " + str(mean_precio))

#MEDIANA DEL PRECIO DE VENTA
median_precio = df['precio de venta S/'].median()
print("MEDIANA DEL PRECIO DE VENTA: " + str(median_precio))

#MAYOR PRECIO DE VENTA
mayor_precio = df['precio de venta S/'].max()
print("MAYOR PRECIO DE VENTA: " + str(mayor_precio))

#MENOR PRECIO DE VENTA
menor_precio = df['precio de venta S/'].min()
print("MENOR PRECIO DE VENTA: " + str(menor_precio))

#DESVIACION ESTANDAR PRECIO DE VENTA
desviacion_precio = df['precio de venta S/'].std()
print("DESVIACION ESTANDAR DEL PRECIO DE VENTA: " + str(desviacion_precio))

#VARIANZA PRECIO DE VENTA
varianza_precio = df['precio de venta S/'].var()
print("VARIANCIA DEL PRECIO DE VENTA: " + str(varianza_precio))

# •	Identificar patrones y correlaciones dentro de los datos.
# correlación entre Marca y Precio
plt.figure(figsize=(8, 6))
sns.barplot(x='Marca', y='precio de venta S/', data=df, hue="Marca", palette="coolwarm", legend=False)
plt.title('Correlación entre Marca y Precio')
plt.xlabel('Marca')
plt.ylabel('Precio de Venta S/')
plt.xticks(rotation=45)
plt.show()

# correlación entre Categoría y Precio
plt.figure(figsize=(8, 6))
sns.barplot(x='Categoria', y='precio de venta S/', data=df, hue="Categoria", palette="coolwarm", legend=False)
plt.title('Correlación entre Categoría y Precio')
plt.xlabel('Categoría')
plt.ylabel('Precio de Venta S/')
plt.xticks(rotation=45)
plt.show()

### PATRÓN 1: Distribución de ventas por tienda (Lima vs Provincias)
plt.figure(figsize=(7,5))
sns.boxplot(x="Tienda", y="precio de venta S/", data=df, hue="Tienda", palette="coolwarm", legend=False)
plt.title("Distribución de Precios de Venta por Tienda")
plt.xlabel("Tienda")
plt.ylabel("Precio de Venta (S/)")
plt.show()

### PATRÓN 2: Cantidad de productos vendidos por categoría
plt.figure(figsize=(8,5))
sns.countplot(x="Categoria", data=df, hue="Categoria", palette="viridis", legend=False)
plt.title("Cantidad de Productos Vendidos por Categoría")
plt.xlabel("Categoría")
plt.ylabel("Frecuencia")
plt.xticks(rotation=45)
plt.show()

### PATRÓN 3: Relación entre precio de venta y marca
plt.figure(figsize=(7,5))
sns.scatterplot(x="precio de venta S/", y="Marca", hue="Tienda", data=df, alpha=0.7)
plt.title("Relación entre Precio de Venta y Marca")
plt.xlabel("Precio de Venta (S/)")
plt.ylabel("Marca")
plt.legend(title="Tienda")
plt.show()

# •	Aplicar filtros y segmentaciones relevantes.
### FILTRO 1: Productos con precio mayor a S/100
productos_precios_altos = df[df["precio de venta S/"] > 100]
print("Productos con precio mayor a S/100:")
print(productos_precios_altos.head())

### FILTRO 2: Segmentar ventas por Tienda
ventas_lima = df[df["Tienda"] == "Lima"]
ventas_provincias = df[df["Tienda"] == "Provincias"]

print(f"\nVentas en Lima: {ventas_lima.shape[0]} filas")
print(f"Ventas en Provincias: {ventas_provincias.shape[0]} filas")

### FILTRO 3: los productos de la marca más frecuente
marcas_frecuentes = df["Marca"].value_counts()
marca_mas_frecuente = marcas_frecuentes.idxmax()
productos_marca_mas_frecuente = df[df["Marca"] == marca_mas_frecuente]
print("\nProductos de la marca más frecuente:")
print(productos_marca_mas_frecuente)

### FILTRO 4: Segmentación de ventas por Categoría de Producto
categorias_ventas = df.groupby("Categoria")["precio de venta S/"].sum()
print("\nVentas totales por Categoría de Producto:")
print(categorias_ventas)

### FILTRO 5: MEDIA DEL PRECIO DE VENTA POR MARCA
media_precio_marca = df.groupby("Marca")["precio de venta S/"].mean().sort_values(ascending=False)
print("MEDIA DE PRECIO POR MARCA:\n" + str(media_precio_marca))

#FILTRO 6: MEDIA DEL PRECIO DE VENTA POR TIENDA
media_precio_tienda = df.groupby("Tienda")["precio de venta S/"].mean().sort_values(ascending=False)
print("MEDIA DE PRECIO POR TIENDA:\n" + str(media_precio_tienda))

#FILTRO 7: VENTAS EN LIMA
filtro_lima = df[df["Tienda"] == "Lima"]
print("VENTAS EN LIMA:\n" + str(filtro_lima))
print("TOTAL DE VENTAS EN LIMA: " + str(len(filtro_lima)))

# ==================================================
print("============== 4. Visualizacion de Datos =============================")
# ==================================================

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