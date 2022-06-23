﻿select * from cust_dimen
select * from market_fact
select * from orders_dimen
select * from prod_dimen
select * from shipping_dimen

UPDATE market_fact
   SET Discount = round(Discount, 2 ),
       Product_Base_Margin = round(Product_Base_Margin, 2 )

UPDATE prod_dimen 
   SET Prod_id = SUBSTRING(Prod_id, PATINDEX('%[0-9]%', Prod_id), LEN(Prod_id)) 

ALTER TABLE prod_dimen
ALTER COLUMN Prod_id int;

UPDATE shipping_dimen 
   SET Ship_id = SUBSTRING(Ship_id, PATINDEX('%[0-9]%', Ship_id), LEN(Ship_id)) 

ALTER TABLE shipping_dimen
ALTER COLUMN Ship_id int;

UPDATE market_fact 
   SET  Ord_id= SUBSTRING(Ord_id, PATINDEX('%[0-9]%', Ord_id), LEN(Ord_id)) 

ALTER TABLE market_fact
ALTER COLUMN Ord_id int;

UPDATE market_fact 
   SET  Prod_id= SUBSTRING(Prod_id, PATINDEX('%[0-9]%', Prod_id), LEN(Prod_id))
   
ALTER TABLE market_fact
ALTER COLUMN Prod_id int;

UPDATE market_fact 
   SET  Ship_id= SUBSTRING(Ship_id, PATINDEX('%[0-9]%', Ship_id), LEN(Ship_id)) 

ALTER TABLE market_fact
ALTER COLUMN Ship_id int;

UPDATE market_fact 
   SET  Cust_id= SUBSTRING(Cust_id, PATINDEX('%[0-9]%', Cust_id), LEN(Cust_id)) 

ALTER TABLE market_fact
ALTER COLUMN Cust_id int;

UPDATE cust_dimen 
   SET  Cust_id= SUBSTRING(Cust_id, PATINDEX('%[0-9]%', Cust_id), LEN(Cust_id)) 

ALTER TABLE Cust_dimen
ALTER COLUMN Cust_id int;

UPDATE orders_dimen 
   SET  Ord_id= SUBSTRING(Ord_id, PATINDEX('%[0-9]%', Ord_id), LEN(Ord_id))

ALTER TABLE cust_dimen

ALTER TABLE market_fact
ALTER TABLE orders_dimen
ALTER TABLE prod_dimen
ALTER TABLE shipping_dimen


ALTER TABLE cust_dimen ADD CONSTRAINT PK_1 PRIMARY KEY (Cust_id)

------------------------------------------------
Alter Table market_fact Add Id int Identity(1,1)
ALTER TABLE market_fact

ALTER TABLE market_fact ADD CONSTRAINT PK_5 PRIMARY KEY (Id)


select * from market_fact


ALTER TABLE market_fact ADD CONSTRAINT FK_22 FOREIGN KEY (Cust_id) REFERENCES cust_dimen (Cust_id)

--select * from cust_dimen where Customer_Name='ERIC BARRETO'
--select * from cust_dimen where Customer_Name='KARL BROWN'


----------------------------------------------------------------------
--1. Using the columns of “market_fact”, “cust_dimen”, “orders_dimen”, 
--“prod_dimen”, “shipping_dimen”, Create a new table, named as
--“combined_table”.

select * from combined_df

-----------------------------------------------------------------
--2. Find the top 3 customers who have the maximum count of orders.


select Top 3 Cust_id, COUNT(distinct Ord_id) count_of_orders from combined_df

--3.Create a new column at combined_table as DaysTakenForDelivery that contains the date difference of Order_Date and Ship_Date.
--Use "ALTER TABLE", "UPDATE" etc.

ALTER TABLE combined_df ADD DaysTakenForDelivery INT

UPDATE combined_df 
SET DaysTakenForDelivery = DATEDIFF(DAY, Order_date, Ship_date

select * from combined_df

--ALTER TABLE combined_df 
--ADD 
--  DaysTakenForDelivery AS DATEDIFF (DAY,Order_date,Ship_date) PERSISTED

--4. Find the customer whose order took the maximum time to get delivered

select TOP 1 Cust_id,Customer_Name, Max(DaysTakenForDelivery) Max_delivery_day from combined_df


--5. Count the total number of unique customers in January and how many of them came back every month over the entire year in 2011
--You can use such date functions and subqueries
--Ocak ayındaki toplam benzersiz müşteri sayısını ve 2011'de tüm yıl boyunca her ay kaç tanesinin geri geldiğini sayın.

(
)
) 
select MONTH(order_date) month_2011, COUNT(DISTINCT cust_id) total_cust
from v1
where Year(Order_Date)='2011'
group by MONTH(order_date) 

select * from v1 

--select distinct Cust_id,count(MONTH(order_date)) a from v1
--where Year(Order_Date)='2011'
--group by Cust_id
--order by a desc 

-----------------------------------------------------------------------
--6--- Write a query to return for each user the time elapsed between the first 
--purchasing and the third purchasing, in ascending order by Customer ID.

CREATE VIEW T1 as (

------------------------------------
--7. Write a query that returns customers who purchased both product 11 and 
--product 14, as well as the ratio of these products to the total number of 
--products purchased by the customer.


create view p1 as (
select distinct b.Prod_id,A.Cust_id, count(Prod_id) num_of_prod ,b.Order_Quantity num_of_quantity from (


select a.prod_id,a.sum_quantity_prod ,round(cast((1.0*a.sum_quantity_prod) as float) /cast(sum(1.0*p1.num_of_quantity) as float),2)
from (
select Prod_id,sum(num_of_quantity) sum_quantity_prod from p1
where prod_id=11 or prod_id=14
group by Prod_id
) A,p1 where A.prod_id=p1.prod_id
group by a.prod_id,a.sum_quantity_prod

-----------------------------
create view p1 as (
from H1,H2


---------------------------------------------------------
--Customer Segmentation
--Categorize customers based on their frequency of visits. The following steps 
--will guide you. If you want, you can track your own way.
--1. Create a “view” that keeps visit logs of customers on a monthly basis. (For 
--each log, three field is kept: Cust_id, Year, Month
CREATE VIEW L1 AS(
SELECT Month , COUNT(*) FROM (select Cust_id, L1.MONTH,L1.YEAR from L1) A

-- 3.For each visit of customers, create the next month of the visit as a separate column


--5. Categorise customers using average time gaps. Choose the most fitted
--labeling model for you.
--For example: 
--o Labeled as churn if the customer hasn't made another purchase in the 
--months since they made their first purchase.
--o Labeled as regular if the customer has made a purchase every month.
--Etc.



--labelıng
CREATE VIEW LABELLING as (
)

select * from LABELLING
/* Month-Wise Retention Rate
Find month-by-month customer retention ratei since the start of the business.
There are many different variations in the calculation of Retention Rate. 
But we will try to calculate the month-wise retention rate in this project.
So, we will be interested in how many of the customers in the previous month could be retained in the next month.
Proceed step by step by creating views. 
You can use the view you got at the end of the Customer Segmentation section as a source. */

-- 1. Find the number of customers retained month-wise. (You can use time gaps)


select count(*) from REGULAR

--2. Calculate the month-wise retention rate.
--Month-Wise Retention Rate = 1.0 * Total Number of Customers in The Previous Month /
--Number of Customers Retained in The Next Month

-- Month-Wise Retention Rate














