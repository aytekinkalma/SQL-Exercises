--SQL-9. ders_13.06.2022(session-8)


--1.CORRELATED SUBQUERIES
-- �ok yayg�n kullan�l�r
-- 2 fonksiyon var burada. 1.Exist 2.non-exist
-- exist : tabloya bir sorgu at�yorusunuz sonra B tablosundan ya da yine A tablosunda bu kay�tlar�n ba�ka bir yerde bulunup
-- .. bulunmad���na bak�yorsunuz. Bir alan �ekmiyorsunuz oradan. Sadece var m� yok mu buna bak�yoruz. Bir check etme i�lemi yani
-- NOT exist : Tam tersi 2. tabloda olmama durumunu test ediyorsunuz


-- EXIST
SElect * from sale.customer WHERE EXISTS(SELECT 1)

SELECT * from sale.customer A WHERE EXISTS (SELECT 1 FROM sale.orders B WHERE B.order_date > '2020-01-01' AND A.customer_id=B.customer_id)
-- Bana sadece 2020 ocak 1 den sonra sipari� vermi� olma "durumunu" g�ster
-- SELECT 1: Buradaki 1 in hi� bir anlam� yok. Buna tak�lmayal�m

------------

-- NOT EXIST
SElect * from sale.customer WHERE NOT EXISTS(SELECT 1)

SELECT * from sale.customer A WHERE NOT EXISTS (SELECT 1 FROM sale.orders B WHERE B.order_date > '2020-01-01' AND A.customer_id=B.customer_id)
-- Bana sadece 2020 ocak 1 den sonra sipari� yapm�� olmama "durumunu" g�ster
-- Soru: Bu sorguda diyelim biri yeni kaydedilmi� ve sipari�i olmam��. BU sorgu sonucunda bu m��teri gelir mi gelmez mi ?
-- ...Kriter �u burada: Customer tablosuna gidiyor her bir sat�r i�in customer_id 1 sonra order tablosuna gidiyor orders � varsa al�yor yoksa alm�yor
-- ... inner query i�inde varsa o ki�iyi al�yor yoksa eliyor. Yani gelmesi laz�m

--Soru: Apple - Pre-Owned iPad 3 - 32GB - White �r�n�n hi� sipari� verilmedi�i eyaletleri bulunuz.
--Eyalet m��terilerin ikamet adreslerinden al�nacakt�r.

Select * from product.product WHERE product_name = 'Apple - Pre-Owned iPad 3 - 32GB - White'

-- Bu �r�n�n hangi sipari�lerde verildi�ini bir sorgulayay�m sonra eyalet k�sm�na ge�i� yapal�m�

select	distinct C.state
from	product.product P,
		sale.order_item I,
		sale.orders O,
		sale.customer C
where	P.product_name = 'Apple - Pre-Owned iPad 3 - 32GB - White' and
		P.product_id = I.product_id and
		I.order_id = O.order_id and
		O.customer_id = C.customer_id
;

-- �imdi bana �yle bir eyalet getir ki o eyalette bu �r�n sat�n al�nmam�� olsun
-- UNION la birle�tirip olmayanlar� EXCEPT ile ��kartabiliriz vs ama �imdi biz NOT EXIST ile yapaca��z burada

-- Exist i�ine yukar�daki sorguyu yap��t�r�yoruz outer query de from dan sonra sale.customer C2 dedik
-- .. ��nk� bir �art eklemeliyiz(Altta a��klan�yor)
select	distinct [state]
from	sale.customer C2
where	not exists (
			select	distinct C.state
			from	product.product P,
					sale.order_item I,
					sale.orders O,
					sale.customer C
			where	P.product_name = 'Apple - Pre-Owned iPad 3 - 32GB - White' and
					P.product_id = I.product_id and
					I.order_id = O.order_id and
					O.customer_id = C.customer_id and
					C2.state = C.state
		)
;

