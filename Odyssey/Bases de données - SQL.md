# Les bases de données - SQL

## 01 - Introduction aux bases de données 

- *Créer une base de données wild_db_quest et se déplacer dessus.*
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

## 04 - Les bases de la modélisation

*Énoncé :
Chaque potion que tu vas créer a un nom. Les potions sont constituées d’un mélange d’ingrédients, qui ont chacun un nom.* 

*Ça fait beaucoup d’informations à retenir. Pour ne rien oublier, tu aimerais stocker en base de données quels ingrédients sont nécessaires pour chaque potion. Prends un papier et un crayon, et dessine le schéma permettant de modéliser cette problématique.*

https://drive.google.com/open?id=1PpKFAkJ7HCEyZGocEggjVUcEQMtj554o

## 05 - Les jointures

- *Modifie la table wizard afin qu’elle corresponde exactement au schéma ci-dessous, et vide là également de tout contenu (TRUNCATE ou DELETE).*
```SQL
ALTER TABLE wizard 
DROP birthday;

ALTER TABLE wizard 
DROP birth_place;

ALTER TABLE wizard 
DROP biography;

ALTER TABLE wizard 
DROP is_muggle;

ALTER TABLE wizard
MODIFY firstname VARCHAR(80);

ALTER TABLE wizard
MODIFY lastname VARCHAR(80);
```

- *Crée les tables player et team comme indiqué sur la modélisation ci-dessous (noms et types des champs), en prenant soin de déclarer correctement les clés étrangères.*
```SQL
CREATE TABLE wild_db_quest.player ( 
id INT PRIMARY KEY AUTO_INCREMENT, 
wizard_id INT, 
team_id INT, 
role VARCHAR(50), 
enrollment_date DATE, 
CONSTRAINT fk_wizard_player 
FOREIGN KEY (wizard_id) 
REFERENCES wizard(id)); 

CREATE TABLE wild_db_quest.team ( 
id INT NOT NULL AUTO_INCREMENT, 
name VARCHAR(80),
PRIMARY KEY (id));


ALTER TABLE player 
ADD CONSTRAINT fk_player_team 
FOREIGN KEY (team_id) 
REFERENCES team(id); 
```

- *Charge ensuite dans ta BDD ce fichier SQL et vérifie que tout s’est bien passé.*
```SQL
SELECT * FROM wizard LIMIT 0,10;
SELECT * FROM player LIMIT 0,10;
SELECT * FROM team LIMIT 0,10;
```
```
+----+-----------+----------+
| id | firstname | lastname |
+----+-----------+----------+
|  1 | harry     | potter   |
|  2 | hermione  | granger  |
|  3 | lily      | potter   |
|  4 | ron       | weasley  |
|  5 | ginny     | weasley  |
|  6 | fred      | weasley  |
|  7 | george    | weasley  |
|  8 | arthur    | weasley  |
|  9 | molly     | weasley  |
| 10 | drago     | malefoy  |
+----+-----------+----------+

+----+-----------+---------+--------+-----------------+
| id | wizard_id | team_id | role   | enrollment_date |
+----+-----------+---------+--------+-----------------+
|  1 |         1 |       4 | beater | 1995-10-09      |
|  2 |         2 |       1 | chaser | 1995-08-17      |
|  3 |         3 |       1 | seeker | 1994-12-03      |
|  4 |         4 |       3 | chaser | 1995-03-24      |
|  5 |         5 |       3 | keeper | 1997-07-16      |
|  6 |         6 |       1 | beater | 1994-01-10      |
|  7 |         7 |       4 | chaser | 1999-01-21      |
|  8 |         8 |       4 | keeper | 1991-10-20      |
| 10 |        10 |       1 | beater | 1991-08-03      |
| 11 |        11 |       3 | beater | 1996-10-04      |
+----+-----------+---------+--------+-----------------+

+----+------------+
| id | name       |
+----+------------+
|  1 | Gryffindor |
|  2 | Ravenclaw  |
|  3 | Slytherin  |
|  4 | Hufflepuff |
+----+------------+
```

***Une fois ces données correctement chargées, écris les requêtes suivantes, et poste-les dans un Gist dont tu posteras le lien en solution :***

