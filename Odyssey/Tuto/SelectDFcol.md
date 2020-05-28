# Sélectionner des colonnes d'un DataFrame

## Sélection des colonnes par type :
Ici type != de 'object'
```py
obj = df.columns[df.dtypes.values == np.dtype("object")]
columnsNames = [x for x in df.columns if x not in obj]
columnsNames
```

## Sélection par index
```py
df.iloc[<rows>, <col>]
```
