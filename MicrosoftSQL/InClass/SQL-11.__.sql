-- SQL-11. ders_16.06.2022(session-10)

--

-- How many different product are in each brand in each category?
-- group by ile
select category_id,brand_id,COUNT(product_id)
from product.product
group by category_id,brand_id
------------------------------------------------
--WF ile
select distinct category_id,brand_id,COUNT(product_id) OVER(PARTITION BY category_id,brand_id) cnt_prod
from product.product
"""

--------------------------------
-- FIRST_VALUE FUNCTION
-- Bir s�tun i�in en �st sat�rda yer alan de�eri getiriyor(Partition, WF ve ko�ullara g�re)
"""
-- �rnek kod
Select A.customer_id, A.first_name, B.order_date,
FIRST_VALUE(order_date) OVER (ORDER BY B.Order_date) first_date from sale.customer A, sale.orders B 
WHERE A.customer_id = B.customer_id

--------------------------

-- Soru: Write a query that returns most stocked product in each store
-- Sorunun ilk k�sm�n� yapal�m burada her bir store a g�re en �ok sto�u olan product_id ne buna bakaca��m
Select store_id, product_id,
FIRST_VALUE(product_id) OVER(PARTITION BY store_id ORDER BY quantity DESC) most_stocked_prod
FROM product.stock
-- product_id nin ilk de�erini al�p , quantity ye g�re DESCENDING s�ralamam gerekiyor. 
-- ��nk� azalan s�ralamada en y�ksekten d����e gidiyor. Yani first value dedi�imde
-- bunun en �sttekini yani order by yapt���m�z i�in maximum de�erini ald�
-- store_id 1 kar��s�na gelen 30 numaral� �r�n 30 tane varm��
-- store_id 2 kar��s�na gelen 64 numaral� �r�n 30 tane varm��
-- most_stocked_prod --> first_value of product_id
-- �imdi istedi�imiz ��kt�y� getirelim
Select distinct store_id, 
FIRST_VALUE(product_id) OVER(PARTITION BY store_id ORDER BY quantity DESC) most_stocked_prod
FROM product.stock
-- Elde etmek istedi�imiz sonu� geldi
-------------------------
-- �stteki sorguda En y�ksek quantity ye sahip �r�n ve miktar�
Select distinct store_id, 
FIRST_VALUE(product_id) OVER(PARTITION BY store_id ORDER BY quantity DESC) most_stocked_prod,
FIRST_VALUE(product_id) OVER(ORDER BY quantity DESC) MSP_W
FROM product.stock

-- Dersin 2. b�l�m�
-- Soru: --Write a query that returns customers and their most valuable order with total amount of it.
-- M��terilerin en y�ksek miktara sahip de�erlerini d�nd�r�n
select B.customer_id
from sale.order_item A, sale.orders B
WHERE A.order_id = B.order_id
--�imdi.. En de�erli sipari�i nas�l bulabiliriz. m��teriler- sipari�ler ve net price lar�na bakaca��m ve
-- her bir m��teri i�in en y�kse�ini bulaca��m
SELECT	customer_id, B.order_id, SUM(quantity * list_price* (1-discount)) net_price
FROM	sale.order_item A, sale.orders B
WHERE	A.order_id = B.order_id
GROUP BY customer_id, B.order_id
ORDER BY 1,3 DESC;
-- net price � her bir customer_id ve sipari� i�in bulmu� olduk
--customer_id 1 i�in en y�ksek amoun 1038.5370, -- order_id 1555, 3 i�in, 6763.3454 -- order_id 1612

-- Devam edelim ve �sttekini bir alt sorguya al�p kaydedelim WITH ile
-- Sonra onu(WITH T1) i kullanarak istedi�imiz sonuca ula�al�m
WITH T1 AS (
select customer_id, B.order_id, SUM(quantity*list_price*(1-discount)) net_price
from sale.order_item A, sale.orders B where A.order_id = B.order_id
Group by customer_id, B.order_id
)
Select distinct customer_id,
FIRST_VALUE(order_id) OVER(PARTITION BY customer_id ORDER BY net_price Desc) MV_order,
FIRST_VALUE(net_price) OVER(PARTITION BY customer_id ORDER BY net_price Desc) MV_order_NET_PRICE
from T1
-- En y�ksek net price a sahip sipari�i getirdik ve distinct yapt�k
-- 2. partition da net price � getirece�iz ve ilk sat�rdaki de�eri alaca��z
-- MV: most valuable

-----------------------------------------

--Soru: Write a query that returns first order date by month
Select distinct Year(order_date) Year, Month(order_date) Month,
FIRST_VALUE(order_date) 
OVER(PARTITION BY Year(order_date),Month(order_date) ORDER BY Year(order_date)) first_order_date 
from  sale.orders

-- FIRST_VALUE(order_date): Her bir ay baz�nda ilk order_date i istiyorduk

