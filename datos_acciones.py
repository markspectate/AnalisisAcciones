import yfinance as yf

# Define las empresas a analizar
empresas = ["AAPL", "MSFT", "GOOGL"]  # Apple, Microsoft, Google

# Descargar datos históricos de las empresas
try:
    datos = yf.download(empresas, start="2020-01-01", end="2023-01-01")
    print(datos)  # Imprime los datos descargados para revisar
    
    # Verifica si los datos están disponibles
    if not datos.empty:
        # Guardar precios ajustados de cierre en un archivo CSV
        datos['Close'].to_csv("rendimiento_acciones.csv")
        print("Datos descargados y guardados en 'rendimiento_acciones.csv'")
    else:
        print("No se pudieron descargar los datos. Verifica los símbolos o el rango de fechas.")
except Exception as e:
    print(f"Error al descargar los datos: {e}")
    