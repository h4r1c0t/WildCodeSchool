# Non au SQL

## 1. Installe Robo 3T
> ![img0](https://raw.githubusercontent.com/h4r1c0t/WildCodeSchool/master/Odyssey/NoSQL/img/0.png)


## 2. Crée une collection nommé “macollection” dans une base de données nommé “mabdd”
> ![img1](https://raw.githubusercontent.com/h4r1c0t/WildCodeSchool/master/Odyssey/NoSQL/img/1.png)

## 3. Ajoute un document JSON selon le modèle suivant :
```JSON
{
"cours" : "NoSQL",
"compétences" : ["installation", "collection", "requête", "théorie"],
"métier" : {
  "intitulé" : "Data Analyst",
  "domaine" : "Informatique"
  }
}
```

> ![img2](https://raw.githubusercontent.com/h4r1c0t/WildCodeSchool/master/Odyssey/NoSQL/img/2.png)

## 4. Importe la base de données restaurants.zip
> ![img3](https://raw.githubusercontent.com/h4r1c0t/WildCodeSchool/master/Odyssey/NoSQL/img/3.png)

## 5. Ecris une requête qui compte le nombre de restaurants avec un grade A
```SQL
-- QUERY
db.collection('restaurants').find({"grades.0.grade": "A"}).count()
```
> ![img4](https://raw.githubusercontent.com/h4r1c0t/WildCodeSchool/master/Odyssey/NoSQL/img/4.png)

## 6. Ecris une requête qui trie tous les différents scores de restaurants en ordre décroissant
```SQL
-- QUERY
db.collection('restaurants').find({}).sort({"grades.0.score": -1})
-- or
db.collection('restaurants').find({}).sort({"grades.score": -1})
```
> ![img5](https://raw.githubusercontent.com/h4r1c0t/WildCodeSchool/master/Odyssey/NoSQL/img/5.png)

## 7. Ecris une requête qui trouve tous les restaurants dans lesquels les noms des villes commencent par la lettre “B”, “C” ou “D”, ou se terminent par une voyelle sauf “y”
```SQL
-- QUERY
db.collection('restaurants').find({"borough": /^[B-D].*|.*[AEIOU]$/gi})
```
> ![img6](https://raw.githubusercontent.com/h4r1c0t/WildCodeSchool/master/Odyssey/NoSQL/img/6.png)

## 8. Ecris une requête qui affiche tous les restaurants si et seulement si le score est inférieur à 20 ou égale à 25, 30, 35 et 40 (n’oubliez pas de préciser que la vérification se fasse sur chaque instance)
```SQL
-- QUERY
db.getCollection('restaurants').find({
    $or: [
        { "grades.score": { $lt: 20 }},
        { "grades.score": { $in: [ 25, 30, 35, 40 ] }}
    ]
})
```
> ![img7](https://raw.githubusercontent.com/h4r1c0t/WildCodeSchool/master/Odyssey/NoSQL/img/7.png)

## 9. Ecris une requête qui fait la somme du nombre de restaurants par type de cuisine
```SQL
-- QUERY
db.restaurants.aggregate([
    {"$group" : {_id:"$cuisine",
        count:{$sum:1}}
    }
])
```
> ![img8](https://raw.githubusercontent.com/h4r1c0t/WildCodeSchool/master/Odyssey/NoSQL/img/8.png)

## 10. Ecris une requête qui ajoute le commentaire “Je gère le NoSQL” pour les boroughs dont le nom commence par “B”
```SQL
-- QUERY
db.collection('restaurants').find({"borough": /^B.*/gi}).
```
> ![img9](https://raw.githubusercontent.com/h4r1c0t/WildCodeSchool/master/Odyssey/NoSQL/img/9.png)

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
