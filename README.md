# Obligatorio de Machine Learning - Predicción de Precios de Airbnb

Este repositorio contiene el desarrollo del trabajo obligatorio para el curso de Machine Learning. El objetivo del proyecto es construir un modelo predictivo para estimar el precio de alojamientos de Airbnb utilizando técnicas de aprendizaje automático.

## Estructura del Repositorio

El proyecto está organizado de la siguiente manera:

*   **`Obligatorio_ML.ipynb`**: Jupyter Notebook principal. Contiene todo el flujo de trabajo:
    *   Análisis Exploratorio de Datos (EDA).
    *   Limpieza y Preprocesamiento.
    *   Ingeniería de Características (Feature Engineering).
    *   Entrenamiento y optimización de modelos (GridSearch).
    *   Evaluación y generación de predicciones.
*   **`Informe/`**: Código fuente del informe técnico en LaTeX.
    *   El archivo principal es `Obligatorio.tex`.
    *   Contiene subcarpetas para imágenes (`img/`), tablas (`tables/`) y secciones (`tex/`).
*   **`pred/`**: Directorio de salida para los archivos CSV con las predicciones generadas por los diferentes modelos.
*   **`img/`**: Gráficos generados por el notebook (histogramas, análisis de percentiles, etc.).
*   **`train.csv` / `test.csv`**: Conjuntos de datos de entrenamiento y prueba.
*   **`setup_python_env.sh`**: Script de Bash para automatizar la creación del entorno virtual y la instalación de dependencias.

## Instalación y Configuración

Para asegurar la reproducibilidad del entorno, sigue estos pasos:

1.  **Ejecutar el script de configuración**:
    Este script buscará una instalación de Python adecuada, creará un entorno virtual (por defecto en `.venv`) e instalará las librerías necesarias.
    ```bash
    chmod +x setup_python_env.sh
    ./setup_python_env.sh
    ```

2.  **Activar el entorno virtual**:
    ```bash
    source .venv/bin/activate
    ```

## Uso

1.  Abre el archivo `Obligatorio_ML.ipynb` en VS Code o Jupyter Lab.
2.  Selecciona el kernel correspondiente al entorno virtual creado (`.venv`).
3.  Ejecuta las celdas en orden secuencial.

> **Nota**: El notebook está configurado para exportar automáticamente tablas y gráficos a las carpetas del informe (`Informe/tex/tables` e `Informe/img`).

## Informe

El informe final se encuentra en la carpeta `Informe`. Para compilarlo, asegúrate de tener una distribución de LaTeX instalada (como TeX Live) y compila el archivo `Obligatorio.tex`.

## Información del Sistema

El script `env.py` (si se utiliza) o las celdas correspondientes en el notebook pueden generar un archivo `system_info.json` con detalles sobre el hardware y software utilizado para el entrenamiento, facilitando la comparación de tiempos de ejecución.