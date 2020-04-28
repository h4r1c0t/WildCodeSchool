# Yuka 2
**Question :**
*"Comment savoir si un aliment est sain ou non ?""*

Indices pouvant être utiles :
- nutrition-score-fr_100g
- nutrition-score-uk_100g
- pnns_groups_1
- pnns_groups_2

## 0. Connaissance métier
### Le nutriscore
Le calcul du score nutritionnel des aliments, donné à titre d’exemple, est basé sur la méthode proposée par l’OfCom (Rayner et al., 2009).
Le calcul repose sur la prise en compte, pour chaque aliment, de 4 éléments constitutifs « négatifs », c’est-à-dire plutôt « défavorables » sur le plan nutritionnel : **la densité énergétique**(apport calorique pour 100g d’aliment), **la teneur en sucres simples**, **la teneur en graisses saturées** et **la teneur en sel**.
- **Composante négative** ***N*** :
Pour chacun de ces éléments, sont attribués des points, allant de **1 à 10 en fonction de l’apport calorique**(densité énergétique) ou du contenu en graisses saturées, en sucres simples et en sel (pour 100 g d’aliment). La **composante négative N du score PNNS** est la note correspondant à la **somme des points définis pour les 4 éléments** : *cette note va donc théoriquement du plus favorable au moins favorable de 0 à 40*.

| Note  | Densité énergétique (KJ/100g) |  Graisses saturées (g/100g)  | Sucres simples (g/100g) | Sodium (mg/100g) |
|-------|-------------------------------|------------------------------|-------------------------|------------------|
|    0  |                         < 335 |                         < 1  |                   < 4.5 |             < 90 |
|    1  |                         > 335 |                         > 1  |                   > 4.5 |             > 90 |
|    2  |                         > 670 |                         > 2  |                   > 9.0 |            > 180 |
|    3  |                        > 1005 |                         > 3  |                  > 13,5 |            > 270 |
|    4  |                        > 1340 |                         > 4  |                    > 18 |            > 360 |
|    5  |                        > 1675 |                         > 5  |                  > 22,5 |            > 450 |
|    6  |                        > 2010 |                         > 6  |                    > 27 |            > 540 |
|    7  |                        > 2345 |                         > 7  |                    > 31 |            > 630 |
|    8  |                        > 2680 |                         > 8  |                    > 36 |            > 720 |
|    9  |                        > 3015 |                         > 9  |                    > 40 |            > 810 |
|    10 |                        > 2350 |                         > 10 |                    > 45 |            > 900 |

- **Composante positive** ***P*** :
Cette composante est calculée en fonction de la teneur de l’aliment en fruits ou légumes (et noix), en fibres et en protéines. Pour chacun de ces éléments, des points, allant de **1 à 5 sont attribués en fonction de l’apport de fruit et légumes, de fibres et de protéines** (pour 100 g d’aliment). La composante positive P du score nutritionnel est la note correspondant à la somme des points définis pour les 3 éléments : cette note va donc théoriquement **du plus favorable au moins favorable de 15 à
0**.

| Note  | Fruits et légumes et noix (g/100g)  | Fibres (g/100g) AOAC  | Protéines (g/100g) |
|-------|-------------------------------------|-----------------------|--------------------|
|    0  |                               < 40  |                < 0,9  |              < 1,6 |
|    1  |                               > 40  |                > 0,9  |              > 1,6 |
|    2  |                               > 60  |                > 1,9  |              > 3,2 |
|    3  |                                  -  |                > 2,8  |              > 4,8 |
|    4  |                                  -  |                > 3,7  |              > 6,4 |
|    5  |                                 80  |                > 4,7  |              > 8,0 |

- **Le Score Nutritionnel** :
Le calcul final du score nutritionnel se fait en soustrayant à la note de composante négative N la note de la composante positive P.

***Score nutritionnel = N (0-40) – P (0-15)***

> **Les notes théoriques du score vont donc de** ***-15*** **(le plus favorable sur le plan nutritionnel)** ***à +40*** **(le plus défavorable sur le plan nutritionnel).**

