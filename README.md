# 📊 Análisis de Segmentación de Clientes & Estrategia RFM (E-Commerce)

## Resumen Ejecutivo
Este proyecto transforma datos transaccionales crudos de **Olist** (E-Commerce brasileño) en una estrategia de segmentación de clientes accionable utilizando la metodología **RFM (Recencia, Frecuencia, Monetización)**.  
El objetivo es resolver el problema de la "talla única" en marketing, permitiendo identificar a los clientes VIP y reactivar usuarios en riesgo.

---

## 🚀 Contexto de Negocio y Problema

En un entorno de e-commerce saturado, el **costo de adquisición de clientes (CAC)** suele ser alto.  
El desafío principal de Olist es **retener usuarios existentes y maximizar su valor de vida (LTV)**.

Este proyecto responde a las siguientes preguntas estratégicas:

- ¿Quiénes son nuestros clientes más valiosos (Gold/Champions)?
- ¿Qué porcentaje de la base de usuarios está inactiva o en riesgo de fuga (Churn)?
- ¿Cómo podemos personalizar campañas de marketing basándonos en comportamiento real de compra?

---

## 🛠️ Stack Tecnológico y Metodología

El enfoque priorizó la **escalabilidad** y el **código limpio**, alejándose de notebooks monolíticos para simular un entorno productivo.

- **Python 3.13 & Pandas**: Ingeniería de características y manipulación vectorial de datos.
- **Pipeline ETL Modular**: Separación entre extracción, limpieza y carga (`src/utils.py`).
- **Análisis RFM**: Scoring mediante quintiles estadísticos (`pd.qcut` y `rank` para sesgos de frecuencia).
- **Visualización**: Matplotlib/Seaborn para storytelling de datos.
- **Entorno**: Gestión de dependencias reproducible con Conda.

---

## 📊 Key Insights (Resultados Clave)

Tras analizar **+100k órdenes**, se segmentó la base de usuarios en tres categorías principales.

> *(Nota: El gráfico anterior es un placeholder. Ejecutá `main.py` para generar la visualización actualizada.)*

### Hallazgos Principales:

- **Retención problemática**: Aproximadamente el **96% de los usuarios compró una sola vez**, ubicándose en el segmento *Bronze* o *Promedio*.
- **Los Gold importan mucho**: Representan **menos del 1% de la base**, pero generan un porcentaje desproporcionado de ingresos recurrentes.
- **Acción Recomendada**: Implementar *programas de fidelización* para el segmento **Silver**, que tiene potencial para convertirse en recurrente.

---

## 📂 Estructura del Repositorio

El proyecto sigue una estructura basada en **Cookiecutter Data Science** para garantizar orden y reproducibilidad:

```bash
📁 analisis-de-cohortes
├── 📂 data
│   ├── 📄 raw/                  # Datos originales (inmutables)
│   └── 📄 processed/            # Datos limpios y tablas maestras
├── 📂 notebooks
│   ├── 📘 01_data_cleaning.ipynb   # Prototipado de limpieza
│   └── 📘 02_rfm_analysis.ipynb    # Lógica de segmentación paso a paso
├── 📂 src
│   ├── 📄 __init__.py
│   └── ⚙️ utils.py               # Módulos reutilizables (ETL, Scoring)
├── 📄 environment.yml            # Definición del entorno Conda
├── ▶️ main.py                    # Script orquestador (Pipeline completo)
└── 📄 README.md                  # Documentación del proyecto

## ⚙️ Guía de Instalación y Uso

Sigue estos pasos para replicar el análisis en tu entorno local:

---

### 🧩 1. Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/olist-rfm-analysis.git
cd Nombredelrepositorio

### 📦 2. Crear el entorno virtual (Conda)

Este proyecto utiliza `environment.yml` para garantizar un entorno reproducible.

```bash
conda env create -f environment.yml
conda activate olist_env
```

### 📦 3. Ejecutar el pipeline
El script main.py ejecuta todo el flujo:

- Carga de datos
- Limpieza
- Cálculo de métricas RFM
- Exportación de resultados

```bash
python main.py
```
## 📁 Resultado

Al finalizar, encontrarás el archivo generado:

`data/processed/rfm_final_segmentation.csv`

---

Si querés, puedo integrarlo directamente con tu estructura de carpetas y el resto del README para dejarlo 100% profesional.

---

## ✒️ Autor

**[Nahuel Caero] — Data Scientist en formación**  
Conectando datos con estrategia de negocio.

🔗 [**LinkedIn**](https://www.linkedin.com/in/nahuel-agustin-caero/)

---

Este proyecto utiliza el dataset público:

🔗 [**Brazilian E-Commerce Public Dataset by Olist**](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce/) disponible en *Kaggle*.