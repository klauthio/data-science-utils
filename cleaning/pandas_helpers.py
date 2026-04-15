import pandas as pd

def get_data_report(df):
    """
    Genera un reporte resumido sobre la calidad del DataFrame.
    
    Muestra:
    - Cantidad de filas y columnas.
    - Tipos de datos por columna.
    - Conteo de nulos y su porcentaje.
    - Cantidad de valores únicos.
    """
    print(f"--- Resumen del Dataset ---")
    print(f"Filas: {df.shape[0]}")
    print(f"Columnas: {df.shape[1]}")
    print(f"Duplicados: {df.duplicated().sum()}")
    print("-" * 27)
    
    report = pd.DataFrame({
        'Dtype': df.dtypes,
        'Nulos': df.isnull().sum(),
        '% Nulos': (df.isnull().sum() / len(df)) * 100,
        'Unicos': df.nunique()
    })
    
    return report

def clean_column_names(df):
    """
    Estandariza los nombres de las columnas: minúsculas, sin espacios y sin tildes.
    Ideal para datasets con nombres de columnas desordenados.
    """
    df.columns = (df.columns
                  .str.strip()
                  .str.lower()
                  .str.replace(' ', '_', regex=False)
                  .str.replace('á', 'a')
                  .str.replace('é', 'e')
                  .str.replace('í', 'i')
                  .str.replace('ó', 'o')
                  .str.replace('ú', 'u'))
    return df
