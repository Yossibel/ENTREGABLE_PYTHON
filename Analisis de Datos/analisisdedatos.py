import pandas as pd;

df = pd.read_csv("ventaspordepartamento.csv", encoding='latin1')
print(df)

# ANALISIS DE DATOS

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

#MEDIA DEL PRECIO DE VENTA POR MARCA
media_precio_marca = df.groupby("Marca")["precio de venta S/"].mean().sort_values(ascending=False)
print("MEDIA DE PRECIO POR MARCA:\n" + str(media_precio_marca))

#MEDIA DEL PRECIO DE VENTA POR TIENDA
media_precio_tienda = df.groupby("Tienda")["precio de venta S/"].mean().sort_values(ascending=False)
print("MEDIA DE PRECIO POR TIENDA:\n" + str(media_precio_tienda))

#VENTAS EN LIMA
filtro_lima = df[df["Tienda"] == "Lima"]
print("VENTAS EN LIMA:\n" + str(filtro_lima))

#TOTAL DE VENTAS EN LIMA
print("TOTAL DE VENTAS EN LIMA: " + str(len(filtro_lima)))

#VENTAS EN OTROS
filtro_otros = df[df["Tienda"] != "Lima"]
print("VENTAS EN PROVINCIA:\n" + str(filtro_otros))

#TOTAL DE VENTAS EN OTROS
print("TOTAL DE VENTAS EN OTROS: " + str(len(filtro_otros)))

#CORRELACIONES Y PATRONES ENCONTRADOS
#1)La mayoría de los precios se concentran entre S/ 24 y S/ 99
#2)Los precios tienden a ser mas caros en Lima que en Provincias
#3)Los precios de Adidas tienden a ser mas caros que las demas marcas