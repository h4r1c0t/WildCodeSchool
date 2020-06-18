USE retail_shake;

-- Average price at each date for product 4000870702536
SELECT DISTINCT prpcpc.product_company_id pc_id, gtin, AVG(prpcpc.price_after) avg_price,
                DATE_FORMAT(prpcpc.change_date, '%Y-%c-%d') date
FROM piwigo_retail_product_company_price_changes AS prpcpc
    JOIN piwigo_retail_product_company AS prpc ON `product-company-id` = product_company_id
WHERE gtin = 4000870702536
GROUP BY date, pc_id;
