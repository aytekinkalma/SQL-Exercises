--SQL-13. ders_20.06.2022(session-12)

-- DATABASE INDEX

-- Bir tabloda belli alanlara yap�lan sorgular daha fazla ise
-- .. ( Mesela: Ki�i tablosunda s�rekli isim �zerinden sotgu yap�l�yor)
-- .. Bu alanlara index at�yorsunuz. Bize fayda sa�l�yor
-- .. Indexler database seviyesinde oluyor. Yani DB deki b�t�n s�tunlara index atal�m diyemiyoruz
-- NOT: Primary key ler ve foreign key ler de birer indextir asl�nda
-- Management studioda bir sorgu yazd�ktan sonra bu sorgu ne kadar s�r�yor bunun i�in bir yap� sunuyor
-- .. Bu bilgiye g�re tablo ya da sorgular�n�z� de�i�tirebilirsiniz

-- Burada 2 temel terim var. SCAN, SEEK
-- Scan : SQL server sorguya bak�p bu kriter hangi sat�rlarda var ona bak�yor. Yani Full scan yap�yor.
-- .. Bu yava� metodtur ama her zaman do�ru sonu� getirir
-- Seek : Indexleri koyduktan sonra dict mant���yla ilgili yeri bulur
-- .. Index seek : 1.Clustered 2.Non-clustered
-- a.Clustered Index: Belirli bir s�tun �zerinde olu�turmu� oldu�unuz cluster indexte SQL o sorgusunda
-- .. o alana nerede ise o alana(k�meye) gidiyor h�zl�ca buluyor. Her bir tabloda tek bir clustered index
-- .. olabiliyor. ��nk� s�ralama belli bir s�tuna g�re yap�ld�ysa, di�er s�tunlar o s�ralanan s�tuna g�re 
-- .. s�raya girece�i i�in tek bir clustered index oluyor. (B-tree mant���yla �al���r)

-- �rnek kod
-- CREATE CLUSTERED INDEX index_name ON schema_name.table_name (column_list);
-- Bunu �al��t�r�nca bir "VIEW" mant���yla DB de bir nesne olu�uyor

-- b.Non-Clustered Index: Bir tabloda clustered index olu�turdunuz. Sonra farkl� alanlara da index olu�turmak istiyorsunuz
-- .. Bunlar non-clustered indexler olacakt�r. Birden fazla tabloda non-clustered index olu�turulabiliyor ve 2 den fazla
-- .. s�tun �zerinde non-clustered index olu�turulabiliyor.(B-tree yap�s� burada da ge�erli)

-- ADVANTAGES AND DISADVANTAGES
-- ADVANTAGE    : 1.H�z, 2.s�ralama 3.Unique indexes guarantee
-- DISADVANTAGES: 1.INSERT, UPDATE and DELETE becomes slower, 2.Disk alan�nda yer kaplar

--�nce tablonun �at�s�n� olu�turuyoruz.
create table website_visitor 
(
visitor_id int,
ad varchar(50),
soyad varchar(50),
phone_number bigint,
city varchar(50)
);

-- veri insert edelim while d�ng�s�nde 1 den 200000 e kadar
DECLARE @i int = 1
DECLARE @RAND AS INT
WHILE @i<200000
BEGIN
	SET @RAND = RAND()*81
	INSERT website_visitor
		SELECT @i , 'visitor_name' + cast (@i as varchar(20)), 'visitor_surname' + cast (@i as varchar(20)),
		5326559632 + @i, 'city' + cast(@RAND as varchar(2))
	SET @i +=1
END;

-- Tabloyu kontrol edelim
SELECT top 10*
FROM
website_visitor

-- indexleri olu�turdunuz diyelim. Ama zaman i�inde tabloda de�i�iklikler oldu diyelim.
-- SQL server sorgular aras�nda y�nlendirme yapabilir. Y�nlendirme yapabilmesi i�in bu istatistikleri kullan�r
-- Biz bu istatistikleri kapat�p a�abiliyoruz. Biz bu istatistikleri a�al�m
--�statistikleri (Process ve time) a��yoruz, bunu a�mak zorunda de�ilsiniz sadece yap�lan i�lemlerin detay�n� g�rmek i�in a�t�k.
SET STATISTICS IO on
SET STATISTICS TIME on