-- �art�m�z: C2.state = C.state : Yani, outer query de gelen statelerin inner query de olmama �art�n� inner query ye ekliyorum
-- EXIST ya da NOT EXIST i foreign keyler ya da primary keyler �zerinden yaparsak daha h�zl� �al���r
-- .. Di�er t�rl� t�m tabloyu taramas� gerekiyor


--Dersin 2. b�l�m�
--Soru: Burkes Outlet ma�aza sto�unda bulunmay�p,
-- Davi techno ma�azas�nda bulunan �r�nlerin stok bilgilerini d�nd�ren bir sorgu yaz�n

SELECT PC.product_id, PC.store_id, PC.quantity
FROM product.stock PC, sale.store SS
WHERE PC.store_id = SS.store_id AND SS.store_name = 'Davi techno Retail' AND
NOT EXISTS( SELECT DISTINCT A.product_id, A.store_id, A.quantity
FROM product.stock A, sale.store B
WHERE A.store_id = B.store_id AND B.store_name = 'Burkes Outlet' AND PC.product_id = A.product_id AND A.quantity>0)

--- Davi techno Retail da sto�u bulunnanlar� alacak
--- Burkes Outlet in stocklar�nda quantity>0 olanlar� not exists yapacak
--- quantityi belirtmeseydik;
--- ��kt� hi�bir �ey getirmedi. Buradan �u ��k�yor olabilir. Bu �r�nlerin(��kt�daki 5 tane) Burkes outlet ma�aza�nda sat�rlar� var
-- ancak bu �r�nlerin stock miktarlar� 0.
-- sale.store tablosunu inner query ile kullanmad�k ama yinede outer query de SS.store_name diyebiliriz

-- B�t�n �r�nlerimin stock bilgisi stock tablosunda var. Burkes in sto�unda 0 olarak g�z�ken �r�nlerden bul diye de sonuca ula�abiliriz
-- Exists ve quantity=0 diyerek
SELECT PC.product_id, PC.store_id, PC.quantity
FROM product.stock PC, sale.store SS
WHERE PC.store_id = SS.store_id AND SS.store_name = 'Davi techno Retail' AND
EXISTS( SELECT DISTINCT A.product_id, A.store_id, A.quantity
FROM product.stock A, sale.store B
WHERE A.store_id = B.store_id AND B.store_name = 'Burkes Outlet' AND PC.product_id = A.product_id AND A.quantity=0)


-- Soru: -- Brukes Outlet storedan al�n�p The BFLO Store ma�azas�ndan hi� al�nmayan �r�n var m�?
-- Varsa bu �r�nler nelerdir?
-- �r�nlerin sat�� bilgileri istenmiyor, sadece �r�n listesi isteniyor.

SELECT P.product_name
FROM product.product P   
WHERE NOT EXISTS (
SELECt I.product_id
FROM sale.order_item I, sale.orders O, sale.store S
WHERE I.order_id = O.order_id AND S.store_id = O.store_id 
AND S.store_name = 'The BFLO Store' 
and P.product_id = I.product_id)

-- sorguya devam ediyoruz
-- P.product_name: product name geliyor ancak bu a�a��daki kurala uymal�(subquery de)
-- NOT EXIST Dedi�ine g�re bir�eyleri eleyece�iz. (The BFLO Store ma�azas�ndan hi� al�nmayan)
-- Elemek istedi�imiz yer: P.product_id = I.product_id  bu kod . B�t�n product listemizde "The BFLO Store" dan sipari� edilmi� �r�nleri eliyorum
-- Bir kriter daha vard�: Brukes Outlet storedan al�nan o y�zden AND diyip EXISTS diyip devam ediyorum
-- Sonu� olarak 8 tane �r�n geldi. 520 tane �r�nden 8 geldi
-- Tek sorguda product tablosunda istedi�imiz 8 sat�r� se�mi� olduk