*1. Retourne les noms, prénoms, rôle et équipe de tous les joueurs, classés dans l’ordre alphabétique par équipe, puis par rôle dans l’équipe, puis par nom de famille, puis par prénom.*
```SQL
SELECT firstname, lastname, role, name FROM player 
JOIN wizard ON wizard.id=player.wizard_id
JOIN team ON team.id=player.team_id
ORDER BY name, role, lastname, firstname;
```
```
+-----------+------------+--------+------------+
| firstname | lastname   | role   | name       |
+-----------+------------+--------+------------+
| drago     | malefoy    | beater | Gryffindor |
| fred      | weasley    | beater | Gryffindor |
| hermione  | granger    | chaser | Gryffindor |
| lily      | potter     | seeker | Gryffindor |
| harry     | potter     | beater | Hufflepuff |
| george    | weasley    | chaser | Hufflepuff |
| arthur    | weasley    | keeper | Hufflepuff |
| tom       | j├â┬®dusor | beater | Ravenclaw  |
| severus   | rogue      | chaser | Ravenclaw  |
| dudley    | dursley    | seeker | Ravenclaw  |
| albus     | dumbledore | beater | Slytherin  |
| ron       | weasley    | chaser | Slytherin  |
| ginny     | weasley    | keeper | Slytherin  |
+-----------+------------+--------+------------+
```

*2. Retourne uniquement les prénom et nom des joueurs ayant le rôle de seeker (attrapeur), classés par ordre alphabétique de nom puis prénom*
```SQL
SELECT firstname, lastname FROM player
JOIN wizard ON wizard.id=player.wizard_id
WHERE role = 'seeker'
ORDER BY lastname, firstname;
```
```
+-----------+----------+
| firstname | lastname |
+-----------+----------+
| dudley    | dursley  |
| lily      | potter   |
+-----------+----------+
```
*3. Retourne la liste de tous les sorciers qui ne pratiquent pas le quidditch.*
```SQL
SELECT * FROM wizard 
WHERE NOT EXISTS (SELECT * FROM player WHERE wizard_id = wizard.id);
```
```
+----+-----------+----------+
| id | firstname | lastname |
+----+-----------+----------+
|  9 | molly     | weasley  |
+----+-----------+----------+
```

## 06 - SQL avancé

1. *Retourne le nom des équipes et le nombre de joueurs par équipe, le tout classé par nombre de joueurs par équipe, de la plus nombreuse à la moins nombreuse.*
```SQL
SELECT name, count(player.id) FROM team 
JOIN player ON player.team_id = team.id 
GROUP BY team.name 
ORDER BY count(player.id) DESC;
```
```
+------------+------------------+
| name       | count(player.id) |
+------------+------------------+
| Gryffindor |               36 |
| Slytherin  |               21 |
| Ravenclaw  |               15 |
| Hufflepuff |               12 |
+------------+------------------+
```

2. *Retourne uniquement les noms des équipes complètes (ayant 14 joueurs ou plus, c’est-à- dire 7 joueurs et 7 remplaçants minimum), classés par ordre alphabétique.*
```SQL
SELECT name, count(player.id) FROM team 
JOIN player ON player.team_id = team.id 
GROUP BY name 
HAVING count(player.id) > 13 
ORDER BY name;
```
```
+------------+------------------+
| name       | count(player.id) |
+------------+------------------+
| Gryffindor |               36 |
| Ravenclaw  |               15 |
| Slytherin  |               21 |
+------------+------------------+
```

***3.*** *L’entraîneur des Gryffondor est superstitieux, son jour préféré est le lundi. Retourne la liste des joueurs de son équipe qui ont été enrôlés un lundi (il souhaite les faire jouer en priorité), et classe les résultats par date d’enrôlement chronologique.*
```SQL
SELECT id, enrollment_date FROM player 
WHERE DAYOFWEEK(enrollment_date) = 2 
ORDER BY enrollment_date ASC; 
```
```
+----+-----------------+
| id | enrollment_date |
+----+-----------------+
| 44 | 1991-03-11      |
| 88 | 1991-07-08      |
| 82 | 1991-08-26      |
| 12 | 1992-01-27      |
| 39 | 1992-02-17      |
| 90 | 1993-01-04      |
| 30 | 1993-08-30      |
|  6 | 1994-01-10      |
| 20 | 1995-04-24      |
|  1 | 1995-10-09      |
| 50 | 1996-12-02      |
| 25 | 1996-12-16      |
| 41 | 1999-10-25      |
+----+-----------------+
```
