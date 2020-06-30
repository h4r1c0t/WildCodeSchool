# Non au SQL

## 1. Installe Robo 3T
Check

## 2. Crée une collection nommé “macollection” dans une base de données nommé “mabdd”
![img1](https://raw.githubusercontent.com/h4r1c0t/WildCodeSchool/master/Odyssey/NoSQL/img/1.png)

## 3. Ajoute un document JSON selon le modèle suivant :
```
{
"cours" : "NoSQL",
"compétences" : ["installation", "collection", "requête", "théorie"],
"métier" : {
  "intitulé" : "Data Analyst",
  "domaine" : "Informatique"
  }
}
```

## 4. Importe la base de données restaurants.zip

## 5. Ecris une requête qui compte le nombre de restaurants avec un grade A

## 6. Ecris une requête qui trie tous les différents scores de restaurants en ordre décroissant

## 7. Ecris une requête qui trouve tous les restaurants dans lesquels les noms des villes commencent par la lettre “B”, “C” ou “D”, ou se terminent par une voyelle sauf “y”

## 8. Ecris une requête qui affiche tous les restaurants si et seulement si le score est inférieur à 20 ou égale à 25, 30, 35 et 40 (n’oubliez pas de préciser que la vérification se fasse sur chaque instance)

## 9. Ecris une requête qui fait la somme du nombre de restaurants par type de cuisine

## 10. Ecris une requête qui ajoute le commentaire “Je gère le NoSQL” pour les boroughs dont le nom commence par “B”

## 11. Ecris une requête qui supprime la clé “adress” des restaurants qui ont un score supérieur à 25

## 12. Ecris une requête qui supprime tous les restaurants dont le nom de quartier est “Queens”





## Commente le code ci-dessous pour expliquer ce qu'il fait (j'ai ajouté un espace après $ pour que tu puisses le voir, il faut les enlever):

```
- varUnwind = {$ unwind : "$grades"}

- varGroup4 = { $ group : {"_id" : "$ borough", "moyenne" : {$ avg : "$ grades.score"} } };

- varSort2 = { $ sort : { "moyenne" : -1 } }

- db.restaurants.aggregate( [ varUnwind, varGroup4, varSort2 ] );

- Voir lignes ci-dessous :

  { "_id" : "Queens", "moyenne" : 11.634865110930088 }

  { "_id" : "Brooklyn", "moyenne" : 11.447723132969035 }

  { "_id" : "Manhattan", "moyenne" : 11.41823125728344 }

  { "_id" : "Staten Island", "moyenne" : 11.370957711442786 }

  { "_id" : "Bronx", "moyenne" : 11.036186099942562 }

  { "_id" : "Missing", "moyenne" : 9.632911392405063 }
  ```
