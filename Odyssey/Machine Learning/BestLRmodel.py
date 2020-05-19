def best_LRmodel_training(data, y_column, X_columns):
  ''' Give the best model for multiple linear regression''' 
  from sklearn.model_selection import train_test_split
  from sklearn.linear_model import LinearRegression

  dico = {}

  # First step: loop to sort variables from best to worst explanation 
  for col in X_columns: 
    X = data[[col]]
    y = data[y_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.8)
    LRmodel = LinearRegression().fit(X_train, y_train)
    score_train = LRmodel.score(X_train, y_train)
    dico[col] = score_train

  a = sorted(dico.items(), key=lambda t: t[1], reverse = True)

  var_list = []
  for i in range(len(a)):
    var_list.append(a[i][0]) 

  # Second step: loop to find the best model
  X_cols = []
  score_max_train = 0
  for var in var_list: 
    X_cols.append(var) 
    X = data[X_cols]
    y = data[y_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.8)
    LRmodel = LinearRegression().fit(X_train, y_train)
    score_train = LRmodel.score(X_train, y_train)
    score_test = LRmodel.score(X_test, y_test)

    if round(abs(score_train), 2) > round(abs(score_max_train), 2):
      best_variables = X_cols
      score_max_train = score_train
      score_max_test = score_test

  print('\n LR model with the 2 best variables :\n - variables : {} \n - R2 train = {} \n - R2 test = {}'.format(best_variables, score_max_train, score_max_test))

  # Third step: repeat step 2?
  ''' On pourrait rajouter un tour où on teste la constance du model '''

  return LRmodel, best_variables
