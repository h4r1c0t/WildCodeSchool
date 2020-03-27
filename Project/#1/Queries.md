# Liste des requêtes SQL - Toys & Models

## VENTES 
Afficher le total des ventes par catégories pour le mois en cours et le même mois l'année précédente. 
```SQL
SELECT productLine AS Category, 
SUM(quantityOrdered) AS Quantity, 
MONTH(orderDate) AS `Month`, 
YEAR(orderDate) AS `Year` 
FROM toys_and_models.orderdetails 
JOIN toys_and_models.orders ON orders.orderNumber = orderdetails.orderNumber 
JOIN toys_and_models.products ON products.productCode = orderdetails.productCode
WHERE MONTH(orderDate) = MONTH(CURRENT_DATE) - 1 AND YEAR(orderDate) BETWEEN YEAR(CURRENT_DATE) - 1 AND YEAR(CURRENT_DATE) 
GROUP BY `Year`, `Category`
ORDER BY `Year` DESC, `Category`;
```
## FINANCES
### Chiffre d'affaire
Afficher le **chiffre d'affaire prévisionnel** (`total d'articles commandés x le prix unitaire`) 
et le **chiffre d'affaire réel** (`total de paiements reçus`) pour les deux dernies mois *révolus* 
(*i.e.,*  pour mars, calculs fait sur janvier et février).
```SQL
SELECT tab1.country, tab1.turnover1 AS Previsionnal_Turnover, tab2.turnover2 AS Real_Turnover
FROM (
	SELECT customers.customerNumber, offices.country, sum(priceEach * quantityOrdered) AS turnover1
	FROM toys_and_models.orderdetails 
	JOIN toys_and_models.orders ON orders.orderNumber = orderdetails.orderNumber 
	JOIN toys_and_models.customers ON customers.customerNumber = orders.customerNumber 
	JOIN toys_and_models.employees ON employees.employeeNumber = customers.salesRepEmployeeNumber 
	JOIN toys_and_models.offices ON offices.officeCode = employees.officeCode 
	WHERE MONTH(orders.orderDate) BETWEEN MONTH(CURRENT_DATE) - 2 AND MONTH(CURRENT_DATE) - 1 
	GROUP BY offices.country
) AS tab1
LEFT JOIN (
	SELECT subtab2.country, sum(amount) AS turnover2, owed
	FROM (
		SELECT DISTINCT off.country, amount, sum(quantityOrdered * priceEach) - sum(amount) AS owed
		FROM payments AS p
		LEFT OUTER JOIN customers AS c ON p.customerNumber=c.customerNumber
		LEFT OUTER JOIN orders AS o ON o.customerNumber=p.customerNumber
		LEFT OUTER JOIN orderdetails AS od ON o.orderNumber=od.orderNumber
		LEFT OUTER JOIN employees AS e ON e.employeeNumber = c.salesRepEmployeeNumber 
		LEFT OUTER JOIN offices AS off ON off.officeCode = e.officeCode
		WHERE o.status NOT LIKE 'C%' AND MONTH(p.paymentDate) BETWEEN MONTH(CURRENT_DATE) - 2 AND MONTH(CURRENT_DATE) - 1 
		GROUP BY off.country, amount
		ORDER BY off.country
	) AS subtab2
	GROUP BY subtab2.country
	HAVING owed <>0
) AS tab2 
ON tab2.country = tab1.country
ORDER BY tab1.country
;
```

### Impayés
#### Commandes bloquées
Afficher les commandes avec le statut "Hold On". 
```SQL
SELECT c.customerName company, c.country, c.contactLastName, c.contactFirstName contact, c.phone, SUM( od.priceEach * od.quantityOrdered ) owed, o.comments problem, c.creditLimit, o.orderDate, o.orderNumber 
FROM toys_and_models.orders o, toys_and_models.orderdetails od, toys_and_models.customers c 
WHERE o.orderNumber = od.orderNumber AND o.customerNumber = c.customerNumber AND o.status = 'On Hold'
```
#### Client débiteurs
Afficher la liste des clients qui ont une différence entre le total commandé et le total payé (aussi bien négative que positive, dans le cas
de commandes annulées mais déjà réglées). 
```SQL
SELECT table1.customerName, table1.phone, table1.creditLimit, totalOrdered, SUM( amount ) totalPayed, totalOrdered - SUM( amount ) owed 
FROM ( 
SELECT DISTINCT c.customerName, c.phone, c.customerNumber, od.orderNumber, SUM( PriceEach * quantityOrdered ) totalOrdered, amount, c.creditLimit 
FROM payments AS p LEFT OUTER JOIN customers AS c ON p.customerNumber = c.customerNumber 
LEFT OUTER JOIN orders AS o ON o.customerNumber = p.customerNumber 
LEFT OUTER JOIN orderdetails AS od ON o.orderNumber = od.orderNumber 
WHERE o.status NOT LIKE 'C%' 
GROUP BY amount 
ORDER BY c.customerNumber, od.orderNumber, amount 
) AS table1 
GROUP BY table1.customerName 
HAVING owed <> 0
```

## LOGISTIQUE
Afficher les stocks et la quantité commandée des 5 prouits les plus vendus. 
```SQL
SELECT productName, quantityInStock, kiki.totalOrdered
FROM ( 
	SELECT products.productName, products.quantityInStock, SUM( orderdetails.quantityOrdered ) AS totalOrdered 
	FROM products 
    INNER JOIN orderdetails ON products.productCode = orderdetails.productCode 
	GROUP BY products.productName 
	ORDER BY totalOrdered DESC LIMIT 5 
) AS kiki;
```
## RH 
Classer les meilleurs vendeurs par mois et afficher les deux premiers. 
```SQL
SELECT orderDate, lastname, firstname, turnOver 
FROM ( 
SELECT DATE_FORMAT( orders.orderDate, '%Y %M' ) orderDate, lastname, firstname, orders.customerNumber, employeeNumber, SUM( priceEach * quantityOrdered ) turnOver 
FROM employees JOIN customers ON employees.employeeNumber = customers.salesRepEmployeeNumber JOIN orders ON customers.customerNumber = orders.customerNumber 
JOIN orderdetails ON orders.orderNumber = orderdetails.orderNumber 
WHERE orders.status = 'Shipped' 
GROUP BY orders.orderDate, orders.customerNumber 
ORDER BY YEAR( orderDate ) DESC, MONTH( orderDate ) DESC, turnOver DESC 
) AS table1 
GROUP BY employeeNumber LIMIT 2
```
