#3.Bölüm
#1.video
# TEMEL SQL komutlarını 2 şekilde değerlendirebiliriz.
"""
1.Data Manüpülasyonu: yani datayı çeken ya da datayı değiştiren.
     Select : Veritabanından kayıtları çeker
     Update : Bir tablodaki kaydın bir ya da daha fazla alanını günceller
     ........(girilmiş doğum tarihi yerine başka bir şey girmek)
     Delete : Bir tablodan kayıt siler(Bir şarta göre tablonun tamamınıda 
     .......silebilirsiniz ya da bir satır veya birkaç satırda silebilirsiniz)
     Insert into : Tabloya yeni kayıt ekler.
     Truncate table : Tablonun içini komple boşaltır.

2.Veritabanı Manüpülasyon: Veritabanı objelerini değiştirmeye silmeye ya da 
     ....eklemeye yarar.
     Create Database : Sistem üzerinde yeni veritabanı oluştur.
     Alter Database : Bir veritabanının özelliklerini değiştir.
     Create Table : Yeni bir tablo oluştur.
     Alter Table : Bir tablonun özelliklerini değiştirir.
     Drop Table : Bir tabloyu tamamen siler.
     Create Index : İndex oluşturur.
     Drop Index : Index'i siler.
"""
# Uygulama yaparken detaylı öğreneceğiz.
#%%2. Video - SELECT
# Şimdi Select komutumuzu tablomuzda deneyelim.
# ETRADE diye database oluşturmuştuk. Üzerine sağ tıkla - new query yap.
# Oraya komutları yazmaya başlayalım.
"""
SELECT
COLUMN1
FROM
CUSTOMER # Tablonun adı
"""
# Sol üstte seçili olan veritabanım "ETRADE", eğer başka bir veritabanı seçili
#... olsaydı şöyle yapacaktık.
"""
SELECT
COLUMN1
FROM
ETRADE.DBO.CUSTOMER # Tablonun adı
"""
# .. şeklinde yapmalıydım.
# Şimdi colonlarda neler vardır aslında, bi yazalım.

"""
SELECT
ID,CUSTOMERNAME,CITY,BIRTHDATE,DISTRICT,GENDER
FROM
CUSTOMER
"""
# Çalıştırmak için üstte sol da "Execute" a basıyorum.ya da CTRL+E(önceden f5 di)
# Peki çok daha uzun kolon sayısı olan tablolarda ne yapacağım?
# Sol altta veritabanının içinde "dbo.CUSTOMER" ın altındaki "columns" a
# ... basılı tut ve SELECT in altına sürüklersen alttaki gelecek.
"""
SELECT
[ID], [CUSTOMERNAME], [CITY], [DISTRICT], [BIRTDAY], [GENDER]
FROM
CUSTOMER
"""
# Peki köşeli parantezin farkı ne ?, 
# Eğer benim columlarımda,boşluk ya da türkçe karakter olursa hatayı önlemek 
# .. adına köşeli parantez koyuyor, pythondaki "Type 1" yazılması gibi.

# Sadece belli columları getirmek isteseydim.
"""
SELECT
[ID], [CUSTOMERNAME]
FROM
CUSTOMER
"""
# .. şeklinde yapabilirdim.

#%%3.video - INSERT
# formül
"""
INSERT INTO tablo adı
(KOLON1,KOLON2,KOLON3,...)
VALUES
(DEĞER1,DEĞER2,DEĞER3,...)
"""
# CUSTOMER tablomuza 5. kaydı eklemek istersek, sağ tıklayıp edit yapıyorduk vs.
# Diğer yol neydi.

