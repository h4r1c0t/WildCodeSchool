SELECT *
FROM piwigo_retail_product_company
WHERE `product-company-store-id` = "0000098024135000001";

SELECT *
FROM piwigo_retail_product_store
WHERE `product-company-store-id` = "0000098024135000001";


-- Permet la sélection de la catégorie "SUSPENSION"
SELECT label, cat_id
FROM piwigo_retail_category_company
WHERE label LIKE '%suspension%';

-- Permet de trouver tous les produits correspondants à la `cat_id`
SELECT cat_id, `product-company-id`
FROM piwigo_retail_product_company
WHERE cat_id = "l1400351717";

-- Permet de sélectionner tous les prix enregistrés pour un produit
SELECT `product_company_id`, price_after, change_date
FROM piwigo_retail_product_company_price_changes
WHERE product_company_id = 137130690002;

--
SELECT `product_company_id`, price_after price, MAX(change_date) date
FROM piwigo_retail_product_company_price_changes pcpc
WHERE EXISTS (
    SELECT `product-company-id`
    FROM piwigo_retail_product_company
    WHERE cat_id = "l1400351717" AND product_company_id = `product-company-id`
    )
GROUP BY product_company_id
LIMIT 10;