import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta


# Configuración inicial de parámetros para la generación del dataset
num_registros = 1000
marcas_modelos = {
    'Chevrolet': ['Aveo', 'Onix', 'Chevy', 'Trax', 'Silverado'],
    'Nissan': ['Versa', 'Sentra', 'March', 'Kicks', 'Frontier'],
    'Volkswagen': ['Jetta', 'Vento', 'Polo', 'Tiguan', 'Saveiro'],
    'Ford': ['Figo', 'Focus', 'Escape', 'Explorer', 'Ranger'],
    'Honda': ['Civic', 'City', 'CR-V', 'HR-V', 'Accord']
}
estatus_lista = ['Vendido', 'En Lote', 'En Taller', 'Vendido', 'Vendido'] # Mayor probabilidad de vendido
sucursales = ['Barragán', 'Linda Vista', 'Cumbres', 'Sendero']

datos = []
fecha_actual = datetime(2026, 6, 26)

for i in range(num_registros):
    id_vehiculo = f"VIN{10000 + i}"
    marca = random.choice(list(marcas_modelos.keys()))
    modelo = random.choice(marcas_modelos[marca])
    anio = random.randint(2015, 2024)
    kilometraje = random.randint(15000, 150000)
    
    # Lógica financiera básica establecida
    precio_compra = random.randint(100000, 450000)
    costo_reacondicionamiento = random.randint(2000, 25000)
    # Margen esperado entre 10% y 30%
    margen_esperado = random.uniform(1.10, 1.30)
    precio_venta = int((precio_compra + costo_reacondicionamiento) * margen_esperado)
    
    estatus = random.choice(estatus_lista)
    sucursal = random.choice(sucursales)
    
    # Lógica de fechas
    dias_en_lote_historico = random.randint(5, 90)
    fecha_ingreso = fecha_actual - timedelta(days=random.randint(10, 150))
    
    if estatus == 'Vendido':
        fecha_venta = fecha_ingreso + timedelta(days=dias_en_lote_historico)
    else:
        fecha_venta = pd.NaT # Nulo si aún no se vende
        
    datos.append([
        id_vehiculo, marca, modelo, anio, kilometraje, sucursal, estatus,
        fecha_ingreso.strftime('%Y-%m-%d'), 
        fecha_venta.strftime('%Y-%m-%d') if pd.notna(fecha_venta) else np.nan,
        precio_compra, costo_reacondicionamiento, precio_venta
    ])

# Creación de DataFrame y archivo a exportar
columnas = ['ID_Vehiculo', 'Marca', 'Modelo', 'Anio', 'Kilometraje', 'Sucursal', 'Estatus', 
            'Fecha_Ingreso', 'Fecha_Venta', 'Precio_Compra', 'Costo_Reacondicionamiento', 'Precio_Venta_Publicado']

df = pd.DataFrame(datos, columns=columnas)

# Se agregarón datos sucios para simular la realidad del dataset en este caso de estudio un 5%
indices_nulos = df.sample(frac=0.05).index
df.loc[indices_nulos, 'Kilometraje'] = np.nan
df.loc[df.sample(frac=0.02).index, 'Sucursal'] = 'Desconocida'

df.to_csv('dataset_seminuevos_mx.csv', index=False)
print("¡Dataset 'dataset_seminuevos_mx.csv' generado con éxito con 1000 registros!")