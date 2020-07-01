SELECT Company.name, Category.label, Product.label, Product.gtin, Product.`internal-reference`,
    Price.price_before, Price.price_after, Price.change_date
FROM piwigo_retail_product_company AS Product
INNER JOIN
    (SELECT id, name
    FROM piwigo_retail_companies
    WHERE name  = 'Leroy Merlin')
AS Company ON  Product.`company-id` = Company.id
INNER JOIN
    (SELECT cat_id, label
    FROM piwigo_retail_category_company
    WHERE label LIKE '%suspension%')
AS Category ON Product.cat_id = Category.cat_id
INNER JOIN
    (SELECT product_company_id, price_before, price_after, MAX(change_date) AS change_date
    FROM piwigo_retail_product_company_price_changes
    GROUP BY product_company_id, price_before, price_after)
AS Price ON Product.`product-company-id` = Price.product_company_id ;