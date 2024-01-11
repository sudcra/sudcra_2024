from xlsx_a_df import convertir_a_df_tipo_2

ruta="C:\\Users\\mcorteze\\Desktop\\EMP1101-041V_VALPARAISO_E3.xlsm"

df=convertir_a_df_tipo_2(ruta, "EMP1101-041V", 9, 52, 1, 3)
print(df)