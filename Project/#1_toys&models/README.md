# Model company - Dashboarding

## Introduction

You are commissioned by a company selling models and scale models. The company already has a database that lists employees, products, orders, and much more. You are invited to browse and discover this database. The director of the company wishes to have a dashboard which he could refresh each morning to have the latest information in order to manage the company.

## Objective

Your dashboard should revolve around this 4 main topics : sales, finance, logistics and human resources.
Here are the indicators that should be present in your dashboard. Graphics would also be appreciated. And you are invited to practice your advisory role, by proposing additional KPIs and graphics.
- Sales: The number of products sold by category and by month, with comparison and rate of change compared to the same month of the previous year.
- Finances:
  - The turnover of the orders of the last two months by country.
  - Orders that have not yet been paid.
- Logistics: The stock of the 5 most ordered products.
- Human Resources: Each month, the 2 sellers with the highest turnover.

## Resources
https://www.mysqltutorial.org

## Tools
You will install a MySQL Community server on your machine, as well as the MySQL Workbench client.

The director does not want to do SQL, he wants to be able to access the data automatically via his LibreOffice Calc spreadsheet. The dashboard will therefore be a LibreOffice Calc workbook, connected to the MySQL server, and distributed on several tabs by theme. The director can then refresh the data when he wants.

The database is ready to be loaded into a MySQL server. Connect to your server via Workbench, and run all of the code in this file.