-- Dersin 3. b�l�m�
-- LAST_VALUE
-- S�ralanm�� s�tun de�erleri i�erisinden son de�eri getiriyor
-- �rnek kod
Select A.customer_id, A.first_name, B.order_date,
last_value(order_date) OVER (ORDER BY B.Order_date desc) last_date from sale.customer A, sale.orders B 
WHERE A.customer_id = B.customer_id

-- order_date ve last_date ayn� de�erler gelmi�. ��nk� default frame ko�ulunu kulland�
-- Her bir sat�r i�in bir �nceki sat�r� hesaba katt�
-- 1. sat�r, �nceki sat�r yok, kendisini ald�,
-- 2. sat�rda �nceki sat�r� 1. sat�r, bunlardan last_valueyu al�yor yani 2 yi o y�zde
-- 3. ... 
--- O y�zden Rows between unboundend preciding and unbounded following demek laz�m.
-- yani last_value kullan�rken Window frame i �tteki �ekilde kullanmal�y�z

--------------------------------------------

-- Store tablosunda en y�ksek quantity ye sahip �r�n� last_value ile getirmek istiyorum
-- �nce stock tablomuza bakal�m tekrar
select * from product.stock order by 1,3 asc
-- Devam edelim
SELECT	DISTINCT store_id,
		LAST_VALUE(product_id) OVER (PARTITION BY store_id ORDER BY quantity ASC, product_id DESC ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) most_stocked_prod
FROM	product.stock
-------
SELECT	DISTINCT store_id,
		LAST_VALUE(product_id) OVER (PARTITION BY store_id ORDER BY quantity ASC, product_id DESC RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) most_stocked_prod
FROM	product.stock

-- order by da 2 tane s�tun kulland�k
-- NOT: range ile rows hemen hemen ayn� i�lemleri yap�yor
    -- rows : unbounded preciding/following gibi keyword lerle kullan�p sta�r say�s� belirtmek istiyorsan�z kullan�yoruz
    -- range: yine keyword ler kullan�l�yor ANCAK Manuel olarak sat�r say�s� belirtemiyorsunuz

---------------
-- LAG() AND LEAD()
-- LAG() : Her bir sat�r i�in kendisinden belirtti�imiz kadar �nceki sat�r de�erini getiriyor
        -- �rne�in; order_date s�tunundan 3 �nceki de�eri o de�erin yan�na getiriyoruz
        -- default u 1 : Kendisinden 1 �nceki sat�r de�erini al
        -- Null de�er i�in bir �ey yazd�rmak istiyorsak, onu null un yerine yazd�rabiliyoruz
-----------------------------------------
-- �rnek kod
SELECT order_date,
lag(order_date,2) OVER(ORDER BY order_date) previous_second_w_lag from sale.orders
-- LEAD() : lag �n tersi olarak sonraki sat�r dde�erlerini al�yoruz

-- �rnek kod
SELECT order_date,
lead(order_date,2) OVER(ORDER BY order_date) next_second_w_lead from sale.orders

--------------------------------
-- Soru: Her bir staff i�in �al��anlar�n ald��� sipari�lerin 1 �nceki sipari� tarihlerini yazd�r�n
SELECT	A.staff_id, B.first_name, B.last_name, A.order_id, A.order_date,
		LAG(order_date) OVER(PARTITION BY A.staff_id ORDER BY A.order_id) prev_order
FROM	sale.orders A, sale.staff B
WHERE	A.staff_id = B.staff_id

--Write a query that returns the order date of the one next sale of each staff (use the LEAD function)
SELECT	DISTINCT A.order_id, B.staff_id, B.first_name, B.last_name, order_date,
		LEAD(order_date, 1) OVER(PARTITION BY B.staff_id ORDER BY order_id) next_order_date
FROM	sale.orders A, sale.staff B
WHERE	A.staff_id = B.staff_id

-- S�tunlar� �ektik
-- her bir sipari�in kendisinden 1 �nceki sipari� tarihini ald�k
-- �rne�in ;3. sipari�ten bir �nceki sipari� 9 , bunun tarihi 2018-01-05 sonra 3. sat�rda 12, 2018-01-06 n�n yan�na 2018-01-05 geldi
-- di�er sat�rlar ayn� mant�k. �lk s�tundan �nce sipari� olmad��� i�in NULL geldi
-- Not: order_id 20 numaral� sipari� i�in 1 �nceki tarih ayn� o y�zden order_by da A.order_date yerine
-- .. A.order_id ye g�re yaparsak daha mant�kl� olabilir. ��nk� order_date e g�re s�ralay�nca �nce order_id 19 u mu almal� yoksa 20 yi mi
-- .. gibi bir sorun olu�uyor. O y�zden order_id ye g�re s�ralad�k

-- E�er partition yapmasayd�m order_id 1,2,3,4 diye gidecek ve staff ler farkl� olacakt�
SELECT	A.staff_id, B.first_name, B.last_name, A.order_id, A.order_date,
		LAG(order_date) OVER(ORDER BY A.order_id) prev_order
FROM	sale.orders A, sale.staff B
WHERE	A.staff_id = B.staff_id