"""
INSERT INTO
CUSTOMER
(CUSTOMERNAME,CITY,DISTRICT,BIRTHDATE,GENDER)
VALUES
('BURCU CANDAN','KOCAELİ','MERKEZ','1994-05-08','F')
"""
# Not: stringleri yazarken tek tırnak kullanıyoruz.
# Sonra alttakini yazıp kontrol edelim gerçekten ekledimi diye
"""
SELECT
[ID], [CUSTOMERNAME], [CITY], [DISTRICT], [BIRTDAY], [GENDER]
FROM
CUSTOMER
"""
# Şimdi bizim bi tane Excel dosyamız var, burada 1000 tane kayıt var.
# Bunu şimdi INSERT ile nasıl veritabanına aktarabilirim bakalım.
# Not: Normalde 1 den fazla yolu var.
### 1. yol exceldeki belli satırları kopyalarım.veritabanındaki CUSTOMER ın içine yapıştırırım.
# Ben CUSTOMER A SAĞ tıkladım ve edit dedim.
# Ancak; Oradaki sütun sayım veritabanı ile aynı olmalı. Burada değil mesela
# Yani "ID" sütunum fazla, bundan kurtulmam gerek.
# Sağ üstte bi "SQL" işareti çıkıyor ona tıklıyorum.
# Açılan yerde "TOP(200) ID" yi siliyorum. sağ tıklayıp "Execute SQL" diyorum.
# Şimdi colon sayım 5 e düştü. 
# Sonra aşağıdaki boş satırın solundaki * işaretine sağ tıklayıp "paste" diyorum 
# Yani excelden yapıştırıyorum.
# Sonra select ile "ID" sütunu dahil çağırdığımızda eklediğimiz kayıtları göreceğiz

### 2.yol kendi insert cümlelerimizi yazacağız.
# Elimizde excel var.
# Bizim insert cümlemiz neydi;
"""
INSERT INTO CUSTOMER ([CUSTOMERNAME],[CITY],[DISTRICT], [BIRTHDATE],[GENDER]) VALUES ('BURCU CANDAN','KOCAELİ','MERKEZ','1994-05-08','F')
"""
# ... şeklindeydi. Bunu kopyalayalım şimdi.
# Exceldeki 6. kolon(Boş kolon) ve ilk müşterinin başladığı kutucuk olan F2 ye
# ...önce (eşittir)= yazıp sonra ünlem yapıp arasına yapıştırıyoruz. Sonra;
# Formülü uyguluyoruz, Bahar Candan yazan yeri değiştirip A2 kolonunu koyuyoruz.
# ... ve bi tek tırnak bi çift tırnak içine alıp & & yazıp arasına kutucuk
# ... ismini koyuyoruz.
# NOT: Tek tırnak SQL in komut düzeninden, çift tırnak Excel in komutlarından geliyor.
"""
="INSERT INTO CUSTOMER ([CUSTOMERNAME],[CITY],[DISTRICT], [BIRTHDATE],[GENDER]) VALUES ('"&A2&"','"&B2&"','"&C2&"','"&D2&"','"&E2&"')"
""" 
# Bunu sonra tüm column lara yazacağız(Aşağı çekerek doldur diyoruz)
# Sonra o yazdığımız F kolonunun tamamını kopyalayıp SQL e geri dönüyoruz.
# Üstte New Query diyor. Ona tıklıyoruz. ve oraya yapıştırıp kontrol ediyoruz oldu mu diye.
# SQL de SELECT komutunun olduğu sekmeye(Query ye) gelelim. Tablomuzun içini bi boşaltalım önce.
# "Truncate table" metodunu kullanıyorduk bunun için.
"""
SELECT
[ID], [CUSTOMERNAME], [CITY], [DISTRICT], [BIRTDAY], [GENDER]
FROM
CUSTOMER

TRUNCATE TABLE CUSTOMER
"""
# Run edince içi boşaldı.
# Sonra 1000 taneyi kopyaladığımız sayfayı run et. 
# Sonra geri select in olduğu yere gel ve gerçekten 1000 tane kaydı attı mı bakalım?
"""
SELECT
[ID], [CUSTOMERNAME], [CITY], [DISTRICT], [BIRTDAY], [GENDER]
FROM
CUSTOMER
"""
# Evet 1000 kaydı içine atmış.
# Şimdi artık bu tablo üzerinde çalışmalar yapabiliriz.

#%% 4. video - UPDATE
# Veritabanı tablolarında 1 veya birden fazla alanı değiştirmek isteiğimizde
# ... kullanırız. Formülü ;
"""
UPDATE TABLOADI
SET COLUMN1=VALUE1,COLUMN2=VALUE2
"""
# Update komutu için güncelleyeceğimiz bi alana ihtiyacımız var.
# Customer tablosuna sağ tıklayıp "Design" diyorum ve yeni bir alan ekliyorum.
# Alta birde yaş alanı eklemek istiyorum "AGE" yazdım integer dedim. 
# ... Çarpıya bas. Yes diyelim. Kaydetmiş olduk.
# AGE alanı NULL(Nal)=içinde bir veri yok demek) görünüyor. 
# Birthdate den hesaplayıp Age i yazsın istiyorum ben.
"""

UPDATE CUSTOMER
SET AGE=DATEDIFF(YEAR,BIRTHDAY,GETDATE())
"""
# Kontrol edelim.
"""
SELECT * FROM CUSTOMER
"""
# Burada * tüm sütunlar demek.
# Burada Datediff SQL in bir fonksiyonu içine de 3 şey aldı.
# Yıl hesabı istediğim için YEAR dedim.
# Başlangıç tarihi:(BU tablodaki) BIRTHDAY
# Bitiş tarihi :(Şimdiki tarih) GETDATE

