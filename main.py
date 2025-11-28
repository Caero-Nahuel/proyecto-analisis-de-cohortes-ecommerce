import sys
import os
import pandas as pd

# Añadimos el directorio actual al path para poder importar src
sys.path.append(os.getcwd())

from src.utils import load_and_merge_raw_data, clean_data, calculate_rfm_metrics, segment_customers

# --- CONFIGURACIÓN ---
RAW_DATA_PATH = './data/raw'
OUTPUT_PATH = './data/processed/rfm_final_segmentation.csv'

def main():
    print("🚀 Iniciando Pipeline de Segmentación de Clientes...")

    # 1. Carga
    print("\n[1/4] Cargando y fusionando datos raw...")
    df_raw = load_and_merge_raw_data(RAW_DATA_PATH)
    
    if df_raw is None:
        print("⛔ Deteniendo ejecución por error en carga.")
        return

    # 2. Limpieza
    print(f"\n[2/4] Limpiando datos (Filas iniciales: {len(df_raw)})...")
    df_clean = clean_data(df_raw)
    print(f"      -> Filas tras limpieza: {len(df_clean)}")

    # 3. Cálculo RFM
    print("\n[3/4] Calculando métricas RFM y Scores...")
    df_rfm = calculate_rfm_metrics(df_clean)
    print("      -> Scores calculados exitosamente.")

    # 4. Segmentación
    print("\n[4/4] Aplicando reglas de negocio (Gold/Silver/Bronze)...")
    df_final = segment_customers(df_rfm)

    # --- RESULTADOS ---
    print("\n" + "="*40)
    print("📊 RESUMEN DE SEGMENTACIÓN")
    print("="*40)
    summary = df_final['Segment'].value_counts(normalize=True) * 100
    print(summary.to_string(float_format="%.2f%%"))
    print("="*40)

    # Guardado
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    df_final.to_csv(OUTPUT_PATH, index=False)
    print(f"\n✅ Pipeline finalizado. Resultados guardados en:\n   {OUTPUT_PATH}")

if __name__ == "__main__":
    main()