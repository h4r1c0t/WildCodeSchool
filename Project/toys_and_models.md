# Toys and models

## Client demands:
**1. Sales:** *The number of products sold by category and by month, with comparison and rate of change compared to the same month of the previous year.*

**2. Finances:**
  - *The turnover of the orders of the last two months by country.*
  - *Orders that have not yet been paid.*

**3. Logistics:** *The stock of the 5 most ordered products.*

**4. Human Resources:** *Each month, the 2 sellers with the highest turnover.*

**5. Any other features ?**

## Data exploration:
### Tables screening 
#### customers
```SQL
SELECT * FROM customers LIMIT 0,5;
```
```
+----------------+----------------------------+-----------------+------------------+--------------+------------------------------+--------------+-----------+----------+------------+-----------+------------------------+-------------+
| customerNumber | customerName               | contactLastName | contactFirstName | phone        | addressLine1                 | addressLine2 | city      | state    | postalCode | country   | salesRepEmployeeNumber | creditLimit |
+----------------+----------------------------+-----------------+------------------+--------------+------------------------------+--------------+-----------+----------+------------+-----------+------------------------+-------------+
|            103 | Atelier graphique          | Schmitt         | Carine           | 40.32.2555   | 54, rue Royale               | NULL         | Nantes    | NULL     | 44000      | France    |                   1370 |    21000.00 |
|            112 | Signal Gift Stores         | King            | Jean             | 7025551838   | 8489 Strong St.              | NULL         | Las Vegas | NV       | 83030      | USA       |                   1166 |    71800.00 |
|            114 | Australian Collectors, Co. | Ferguson        | Peter            | 03 9520 4555 | 636 St Kilda Road            | Level 3      | Melbourne | Victoria | 3004       | Australia |                   1611 |   117300.00 |
|            119 | La Rochelle Gifts          | Labrune         | Janine           | 40.67.8555   | 67, rue des Cinquante Otages | NULL         | Nantes    | NULL     | 44000      | France    |                   1370 |   118200.00 |
|            121 | Baane Mini Imports         | Bergulfsen      | Jonas            | 07-98 9555   | Erling Skakkes gate 78       | NULL         | Stavern   | NULL     | 4110       | Norway    |                   1504 |    81700.00 |
+----------------+----------------------------+-----------------+------------------+--------------+------------------------------+--------------+-----------+----------+------------+-----------+------------------------+-------------+
```

#### employees
```SQL
SELECT * FROM employees LIMIT 0,5;

```
```
+----------------+-----------+-----------+-----------+---------------------------------+------------+-----------+----------------------+
| employeeNumber | lastName  | firstName | extension | email                           | officeCode | reportsTo | jobTitle             |
+----------------+-----------+-----------+-----------+---------------------------------+------------+-----------+----------------------+
|           1002 | Murphy    | Diane     | x5800     | dmurphy@classicmodelcars.com    | 1          |      NULL | President            |
|           1056 | Patterson | Mary      | x4611     | mpatterso@classicmodelcars.com  | 1          |      1002 | VP Sales             |
|           1076 | Firrelli  | Jeff      | x9273     | jfirrelli@classicmodelcars.com  | 1          |      1002 | VP Marketing         |
|           1088 | Patterson | William   | x4871     | wpatterson@classicmodelcars.com | 6          |      1056 | Sales Manager (APAC) |
|           1102 | Bondur    | Gerard    | x5408     | gbondur@classicmodelcars.com    | 4          |      1056 | Sale Manager (EMEA)  |
+----------------+-----------+-----------+-----------+---------------------------------+------------+-----------+----------------------+
```

#### offices
```SQL
SELECT * FROM offices LIMIT 0,5;

```
```
+------------+---------------+-----------------+--------------------------+--------------+------------+---------+------------+-----------+
| officeCode | city          | phone           | addressLine1             | addressLine2 | state      | country | postalCode | territory |
+------------+---------------+-----------------+--------------------------+--------------+------------+---------+------------+-----------+
| 1          | San Francisco | +1 650 219 4782 | 100 Market Street        | Suite 300    | CA         | USA     | 94080      | NA        |
| 2          | Boston        | +1 215 837 0825 | 1550 Court Place         | Suite 102    | MA         | USA     | 02107      | NA        |
| 3          | NYC           | +1 212 555 3000 | 523 East 53rd Street     | apt. 5A      | NY         | USA     | 10022      | NA        |
| 4          | Paris         | +33 14 723 4404 | 43 Rue Jouffroy D'abbans | NULL         | NULL       | France  | 75017      | EMEA      |
| 5          | Tokyo         | +81 33 224 5000 | 4-1 Kioicho              | NULL         | Chiyoda-Ku | Japan   | 102-8578   | Japan     |
+------------+---------------+-----------------+--------------------------+--------------+------------+---------+------------+-----------+
```