SELECT P.product_name, p.list_price, p.model_year
FROM product.product P
WHERE NOT EXISTS (
		SELECt	I.product_id
		FROM	sale.order_item I,
				sale.orders O,
				sale.store S
		WHERE	I.order_id = O.order_id AND S.store_id = O.store_id
				AND S.store_name = 'The BFLO Store'
				and P.product_id = I.product_id)
	AND
	EXISTS (
		SELECt	I.product_id
		FROM	sale.order_item I,
				sale.orders O,
				sale.store S
		WHERE	I.order_id = O.order_id AND S.store_id = O.store_id
				AND S.store_name = 'Burkes Outlet'
				and P.product_id = I.product_id)
;
    
--- Bunu yine except ile yapabilirdik

SELECT	distinct I.product_id
		FROM	sale.order_item I,
				sale.orders O,
				sale.store S
		WHERE	I.order_id = O.order_id AND S.store_id = O.store_id
				AND S.store_name = 'Burkes Outlet'
except
		SELECT	distinct I.product_id
		FROM	sale.order_item I,
				sale.orders O,
				sale.store S
		WHERE	I.order_id = O.order_id AND S.store_id = O.store_id
				AND S.store_name = 'The BFLO Store'
;


-------------------------------------
-- CTE(Common Table Expressions)
-- Bir VIEW gibi �al���rlar.
-- Sorgu s�recinde o s�rada meydana gelip daha sonra Sorgu sonunda kaybolan objelerdir.
-- Sadece sorguya �zg� VIEW diyebiliriz.
-- ALL CTEs(ordinary or recursive) stat with a "WITH" clause ...
-- Bir common table i�inde birden fazla WITH clause kullan�labilir
-- 2. �e�iti var 1.Ordinary 2. Recursive

-------------------------
-- 1.Ordinary Common Table Expressions
/*
WITH query_name [(column_name1, ...)] AS
(SELECT ... ) -- CTE Definition

SQL_Statement; -- yukarda tan�mlam�� oldu�umuz tabloyu kullan�yoruz bu statementta
*/
------------
-- 2.Recursive Common Table Expressions
/*
WITH table_name (column_list) AS
..............
Hoca: devam� �nemli de�il ��nk� ihtiya� olunca gerekli kaynaklardan kopyala yap��t�r yapaca��z �al���rken
*/
-- for d�ng�s� gibi kural tan�mlayarak bir sorgu olu�turabiliyorsunuz

---------

-----------------------------
-- 1.Ordinary Common Table Expressions
-- Soru: -- Jerald Berray isimli m��terinin son sipari�inden �nce sipari� vermi� 
--ve Austin �ehrinde ikamet eden m��terileri listeleyin.

SELECT * FROM sale.customer a, sale.orders b
WHERE a.first_name = 'Jerald' and a.last_name ='Berray'
and a.customer_id = b.customer_id 

-- her y�lda 1 er tane sipari� var. Buradan max(order_date i se�ece�iz)

SELECT  max(b.order_date) FROM sale.customer a, sale.orders b
WHERE a.first_name = 'Jerald' and a.last_name ='Berray'
and a.customer_id = b.customer_id 

--- bu elimizde dursun. �imdi austin �ehrinde ikamet edenlere bakal�m
SElect * from sale.customer a 
where a.city = 'Austin'
--42 rows

----

SElect * from sale.customer a , sale.orders b
where a.city = 'Austin' and a.customer_id = b.customer_id
--35 row.. hepsinin sipari� bilgisi yokmu�

--- WITH i kullanal�m

with tbl AS (
	select	max(b.order_date) JeraldLastOrderDate
	from	sale.customer a, sale.orders b
	where	a.first_name = 'Jerald' and a.last_name = 'Berray'
			and a.customer_id = b.customer_id
)
select	*
from	sale.customer a,
		Sale.orders b,
		tbl c
where	a.city = 'Austin' and a.customer_id = b.customer_id and
		b.order_date < c.JeraldLastOrderDate
;


--- b.order_date < c.JeraldLastOrderDate ko�ulu sona eklemi� olduk