# Mesela yaşı 1 arttıralım.

"""
SELECT * FROM CUSTOMER

UPDATE CUSTOMER
SET AGE=DATEDIFF(YEAR,BIRTDAY,GETDATE())

UPDATE CUSTOMER SET AGE=AGE+1
"""
# Yaşlar 1 arttı.
# Bunları şu an temel anlamlarda görüyoruz. Daha sonra farklı uygulamalar yapacağız.

#NOT: Bir query de execute yaparsak sırayla komutları çalıştırır.
# ... Eğer sorgunun bir bölümünü seçersek sadece onu çalıştırır.

#%% 5.Video - DELETE
# formül
"""
DELETE FROM TABLOADI
"""
# Tablodaki tüm kayıtları silecektir.
# Önce bizim listemiz gitmesin diye bir kopyasını alalım.
"""
SELECT * FROM CUSTOMER

SELECT * INTO CUSTOMERYEDEK FROM CUSTOMER
"""
# Customer içindeki dataları al ve customeryedek in içine alt
# CUSTOMERYEDEK i otomatik olarak oluşturdu.
# Şimdi bu kayıtları silmek istiyorum.

"""
SELECT * FROM CUSTOMERYEDEK
DELETE FROM CUSTOMERYEDEK
"""
# Tabloyu komple uçurduk.

# Eğer tabloyu sildiğimizde yeni kayıt eklemek istersek ID 1001 den başlayacak.
# Tablonun içini silmiş olsamda Id kaldığı yerden devam eder.
# NOT: Gerçekte bu kayıtları silmiyor aslında(Kurtarma yöntemleri var)
# Peki 1001 den başlamasında normal 1 den başlasınd istersek
# "TRUNCATE TABLE" komutunu kullanmamız gerekir.

"""
TRUNCATE TABLE CUSTOMERYEDEK
"""
# Sonra bi kayıt ekleme yapalım.

"""
SELECT * FROM CUSTOMERYEDEK
"""
# Gördüğümüz gibi 1 den başladı.
# İlerde daha detaylı silme işlemleri yapacağız.

#%%6. Video - WHERE
# formül
"""
SELECT * FROM TABLOADI
WHERE COLUMN1 = VALUE1
"""
# WHERE KOMUTU bir şart komutudur. Yani mesela ismi Ömer olanları çekmek istersem,
# Bu komutu kullanırım. Ya da yaşı 20 den büyük olan müşterileri çekebilirim.
# Birden fazla da şart koyabilir. Yaşı 20 den büyük ve istanbulda yaşayan.
# Sadece select in için geçerli değil update ve delete ile birliktede kullanabiliriz.
# İçerisine nasıl parametreler alır.
"""
 = , <>(eşit değildir) , > , < , >= , <=, 
BETWEEN(Arasındadır)(Doğum tarihi şu tarihler arasında olanları getir)
LIKE(ile başlar-ile biter)(İsmi Ömerle başlayanları getir)
IN(Içinde)(İstanbul-Ankara-İzmir de yaşayanları getir)
"""
# Başlayalım.
# Ben mesela 7. sıradaki Salih Faydalıyı çekmek istiyorum.
"""
SELECT * FROM CUSTOMER 
WHERE CUSTOMERNAME = 'Salih FAYDALI'
"""
# Sadece onu getirdi. string olduğu için tek tırnakda yazdık.

"""
SELECT * FROM CUSTOMER 
WHERE ID=18
"""
# Aykut suyur u getirdi.

"""
SELECT * FROM CUSTOMER 
WHERE CITY = 'Istanbul'
"""
# Istanbuldan 36 kişi varmış

