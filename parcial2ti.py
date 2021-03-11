#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import matplotlib.pyplot as plt
# # Parcial Segundo Corte TI# ##### ESTUDIANTE:  ANGIE XIMENA MACHADO
# ##### COD: 1010244188
# ModIdent = pd.read_excel("identificacion.xlsx", index_col=0)
ModIdent = pd.read_csv('Id_Class_Eco.csv',sep=';')

# ModTIC = pd.read_excel("mTIC.xlsx", index_col=0)
ModTIC = pd.read_csv('M_TIC.csv',sep=';')

# VentasIngresos = pd.read_excel("ventasingresos.xlsx", index_col=0)
VentasIngresos = pd.read_csv('M_Ventas_Ingresos.csv',sep=';')

#print(ModTIC.info(verbose=True))

#print(ModIdent.info(verbose=True))

#print(VentasIngresos.info(verbose=True))

#print(ModTIC.head(5))

#print(ModTIC.columns)

#Eliminar columnas de la matriz TIC
ModTIC.drop(['SECUENCIA_ENCUESTA', 'SECUENCIA_P', 'P4001', 'P1087',
       'P1088', 'P977', 'P976', 'P978', 'P979', 'P994', 'P2532',
       'P2524', 'P1093', 'P2528', 'P1095', 'P980', 'P1006_1', 'P1006_2',
       'P1006_3', 'P1006_4', 'P1006_5', 'P1006_8',
       'P1006_9', 'P1006_10', 'P1006_11', 'P1006_12', 'P1006_13'], axis=1, inplace=True)
#print(ModTIC.columns)

#print(ModTIC.head(5))

ModTIC.rename(columns={'P1559': 'URedesSociales', 'P1006_6': 'ComprasXInternet', 'P1006_7': 'VentasXInternet' }, inplace=True) #Asi se renombran las columnas
#print(ModTIC.columns)

#print(ModIdent.head(5))

#print(ModIdent.columns)

#Eliminar columnas de la matriz identificacion
ModIdent.drop(['SECUENCIA_ENCUESTA', 'SECUENCIA_P', 'AREA', 'CLASE',
       'P35', 'P241', 'MES_REF', 'P3031', 'P3032_2',
       'P3033', 'P3034', 'P3035', 'P3000', 'GRUPOS4', 'F_EXP'], axis=1, inplace=True)
#print(ModIdent.columns)

ModIdent.rename(columns={'COD_DEPTO': 'UbicacionOrg', 'P3032_1': 'TPagos', 'P3032_3': 'TsinPago', 'GRUPOS12': 'Sectores' }, inplace=True) #Asi se renombran las columnas
#print(ModIdent.columns)

#print(VentasIngresos.head(5))

#print(VentasIngresos.columns)

#Eliminar columnas de la matriz Ventas e Ingresos
VentasIngresos.drop(['SECUENCIA_ENCUESTA', 'SECUENCIA_P', 'P3057', 'P3058', 'P3059', 'P3060',
       'P3061', 'P3062', 'P4002', 'P3063', 'P3064', 'P3065', 'P3066', 'P3067',
       'P3092', 'P3093', 'P4005', 'P4006', 'P4007', 'P4008', 'P4009', 'P4010',
       'P4011', 'P4012', 'P4013', 'P4014', 'P4015', 'P4016', 'P4017', 'P4018',
       'P3075', 'P3068_ENE', 'P3068_1', 'P3068_FEB', 'P3068_2', 'P3068_MAR',
       'P3068_3', 'P3068_ABR', 'P3068_4', 'P3068_MAY', 'P3068_5', 'P3068_JUN',
       'P3068_6', 'P3068_JUL', 'P3068_7', 'P3068_AGO', 'P3068_8', 'P3068_SEP',
       'P3068_9', 'P3068_OCT', 'P3068_10', 'P3068_NOV', 'P3068_11',
       'P3068_DIC', 'P3068_12', 'P3068_TOD', 'P3068_NIN', 'P4019', 'P4020',
       'P4021', 'P4022', 'P4023', 'P4024', 'P4025', 'P4026', 'P4027', 'P4028',
       'P4029', 'P4030', 'P4031', 'P4032'], axis=1, inplace=True)
#print(VentasIngresos.columns)

VentasIngresos.rename(columns={'P3072': 'Utilidad', 'VENTAS_MES_ANTERIOR': 'VmesAnterior', 'VENTAS_MES_ANIO_ANTERIOR': 'VmesAnoAnterior', 'VENTAS_ANIO_ANTERIOR': 'VanoAnterior' }, inplace=True)
#print(VentasIngresos.columns)
consolidado = VentasIngresos.merge(ModTIC, left_index=True, right_index=True)
consolidadoFinal = consolidado.merge(ModIdent, left_index=True, right_index=True)
#print(consolidadoFinal.head(5))
consolidadoFinal['CantEmpleados'] =consolidadoFinal['TPagos'] + consolidadoFinal['TsinPago']
consolidadoFinal.head()
consolidadoFinal.drop(['TPagos', 'TsinPago'], axis=1, inplace=True )
#print(consolidadoFinal.columns)
#print(consolidadoFinal.head(5))
# ## Gráficas#
# consolidadoFinal.plot.bar(x='Sectores', y='Utilidad', rot=0)
pcien = consolidadoFinal[:100]
pcien['Utilidad'] = pd.to_numeric(pcien['Utilidad'])#convertir a tipo numero para que pueda hacer el group by
GraficaXSectores = pcien[['Sectores', 'Utilidad','VentasXInternet', 'CantEmpleados', 'UbicacionOrg']] #Solo las columnas que se necesitan para graficar
GraficaXSectores['VentasXInternet'] = GraficaXSectores['VentasXInternet'].replace('\\s', '0', regex=True) #Cambiar espacios vacios por cero '\s' -> regular expression de un espacio
GraficaXSectores['VentasXInternet'] = pd.to_numeric(GraficaXSectores['VentasXInternet'])
GraficaXSectores['CantEmpleados'] = GraficaXSectores['CantEmpleados'].replace('\\s', '0', regex=True)
GraficaXSectores['CantEmpleados'] = pd.to_numeric(GraficaXSectores['CantEmpleados'])
#print(GraficaXSectores.info(verbose=True))
GroupBySectores = GraficaXSectores.groupby('Sectores').sum()#Agrupar por sectores y sumar
# print(GroupBySectores.head(5))
# GraficaXSectores
# plt.figure(figsize=(9, 4))
# plt.subplot(141, ylabel='Utilidad')
# plt.bar(GroupBySectores.index, GroupBySectores["Utilidad"])
# plt.subplot(142,ylabel='VentasXInternet')
# plt.bar(GroupBySectores.index, GroupBySectores["VentasXInternet"])
# plt.subplot(143,ylabel='CantEmpleados')
# plt.bar(GroupBySectores.index, GroupBySectores["CantEmpleados"])
# plt.subplot(144,ylabel='UbicacionOrg')
# plt.scatter(GraficaXSectores['Sectores'], GraficaXSectores["UbicacionOrg"])
# plt.suptitle('SECTORES')
# plt.show()
#print(GroupBySectores.head(3))
GroupBySectores.plot.bar(y='Utilidad', rot = 0)
plt.show()