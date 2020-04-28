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

Note  | Densité énergétique (KJ/100g) |  Graisses saturées (g/100g)  | Sucres simples (g/100g) | Sodium (mg/100g)
------|-------------------------------|------------------------------|-------------------------|------------------
   0  |                         < 335 |                         < 1  |                   < 4.5 |             < 90
   1  |                         > 335 |                         > 1  |                   > 4.5 |             > 90
   2  |                         > 670 |                         > 2  |                   > 9.0 |            > 180
   3  |                        > 1005 |                         > 3  |                  > 13,5 |            > 270
   4  |                        > 1340 |                         > 4  |                    > 18 |            > 360
   5  |                        > 1675 |                         > 5  |                  > 22,5 |            > 450
   6  |                        > 2010 |                         > 6  |                    > 27 |            > 540
   7  |                        > 2345 |                         > 7  |                    > 31 |            > 630
   8  |                        > 2680 |                         > 8  |                    > 36 |            > 720
   9  |                        > 3015 |                         > 9  |                    > 40 |            > 810
   10 |                        > 2350 |                         > 10 |                    > 45 |            > 900

- **Composante positive** ***P*** :
Cette composante est calculée en fonction de la teneur de l’aliment en fruits ou légumes (et noix), en fibres et en protéines. Pour chacun de ces éléments, des points, allant de **1 à 5 sont attribués en fonction de l’apport de fruit et légumes, de fibres et de protéines** (pour 100 g d’aliment). La composante positive P du score nutritionnel est la note correspondant à la somme des points définis pour les 3 éléments : cette note va donc théoriquement **du plus favorable au moins favorable de 15 à
0**.

Note  | Fruits et légumes et noix (g/100g)  | Fibres (g/100g) AOAC  | Protéines (g/100g)
------|-------------------------------------|-----------------------|--------------------
   0  |                               < 40  |                < 0,9  |              < 1,6
   1  |                               > 40  |                > 0,9  |              > 1,6
   2  |                               > 60  |                > 1,9  |              > 3,2
   3  |                                  -  |                > 2,8  |              > 4,8
   4  |                                  -  |                > 3,7  |              > 6,4
   5  |                                 80  |                > 4,7  |              > 8,0

- **Le Score Nutritionnel** :
Le calcul final du score nutritionnel se fait en soustrayant à la note de composante négative N la note de la composante positive P.

***Score nutritionnel = N (0-40) – P (0-15)***

> **Les notes théoriques du score vont donc de** ***-15*** **(le plus favorable sur le plan nutritionnel)** ***à +40*** **(le plus défavorable sur le plan nutritionnel).**

### Le Programme National Nutrition Santé (PNNS; Hercberg, 2011)
Le PNNS a pour finalité de promouvoir les facteurs de protection de la santé au travers de l’alimentation et de l’activité physique et de réduire l'exposition aux facteurs de risque au niveau de la population générale et des groupes à risque spécifiques.

Le PNNS dans les données :
- **pnns_groups_1** (*229 259 NaN*)
- **pnns_groups_2** (*226 281 NaN*)

Groupes                                                        | Sous-groupes                                       | Exemples
---------------------------------------------------------------|----------------------------------------------------|-----------------------------------------------------------------------
**Fruits et légumes**                                          |  Fruits frais                                      |	Pommes, bananes, oranges
                                                               |  Fruits secs	                                      | Abricots secs, pruneaux
                                                               |  Fruits transformés                                |	Compotes, fruits au sirop
                                                               |  Légumes                                           | Courgettes, carottes, tomates, haricots verts, maïs doux, petit-pois
                                                               |  Oléagineux	                                      | Noix, amandes
**Féculents**                                                  |	Pain et produits de panification complets         | Pain et biscottes complets
                                                               |  Pain et produits de panification raffinés	        | Pain et biscottes blancs
                                                               |  Produits à base d’amidon, transformés sucrés/gras |	Céréales de petit-déjeuner
                                                               |  Produits à base d’amidon, transformés salés/gras	| Frites, biscuits apéritifs
  |Autres féculents complets	Riz complet, blé complet
                                                               |  Autres féculents raffinés	                        | Riz, pâtes, pommes de terre bouillies
**Légumineuses**                                               |  Légumineuses                                      |	Lentilles, pois chiches, fèves
**Viandes et charcuteries, produits de la pêche, œufs (VPO)**  |	Charcuterie	                                      | Saucisse, jambon, pâtés
                                                               |  Œufs                                              |	Œufs
                                                               |  Poissons gras                                     |	Saumon, maquereau, sardine, hareng
                                                               |  Autres poissons, mollusques et crustacés          |	Cabillaud, bar, dorade, moules, crevettes
                                                               |  Viande hors volaille                              |	Bœuf, veau, porc, mouton, agneau, cheval, abats, gibier
                                                               |  Volaille                                          |	Poulet, canard
**Lait et produits laitiers**                                  |	Desserts sucrés lactés                            |	Crèmes dessert, crèmes glacées
                                                               |  Fromages                                          |	Fromages à pâte molle, pressée
                                                               |  Lait                                              |	Lait demi-écrémé, lait entier
                                                               |  Produits laitiers frais nature                    |	Yaourts nature, fromages blancs
                                                               |  Produits laitiers frais sucrés                    |	Yaourts sucrés
**Matières grasses ajoutées**                                  |	Beurre                                            |	Beurre et beurres allégés
                                                               |  Huiles végétales riches ALA                       |	Huile de colza, de noix
                                                               |  Huiles végétales pauvres en ALA et margarines     |	Huile de tournesol, huile d’olive
                                                               |  Sauces, crèmes fraîches et condiments             |	Mayonnaise, ketchup, crème fraîche
**Produits sucrés ou sucrés et gras**                          |	Produits sucrés ou sucrés et gras                 |	Confiture, viennoiseries, biscuits,
**Eau**                                                        |	Eau de boisson                                    |	Eau
**Boissons sucrées**                                           |	Boissons sucrées de type soda                     |	Sodas, limonades
                                                               |  Jus de fruits                                     |	Jus d’orange
**Sel**                                                        |	Sel                                               |	Sel

## 1. Importation du dataset

## 2. Nettoyage du dataset
