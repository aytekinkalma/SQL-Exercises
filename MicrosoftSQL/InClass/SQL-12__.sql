-- SQL-12. ders_18.06.2022(session-11)


--NUMBERING FUNCTIONS
-- S�ralama ile partition lara b�lme, k�m�latif oranlar olu�turma, Numaraland�rma vs

----- NUMBERING FUNCTIONS 1
-- ROW_NUMBER : HEr bir partition i�erisinde 1 den ba�lay�p artan bir s�tun olu�uyor
-- RANK : 1 den ba�layarak De�erler aras�nda fark var ise s�ral�yor. Ayn� de�erlere ayn� rank� veriyor. (�rnekle daha iyi anla��lacak)
-- DENSE_RANK: Dense_rank e benziyor ancak --> (�rnekle daha iyi anla��lacak)
    -- ayn� partition i�inde; 
        -- row_number: 1-2-3-4-5
        -- Rank �rnek: 1-2-2-2-5
       -- DEnse_rank: 1-2-2-2-3    

-- Row_Number()
--Soru: Her bir kategori i�inde �r�nlerin fiyat s�ralamas�n� yap�n�z.
select product_id, category_id, list_price
from product.product

-- Partition i�inde s�ralama yapt�
----------------------------------
-- Rank() -- Dense_Rank()
select product_id, category_id, list_price,
ROW_NUMBER() over(partition by category_id order by list_price) RowNum,
RANK() over(partition by category_id order by list_price) [Rank],
DENSE_RANK() over(partition by category_id order by list_price) Dense_Rank
from product.product

