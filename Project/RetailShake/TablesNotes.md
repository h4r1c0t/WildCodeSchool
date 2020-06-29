# Exploration des tables
```SQL
DESCRIBE piwigo_retail_product_company;
``` 

```
product-company-store-id,varchar(130),NO,PRI,,""
company-id,int,YES,MUL,,""
internal-reference,varchar(30),NO,MUL,,""
internal-store-id,varchar(32),YES,MUL,,""
price,"decimal(10,2)",YES,"",,""
price_advice,varchar(100),YES,"",,""
original-price,"decimal(10,2)",YES,"",,""
discount,tinyint(1),YES,"",,""
price-date,datetime,YES,"",,""
stock,int,YES,"",,""
stock_advice,varchar(100),YES,"",,""
stock-indicator,"set('available','not_sure','out_of_stock','soon_available','not_sold','to_order')",YES,MUL,,""
stock-date,datetime,NO,"",CURRENT_TIMESTAMP,DEFAULT_GENERATED
```
