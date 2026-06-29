# AutoXpert
AutoXpert Es una Empresa Ficticia. Los datos mostrados provienen de un script (Python), para realizar un caso de estudio hipotético. 
Contenido:
---
Este proyecto es una propuesta integral de Inteligencia de Negocios diseñada para el sector de retail automotriz. El objetivo principal que se abarco es proporcionar a la dirección una herramienta interactiva para auditar el capital inmovilizado, medir la rentabilidad del inventario y detectar fugas de liquidez operativa en tiempo real.

El proyecto abarca el ciclo de vida completo de los datos: desde la generación y extracción de datos con Python, hasta el modelado de negocio y visualización avanzada con Power BI y DAX.
#Herramientas y Metodología Implementada: 
*Python (/scripts/generador_datos.py):
Script desarrollado para la generación algorítmica del dataset. Simula comportamientos reales de un piso de ventas, incluyendo fechas lógicas de ingreso/venta, asignación de precios con márgenes variables y generación de datos nulos intencionales para pruebas de calidad.
[Haz clic aquí para ver el código completo que se genero en este caso de estudio(Python)](dataset_caso_estudio.py)

*Microsoft Power BI: Herramienta de visualización, utilizando un diseño minimalista, eliminación de "ruido visual" (efecto arcoíris) y paletas de colores enfocadas en la legibilidad ejecutiva.

*Formulas DAX
Aplicación de funciones iterativas (AVERAGEX), modificación de contexto (CALCULATE, KEEPFILTERS) y variables (VAR) para la creación de reglas de negocio estrictas, entre otras formulas y calculos que se detallan en el documento.

## Power BI
📸 Vista Previa del Dashboard
---
![Dashboard AutoXpert](img/dashboard.png)

 **[Interactuar con el Dashboard (Power BI Service)](https://app.powerbi.com/view?r=eyJrIjoiODI2NzU0Y2EtZGUwNi00YWE2LThlYTctN2M4ZDE5Yzk0N2Q4IiwidCI6ImNhY2E5MDExLTdiNmEtNDRkZS04NjFmLTA5NWEyY2E4ODNiNyIsImMiOjR9)**  

  **[Descargar archivo del modelo para escritorio (.pbix)](Proyecto/ReporteAutosVisual.pbix)**
