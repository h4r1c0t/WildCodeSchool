# Les bases de données - SQL

## 01 - Introduction aux bases de données 

[X] *Créer une base de données wild_db_quest et se déplacer dessus.*
```SQL
CREATE DATABASE wild_db_quest;
```
- *Importer le fichier SQL db.sql (cela te créera la table wizard comme indiqué dans l’exemple plus haut)*
```SQL
CREATE TABLE `wild_db_quest`.`wizard` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `firstname` VARCHAR(100) NOT NULL,
  `lastname` VARCHAR(100) NOT NULL,
  `birthday` DATE NOT NULL,
  `birth_place` VARCHAR(255) NULL,
  `biography` TEXT NULL,
  PRIMARY KEY (`id`));
```
- *Modifier la table wizard en ajoutant un champ is_muggle de type booléen, obligatoire, qui permettra d’indiquer si le sorcier est ou non un moldu. Si tu ne sais pas ce qu’est un moldu, c’est que tu en es sans doute un toi-même !* 


- *Créer la table school, contenant les champs :*
id (clé primaire, entier auto-incrémenté)name (chaîne de caractères de longueur 100, obligatoire)capacity (entier, non obligatoire)country (chaîne de caractères de longueur 255, obligatoire)

```SQL
CREATE TABLE `wild_db_quest`.`school` (
	`id` INT NOT NULL AUTO_INCREMENT, 
	`name` VARCHAR(100) NOT NULL, 
	`capacity` INT, 
	`country` VARCHAR(255) NOT NULL,
	PRIMARY KEY (`id`));
```

- *Exécuter les commandes SHOW TABLES et faire un DESCRIBE sur les tables wizard et school.*

- *Poster une capture d’écran montrant la sortie de ces deux commandes.*

## 02 - Récupérer des informations avec SELECT

- *Récupère tous les champs pour les sorciers nés entre 1975 et 1985*
```SQL
SELECT * FROM wizard 
WHERE birthday BETWEEN '1975-01-01' AND '1985-12-31'; 
```
```
+----+-----------+----------+------------+-------------+---------------------------------------+-----------+
| id | firstname | lastname | birthday   | birth_place | biography                             | is_muggle |
+----+-----------+----------+------------+-------------+---------------------------------------+-----------+
|  1 | harry     | potter   | 1980-07-31 | london      |                                       |         0 |
|  2 | hermione  | granger  | 1979-09-19 |             | Friend of Harry Potter                |         0 |
|  4 | ron       | weasley  | 1980-03-01 |             | Best friend of Harry                  |         0 |
|  5 | ginny     | weasley  | 1981-08-11 |             | Sister of Ron and girlfriend of Harry |         0 |
|  6 | fred      | weasley  | 1978-04-01 |             |                                       |         0 |
|  7 | george    | weasley  | 1978-04-01 |             |                                       |         0 |
| 10 | drago     | malefoy  | 1980-06-05 |             |                                       |         0 |
| 14 | dudley    | dursley  | 1980-06-23 |             | Cousin d'Harry                        |         1 |
+----+-----------+----------+------------+-------------+---------------------------------------+-----------+
```

- *Le prénom uniquement des sorciers dont le prénom commence par la lettre ‘H’*
```SQL
SELECT firstname FROM wizard
WHERE firstname LIKE 'H%';
```
```
+-----------+
| firstname |
+-----------+
| harry     |
| hermione  |
+-----------+
```

- *Les prénom et nom de tous les membres de la famille ‘Potter’, classés par ordre de prénom*
```SQL
SELECT firstname, lastname FROM wizard
WHERE lastname = 'potter'
ORDER BY firstname;
```
```
+-----------+----------+
| firstname | lastname |
+-----------+----------+
| harry     | potter   |
| lily      | potter   |
+-----------+----------+
```

- *Le prénom, nom et date de naissance du plus vieux sorcier (doit fonctionner quelque soit le contenu de la table)*
```SQL
SELECT firstname, lastname, birthday FROM wizard
ORDER BY birthday ASC 
LIMIT 0, 1;
``` 
```
+-----------+------------+------------+
| firstname | lastname   | birthday   |
+-----------+------------+------------+
| albus     | dumbledore | 1881-07-01 |
+-----------+------------+------------+
```

## 03 - Manipulation des données

