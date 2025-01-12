import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
try:
    datos = pd.read_csv("rendimiento_acciones.csv", index_col=0, parse_dates=True)
    print("Datos cargados con éxito:")
    print(datos.head())  # Verifica las primeras filas
except FileNotFoundError:
    print("Error: El archivo 'rendimiento_acciones.csv' no existe.")
    exit()

# Eliminar valores nulos (si los hay)
datos = datos.dropna()

# Calcular rendimiento diario
rendimiento = datos.pct_change()

# Calcular métricas clave
promedio = rendimiento.mean() * 252  # Rendimiento anualizado
volatilidad = rendimiento.std() * (252 ** 0.5)  # Volatilidad anualizada

print("\nRendimiento promedio anualizado:")
print(promedio)
print("\nVolatilidad anualizada:")
print(volatilidad)

# Visualizar los datos
if not datos.empty:
    datos.plot(figsize=(10, 6), title="Precios ajustados de cierre")
    plt.show()
else:
    print("No hay datos para graficar.")# Calcular medias móviles
media_corto_plazo = datos.rolling(window=20).mean()  # Media móvil de 20 días
media_largo_plazo = datos.rolling(window=50).mean()  # Media móvil de 50 días

# Visualizar los datos con medias móviles
plt.figure(figsize=(14, 7))
for columna in datos.columns:
    plt.plot(datos.index, datos[columna], label=f"{columna} - Precios ajustados")
    plt.plot(media_corto_plazo.index, media_corto_plazo[columna], linestyle='--', label=f"{columna} - Media 20 días")
    plt.plot(media_largo_plazo.index, media_largo_plazo[columna], linestyle=':', label=f"{columna} - Media 50 días")

plt.title("Precios ajustados y medias móviles")
plt.xlabel("Fecha")
plt.ylabel("Precio")
plt.legend()
plt.show()