#### orderdetails
```SQL
SELECT * FROM orderdetails LIMIT 0,5;

```
```
+-------------+-------------+-----------------+-----------+-----------------+
| orderNumber | productCode | quantityOrdered | priceEach | orderLineNumber |
+-------------+-------------+-----------------+-----------+-----------------+
|       10100 | S18_1749    |              30 |    136.00 |               3 |
|       10100 | S18_2248    |              50 |     55.09 |               2 |
|       10100 | S18_4409    |              22 |     75.46 |               4 |
|       10100 | S24_3969    |              49 |     35.29 |               1 |
|       10101 | S18_2325    |              25 |    108.06 |               4 |
+-------------+-------------+-----------------+-----------+-----------------+
```

#### orders
```SQL
SELECT * FROM orders LIMIT 0,5;

```
```
+-------------+------------+--------------+-------------+---------+------------------------+----------------+
| orderNumber | orderDate  | requiredDate | shippedDate | status  | comments               | customerNumber |
+-------------+------------+--------------+-------------+---------+------------------------+----------------+
|       10100 | 2018-01-06 | 2018-01-13   | 2018-01-10  | Shipped | NULL                   |            363 |
|       10101 | 2018-01-09 | 2018-01-18   | 2018-01-11  | Shipped | Check on availability. |            128 |
|       10102 | 2018-01-10 | 2018-01-18   | 2018-01-14  | Shipped | NULL                   |            181 |
|       10103 | 2018-01-29 | 2018-02-07   | 2018-02-02  | Shipped | NULL                   |            121 |
|       10104 | 2018-01-31 | 2018-02-09   | 2018-02-01  | Shipped | NULL                   |            141 |
+-------------+------------+--------------+-------------+---------+------------------------+----------------+
```

#### payments
```SQL
SELECT * FROM payments LIMIT 0,5;

```
```
+----------------+-------------+-------------+----------+
| customerNumber | checkNumber | paymentDate | amount   |
+----------------+-------------+-------------+----------+
|            103 | HQ336336    | 2019-10-19  |  6066.78 |
|            103 | JM555205    | 2018-06-05  | 14571.44 |
|            103 | OM314933    | 2019-12-18  |  1676.14 |
|            112 | BO864823    | 2019-12-17  | 14191.12 |
|            112 | HQ55022     | 2018-06-06  | 32641.98 |
+----------------+-------------+-------------+----------+
```

#### productlines
```SQL
SELECT * FROM productlines LIMIT 0,5;

```
```
+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+--------------+
| productLine  | textDescription                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | htmlDescription | image        |
+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+--------------+
| Classic Cars | Attention car enthusiasts: Make your wildest car ownership dreams come true. Whether you are looking for classic muscle cars, dream sports cars or movie-inspired miniatures, you will find great choices in this category. These replicas feature superb attention to detail and craftsmanship and offer features such as working steering system, opening forward compartment, opening rear trunk with removable spare wheel, 4-wheel independent spring suspension, and so on. The models range in size from 1:10 to 1:24 scale and include numerous limited edition and several out-of-production vehicles. All models include a certificate of authenticity from their manufacturers and come fully assembled and ready for display in the home or office. | NULL            | 0x           |
| Motorcycles  | Our motorcycles are state of the art replicas of classic as well as contemporary motorcycle legends such as Harley Davidson, Ducati and Vespa. Models contain stunning details such as official logos, rotating wheels, working kickstand, front suspension, gear-shift lever, footbrake lever, and drive chain. Materials used include diecast and plastic. The models range in size from 1:10 to 1:50 scale and include numerous limited edition and several out-of-production vehicles. All models come fully assembled and ready for display in the home or office. Most include a certificate of authenticity.                                                                                                                                             | NULL            | 0x           |
| Planes       | Unique, diecast airplane and helicopter replicas suitable for collections, as well as home, office or classroom decorations. Models contain stunning details such as official logos and insignias, rotating jet engines and propellers, retractable wheels, and so on. Most come fully assembled and with a certificate of authenticity from their manufacturers.                                                                                                                                                                                                                                                                                                                                                                                               | NULL            | 0x           |
| Ships        | The perfect holiday or anniversary gift for executives, clients, friends, and family. These handcrafted model ships are unique, stunning works of art that will be treasured for generations! They come fully assembled and ready for display in the home or office. We guarantee the highest quality, and best value.                                                                                                                                                                                                                                                                                                                                                                                                                                          | NULL            | 0x           |
| Trains       | Model trains are a rewarding hobby for enthusiasts of all ages. Whether you're looking for collectible wooden trains, electric streetcars or locomotives, you'll find a number of great choices for any budget within this category. The interactive aspect of trains makes toy trains perfect for young children. The wooden train sets are ideal for children under the age of 5.                                                                                                                                                                                                                                                                                                                                                                             | NULL            | 0x           |
+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+--------------+
```