-- Dersin 3. b�l�m�
-- NOT : With clause sadece tek bir sorguda �al���yor. 
-- Fakat with blo�unda birden fazla sorgu tan�mlayabilirsiniz
-- Bununla ilgili bir �rnek yapal�m


-- Herbir markan�n sat�ld��� en son tarihi bir CTE sorgusunda,
-- Yine herbir markaya ait ka� farkl� �r�n bulundu�unu da ayr� bir CTE sorgusunda tan�mlay�n�z.
-- Bu sorgular� kullanarak  Logitech ve Sony markalar�na ait son sat�� tarihini ve toplam �r�n say�s�n� (product tablosundaki) ayn� sql sorgusunda d�nd�r�n�z

with tbl as(
	select	br.brand_id, br.brand_name, max(so.order_date) LastOrderDate
	from	sale.orders so, sale.order_item soi, product.product pr, product.brand br
	where	so.order_id=soi.order_id and
			soi.product_id = pr.product_id and
			pr.brand_id = br.brand_id
	group by br.brand_id, br.brand_name
) ,  ---1. tablo sonucunda her bir product �n son sipari� tarihi . 23 brand_id li DENAQ 2020-04-23 te en son sipari� verilmi�
tbl2 as(
	select	pb.brand_id, pb.brand_name, count(*) count_product
	from	product.brand pb, product.product pp
	where	pb.brand_id=pp.brand_id
	group by pb.brand_id, pb.brand_name
)  ---2. tabloda Her bir markada ka� �r�n�n bulundu�u. 40 sat�r geldi
select	*
from	tbl a, tbl2 b
where	a.brand_id=b.brand_id and
		a.brand_name in ('Logitech', 'Sony')

--- Sony markas�na ait herhangi bir �r�n en son 2020-10-21 de sipari� verilmi�
--- ve sony markas�na ait envanterimde 46 �r�n varm�� 
--- Logitect markas�na ait herhangi bir �r�n en son 2020-08-23 de sipari� verilmi�
--- ve sony markas�na ait envanterimde 27 �r�n varm��


------------------------
-- Recursive CTE Expressions
-- ��erisinde UNION ALL yaz�p CTE i�erisinde belirtmi� oldu�umuz tabloyu kullanaca��z recursive �ekilde

-- 0'dan 9'a kadar herbir rakam bir sat�rda olacak �ekide bir tablo olu�turun.
-- Normalde kal�b�m�z a�a��daki gibi
/*
WITH CTE AS ()
SELECT * from CTE;
*/

-- Bu hata veriyor.�imdi parantez i�ini dolduraca��m
-- Tablo ad�m CTE olsun

WITH CTE AS (select 0 rakam UNION ALL select 1 rakam)  -- Bu �ekilde 10 a kadar gidebiliriz
SELECT * from CTE;

--- Bunu dinamik yapal�m ad�m ad�m ..DIKKAT Bu alttaki sonsuza kadar gider
---WITH CTE AS (select 0 rakam UNION ALL select rakam+1)
---SELECT * from CTE;

---WHERE blo�unda bunu s�n�rlayal�m

WITH CTE AS (select 0 rakam UNION ALL select rakam+1 from cte where rakam<9)
SELECT * from CTE;

--- Raporlamada bu tip tablolar �ok kullan�yorlar.
-- PowerBI da bir database olu�turarak bunu kullanacaks�n�z
-- DB ler genelde tarihler olur. Haftan�n g�n�, tatil mi de�il. O tarihin i�inde bulundu�u ay�n ilk g�n�, son g�n� vs
-- .. gibi attribute lar olur. Bunlar �ok b�y�k esneklik sa�lar. Sizde CTE ile ba�lay�p b�yle bir attribute(ya da tablo) olu�turabilirsiniz


--Soru: 2020 ocak ay�n�n herbir tarihi bir sat�r olacak �ekilde 31 sat�rl� bir tablo olu�turunuz.
--with cast('2020-01-01' as date) tarih  --- veriyi date olarak cast ettik

