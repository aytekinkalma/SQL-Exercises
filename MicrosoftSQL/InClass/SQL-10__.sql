-- SQL-10. ders_15.06.2022(session-9)
-- Dersin 1. b�l�m�
-- WINDOW FUNCTIONS
-- 3 g�n s�recek
-- Daha az sat�r sorgu ile hem de verideki detay� kaybetmiyoruz

-- CONTENT
-- 1.Window Functions(WF) vs GROUP BY
-- 2.Types of WF
-- 3.WF Syntax and Keywords
-- 4.Window frames      -- �ok �nemli
-- 5.How to Apply WF

---------------------------------
-- 1.GROUP BY vs WF
-- GROUP BY  aggregate fonksiyon ile tek sat�r sonu� d�nd�r�yordu.
-- WF Ayn� group by mant���nda �al���yor ama sat�r say�s�nda azalma olmuyor
-- Group by biraz yava�, WF daha h�zl�d�r(Genelde)

/*
                                   Group by       Window Functions      
 Distinct                          necessity      optional
 Aggregation                       necessity      optional
 Ordering                          invalid         valid
 Performance                       shower          faster
 Dependency on selected Field      dependent      independent

Distinct    : Group by da distinct sonu� gelir, WF de bu oladabilir olmayadabilir
Aggregation : Aggregate kullanmak gerekir group by da, WF de bu oladabilir olmayadabilir ��nk� aggregare haricinde bir �ok fonksiyonu vard�r 
Ordering    : Group by i�inde kullan�lm�yor. Bir grup belirliyorsunuz. TAbloda birden fazla s�n�f olsun
 .. bu tabloda s�n�fa g�re gruplama yaparsan�z ��rencilerin notlar� aras�nda ortalama de�i�mez group by da
 .. WF de order by gerekiyor genelde. Belirledi�iniz grubun ortalamas�na g�re farkl� sonu�lar d�nd�r�yor WF

Performance : Group by biraz yava�, WF daha h�zl�d�r(Genelde)
Dependency on selected Field: Group by yaparken bilgilerin se�ilen alana ba�l�d�r. Baz� bilgiler kaybolur ��kt�da  WF de bu ba��ms�zd�r
*/

-- GROUP BY: Group by yapt�ktan sonra fonksiyon unique belirliyor gruplar� ve ��kt� veriyor
-- WF: Gruplar� kendiniz manuel tan�mlayabiliyorsunuz. Bu her bir grup bize bir Frame(window) i g�steriyor

-- �imdi group by ve WF kullanarak bir �rnek yapal�m
-- Soru: Her bir �r�n�n toplam stok miktar�n� hesaplay�n
---------- group by ; 
select product_id, Sum(quantity) from product.stock
group by product_id
order by 1

----------- WF;
-- �nce bir stock tablomuza bakal�m
select * from product.stock
order by product_id

-- Yeni bir sat�r ekleyece�iz �imdi
-- 1 numaralar� �r�n�n b�t�n sat�rlardaki toplam�n� yazd�rmak istiyorum
select *, sum(quantity) over(partition by product_id) sumWF
from product.stock
order by product_id

--- sum(quantity) over(partition by product_id) sumWF : her bir product_id i�in quantity toplam�n� al ve sumWF de yazd�r

--- group by ile ayn� sonu� istedi�i i�in distinct ataca��z. distinct i product_id ye ataca��z
select	distinct product_id, sum(quantity) over(partition by product_id) sumWF
from	product.stock
order by product_id

-- �NEML� NOT: Where �art�na yazaca��n�z �art WF hesaplanmadan �nce uygulan�r
-- Soru: markalara g�re ortalama �r�n fiyatlar�n� group by ve WF ile yapal�m
----------- group by;
select brand_id, avg(list_price)
from product.product
group by brand_id 

------------ WF;
select brand_id, avg(list_price) over(partition by brand_id) as avg_price
from product.product
-- 520 rows
--  group by ile ayn� ��kt� gelmesi i�in distinct ekleyelim
select distinct brand_id, avg(list_price) over(partition by brand_id) as avg_price
from product.product
-- 40 rows
-----------------------------------------------

-- 2 tane WF kullanal�m
-- Soru: brand_id ye g�re her bir brand_id de ka� �r�n var ve her bir brand id ye g�re en y�ksek fiyatl� �r�n
select	*,
		count(*) over(partition by brand_id) CountOfProduct,
		max(list_price) over(partition by brand_id) MaxListPrice
from	product.product
order by brand_id, product_id


---- Dersin 2. b�l�m�


--  WF ile olu�turdu�unu kolonlar birbirinden ba��ms�z hesaplan�r.
-- Dolay�s�yla ayn� select blo�u i�inde farkl� partitionlar tan�mlayarak yeni kolonlar olu�turabiliriz
-- group by l� sorgularda tek bir partition vard�r(Select den sonra yaz�lan aggregate fonksiyonlar tek bir partition d�r)
-- WF de s�tunlar aras�nda partitionlar farkl� olabilir

--Soru: WF ile her bir markadan ka�ar tane �r�n var ve her bir kategory i�indeki toplam �r�n say�s�n� bulal�m

select	product_id, brand_id, category_id, model_year,
		count(*) over(partition by brand_id) CountOfProductinBrand,
		count(*) over(partition by category_id) CountOfProductinCategory
from	product.product
order by brand_id, product_id, model_year

-- 520 rows
-- brand_id    si 1 olandan toplam 41 �r�n varm��, vs vs
-- category_id si 1 olandan toplam 40 �r�n varm��, 4 numaral� kategoriden 283 tane �r�n varm�� vs vs
-- order by ile s�ralamay� de�i�tirip ona g�re ��kt�m�z� istedi�imiz s�ralamada getirebiliriz
-- order by ile sonucu daha rahat g�zlemliyoruz. O y�zden order by ile kullanmam�z daha iyi olacakt�r

-- NOT: Burada distinct yapabilir miyiz? Sonu� de�i�mez ��nk� product_id ler unique zaten
-- .. o y�zden product_id select blo�unda durdu�u s�rece distinct i�e yaramayacakt�r
-- .. product_id yi silip yaparsam distinct row say�s� azalacakt�r. ��nk� �oklayan sat�rlar varolacak.

----------------------------
-- 2.TYPES of WF
-- a.Aggregate Functions --- Avg, min, ...
-- b.Navigation Funtions --- Partition i�erisinden gezinerek yapt���m�z 
-- c.Numbering Functions --- Partition lar i�erisinde belirledi�imiz s�ralama ile

----------------------------
-- 3.TYPES of WF
-- Syntax and Keywords
-- Select(columns) FUNCTION() OVER(PARTITION BY ... ORDER BY ... WINDOW FRAME) from table1;
-- Hesaplayaca��m�z fonksiyonda s�ralama �nemliyse partition i�inde order by yap�yoruz

-- �rnek kod(Hata verir)
-- SELECT *, avg(time) over (partition by id order by date rows between 1 preciding and current row) as avg_time from time_of_sales  --  

-- rows between 1 preciding and current row : 1 �nceki sat�rla i�inde bulundu�u sat�r ortalamas�n� al

-------------------------------------------
-- 4.Window frames 
-- Verinin tamam� bir partition olsun sonra biz bunu farkl� partition lara b�l�yoruz sonra da
-- .. bi basamak sonra sat�rlar aras�ndaki ili�kiye window frame tan�ml�yoruz. As�l konu burada d�n�yor.
-- .. belirledi�imiz frame �zerinde fonksiyonumuz �al���yor. Bunun s�n�rlar�n� de�i�tirebiliyorum
-- .. �rneklerde daha net oturacak.
-- current row: i�lem yap�lan sat�r olsun mesela
-- partition ba��ndan itibaren current row a kadar olan sat�r bu sat�r benim frame im olsun diyebilirim(current row dahil) -- unbounded(k�m�latif toplam)
-- partition  current row dan itibaren sona kadar olan sat�r bu sat�r benim frame im olsun diyebilirim .. 
-- N Preciding, M following Current row dan ba�larsam; 3 �nceki sat�rdan ba�lay�p 5 sonraki sat�ra kadar git diyebilirim. Toplam 9 sat�r�m olacakt�r

------------------------------------------
-- 5. How to Apply WF

/*
�rnek

id      date       time
1     2019-07-05    22
1     2019-04-15    26
2     2019-02-06    28
1     2019-01-02    30
2     2019-08-30    20
2     2019-03-09    22

PARTITION BY id                ---> ORDER by             -- avg(time)(ROWS BETWEEN 1 PRECIDING AND CURRENT ROW)
id      date        time      id  date         time     id        date    time       avg_time
1     2019-07-05    22        1   2019-01-02    30       1   2019-01-02    30          30
1     2019-04-15    26        1   2019-04-15    26       1   2019-04-15    26          28
1     2019-01-02    30        1   2019-07-05    22       1   2019-07-05    22          24
                                                         2   2019-02-06    28          28
id      date        time      id  date         time      2   2019-03-09    22          25
2     2019-02-06    28         2  2019-02-06   28        2   2019-08-30    20          21
2     2019-08-30    20         2  2019-03-09   22
2     2019-03-09    22         2  2019-08-30   20

*/
--- Hoca : �al��aca��n�z yerde raporlama yap�l�yorsa bu WF konusunu �ok fazla kullan�yorsunuz
---------------------------------------------------------------------------------
-- S�rekli kullan�labilecek bir sorgu g�sterece�iz WF ile alakal�
-- Windows frame i anlamak i�in birka� �rnek:
-- Herbir sat�rda i�lem yap�lacak olan frame in b�y�kl���n� (sat�r say�s�n�) tespit edip window frame in nas�l olu�tu�unu a�a��daki sorgu sonucuna g�re konu�al�m.