- *Insère dans la table school les données suivantes :*
```
|            name                             |      country     | capacity |
|.............................................|..................|..........|
|Beauxbatons Academy of Magic                 | France           | 550      |
|Castelobruxo                                 | Brazil           | 380      |
|Durmstrang Institute                         | Norway           | 570      |
|Hogwarts School of Witchcraft and Wizardry   | United Kingdom   | 450      |
|Ilvermorny School of Witchcraft and Wizardry | USA              | 300      |
|Koldovstoretz                                | Russia           | 125      |
|Mahoutokoro School of Magic                  | Japan            | 800      |
|Uagadou School of Magic                      | Uganda           | 350      |
```
```SQL
INSERT INTO `wild_db_quest`.`school` (`name`, `country`, `capacity`)
VALUES 
('Beauxbatons Academy of Magic', 'France', 550), 
('Castelobruxo', 'Brazil', 380),
('Durmstrang Institute', 'Norway', 570),
('Hogwarts School of Witchcraft and Wizardry', 'United Kingdom', 450),
('Ilvermorny School of Witchcraft and Wizardry', 'USA', 300),
('Koldovstoretz', 'Russia', 125),
('Mahoutokoro School of Magic', 'Japan', 800),
('Uagadou School of Magic', 'Uganda', 350);
```
```
+----+----------------------------------------------+----------+----------------+
| id | name                                         | capacity | country        |
+----+----------------------------------------------+----------+----------------+
|  1 | Beauxbatons Academy of Magic                 |      550 | France         |
|  2 | Castelobruxo                                 |      380 | Brazil         |
|  3 | Durmstrang Institute                         |      570 | Norway         |
|  4 | Hogwarts School of Witchcraft and Wizardry   |      450 | United Kingdom |
|  5 | Ilvermorny School of Witchcraft and Wizardry |      300 | USA            |
|  6 | Koldovstoretz                                |      125 | Russia         |
|  7 | Mahoutokoro School of Magic                  |      800 | Japan          |
|  8 | Uagadou School of Magic                      |      350 | Uganda         |
+----+----------------------------------------------+----------+----------------+
```

- *“Durmstrang Institute” est en réalité en Suède (Sweden), modifie son pays.*
```SQL
UPDATE school 
SET country = 'Sweden' 
WHERE name = 'Durmstrang Institute';
```
```
+----+----------------------------------------------+----------+----------------+
| id | name                                         | capacity | country        |
+----+----------------------------------------------+----------+----------------+
|  1 | Beauxbatons Academy of Magic                 |      550 | France         |
|  2 | Castelobruxo                                 |      380 | Brazil         |
|  3 | Durmstrang Institute                         |      570 | Sweden         |
|  4 | Hogwarts School of Witchcraft and Wizardry   |      450 | United Kingdom |
|  5 | Ilvermorny School of Witchcraft and Wizardry |      300 | USA            |
|  6 | Koldovstoretz                                |      125 | Russia         |
|  7 | Mahoutokoro School of Magic                  |      800 | Japan          |
|  8 | Uagadou School of Magic                      |      350 | Uganda         |
+----+----------------------------------------------+----------+----------------+
```

- *“Mahoutokoro School of Magic” passe à une capacité de 700*
```SQL
UPDATE school 
SET capacity = 700 
WHERE name = 'Mahoutokoro School of Magic';
```
```
+----+----------------------------------------------+----------+----------------+
| id | name                                         | capacity | country        |
+----+----------------------------------------------+----------+----------------+
|  1 | Beauxbatons Academy of Magic                 |      550 | France         |
|  2 | Castelobruxo                                 |      380 | Brazil         |
|  3 | Durmstrang Institute                         |      570 | Sweden         |
|  4 | Hogwarts School of Witchcraft and Wizardry   |      450 | United Kingdom |
|  5 | Ilvermorny School of Witchcraft and Wizardry |      300 | USA            |
|  6 | Koldovstoretz                                |      125 | Russia         |
|  7 | Mahoutokoro School of Magic                  |      700 | Japan          |
|  8 | Uagadou School of Magic                      |      350 | Uganda         |
+----+----------------------------------------------+----------+----------------+
```

- *Supprime en une seule requête toutes les écoles comportant “Magic” dans leur nom (il y en a 3). Tu peux t’aider du mot clé LIKE.*
```SQL
DELETE FROM school 
WHERE name LIKE '%Magic%';
```
```
+----+----------------------------------------------+----------+----------------+
| id | name                                         | capacity | country        |
+----+----------------------------------------------+----------+----------------+
|  2 | Castelobruxo                                 |      380 | Brazil         |
|  3 | Durmstrang Institute                         |      570 | Sweden         |
|  4 | Hogwarts School of Witchcraft and Wizardry   |      450 | United Kingdom |
|  5 | Ilvermorny School of Witchcraft and Wizardry |      300 | USA            |
|  6 | Koldovstoretz                                |      125 | Russia         |
+----+----------------------------------------------+----------+----------------+
```

- *Ensuite, affiche via une requête SELECT toutes les données de la table school et colle également le résultat dans le Gist.*
```SQL
SELECT * FROM school
```
```
+----+----------------------------------------------+----------+----------------+
| id | name                                         | capacity | country        |
+----+----------------------------------------------+----------+----------------+
|  2 | Castelobruxo                                 |      380 | Brazil         |
|  3 | Durmstrang Institute                         |      570 | Sweden         |
|  4 | Hogwarts School of Witchcraft and Wizardry   |      450 | United Kingdom |
|  5 | Ilvermorny School of Witchcraft and Wizardry |      300 | USA            |
|  6 | Koldovstoretz                                |      125 | Russia         |
+----+----------------------------------------------+----------+----------------+
```