"""
SELECT * FROM CUSTOMER 
WHERE BIRTHDAY ='1991-08-07'
"""
# Yaşar Savurgan Ispartayı getirdi.

# NOT: Date ile ilgili biz ingilizceye göre tarih yazıyoruz.
# Sıkıntı yaşamamak için;
# Sol da,   Security - Logins- (En alttaki hoca da bizde değil) sağ tıkla ona
# ...properties diyince default dili english  yapın ve tarihi ,
# .. ingilizcedeki tarih yazım şekline göre yazınca sorun yaşamayın.
# O yüzden tarihi arada - olmadan kullanabilirsin.
"""
SELECT * FROM CUSTOMER 
WHERE BIRTDAY = "19971024"
"""
# şeklinde yazınca Volkan Çekip gelecektir. Devam edelim.

"""
SELECT * FROM CUSTOMER 
WHERE CITY = 'Rize' AND DISTRICT ="Pazar / Rize"
"""
# Burada and komutunuda kullandık. Bi de eşit değildir kullanırsak

"""
SELECT * FROM CUSTOMER 
WHERE CITY = 'Rize' AND DISTRICT <>'Pazar / Rize'
"""
# Rize den olan ama Pazar/Rize den olmayanlar geldi. Devam edelim.

"""
SELECT * FROM CUSTOMER 
WHERE AGE>77
"""
"""
SELECT * FROM CUSTOMER 
WHERE AGE <=20
"""

# Doğum tarihi 1998 den büyük olanlara bakalım.

"""
SELECT * FROM CUSTOMER 
WHERE BIRTDAY >= '19980101'
"""

# Between e bakalım.

"""
SELECT * FROM CUSTOMER 
WHERE AGE BETWEEN 19 AND 20
"""
# Burada 19 ve 20 dahil 
# Örneğin 1998 doğumluları getirelim.

"""
SELECT * FROM CUSTOMER 
WHERE BIRTDAY BETWEEN '19980101' AND '19981231'
"""

# Like a bakalım. Genelde string ifadelerde kullanırız.

"""
SELECT * FROM CUSTOMER 
WHERE CUSTOMERNAME LIKE 'Rümeysa İNCEDAL'
"""
# dediğim zaman = operatörü gibi çalıştı.

"""
SELECT * FROM CUSTOMER 
WHERE CUSTOMERNAME LIKE 'Rümeysa'
"""
# ... dersem hiç bir şey getirmez. Çünkü ismi "Rümeysa" olan yok.
# Yani ad ve soyad birlikte yazıldığı için ancak birlikte yazarsam gelir.
# Peki ismi Rümeysa ile başlayanlar?

"""
SELECT * FROM CUSTOMER 
WHERE CUSTOMERNAME LIKE 'Rümeysa%'
"""
# 2 tane Rümeysa varmış.
# isminin içinde "ince" geçenlere bakalım.

"""
SELECT * FROM CUSTOMER 
WHERE CUSTOMERNAME LIKE "%İNCE%"
"""
# Bana 4 tane kayıt getirdi.
# Soyadında veya adında örnek geçenlere bakalım.
# Yani başlangıcı benim için önemli değil sonu ÖRNEK ile bitenler.

"""
SELECT * FROM CUSTOMER 
WHERE CUSTOMERNAME LIKE "%ÖRNEK"
"""

# NOT: % INCE % dediğim zaman içinde geçen demek
# .... %ORNEK diyince ... ile biter anlamında.(ÖRNEK le biter.)
# .... NAZLı% diyince .. ile başlar...
# Müşteri arama , ürün arama vs de bu like kullanılır.

# Bir de IN operatörüne bakalım.

"""
SELECT * FROM CUSTOMER 
WHERE CITY = 'Isparta' 
AND DISTRICT IN ('ULUBORLU','YALVAÇ')
"""
# Ispartanın içinde uluborlu ve yalvaçta olanları getir.
# Bir de şunu diyebilirim mesela. Uluborlu ve yalvaç dışında olanları getir.

"""
SELECT * FROM CUSTOMER 
WHERE CITY = 'Isparta' 
AND DISTRICT NOT IN ('ULUBORLU','YALVAÇ')
"""
# Buradada "NOT" komutunu kullanıyorum
# Buradan da cinsiyeti kadın olanlara bakalım.

