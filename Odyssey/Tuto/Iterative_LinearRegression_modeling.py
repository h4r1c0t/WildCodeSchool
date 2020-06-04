def Iterative_LinearRegression_modeling(data, target, mods=False, screening=False):

  '''
  Cette fonction effectue une modélisation de la meilleure régression linéaire
  en fonction des variables du dataset et revoi le model qui obtien les meilleurs
  scores. 
  '''

  if mods:  # Import de module si nécessaire
    import numpy as np
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression

  # Sélection des colonnes qui ne sont pas de type 'object'
  obj = data.columns[data.dtypes.values == np.dtype("object")]
  colNames = [x for x in data.columns if x not in obj]

  # Création d'un dictionnaire avec les variables les plus corrélées à la target
  df_corr = data[colNames].corr()
  dictCorr = dict(df_corr[target])
  del dictCorr[target]

  dictCorr = sorted(dictCorr.items(), key = lambda x : x[1])
  dictCorr.reverse()

  # Variables pour boucle
  cols = []
  train_score_max = 0
  test_score_max = 0
  Xcols = []

  # Début de la boucle de modélisation en partant de la plus forte corrélation
  for x, r in dictCorr:
    cols.append(x)    # Ajout d'une nouvelle variable au model
    X = data[cols]
    y = data[target]

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, 
                                                        train_size = 0.75)

    LRmodel = LinearRegression().fit(X_train, y_train)
    
    train_score = LRmodel.score(X_train, y_train)
    test_score = LRmodel.score(X_test, y_test)

    if test_score > test_score_max:   # Si la nouvelle variable augmente le score, 
      test_score_max = test_score     # on met à jour les variables max
      train_score_max = train_score
      Xcolumns = cols
    else:
      cols.remove(x)                  # Sinon on le retire du modèle.
    

  # Print du mini compte rendu
  if screening:
    if len(Xcolumns) > 1:
      print('Best scores obtained with {} variables :'.format(len(Xcolumns)))
    else:
      print('Best scores obtained with {} variable :'.format(len(Xcolumns)))
    
    for col in Xcolumns:
      print("   ",col)

    print('\nTrain score =', train_score_max)
    print('Test score =', test_score_max)

  # Fit un nouveau model avec les meilleures variables
  Xmax = data[Xcolumns]
  X_train, X_test, y_train, y_test = train_test_split(Xmax, y, random_state=42, 
                                                      train_size = 0.75)
  
  LRmodelMax = LinearRegression().fit(X_train, y_train)

  # Retourne le meilleur model.
  return LRmodelMax, Xcolumns
