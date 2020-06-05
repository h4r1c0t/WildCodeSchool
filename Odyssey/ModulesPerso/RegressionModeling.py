def Regressions_modelisation(model, data, target):

    ##### SELECTION DU TYPE DE REGRESSION
    # Select le linear model
    if lower(model) == 'knn':
        from sklearn.neighbors import KNeighborsRegressor
    elif lower(model) == 'lr':
        from sklearn.linear_model import LinearRegression
    elif lower(model) == 'log':
        from sklearn.linear_model import LogisticRegression
    else:
        print('Error model type not valid')
        break

    ##### IMPORT
    import numpy as np
    import pandas as pd

    from sklearn.metrics import make_scorer, accuracy_score
    from sklearn.model_selection import cross_val_score, StratifiedKFold

    ##### COLUMNS SELECTIONS
    # Sélection des colonnes qui ne sont pas de type 'object'
    obj = data.columns[data.dtypes.values == np.dtype("object")]
    colNames = [x for x in data.columns if x not in obj]

    # Création d'un dictionnaire avec les variables les plus corrélées à la target
    df_corr = data[colNames].corr()
    dictCorr = dict(df_corr[target])
    del dictCorr[target]

    dictCorr = sorted(dictCorr.items(), key = lambda x : x[1])
    dictCorr.reverse()

    ##### BOUCLE D'ENTRAINEMENT DU MODEL
    # Variables
      cols = []
      train_score_max = 0
      test_score_max = 0
      Xcols = []

    # Début de la boucle de modélisation en partant de la plus forte corrélation
    for x, r in dictCorr:
      cols.append(x)    # Ajout d'une nouvelle variable au model
      X = data[cols]
      y = data[target]

        if lower(model) == 'knn':
            cv =  StratifiedKFold(n_splits = 6, random_state = 42, shuffle = True)
            scores = cross_val_score(KNeighborsRegressor(), X, y, cv=cv,
                                        scoring = make_scorer(accuracy_score))
        elif lower(model) == 'lr':
            cv =  StratifiedKFold(n_splits = 6, random_state = 42, shuffle = True)
            scores = cross_val_score(LinearRegression(), X, y, cv=cv,
                                    scoring = make_scorer(accuracy_score))
        elif lower(model) == 'log':
            cv =  StratifiedKFold(n_splits = 6, random_state = 42, shuffle = True)
            scores = cross_val_score(LogisticRegression(), X, y, cv=cv,
                                    scoring = make_scorer(accuracy_score))
        else:
            break

        if mean(scores) > score_max:   # Si la nouvelle variable augmente le score,
            score_max = mean(scores)     # on met à jour les variables
            Xcolumns = cols
        else:
            cols.remove(x)

    ### SCREENING
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
    if lower(model) == 'knn':
        modelMax = KNeighborsRegressor().fit(X_train, y_train)
    elif lower(model) == 'lr':
        modelMax = LinearRegression().fit(X_train, y_train)
    elif lower(model) == 'log':
        modelMax = LogisticRegression().fit(X_train, y_train)
    else:
        break

  # Retourne le meilleur model.
  return modelMax, Xcolumns
