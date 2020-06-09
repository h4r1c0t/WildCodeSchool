def regression_modeling(model, data, target, cv=5, screening=True):
    '''

    :param model: 'knn', 'lr', 'log'
    :param data: DataFrame
    :param target: y
    :param cv: number of split for the cross validation
    :param screening: Do you want a print of the scores
    :return: Return the fitted model and the columns used
    '''
    ##### SELECTION DU TYPE DE REGRESSION
    # Select le linear model
    if model.lower() == 'knn':
        from sklearn.neighbors import KNeighborsRegressor
    elif model.lower() == 'lr':
        from sklearn.linear_model import LinearRegression
    elif model.lower() == 'log':
        from sklearn.linear_model import LogisticRegression
    else:
        print('Error model type not valid')

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
    score_max = 0
    scores_max = 0
    Xcolumns = []

    # Début de la boucle de modélisation en partant de la plus forte corrélation
    for x, r in dictCorr:
        cols.append(x)    # Ajout d'une nouvelle variable au model
        X = data[cols]
        y = data[target]

        if model.lower() == 'knn':
            cv =  StratifiedKFold(n_splits = cv, random_state = 42, shuffle = True)
            scores = cross_val_score(KNeighborsRegressor(), X, y, cv=cv,
                                        scoring = make_scorer(accuracy_score))
        elif model.lower() == 'lr':
            cv =  StratifiedKFold(n_splits = cv, random_state = 42, shuffle = True)
            scores = cross_val_score(LinearRegression(), X, y, cv=cv,
                                    scoring = make_scorer(accuracy_score))
        elif model.lower(model) == 'log':
            cv =  StratifiedKFold(n_splits = cv, random_state = 42, shuffle = True)
            scores = cross_val_score(LogisticRegression(), X, y, cv=cv,
                                    scoring = make_scorer(accuracy_score))
        else:
            break

        if np.mean(scores) > score_max:     # Si la nouvelle variable augmente le score,
            score_max = np.mean(scores)     # on met à jour les variables
            scores_max = scores
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

      print('\nMean score =', score_max)
      print('Scores :', scores_max)

    # Fit un nouveau model avec les meilleures variables
    from sklearn.model_selection import train_test_split
    Xmax = data[Xcolumns]
    X_train, X_test, y_train, y_test = train_test_split(Xmax, y, random_state=42,
                                                          train_size = 0.75)
    if model.lower() == 'knn':
        modelMax = KNeighborsRegressor().fit(X_train, y_train)
    elif model.lower() == 'lr':
        modelMax = LinearRegression().fit(X_train, y_train)
    elif model.lower() == 'log':
        modelMax = LogisticRegression().fit(X_train, y_train)
    else:
        break

    # Retourne le meilleur model.
    return modelMax, Xcolumns