"""
SELECT * FROM CUSTOMER 
WHERE CITY = 'Isparta' 
AND DISTRICT NOT IN ('ULUBORLU','YALVAÇ')
AND GENDER = 'K'
"""

# Böylelikle WHERE şartını görmüş olduk.
# Şuna bakalım birde DELETE ile tablonun tamamını uçurmuştuk.
# WHERE şartıyla sadece 1 tanesini uçurabiliriz.
# Örneğin Volkan Çekip i silmek istiyorum. ID si 1
"""
DELETE FROM CUSTOMER 
WHERE ID = 1
"""
# Çalıştırdığımızda Volkan Çekip gitti :D. direk 2 den başladı.
# Ismi Serhat olan herkesi sil.

"""
DELETE FROM CUSTOMER
WHERE CUSTOMERNAME LIKE 'Volkan%'
"""

# 3 tane satırın gittiğini görüyoruz.

# UPDATE içinde WHERE kullanabiliriz.
# GENDER ı E VE K şeklinde değil de, Erkek ve Kadın şeklinde tutalım.
# Önce Gender ın karakter uzunluğunu 10 falan yapmam lazım.
# Ama hata verecek. Düzeltmek için; 
"""
Yukardan Tools-Options-Designer==> Prevent saving changes i kapatıyoruz.
"""
# Şimdi 10 yapabiliriz.

"""
UPDATE CUSTOMER SET GENDER ='ERKEK'
WHERE GENDER='E'
"""
# Sonra K ları da update edelim.
"""
UPDATE CUSTOMER SET GENDER ='KADIN'
WHERE GENDER='K'
"""
# NOT:Selectteki küçük eşit büyük eşit değil vs yi
# ... update de delete de falanda kullanabiliriz.

#%%7.VİDEO - AND ve OR

# İsmi Ömer olanların içerisinde İstanbulda yaşayanlar 30 kişi gelecek(Mesela)
# AND komutu matematikteki önermelerdeki gibi çalışır
# OR aynı şekilde

# İsmi Ömer ya da şehri = istanbul . Kesişimini alacak.
# Uygulama yapalım.

"""
select * from CUSTOMER where CITY='İstanbul'
select * from CUSTOMER where CUSTOMERNAME LIKE 'Hüseyin%'
"""
# Biri Burdur da biri İstanbulda çıktı.
# Bi de AND ile yapalım(Kesişim)
"""
select * from CUSTOMER where CITY='İstanbul'
and CUSTOMERNAME LIKE 'Hüseyin%'
"""
# Sadece 1 kayıt getirdi.
# Bi de OR ile yapalım(Birleşim)

"""
select * from CUSTOMER where CITY='İstanbul'
OR CUSTOMERNAME LIKE 'Hüseyin%'
"""
# İstanbulda olanlar 36 tane idi. bi de burdur dan var toplam 37 tane

#%%8.VİDEO - DISTINCT

# SELECT ile kullanırız. Tekrar eden satırlar için, tek satırda sonuç döndürür.
# Tablonun içinde Ömer için 1 milyon tane satır varsa select distinct CUSTOMERNAME
# ... dediğim zaman Ömer için sadece 1 tane sonuç getirecektir. Uygulamayı altta
# Yani kaç farklı isim varsa onu gösteriyor. (3 ömer 5 mehmet 3 ahmet ise, çıktıda;
# ... ömer , mehmet ve ahmet görünüyor.
# FORMÜL;
"""
SELECT DISTINCT COLUMN1, COLUMN2
FROM TABLOADI"""

# Örnek
# CITY alanına göre kaç çeşit şehir var görmek istiyorum
"""
select CITY from CUSTOMER
"""
# .. dersem 998 sonuç gelecek ama şöyle dersem;

"""
select distinct CITY from CUSTOMER
"""
# .. 81 farklı şehir varmış onu gördüm.

"""
select CITY from CUSTOMER WHERE CITY='İstanbul'
"""

# Şehri İstanbul olan 36 tane yer geldi.

"""
select distinct CITY from CUSTOMER WHERE CITY='İstanbul'
"""
# 1 sonuç geldi. Çünkü where şartında İstanbul zaten 1 tane

"""
select distinct CITY,DISTRICT from CUSTOMER WHERE CITY='İstanbul'
"""

# 22 tane de ilçe geldi. (36 satırdan 22 si geldi çümkü tekrar eden ilçeler varmış)

