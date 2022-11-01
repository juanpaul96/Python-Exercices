import random as rd
import pandas as pd
import pandasql as pdsql
import numpy as np
import os

os.chdir('C:/Desktop/DDC BI/DDC 2021') ##Establecer directorio de trabajo
df = pd.read_csv('DDC Rand.csv', header=0, na_filter=False)##Coger el archivo na_filter false significa que va a tener en cuenta los NA
##Transformacion de nombre de las columnas
rep = lambda cul: cul.replace(" ","_")## reemplaza los espacios por _ en los nombres de las col del data frame
cols = df.columns##Guarda el nombre de las col originales
z = list(map(rep,cols))##en una lista almacena las col con los _ en los nombres
df.columns = z##Reemplaza nombre
ss = pd.read_csv('Sample Size.csv', header=0)##Cargar el archivo del tamaño de muestra en una data frame
cols = ss.columns## misma transformación --linea 9
z = list(map(rep,cols))
ss.columns = z
j = 5##5 = numero de grupos que se van a generar
while j >0:

    keys = list(ss['Key'])
    frames = []
    for i in keys:
        ro = df[(df['Key']== i) & (df['Sample']== 'YES') & (df['Participant-QC']== 'NO')][['SE_ID','Key']]
        sql = "SELECT DISTINCT SE_ID, Key FROM ro"
        df2 = pdsql.sqldf(sql)
        df2.reindex(range(len(df2)))
        a = list(ss[(ss['Key']==i)]['Sample_Size'])
        k = a[0]
        t = len(df2)
        if k > t:
            k = t
        else:
            k = list(a)[0]  
        aleatory = rd.sample(list(range(df2.shape[0])),k)
        frames.append(df2.filter(items=aleatory,axis=0))

    dff = pd.concat([frames[i] for i in range(len(frames))])
    dff.to_csv('DDC {}.csv'.format(j), index=False)

    j= j-1