SELECT	category_id, product_id,
		COUNT(*) OVER() NOTHING,
		COUNT(*) OVER(PARTITION BY category_id) countofprod_by_cat,
		COUNT(*) OVER(PARTITION BY category_id ORDER BY product_id) countofprod_by_cat_2,
		COUNT(*) OVER(PARTITION BY category_id ORDER BY product_id ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) prev_with_current,
		COUNT(*) OVER(PARTITION BY category_id ORDER BY product_id ROWS BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING) current_with_following,
		COUNT(*) OVER(PARTITION BY category_id ORDER BY product_id ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) whole_rows,
		COUNT(*) OVER(PARTITION BY category_id ORDER BY product_id ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) specified_columns_1,
		COUNT(*) OVER(PARTITION BY category_id ORDER BY product_id ROWS BETWEEN 2 PRECEDING AND 3 FOLLOWING) specified_columns_2
FROM	product.product
ORDER BY category_id, product_id

-- Detay olarak category_id, product_id yi ald�k sadece. 8 tane de WF yazd�k
-- farkl� frame yap�lar� tan�mland�. her bir frame de ka� sat�r geliyor g�rmek i�in bu �rne�i kullan�yoruz
-- sorgunun t�m�n� �al��t�r�nca -520 rows. Herhangi bir sat�rda herhangi bir filtreleme yapmad�k demek bu
-- 1 WF: OVER() NOTHING : Partition �n�m�z tablomuzun tamam�d�r ve tek bir partition vard�r. B�y�kl���? Tablomuzun tamam�d�r. Yani 520 rows
-- 2 WF: COUNT(*) OVER(PARTITION BY category_id) countofprod_by_cat : her bir category_id i�in farkl� bir de�er hesaplanacak
-- 3 WF: COUNT(*) OVER(PARTITION BY category_id ORDER BY product_id) countofprod_by_cat_2, : order by eklenmi�. �r�nlerin s�ralamas� �nemli de�il normalde 
-- .. ama order by tan�mlad���m�z i�in Window frame imiz de�i�iyor.
-- .. yani Window frame tan�mlamazsak partition ba��ndan current row a kadar olan bizim window frame imizdir. (�rn: 10. sat�r i�in ilk sat�rdan 10 a kadar gidiyor hepsini count yap�yor vs vs)
-- 4 WF:COUNT(*) OVER(PARTITION BY category_id ORDER BY product_id ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) prev_with_current, :
-- ... ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW: Bu default de�er oldu�u i�in bir �stteki ile ayn� ��kt� geldi. A��klama i�in bir alt�n a��klamas�na bak�nca onun tersi
-- diye mant�k kurup anlayabiliriz
-- 5 WF:COUNT(*) OVER(PARTITION BY category_id ORDER BY product_id ROWS BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING) current_with_following, :
-- .. �sttekinin tam tersi bir window frame var (yukarda unb-current), burada (current-unb fol)
-- ..BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING: Current rowdan(parition �m�z�n) partition �m�n sonuna kadar(ilk sat�r i�in partition �n tamam�d�r yani 40)
-- .. 2. sat�rdaonun 1 eksi�i vs (yani birinci partition da 40 yazd�rd�, sonra 39, sonra 37 vs vs.)
-- 6 WF:COUNT(*) OVER(PARTITION BY category_id ORDER BY product_id ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) whole_rows, :
-- .. ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) whole_rows : partition �n en ba�� ve en sonu. Partition da hangi sat�rda olursam olay�m daima partition �m�n ba�� ve sonu
-- .. aras�nda i�lem yap. O y�zden hepsi 40 geldi. 1 WF ile ayn� sonucu �retti.
-- 7 WF:COUNT(*) OVER(PARTITION BY category_id ORDER BY product_id ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) specified_columns_1, : 
-- .. ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING : partition i�erisinde 1 sat�r �ne git ve 1 sat�r sonraya git( Toplamda 1 �nceki current ve 1 sonrakini al�p 3 sat�r al�yor 
---.. NOT: E�er 1 �st sat�r ya da 1 alt sat�r partition i�erisinde de�ilse onu i�leme alam�yoruz(1. sat�r i�in count(*)=2 dir(current ve sonraki toplam 2), 2. sat�r i�in 3, 3. sat�r i�in 3 vs , partition sonunda
-- .. yani mesela 40. sat�rda yine 2 gelmi�(1 �nceki ve 1 current toplam 2))
-- 8 WF:COUNT(*) OVER(PARTITION BY category_id ORDER BY product_id ROWS BETWEEN 2 PRECEDING AND 3 FOLLOWING) specified_columns_2 :
-- .. Bu da �stteki ile ayn� mant�k ilk frame 4(1 current ve 3 following), 2. si 5(1 �st,1 current ve 3 following), 3. s� 6(2 sat�r �st,1 current ve 3 following)

-- Dersin 3. b�l�m�
-- WF lerde aggregate functions
-- Analytic Aggregate Functions :  min(), max(), avg(), count(), sum()

-- Soru: Her bir kategorideki en ucuz �r�n�n fiyat� nedir? category_id ve "cheapest_by_cat"
select *, min(list_price) over(partition by category_id) cheapest_by_cat
from product.product

-- her kategorinin yan�na o �r�n�n en ucuz fiyat�n� getirdi
-- distinct li sonu� istedi�i i�in distinct atal�m
select	distinct category_id, min(list_price) over(partition by category_id) cheapest_by_cat
from	product.product

---------------------------
-- Soru: Product tablosnda ka� farkl� product var. Toplam �r�n say�s�n� WF ile yap�n�z
select distinct count(*) over() as num_of_product
from product.product

-- Tek bir sat�rl�k sonu� istiyor. Toplam �r�n say�s�n� istiyor
-- Farkl� �r�n� bulurken count(*) yapmam�z yeterli ��nk� product_id unique
-- her bir product i�in o say�(520) tekrarlayaca�� i�in distinct yazmal�y�m

-----------------------
-- Soru: How many differnt product in the order_item table? 520 tane �r�n�n ka� tanesini satm���m?
-- Bu soru di�er soruya g�re biraz farkl�
-- 1 �r�n bu tabloda 1 den fazla tabloda ge�ebilir burada. product_id unique de�il

select distinct product_id, count(*) over(partition by product_id) as num_of_order
from sale.order_item
-- 307 rows -- Bu tabloda 307 farkl� �r�n(product_id) varm��
-- Bu 307 sonucunu tek sat�rda istiyoruz.

-- group by ile bunu yapsayd�k
select count(distinct product_id) UniqueProduct from sale.order_item

--- WF ile deneyelim
select count(distinct product_id) over() UniqueProduct from sale.order_item -- HATA. Bunu count i�inde distinct olacaksa bunu group by ile yapabiliriz

-- ya da mesela select distinct product_id yi ba�ka yerde tan�mlayaca��z
select distinct count(*) over()
from (select distinct product_id,  count(*) over(partition by product_id) as number_of_product
from sale.order_item) as a

--------------------
-- Soru: Write a query that returns how mant products are in each order?
-- Her bir sipari�te ka� farkl� �r�n oldu�unu d�nd�ren bir sorgu yaz�n? 

-- group by ile
select	order_id, count(distinct product_id) UniqueProduct,
		sum(quantity) TotalProduct
from	sale.order_item
group by order_id
-- o sipari�te uniquer product say�s� ve toplam kalem say�s�n� getirdi
-- sum(quantity) TotalProduct: Mesela order_id 1 de toplam 5 farkl� �r�n var toplam 8 �r�n var

-- WF ile
select distinct order_id, 
count(product_id) over(partition by order_id) Count_of_Uniqueproduct,
SUM(quantity) over (partition by order_id) Count_of_product
from sale.order_item
---------------------------
-- How many different product are in each brand in each category?
-- Herbir kategorideki herbir markada ka� farkl� �r�n�n bulundu�u
select distinct category_id, brand_id,
 count(*) over(partition by brand_id, category_id) count_of_Product
from product.product

-- 1 numaralar� kategoride 1 numaral� markaya ait 15 tane �r�n varm��,
-- 4 numaralar� kategoride 8 numaral� markaya ait 15 tane �r�n varm�� vs vs ...

-- brand isimlerini getirmek istersek �stteki sorguyu bir subquery olarak kullanabiliriz
select A.*, B.brand_name from 
(select distinct category_id, brand_id,
 count(*) over(partition by brand_id, category_id) count_of_Product
from product.product
 ) A, product.brand B
where A.brand_id = B.brand_id

--- join ile WF �rne�i- ayn� sonucu alal�m
select distinct category_id, A.brand_id,
count(*) over(partition by A.brand_id, A.category_id) count_of_Product,
B.brand_name
from product.product A, product.brand B
WHERE A.brand_id = B.brand_id