#%%9.VIDEO - ORDER BY (SIRALAMA KOMUTU)

# Bir tablodan Select ile çektiğim dataları, hangi sırada görmek istiyorsam,
# ... o amaçla order by komutunu kullanırım. 
# Formül;

"""
SELECT COLUMN1 , COLUMN2
FROM TABLOADI
ORDER BY COLUMN1 ASC, COLUMN2 DESC
"""
# ASC= Ascending(Küçükten büyüğe ya da a dan z ye sıralama), 
# DESC = Descending(Büyükten küçüğe ya da z den a ya sıralama)
# Yani yukardaki formülde Column1 e göre a dan z ye, 
# .. column2 ye göre de z den a ya göre sıralayacağım.
# Örnek
"""
select * from CUSTOMER
"""
# Bunu çalıştırdığımızda ID alanına göre default sıralama geliyor.
# Eğer müşteri adına göre sıralattırmak isteseydik;

"""
select * from CUSTOMER
ORDER BY CUSTOMERNAME
"""
# A dan Z ye bir sıralama oldu

"""
select * from CUSTOMER
ORDER BY CITY,CUSTOMERNAME
"""

# Burada önce city ye göre sıralıyor. Sonra city içinde isimleri sıralıyor.
# Tersten yazdırsaydık.

"""
select * from CUSTOMER
ORDER BY CITY (ASC),CUSTOMERNAME DESC
"""

# Adanalılar sıralı(Çünkü default olarak ASC var orada, yazmasakta olur), 
# ...İsimler tersten sıralı.
# Şöyle diyelim

"""
select * from CUSTOMER
ORDER BY CITY DESC ,CUSTOMERNAME (ASC)
"""
# Şuna bakalım bir de 
"""
select * from CUSTOMER
ORDER BY CITY DESC ,BIRTHDAY (ASC)
"""

# ORDER BY ın bir kullanım şekli bu, diğer bir kullanım şekli;

"""
select * from CUSTOMER
ORDER BY 3
"""
# 3. üncü sütun(CITY) ye göre sırala

"""
select * from CUSTOMER
ORDER BY 6,3
"""
# ORDER BY SQL de çok sık kullanılır

#%%10.Video- Top komutu
# Top komutu bir data sette belli bir sayı kadar veya dönen datanın belli bir
# ... yüzdesi kadar kayıt döndürmemizi sağlar.

# SQL serverda yani(MSSQL de) TOP diye kullanılırken
# MYSQL de ; LIMIT
# ORACLE da ; ROWNUM
# ... olarak kullanılır.
# Formül;

"""
SELECT TOP N COLUMN1,COLUMN2
FROM TABLOADI
ORDER BY COLUMN1 ASC, COLUMN2 DESC
"""
# N = 5 , 10 YA DA 100 OLABİLİR.
# ORDER BY KULLANMAYADABİLİRİZ.

#ÖRNEK

"""
SELECT TOP 5 * FROM CUSTOMER
"""

"""
SELECT TOP 5 * FROM CUSTOMER
ORDER BY CUSTOMERNAME
"""
# Müşteri adına göre ilk 5 satırı döndürdü.

"""
SELECT TOP 5 * FROM CUSTOMER
WHERE CITY='İstanbul'
ORDER BY CUSTOMERNAME
"""
# İstanbul şartına göre döndürdük.
# TOP ın başka bir kullanımı

"""
SELECT TOP 10 PERCENT * FROM CUSTOMER
WHERE CITY='İstanbul'
ORDER BY CUSTOMERNAME
"""

# Toplam kayıt sayısının yüzde 10 u

#%%11.VİDEO- DERS sonu
# Şunları bilmemiz gerekiyor
# Temel anlamda SQL konutları nelerdir.
# Data Manipülasyonu ve Veritabanı Manipülasyon komutları ne demektir?
# ... Ne işe yarar?
# TRUNCATE ile DELETE arasında ne fark vardır?
# SELECT, INSERT, UPDATE, DELETE komutları ne işe yarar ve nasıl kullanılır.
# WHERE şartı ile sorgu nasıl filtrelenir?
# =,>,<,<>,LIKE,BETWEEN komutları nasıl kullanılır?
# WHERE şartında AND ve OR kullanımı?
# DISTINCT komutu ne işe yarar? Nasıl kullanılır?
# TOP komutu ne işe yarar? Nasıl kullanılır?
















