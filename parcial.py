import pandas as pd
M_Id_Class_Eco = pd.read_csv('Id_Class_Eco.csv',sep=';') #Asi lees los archivos csv, como este es separado por ';' entonces se le pone sep=';' si fuera separado por no sé '/' entoncs es sep='/'
M_Id_Class_Eco.index = M_Id_Class_Eco['DIRECTORIO']
M_TIC = pd.read_csv('M_TIC.csv',sep=';')
M_TIC.index = M_Id_Class_Eco['DIRECTORIO']
print(M_TIC.describe())
print(M_TIC.info(verbose=True))
M_Ventas_Ingresos = pd.read_csv('M_Ventas_Ingresos.csv',sep=';')
M_Ventas_Ingresos = M_Ventas_Ingresos['DIRECTORIO']
M_Id_Class_Eco.rename(columns={'P35': 'Gender', 'P241':'Edad'}, inplace=True) #Asi se renombran las columnas
print(M_Id_Class_Eco.columns)
M_Id_Class_Eco.drop(['P3032_1','P3032_2'], axis=1, inplace=True) #Asi borras varias columnas
print(M_Id_Class_Eco.columns)
consolidado_Id_TIC = M_Id_Class_Eco.merge(M_TIC, left_index=True, right_index=True) #Asi unes las matrices por indice
consolidado_Id_TIC_Ventas = consolidado_Id_TIC.merge(M_Ventas_Ingresos, left_index=True, right_index=True)