with ocak as (
	select	cast('2020-01-01' as date) tarih  --- veriyi date olarak cast ettik
	union all
	select	cast(DATEADD(DAY, 1, tarih) as date) tarih   -- �stteki "tarih" ile tan�mlanana 1 ekle DATEADD(DAY, 1, tarih) as date datetime olarak geldi�i i�in bunuda cast ettik
	from ocak
	where tarih < '2020-01-31'
)
select * from ocak;
with cte AS (
	select cast('2020-01-01' as date) AS gun
	union all
	select DATEADD(DAY,1,gun)
	from cte
	where gun < EOMONTH('2020-01-01')  --EOMONTH: ay�n son g�n�n� al�r
) --- buradan sonra biz tarih tablosu olu�tural�m
select gun tarih, day(gun) gun, month(gun) ay, year(gun) yil,
	EOMONTH(gun) ayinsongunu
from cte;

-- Siz bunun yan�na tarih tablosu olu�turacaksan�z ekleme yapabilirsiniz
-- Bu �ekilde bir �ok attribute olu�turursan�z bu size �ok b�y�k zenginlik kazand�racakt�r.
-- her bir tablodaki tarih ile bu tabloyu joinlersiniz. Yani bu tarihleri di�er tablolarda kullanabilirsiniz.
-- Bunun ��k�� noktas� common table expressions

----------------------

--- Soru: Write a query that returns all staff with their manager_ids(use recursive CTE)
-- Her bir �al��an�n patronuyla CTE sini alaca��z burada

Select staff_id, first_name, manager_id from sale.staff where staff_id =1
 --- �imdi de manager � james olan ki�ileri getirelim
Select * from sale.staff a where a.manager_id = 1

-- �imdi with ekleyelim ve where a.manager_id = 1 i manuel olarak almayaca��m. Bir �nce tan�mlam�� oldu�um ki�inin id sine(staff_id) sine e�itleyece�iz

with cte as (
	select	staff_id, first_name, manager_id
	from	sale.staff
	where	staff_id = 1
	union all
	select	a.staff_id, a.first_name, a.manager_id
	from	sale.staff a, cte b
	where	a.manager_id = b.staff_id
)
select *
from	cte
;

--- a.manager_id = b.staff_id si 1 olanlar� �a��r sonra   a.manager_id ye d�necek sonra sale.staff a tekrar gidecek tekrar
--- a.manager_id = b.staff_id  ye bakacak vs vs b�yle devam edip En sonra manager_id si olmayana d�necek ve break olacak sorgumuz
--- Bu tip bir sorgu raporlama yaparken i�e yarar yoksa �u �ekilde de yapabilirdik.


select staff_id, first_name, manager_id
from sale.staff
order by manager_id

--------------------
--- Soru: --2018 y�l�nda t�m ma�azalar�n ortalama cirosunun alt�nda ciroya sahip ma�azalar� listeleyin.
--List the stores their earnings are under the average income in 2018.
--- with clause un alt�nda 2 tane tablo tan�mlayaca��z

WITH T1 AS (
SELECT	c.store_name, SUM(list_price*quantity*(1-discount)) Store_earn
FROM	sale.orders A, SALE.order_item B, sale.store C
WHERE	A.order_id = b.order_id
AND		A.store_id = C.store_id
AND		YEAR(A.order_date) = 2018
GROUP BY C.store_name
),
T2 AS (
SELECT	AVG(Store_earn) Avg_earn
FROM	T1
)
SELECT *
FROM T1, T2
WHERE T2.Avg_earn > T1.Store_earn
;

---1. tabloda Her bir store name her bir ma�azan�n yapm�� oldu�u sat�� tutar�. Filtre olarak da y�la 2018 dedik
---2.tabloda T1 deki de�erlere g�re ortalama ald�k
--- Tablolar� birbiri i�erisinde referans g�sterebiliyoruz
--- Final de T1,T2 tablosuna git T2 deki ortalama cironun T1 deki store cirolar�ndan b�y�k olan ma�azalar� getir




