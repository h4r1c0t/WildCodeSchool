# Import iris data set from scikit learn
## Import modules
```py
import pandas as pd 
import numpy as np
from sklearn import datasets
```

## Import dataset
```py
iris = datasets.load_iris()
```

## Convert to pandas dataframe
```py
df_iris = pd.DataFrame(data= np.c_[iris['data'], iris['target']], 
                        columns= iris['feature_names'] + ['target'])
df_iris.head()
```
```md
>>> 
|   | sepal length (cm) | sepal width (cm) | petal length (cm) | petal width (cm) | target |
|---|-------------------|------------------|-------------------|------------------|--------|
| 0 | 5.1               | 3.5              | 1.4               | 0.2              | 0.0    |
| 1 | 4.9               | 3.0              | 1.4               | 0.2              | 0.0    |
| 2 | 4.7               | 3.2              | 1.3               | 0.2              | 0.0    |
| 3 | 4.6               | 3.1              | 1.5               | 0.2              | 0.0    |
| 4 | 5.0               | 3.6              | 1.4               | 0.2              | 0.0    |
```