#### products
```SQL
SELECT * FROM products LIMIT 0,5;

```
```
+-------------+---------------------------------------+--------------+--------------+--------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+----------+--------+
| productCode | productName                           | productLine  | productScale | productVendor            | productDescription                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | quantityInStock | buyPrice | MSRP   |
+-------------+---------------------------------------+--------------+--------------+--------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+----------+--------+
| S10_1678    | 1969 Harley Davidson Ultimate Chopper | Motorcycles  | 1:10         | Min Lin Diecast          | This replica features working kickstand, front suspension, gear-shift lever, footbrake lever, drive chain, wheels and steering. All parts are particularly delicate due to their precise scale and require special care and attention.                                                                                                                                                                                                                                                                          |            7933 |    48.81 |  95.70 |
| S10_1949    | 1952 Alpine Renault 1300              | Classic Cars | 1:10         | Classic Metal Creations  | Turnable front wheels; steering function; detailed interior; detailed engine; opening hood; opening trunk; opening doors; and detailed chassis.                                                                                                                                                                                                                                                                                                                                                                 |            7305 |    98.58 | 214.30 |
| S10_2016    | 1996 Moto Guzzi 1100i                 | Motorcycles  | 1:10         | Highway 66 Mini Classics | Official Moto Guzzi logos and insignias, saddle bags located on side of motorcycle, detailed engine, working steering, working suspension, two leather seats, luggage rack, dual exhaust pipes, small saddle bag located on handle bars, two-tone paint with chrome accents, superior die-cast detail , rotating wheels , working kick stand, diecast metal with plastic parts and baked enamel finish.                                                                                                         |            6625 |    68.99 | 118.94 |
| S10_4698    | 2003 Harley-Davidson Eagle Drag Bike  | Motorcycles  | 1:10         | Red Start Diecast        | Model features, official Harley Davidson logos and insignias, detachable rear wheelie bar, heavy diecast metal with resin parts, authentic multi-color tampo-printed graphics, separate engine drive belts, free-turning front fork, rotating tires and rear racing slick, certificate of authenticity, detailed engine, display stand
, precision diecast replica, baked enamel finish, 1:10 scale model, removable fender, seat and tank cover piece for displaying the superior detail of the v-twin engine |            5582 |    91.02 | 193.66 |
| S10_4757    | 1972 Alfa Romeo GTA                   | Classic Cars | 1:10         | Motor City Art Classics  | Features include: Turnable front wheels; steering function; detailed interior; detailed engine; opening hood; opening trunk; opening doors; and detailed chassis.                                                                                                                                                                                                                                                                                                                                               |            3252 |    85.68 | 136.00 |
+-------------+---------------------------------------+--------------+--------------+--------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+----------+--------+
```

## Requêtes: 
### Requête n°2
**Chiffre d'affaire sur les commandes (prix unitaire * quantité)**
```SQL
-- TunrOver based on orders
SELECT offices.country, (priceEach * quantityOrdered) AS turnOver -- calc the turn over
FROM orderdetails -- select usefull colomn on orderdetails and product. 
-- WHERE orderDate BETWEEN mois actuel - 2 AND mois actuel
JOIN orders ON orders.orderNumber = orderdetails.orderNumber
JOIN customers ON customers.customerNumber = orders.customerNumber
JOIN employees ON employees.employeeNumber = customers.salesRepEmployeeNumber
JOIN offices ON offices.officeCode = employees.officeCode
GROUP BY offices.country;
```

**Chiffre d'affaire sur les commandes payées (amount)**
```SQL
-- TurnOver based on payed orders
SELECT offices.country, payments.amount AS turnOver -- calc the turn over
FROM orderdetails -- select usefull colomn on orderdetails and product. 
-- WHERE orderDate >= 
JOIN orders ON orders.orderNumber = orderdetails.orderNumber
JOIN customers ON customers.customerNumber = orders.customerNumber
JOIN payments ON payments.customerNumber = customers.customerNumber
JOIN employees ON employees.employeeNumber = customers.salesRepEmployeeNumber
JOIN offices ON offices.officeCode = employees.officeCode
GROUP BY offices.country;
```