| Score     |           | Note |  Logo  
|-----------|-----------|------|-------------------------------------------------------------------------------------------------------|
| Aliments  | Boissons  |      |                                                                                                       |
| -15 à -1  | Eaux      | A    |  ![LogoA](https://github.com/h4r1c0t/WildCodeSchool/blob/master/Odyssey/Pandas/Yaka%20quest/NS_A.png) |
| 0 à 2     | -15 à 1   | B    |  ![LogoB](https://github.com/h4r1c0t/WildCodeSchool/blob/master/Odyssey/Pandas/Yaka%20quest/NS_B.png) |
| 3 à 10    | 2 à 5     | C    |  ![LogoB](https://github.com/h4r1c0t/WildCodeSchool/blob/master/Odyssey/Pandas/Yaka%20quest/NS_C.png) |
| 11 à 18   | 3 à 10    | D    |  ![LogoC](https://github.com/h4r1c0t/WildCodeSchool/blob/master/Odyssey/Pandas/Yaka%20quest/NS_D.png) |
| 19 à 40   | 10 à 40   | E    |  ![LogoD](https://github.com/h4r1c0t/WildCodeSchool/blob/master/Odyssey/Pandas/Yaka%20quest/NS_E.png) |

### Le Programme National Nutrition Santé (PNNS; Hercberg, 2011)
Le PNNS a pour finalité de promouvoir les facteurs de protection de la santé au travers de l’alimentation et de l’activité physique et de réduire l'exposition aux facteurs de risque au niveau de la population générale et des groupes à risque spécifiques.

Le PNNS dans les données :
- **pnns_groups_1** (*229 259 NaN*)
- **pnns_groups_2** (*226 281 NaN*)

|Groupes                                                        | Sous-groupes                                       | Exemples                                                             |
|---------------------------------------------------------------|----------------------------------------------------|----------------------------------------------------------------------|
|**Fruits et légumes**                                          |  Fruits frais                                      |	Pommes, bananes, oranges                                            |
|                                                               |  Fruits secs	                                     | Abricots secs, pruneaux                                              |
|                                                               |  Fruits transformés                                |	Compotes, fruits au sirop                                           |
|                                                               |  Légumes                                           | Courgettes, carottes, tomates, haricots verts, maïs doux, petit-pois |
|                                                               |  Oléagineux	                                       | Noix, amandes                                                        |
|**Féculents**                                                  |	Pain et produits de panification complets          | Pain et biscottes complets                                           |
|                                                               |  Pain et produits de panification raffinés	       | Pain et biscottes blancs                                             |
|                                                               |  Produits à base d’amidon, transformés sucrés/gras |	Céréales de petit-déjeuner                                          |
|                                                               |  Produits à base d’amidon, transformés salés/gras	 | Frites, biscuits apéritifs                                           |
|                                                               |  Autres féculents raffinés	                       | Riz, pâtes, pommes de terre bouillies                                |
|**Légumineuses**                                               |  Légumineuses                                      |	Lentilles, pois chiches, fèves                                      |
|**Viandes et charcuteries, produits de la pêche, œufs (VPO)**  |	Charcuterie	                                       | Saucisse, jambon, pâtés                                              |
|                                                               |  Œufs                                              |	Œufs                                                                |
|                                                               |  Poissons gras                                     |	Saumon, maquereau, sardine, hareng                                  |
|                                                               |  Autres poissons, mollusques et crustacés          |	Cabillaud, bar, dorade, moules, crevettes                           |
|                                                               |  Viande hors volaille                              |	Bœuf, veau, porc, mouton, agneau, cheval, abats, gibier             |
|                                                               |  Volaille                                          |	Poulet, canard                                                      |
|**Lait et produits laitiers**                                  |	Desserts sucrés lactés                             |	Crèmes dessert, crèmes glacées                                      |
|                                                               |  Fromages                                          |	Fromages à pâte molle, pressée                                      |
|                                                               |  Lait                                              |	Lait demi-écrémé, lait entier                                       |
|                                                               |  Produits laitiers frais nature                    |	Yaourts nature, fromages blancs                                     |
|                                                               |  Produits laitiers frais sucrés                    |	Yaourts sucrés                                                      |
|**Matières grasses ajoutées**                                  |	Beurre                                             |	Beurre et beurres allégés                                           |
|                                                               |  Huiles végétales riches ALA                       |	Huile de colza, de noix                                             |
|                                                               |  Huiles végétales pauvres en ALA et margarines     |	Huile de tournesol, huile d’olive                                   |
|                                                               |  Sauces, crèmes fraîches et condiments             |	Mayonnaise, ketchup, crème fraîche                                  |
|**Produits sucrés ou sucrés et gras**                          |	Produits sucrés ou sucrés et gras                  |	Confiture, viennoiseries, biscuits,                                 |
|**Eau**                                                        |	Eau de boisson                                     |	Eau                                                                 |
|**Boissons sucrées**                                           |	Boissons sucrées de type soda                      |	Sodas, limonades                                                    |
|                                                               |  Jus de fruits                                     |	Jus d’orange                                                        |
|**Sel**                                                        |	Sel                                                |	Sel                                                                 |

## 1. Importation du dataset

## 2. Nettoyage du dataset

## 3. Exploration des données
En fonction du type d'aliment (solide ou boisson), les critères du nutriscore ne sont pas les mêmes.
Notre programme doit donc prendre en compte le **nom de l'aliment**, définir **sa classe**, son **nutriscore** pour pouvoir donner la ***catégorie qui correspond***.

On constate également que lorsqu'on a le **nutriscore** on peut répondre directement à la quesiton, par contre, sans le nutriscore il ne nous est pas possible de répondre directement. Nous pouvons peut-être nous baser sur le **groupe pnns** pour avoir une idée de l'aliment. En effet, certains aliments comme les fruits et les légumes ont bien souvent un bon score alors que les aliement comme les snacks, eux, vont avoir un score médiocre.

Visualisation des nutriscores en fonction du groupe d'aliment (pnns) :

**Nutriscore FR :**

|                          	|                                  	| nutrition-score-fr_100g 	|           	|          	|       	|      	|      	|      	|        	|
|--------------------------	|----------------------------------	|-------------------------	|-----------	|----------	|-------	|------	|------	|------	|--------	|
| pnns_groups_1            	| pnns_groups_2                    	| count                   	| mean      	| std      	| min   	| 25%  	| 50%  	| 75%  	| max    	|
| Beverages                	| Artificially sweetened beverages 	| 227.0                   	| 3.907489  	| 4.659683 	| -2.0  	| 1.0  	| 2.0  	| 6.0  	| 22.0   	|
| Fruit juices             	| 1592.0                           	| 4.065955                	| 2.707867  	| -10.0    	| 3.0   	| 4.0  	| 5.0  	| 13.0 	| 1592.0 	|
| Fruit nectars            	| 290.0                            	| 13.120690               	| 3.586198  	| 1.0      	| 12.0  	| 14.0 	| 15.0 	| 20.0 	| 290.0  	|
| Non-sugared beverages    	| 1876.0                           	| 6.565565                	| 7.553646  	| -10.0    	| 0.0   	| 2.5  	| 12.0 	| 40.0 	| 1876.0 	|
| Sweetened beverages      	| 1712.0                           	| 12.382009               	| 6.026348  	| -2.0     	| 9.0   	| 13.0 	| 15.0 	| 35.0 	| 1712.0 	|
| Cereals and potatoes     	| Bread                            	| 1483.0                  	| 3.014160  	| 5.954092 	| -7.0  	| -1.0 	| 1.0  	| 7.0  	| 27.0   	|
| Breakfast cereals        	| 1266.0                           	| 6.205371                	| 6.464289  	| -8.0     	| 0.0   	| 8.0  	| 11.0 	| 24.0 	| 1266.0 	|
| Cereals                  	| 3305.0                           	| -0.560061               	| 6.447833  	| -12.0    	| -5.0  	| -2.0 	| 1.0  	| 35.0 	| 3305.0 	|
| Legumes                  	| 658.0                            	| -0.595745               	| 7.709378  	| -12.0    	| -6.0  	| -4.0 	| 1.0  	| 22.0 	| 658.0  	|
| Potatoes                 	| 77.0                             	| -3.012987               	| 4.529127  	| -9.0     	| -7.0  	| -4.0 	| -1.0 	| 12.0 	| 77.0   	|
| Composite foods          	| One-dish meals                   	| 4520.0                  	| 2.293142  	| 5.099900 	| -13.0 	| -1.0 	| 1.0  	| 4.0  	| 26.0   	|
| Pizza pies and quiche    	| 449.0                            	| 8.668151                	| 5.124250  	| -3.0     	| 3.0   	| 11.0 	| 13.0 	| 24.0 	| 449.0  	|
| Sandwich                 	| 625.0                            	| 7.828800                	| 6.209056  	| -4.0     	| 2.0   	| 9.0  	| 12.0 	| 24.0 	| 625.0  	|
| Fat and sauces           	| Dressings and sauces             	| 2560.0                  	| 10.702344 	| 6.666193 	| -8.0  	| 5.0  	| 11.0 	| 16.0 	| 29.0   	|
| Fats                     	| 1168.0                           	| 15.323630               	| 5.762633  	| -3.0     	| 11.0  	| 13.0 	| 19.0 	| 29.0 	| 1168.0 	|
| Fish Meat Eggs           	| Eggs                             	| 152.0                   	| -0.486842 	| 2.403052 	| -4.0  	| -1.0 	| -1.0 	| 0.0  	| 14.0   	|
| Fish and seafood         	| 1805.0                           	| 5.290305                	| 5.942811  	| -6.0     	| 1.0   	| 4.0  	| 11.0 	| 22.0 	| 1805.0 	|
| Meat                     	| 1000.0                           	| 5.687000                	| 6.737836  	| -8.0     	| 1.0   	| 4.0  	| 11.0 	| 25.0 	| 1000.0 	|
| Processed meat           	| 2405.0                           	| 14.815385               	| 7.629689  	| -4.0     	| 5.0   	| 17.0 	| 21.0 	| 27.0 	| 2405.0 	|
| Fruits and vegetables    	| Dried fruits                     	| 366.0                   	| 3.013661  	| 4.340612 	| -7.0  	| 0.0  	| 2.0  	| 5.0  	| 18.0   	|
| Fruits                   	| 1146.0                           	| -2.359511               	| 4.538615  	| -9.0     	| -5.0  	| -4.0 	| -2.0 	| 25.0 	| 1146.0 	|
| Soups                    	| 419.0                            	| 1.420048                	| 1.562166  	| -4.0     	| 1.0   	| 2.0  	| 2.0  	| 9.0  	| 419.0  	|
| Vegetables               	| 1578.0                           	| -4.441065               	| 4.284657  	| -15.0    	| -7.0  	| -5.0 	| -2.0 	| 16.0 	| 1578.0 	|
| Milk and dairy products  	| Cheese                           	| 2951.0                  	| 12.452728 	| 5.600580 	| -5.0  	| 11.0 	| 14.0 	| 16.0 	| 24.0   	|
| Dairy desserts           	| 692.0                            	| 6.236994                	| 4.951448  	| -6.0     	| 3.0   	| 5.0  	| 9.0  	| 24.0 	| 692.0  	|
| Ice cream                	| 612.0                            	| 12.352941               	| 5.336740  	| -5.0     	| 7.0   	| 13.0 	| 17.0 	| 22.0 	| 612.0  	|
| Milk and yogurt          	| 2606.0                           	| 2.706830                	| 4.226233  	| -5.0     	| 0.0   	| 1.0  	| 4.0  	| 30.0 	| 2606.0 	|
| Salty snacks             	| Appetizers                       	| 1817.0                  	| 12.922400 	| 5.898838 	| -9.0  	| 9.0  	| 13.0 	| 16.0 	| 35.0   	|
| Nuts                     	| 521.0                            	| 12.474088               	| 6.320282  	| -9.0     	| 9.0   	| 14.0 	| 17.0 	| 24.0 	| 521.0  	|
| Salty and fatty products 	| 18.0                             	| 13.000000               	| 5.487955  	| -1.0     	| 11.0  	| 12.0 	| 16.5 	| 25.0 	| 18.0   	|
| Sugary snacks            	| Biscuits and cakes               	| 3877.0                  	| 18.292752 	| 5.599340 	| -5.0  	| 15.0 	| 19.0 	| 22.0 	| 33.0   	|
| Chocolate products       	| 2517.0                           	| 21.697259               	| 5.635077  	| -3.0     	| 19.0  	| 23.0 	| 26.0 	| 33.0 	| 2517.0 	|
| Sweets                   	| 3212.0                           	| 14.410648               	| 7.147234  	| -6.0     	| 11.0  	| 14.0 	| 19.0 	| 33.0 	| 3212.0 	|
| cereals-and-potatoes     	| cereals                          	| 10.0                    	| -2.400000 	| 1.577621 	| -5.0  	| -3.0 	| -3.0 	| -1.0 	| 0.0    	|
| legumes                  	| 3.0                              	| -7.000000               	| 2.645751  	| -9.0     	| -8.5  	| -8.0 	| -6.0 	| -4.0 	| 3.0    	|
| fruits-and-vegetables    	| fruits                           	| 40.0                    	| -5.625000 	| 2.628127 	| -9.0  	| -8.0 	| -5.0 	| -4.0 	| 0.0    	|
| vegetables               	| 646.0                            	| -5.453560               	| 4.523857  	| -14.0    	| -9.0  	| -6.0 	| -2.0 	| 10.0 	| 646.0  	|
| salty-snacks             	| nuts                             	| 1.0                     	| -3.000000 	| NaN      	| -3.0  	| -3.0 	| -3.0 	| -3.0 	| -3.0   	|
| sugary-snacks            	| pastries                         	| 395.0                   	| 15.488608 	| 4.282742 	| 0.0   	| 13.0 	| 16.0 	| 18.0 	| 27.0   	|
| unknown                  	| unknown                          	| 11207.0                 	| 9.002855  	| 8.703496 	| -10.0 	| 1.0  	| 9.0  	| 16.0 	| 33.0   	|

**Nutriscore UK :**

|                          	|                                  	| nutrition-score-uk_100g 	|           	|          	|       	|      	|      	|      	|        	|
|--------------------------	|----------------------------------	|-------------------------	|-----------	|----------	|-------	|------	|------	|------	|--------	|
| pnns_groups_1            	| pnns_groups_2                    	| count                   	| mean      	| std      	| min   	| 25%  	| 50%  	| 75%  	| max    	|
| Beverages                	| Artificially sweetened beverages 	| 227.0                   	| 0.599119  	| 3.109022 	| -5.0  	| 0.0  	| 0.0  	| 0.0  	| 16.0   	|
| Fruit juices             	| 1592.0                           	| -3.252513               	| 0.949541  	| -8.0     	| -4.0  	| -3.0 	| -3.0 	| 9.0  	| 1592.0 	|
| Fruit nectars            	| 290.0                            	| 1.244828                	| 1.250076  	| -4.0     	| 1.0   	| 2.0  	| 2.0  	| 4.0  	| 290.0  	|
| Non-sugared beverages    	| 1876.0                           	| 1.668977                	| 4.912430  	| -7.0     	| 0.0   	| 0.0  	| 2.0  	| 32.0 	| 1876.0 	|
| Sweetened beverages      	| 1712.0                           	| 3.282710                	| 5.242186  	| -4.0     	| 1.0   	| 2.0  	| 2.0  	| 29.0 	| 1712.0 	|
| Cereals and potatoes     	| Bread                            	| 1483.0                  	| 3.014160  	| 5.954092 	| -7.0  	| -1.0 	| 1.0  	| 7.0  	| 27.0   	|
| Breakfast cereals        	| 1266.0                           	| 6.205371                	| 6.464289  	| -8.0     	| 0.0   	| 8.0  	| 11.0 	| 24.0 	| 1266.0 	|
| Cereals                  	| 3305.0                           	| -0.560061               	| 6.447833  	| -12.0    	| -5.0  	| -2.0 	| 1.0  	| 35.0 	| 3305.0 	|
| Legumes                  	| 658.0                            	| -0.595745               	| 7.709378  	| -12.0    	| -6.0  	| -4.0 	| 1.0  	| 22.0 	| 658.0  	|
| Potatoes                 	| 77.0                             	| -3.012987               	| 4.529127  	| -9.0     	| -7.0  	| -4.0 	| -1.0 	| 12.0 	| 77.0   	|
| Composite foods          	| One-dish meals                   	| 4520.0                  	| 2.299779  	| 5.116410 	| -13.0 	| -1.0 	| 1.0  	| 4.0  	| 26.0   	|
| Pizza pies and quiche    	| 449.0                            	| 8.668151                	| 5.124250  	| -3.0     	| 3.0   	| 11.0 	| 13.0 	| 24.0 	| 449.0  	|
| Sandwich                 	| 625.0                            	| 7.828800                	| 6.209056  	| -4.0     	| 2.0   	| 9.0  	| 12.0 	| 24.0 	| 625.0  	|
| Fat and sauces           	| Dressings and sauces             	| 2560.0                  	| 10.709766 	| 6.672058 	| -8.0  	| 5.0  	| 11.5 	| 16.0 	| 29.0   	|
| Fats                     	| 1168.0                           	| 19.477740               	| 3.585105  	| -6.0     	| 18.0  	| 19.0 	| 20.0 	| 29.0 	| 1168.0 	|
| Fish Meat Eggs           	| Eggs                             	| 152.0                   	| -0.486842 	| 2.403052 	| -4.0  	| -1.0 	| -1.0 	| 0.0  	| 14.0   	|
| Fish and seafood         	| 1805.0                           	| 5.290305                	| 5.942811  	| -6.0     	| 1.0   	| 4.0  	| 11.0 	| 22.0 	| 1805.0 	|
| Meat                     	| 1000.0                           	| 5.687000                	| 6.737836  	| -8.0     	| 1.0   	| 4.0  	| 11.0 	| 25.0 	| 1000.0 	|
| Processed meat           	| 2405.0                           	| 14.815385               	| 7.629689  	| -4.0     	| 5.0   	| 17.0 	| 21.0 	| 27.0 	| 2405.0 	|
| Fruits and vegetables    	| Dried fruits                     	| 366.0                   	| 3.013661  	| 4.340612 	| -7.0  	| 0.0  	| 2.0  	| 5.0  	| 18.0   	|
| Fruits                   	| 1146.0                           	| -2.359511               	| 4.538615  	| -9.0     	| -5.0  	| -4.0 	| -2.0 	| 25.0 	| 1146.0 	|
| Soups                    	| 419.0                            	| 1.420048                	| 1.562166  	| -4.0     	| 1.0   	| 2.0  	| 2.0  	| 9.0  	| 419.0  	|
| Vegetables               	| 1578.0                           	| -4.441065               	| 4.284657  	| -15.0    	| -7.0  	| -5.0 	| -2.0 	| 16.0 	| 1578.0 	|
| Milk and dairy products  	| Cheese                           	| 2951.0                  	| 16.655032 	| 7.058804 	| -5.0  	| 16.0 	| 19.0 	| 21.0 	| 26.0   	|
| Dairy desserts           	| 692.0                            	| 6.239884                	| 4.957734  	| -6.0     	| 3.0   	| 5.0  	| 9.0  	| 24.0 	| 692.0  	|
| Ice cream                	| 612.0                            	| 12.352941               	| 5.336740  	| -5.0     	| 7.0   	| 13.0 	| 17.0 	| 22.0 	| 612.0  	|
| Milk and yogurt          	| 2606.0                           	| 2.706830                	| 4.226233  	| -5.0     	| 0.0   	| 1.0  	| 4.0  	| 30.0 	| 2606.0 	|
| Salty snacks             	| Appetizers                       	| 1817.0                  	| 12.922400 	| 5.898838 	| -9.0  	| 9.0  	| 13.0 	| 16.0 	| 35.0   	|
| Nuts                     	| 521.0                            	| 12.479846               	| 6.307511  	| -9.0     	| 9.0   	| 14.0 	| 17.0 	| 24.0 	| 521.0  	|
| Salty and fatty products 	| 18.0                             	| 13.000000               	| 5.487955  	| -1.0     	| 11.0  	| 12.0 	| 16.5 	| 25.0 	| 18.0   	|
| Sugary snacks            	| Biscuits and cakes               	| 3877.0                  	| 18.292752 	| 5.599340 	| -5.0  	| 15.0 	| 19.0 	| 22.0 	| 33.0   	|
| Chocolate products       	| 2517.0                           	| 21.697259               	| 5.635077  	| -3.0     	| 19.0  	| 23.0 	| 26.0 	| 33.0 	| 2517.0 	|
| Sweets                   	| 3212.0                           	| 14.408157               	| 7.150165  	| -6.0     	| 11.0  	| 14.0 	| 19.0 	| 33.0 	| 3212.0 	|
| cereals-and-potatoes     	| cereals                          	| 10.0                    	| -2.400000 	| 1.577621 	| -5.0  	| -3.0 	| -3.0 	| -1.0 	| 0.0    	|
| legumes                  	| 3.0                              	| -7.000000               	| 2.645751  	| -9.0     	| -8.5  	| -8.0 	| -6.0 	| -4.0 	| 3.0    	|
| fruits-and-vegetables    	| fruits                           	| 40.0                    	| -5.625000 	| 2.628127 	| -9.0  	| -8.0 	| -5.0 	| -4.0 	| 0.0    	|
| vegetables               	| 646.0                            	| -5.453560               	| 4.523857  	| -14.0    	| -9.0  	| -6.0 	| -2.0 	| 10.0 	| 646.0  	|
| salty-snacks             	| nuts                             	| 1.0                     	| -3.000000 	| NaN      	| -3.0  	| -3.0 	| -3.0 	| -3.0 	| -3.0   	|
| sugary-snacks            	| pastries                         	| 395.0                   	| 15.488608 	| 4.282742 	| 0.0   	| 13.0 	| 16.0 	| 18.0 	| 27.0   	|
| unknown                  	| unknown                          	| 11207.0                 	| 9.000178  	| 8.708119 	| -10.0 	| 1.0  	| 9.0  	| 16.0 	| 33.0   	|
