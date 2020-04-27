# Introduction au machine learning
## Apprentissage supervisé

## Apprentissage non supervisé
### Régressions linéaires
### Clustering KNN (Méthode des k plus proches voisins)
On va regarder comment sont classés les plus proches voisins pour décider de comment classer notre nouvelle observation.

[Principales méthodes utilisées](/home/h4r1c0t/Github/WildCodeSchool/Odyssey/Machine Learning/Capture d’écran du 2020-04-27 14-28-01.png)


**En data analyse**, nous allons rarement créer nos propres algorythmes de machine learning.
On va plutôt **réutiliser ce qui existe déjà**.

Il ne faut pas forcément savoir faire la démonstration d'un algorythme pour pouvoir l'utiliser, mais il est bien de le comprendre.

## Le text mining
Il y a actuellement des algorythmes capables de faire des résumés d'articles !

## Algorythmes de prédictions

___

# Machine Learning: Testing and Error Metrics
Source : [Vidéo youtube](https://www.youtube.com/watch?v=aDW44NPhNw0)

## Les règles d'or
1. *Thou shalt never use your testing data for training*
1. *Friends don't let friends use their testing data for training*
1. *Think not that your country can do for you I'm kidding...* ***DON'T EVER USE YOUR TESTING DATA FOR TRAINING***

## K-Fold Cross Validation

xxx = training set    |   *XXX* = testing set

*XXX* xxx xxx xxx

xxx *XXX* xxx xxx

xxx xxx *XXX* xxx

xxx xxx xxx *XXX*

Faire plusieurs set et tests dans les data.

## Vérification du modèle
### Accuracy
*Parmi toutes les données, combien ont été classées correctement ?*
**Accuracy** *= True positive / Total data*

  |  + | -
+ | *X | X  
- |  X | X  

### Precision
*Parmi tout ceux qui sont détecté positifs/négatifs, combien le sont vraiment ?*

  |  + | -
+ | *X |   
- |  X |   

**Precision** *= True positive /  True pos + False pos (=Positives tests)*
### Recal
*Parmi les personnes positives, combien ont été détectées ?*

  |  + | -
+ | *X | X  
- |    |   

**Recall** *= True positive / True pos + False neg (=Positives data)*

### F1 Score
**Arithmetic mean** = (x+y)/2
**Harmonic mean** = 2xy/(x+y)

In machine learning: **F1 Score** *= Harmonic Mean(Precision, Recall)*

### Fbetha Score
```
Precision ... F.5 Score ... F1 Score ... F2 Score ... Recall
                                                    F10 Score pour l'ex de la fraude
```
## Classification
**Underfitting** |  *Just right*    | **Overfitting**
-----------------|------------------|-----------------
Bad on training  | Good on training | Great on training
Bad on testing   | Good on testing  | Bad on testing
High bias (deg 1)| Right (deg 2)    | High Variance (deg 6)

### Model complexity graph
                **Deg 1 | Deg 2 | Deg 6**
*Training Error*:     3 |     1 |     0
*Testing Error* :     3 |     1 |     2

`/!\` **Rules #1:** *Thou shalt never use your testing data for training*
> Use a **cross validation set** ans after choosing your model, you can test with your testing dataset !

You can also used *Grid Search Cross Validation* to test multiple regressions types.
