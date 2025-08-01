# utils/leer_excel.py

import openpyxl


def leer_datos_excel(path, hoja="Hoja1"):
    wb = openpyxl.load_workbook(path)
    sheet = wb[hoja]
    datos = []

    # Leer encabezados
    headers = [cell.value for cell in sheet[1]]

    for row in sheet.iter_rows(min_row=2, values_only=True):
        fila = dict(zip(headers, row))
        datos.append((fila["username"], fila["password"]))
    return datos
