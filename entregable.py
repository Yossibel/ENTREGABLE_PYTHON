import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# ==================================================
# 2. Carga y Procesamiento de Datos
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

# 