-- sat�r 16 -- > rank:15,  dense_rank:16 ��nk� list_price sat�r 14 ve 15 te ayn�. E�er sat�r 12,13,14,15 te 
-- list_price ayn� olsayd�, sat�r 12,13,14,15 de rank:12 , dense_rank:12 olup, sat�r 16 da rank: 16, dense_rank : 13 olacakt�
-- NOT: RowNum : Buna "Camel type" isimlendirme deniyor
-- NOT: [Rank] : K��eli parantez i�inde yazd���m i�indeki kelimeleri SQL server string ifade gibi alg�lar.
-- NOT: Dense_Rank: Pembe olarak ��k�yor. ��nk� bu SQL de bir fonksiyon ismi. Bunu de�i�tirmek �nerilir
----------------------------------
-- Soru: Herbir model_yili i�inde �r�nlerin fiyat s�ralamas�n� yap�n�z (artan fiyata g�re 1'den ba�lay�p birer birer artacak)
-- row_number(), rank(), dense_rank()
SELECT product_id, model_year,list_price,
		ROW_NUMBER() OVER(PARTITION BY model_year ORDER BY list_price ASC) RowNum,
		RANK() OVER(PARTITION BY model_year ORDER BY list_price ASC) RankNum,
		DENSE_RANK() OVER(PARTITION BY model_year ORDER BY list_price ASC) DenseRankNum
FROM product.product;


------- NUMBERING FUNCTIONS 2
-- CUME_DIST()    : K�m�latif distribution = Row number/total rows. K�m�latif de�erler getirecek ve son sat�r "1" olacak
-- PERCENT_RANK() : Percent_rank = (row number -1) /(total rows -1)
-- NTILE(N)       : E�it say�da k�melere b�lme. Veri s�raland�ktan sonra k�me say�s�n� belirtip k�meleme yap�yoruz


-- Soru: Write a query that returns the cumulative distribution of the list price in product table by brand.
-- product tablosundaki list price' lar�n k�m�latif da��l�m�n� marka k�r�l�m�nda hesaplay�n�z
SELECT brand_id,list_price,
    ROUND(CUME_DIST() OVER(PARTITION BY brand_id ORDER BY list_price),3) as CUM_DIST
FROM product.product;

-- brand_id partition a g�re ilk veri y�zde ka�l�k dilime denk geliyorsa yazd�, 
-- ..partition bitti�inde, yani son de�er 1 oldu
--  ROUND(x,3) --- virg�lden sonra ka� basamak g�rmek istiyoruz: 3 basamak		
----------------------------------
-- Soru: Write a query that returns the relative standing of the list price in product table by brand.
SELECT brand_id,list_price,
    ROUND(CUME_DIST() OVER(PARTITION BY brand_id ORDER BY list_price),3) as CumDist,
    ROUND(PERCENT_RANK() OVER(PARTITION BY brand_id ORDER BY list_price),3) as PercentRank
FROM product.product;
----------------------------------
-- Yukar�daki CumDist s�tununu CUME_DIST fonksiyonu kullanmadan hesaplay�n�z
with tbl as (
	select	brand_id, list_price,
			count(*) over(partition by brand_id) TotalProductInBrand,
			row_number() over(partition by brand_id order by list_price) RowNum,
			rank() over(partition by brand_id order by list_price) RankNum
	from	product.product
)
select *,
	round(cast(RowNum as float) / TotalProductInBrand, 3) CumDistRowNum,
	round((1.0*RankNum / TotalProductInBrand), 3) CumDistRankNum
from tbl
-- WITH ile ge�ici tablo olu�turduk, sorgumuz daha sade g�z�ks�n diye
-- Row_number la hesaplamak m�, Rank_number la hesaplamak m� daha do�ru bakt�k. --
-- Tam istedi�imiz sonuca ula�amad�k 2 si ile de. Hoca bak�p sonucu atacak

-------------------------- Farkl� �rnekler

--Write a query that returns both of the followings:
--The average product price of orders.
--Average net amount.
--A�a��dakilerin her ikisini de d�nd�ren bir sorgu yaz�n:
--Sipari�lerde yer alan �r�nlerin liste fiyatlar�n�n ortalamas�
--T�m sipari�lerdeki ortalama net tutar�
SELECT DISTINCT order_id, 
AVG(list_price) OVER(PARTITION BY order_id) avg_price, 
AVG(list_price * quantity* (1-discount)) OVER() avg_net_amount
FROM sale.order_item

-- OVER() : Tablonun tamam� tek bir partition olmas�n� istedi�imiz i�in partition yapmad�k burada
-----------------------------------
-- Soru: --List orders for which the average product price is higher than the average net amount.
--Ortalama �r�n fiyat�n�n ortalama net tutardan y�ksek oldu�u sipari�leri listeleyin.
select * from (SELECT DISTINCT order_id, 
cast(AVG(list_price) OVER(PARTITION BY order_id) as numeric(6,2)) AvgPrice, 
cast(AVG(list_price*quantity*(1-discount)) OVER() as numeric(6,2)) AvgNetPrice
FROM sale.order_item) A
where A.AvgPrice > A.AvgNetPrice
-------------------------------------------
-- Cumulative sorusu
-- Soru : Calculate the stores' weekly cumulative number of orders for 2018
SELECT A.store_id, A.store_name, B.order_date,
DATEPART(ISO_WEEK, B.order_date) WeekOfYear
FROM sale.store A, sale.orders B where A.store_id = B.store_id And Year(B.order_date)= '2018'
order by 1,3
-- �imdi partition �m burada store_id ve week of year olacak
-- Yani store id ve Select blo�unda DATEPART(ISO_WEEK, B.order_date) fonksiyonun sonucundan d�nene g�re partition yapaca��z
SELECT A.store_id, A.store_name, B.order_date,
DATEPART(ISO_WEEK, B.order_date) WeekOfYear,
COUNT(*) OVER(PARTITION BY A.store_id, DATEPART(ISO_WEEK, B.order_date)) weeks_order
FROM sale.store A, sale.orders B where A.store_id = B.store_id And Year(B.order_date)= '2018'
order by 1,3
-- Bir sonraki s�tuna ge�elim. Ma�azan�n k�m�latif sat�� say�s�(haftal�k)
select  a.store_id, a.store_name, -- b.order_date,
	datepart(ISO_WEEK, b.order_date) WeekOfYear,
	COUNT(*) OVER(PARTITION BY a.store_id, datepart(ISO_WEEK, b.order_date)) weeks_order,
	COUNT(*) OVER(PARTITION BY a.store_id ORDER BY datepart(ISO_WEEK, b.order_date)) cume_total_order
from sale.store A, sale.orders B
where a.store_id=b.store_id and year(order_date)='2018'
ORDER BY 1, 3
-- 1. haftada toplam 4 sat��, ccum sat�� 4 , 2. hafta 6, cum sat�� 10 , 3. hafta 3, cum_sat�� 13 vs vs
-- Son olarak buna bir distinct atal�m.
select distinct a.store_id, a.store_name, -- b.order_date,
	datepart(ISO_WEEK, b.order_date) WeekOfYear,
	COUNT(*) OVER(PARTITION BY a.store_id, datepart(ISO_WEEK, b.order_date)) weeks_order,
	COUNT(*) OVER(PARTITION BY a.store_id ORDER BY datepart(ISO_WEEK, b.order_date)) cume_total_order
from sale.store A, sale.orders B
where a.store_id=b.store_id and year(order_date)='2018'
ORDER BY 1, 3
-- Sonu�: Her bir sat�r o haftan�n toplam sat�� say�s�n� g�steriyor
-------------------------------------------
-- Soru: Calculate 7-day moving average of the number of products sold between '2018-03-12' and '2018-04-12'
-- o g�nl�k sat�� ve 1 �nceki haftan�n ortalama sat�� say�s�

--- �nce ihtiyac�m�z olanlara bakal�m
select B.order_date, A.order_id, A.product_id, A.quantity
from sale.order_item A, sale.orders B
where A.order_id = B.order_id
-- Ay�n 1 inde toplam 11 tane �r�n sat��m��, ay�n 2 sinde toplam 2 �r�n
-- g�nl�k bazda ka� �r�n sat�ld���n� bilmem laz�m
-- 7 g�n geri ve ileri gidebilece�im ve birbiriyle k�yaslayabilece�im bir yap� olmal�
-- Bu veri setinden tek bir g�n i�in toplam quantity yi g�rmem laz�m onu 1 hafta �ncesiyle kat��la�t�raca��z
-- Bunu da sorgum kar���k olmas�n diye WITH ile ge�ici tablo olu�tural�m
with tbl as (
	select	B.order_date, sum(A.quantity) SumQuantity --A.order_id, A.product_id, A.quantity
	from	sale.order_item A, sale.orders B
	where	A.order_id = B.order_id
	group by B.order_date)
select	* from tbl
-- Son 7 g�ndeki hareketli ortalamay� hesaplayaca��z. Bunu da o g�nden geriye 7 sat�r git
-- .. o de�erlerin ortalamas�n� getir diyece�iz. O g�n�n yan�na yazd�raca��z
-----------NOT: HATA var gibi g�r�n�yor ancak sonu� geliyor----
with tbl as (
	select	B.order_date, sum(A.quantity) SumQuantity --A.order_id, A.product_id, A.quantity
	from	sale.order_item A, sale.orders B
	where	A.order_id = B.order_id
	group by B.order_date)
select	*,
	avg(SumQuantity) over(order by order_date rows between 6 preceding and current row) sales_moving_average_7
from	tbl
where	order_date between '2018-03-12' and '2018-04-12'
order by 1

-- partition yapmama gerek yok ancak frame belirlemem laz�m(7 sat�rl�k ortalama i�in)
-- between 6 preciding and current row : 6 sat�r geriye + 1 current row = 7 g�nl�k 
-- Ortalamay� integer yerine float istersek cast(.. as float.. ) �eklinde yapabiliriz
-- Sipari�i olmayan tarihler var. O zaman gerideki g�nleri sayamayaca��z.
-- E�er bu kay�p g�nler �nemliyse, tariht tablosu olu�turmam�z laz�m
-- .. left joinle olmayan tarihleride ekleyelim sonra olmayan tarihlerin kar��s�na 0 yaz�p sonra
-- .. �stteki sorgumuzla sonuca ula�abiliriz
-- where blo�unda ko�ulu al�p ondan sonra filtreleme yap�yor burada
-- �nce partition yap�p sonra filtrelemeyi yapacaksam . partitionl� sorguyu bir tabloya kaydedip
-- .. sonra where blo�u ekleyebilirim ba�ka bir sorguda
-------------------------------
-- Soru: List customers whose have at least 2 consecutive orders are not shipped
-- NOT: Hoca kendisi ger�ek hayatta ��zd��� bir problemin ��z�m�n� atacak notlarda