-- basit bir sorgu yapal�m.
select * from website_visitor where visitor_id = 100 -- Burada 200000 sat�r� tarad�

-- MS-SQL server da sorgumuzu se�ip Execute �n sa��nda "V" i�areti var onunda sa��ndakine(execution plan) t�klayal�m
-- ��kt�da baz� �eyler geldi onlar�n �zerine mouse la geldi�imizde bilgiler g�r�n�yor
-- Select Coat: .. 
-- Table scan: Kullanm�� oldu�u y�ntem. Bu ekranda en �stte. (Cluster yap�nca buras� "Clustered Index seek" olacak)
-- .. "Estimated number of rows to be read-->199999",
-- .. "Estimated number of execution -- 1" 
-- .. vs vs
-- 2 sorguyu kar��la�t�rmak i�in bunu kullanabilirsiniz

-- Dersin 2. b�l�m�

-- Tabloda index olu�tural�m

Create CLUSTERED INDEX CLS_INX_1 ON website_visitor (visitor_id);
-- CLS_INX_1          : Index ad�. NOT: Index ad� DB i�inde unique olmal�
-- ON website_visitor : website_visitor tablosu �zerinde tan�mland�
-- (visitor_id)       : Hangi alana uygulanaca��
-- Object Explorer da -- > tables - dbo.website_visitor -- > Indexes -- > CLS_INX_1(Clustered) ... Olu�mu�

-- Indexi att�k art�k SQL server visitor ID lerin nerede oldu�unu biliyor. Art�k sorgu daha h�zl� gelecektir
select * from website_visitor where visitor_id = 100 -- Burada 200000 �n hepsini okumad�
-- sorguyu se�ip yine "execution plan" a t�klayal�m. ��kt�da "Clustered_Index seek" geldi
-- Not: E�er tablolar �ok b�y�kse mutlaka index atmam�z gerekiyor.

-- visitor_id de index var �u an tekrar bir index olu�turursak bu art�k clustered index olmayacak bu non-clustered index olacak
select ad from website_visitor where ad = 'visitor_name17'; -- 200000 sat�r� okudu yine
-- "execution plan"a bakal�m
-- Peki bu alana index nas�l ataca��z(Non-cluster)
CREATE NONCLUSTERED INDEX ix_NoN_CLS_1 ON website_visitor (ad);
-- "execution plan"a bakal�m. Index seek. Art�k en alttaki "leaf" leri okumak zrounda de�il(B-tree de)
-- .. index i�erisindeki ismi bulmaya �al���yor. Sonra sonucu getiriyor.

 --------------------------------------
-- �sim ve soyisme beraber index atal�m.(Ayn� isim soyisme ait ba�ka bir ki�i olmad��� i�in)
Create unique NONCLUSTERED INDEX ix_NoN_CLS_2 ON website_visitor (ad) include (soyad)
-- Art�k isim ve soyisme beraber g�nderilen planda ne olacak bakal�m 
select ad, soyad from website_visitor where ad = 'visitor_name17';
-- "execution plan" a g�re indexe g�re arama yapt�. Extra isim soyisim �zerinde arama yapmad�

--------------------------------------
-- clustered index (visitor_id)
-- non-clustered index (ad)
-- non-clustered index (ad) include (soyad)
-- �sttekileri yapt�k. Peki sadece soyad� �zerinden sorgu yapsayd�
select ad, soyad from website_visitor where soyad = 'visitor_name17'; -- ��kt� yok ama execution plana bakmak i�in b�yle yazd�k
-- execution plan "Index scan" yani tablonun hepsini kontrol ediyor Yani "index seek" yapmad�


-- Dersin 3. b�l�m�

-- Python �zerinden SQL server a ba�lanma
-- ipynb. dosyas� �zerinde notlar var
