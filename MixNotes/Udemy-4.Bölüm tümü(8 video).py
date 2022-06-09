# 4. Bölüm
# 1. Video
# Öğrendiklerimizi gerçek bir data üzerinde uygulamalar gerçekleştirelim.

# Dosyayı indirelim önce ETRADE.BAK
# Sonra SQL e gelip ETRADE database imizi silelim.(Silerken "close existing connections" 
# ... a tıklayarak silelim).Çünkü veritabanına yapmış olduğumuz bağlantılar var.

# SQL de Database e sağ tıkla Restore database diyelim.
# Gelen ekranda- Device- ...(üç nokta) - Add - 
# ...(Yukarda dosyanın kayıtlı adresini seç) - Dosyayı seç - Okay - (tekrar) Okay
# NOT:ETRADE.BAK ın kayıtlı olduğu adres(C:\Program Files\Microsoft SQL Server\MSSQL14.MSSQLSERVER\MSSQL\Backup)
# ... Bakın burada bu dosyayı gördü(Alt tarafı gösteriyor.)
# Okay dediğim zaman database bir backup dosyasına restore edildi.

# Bu database deki - SALEs tablosunda;
# 81 il genelinde şubesi olan bir marketler zincirinin satışlarının yapıldığı tablo
# Drive dan "Alan Listesi" excel dosyasını indirirsen. Bu sütunların ne anlama geldiğini
# ... görebiliriz.

#%%2. video - Aggregate functions(SUM,COUNT,MIN,MAX,AVG)

# Bu komutlar tablolardan distinct komutunda olduğu gibi max min vs gibi değerlere
# ...bakmamızı sağlar.(tablomda "PRICE" isimli o ürünü kaça sattığımla ilgili alan var)
# SUM(PRICE) : Toplam satış fiyatlarımı getirebilirim.
# COUNT(ID) : Satır sayısını getiririm
# MIN(PRICE)/MAX(PRICE): En ucuz/pahalı hangi fiyAttan satmışım
# AVG(PRICE): Ort olarak hangi fiyattan satmışım.

# Formül
"""
select 
SUM(PRICE),COUNT(ID),MIN(PRICE),MAX(PRICE),AVG(PRICE)
from TABLOADI
"""

# Bunun için biraz daha büyük bir tabloda çalışma yapacağız(SALES)(611.00 satır)

# Burada şubelerin toplam satışlarını getirmek istiyorum
# Mesela Kocaeli
"""
select * from SALES WHERE BRANCH = 'Kocaeli Subesi'
"""
# Tüm Kocaeli şubesinin verileri görünüyor. Şimdi toplam satışa bakalım.
"""
select sum(LINENET) from SALES WHERE BRANCH = 'Kocaeli Subesi'
"""
# Kocaeli şubesini kaldıralım tamamı için neymiş satışım?

"""
select sum(LINENET) from SALES
"""

# Kocaeli şubesinde kaç tane satılmış bakalım.

"""
select sum(LINENET), count(*) from SALES WHERE BRANCH = 'Kocaeli Subesi'
"""
# 14292 geldi. Bunu test edelim gerçekten öyle mi diye.

"""
select * from SALES WHERE BRANCH = 'Kocaeli Subesi'
"""
# sağ altta rows: 14292 yazıyor.

"""
select sum(LINENET), count(*), MIN(LINENET), MAX(LINENET) from SALES WHERE BRANCH = 'Kocaeli Subesi'
"""
# tek seferde minimum sattığım miktar 0.01 , tek seferde max satığım miktar 162,22

# Şimdi aşağıda rakamların üstünde (No column name yazıyor)
# Oralara birşey yazmamız için AS kullanıyoruz yanına

"""
select sum(LINENET) AS TOPLAMSATIS,
count(*) AS SATIRSAYISI,
MIN(LINENET) ENDUSUKFIYAT,
MAX(LINENET) ENYUKSEKFIYAT,
AVG(LINENET) AS ORTALAMASATISFIYATI
from SALES
WHERE BRANCH = 'Kocaeli Subesi'
"""
# Şimdilik bu kadarını bilmemiz yeterli. İlerde daha detaylı uygulamalar yapacağız.

#%%3.Video- Group By Kullanımı 1

# Ben 81 ile göre gruplandırıp satışlarını ,min, max vs görmek istiyorum.

"""
select BRANCH,
sum(LINENET) AS TOPLAMSATIS,
count(*) AS SATIRSAYISI,
MIN(LINENET) ENDUSUKFIYAT,
MAX(LINENET) ENYUKSEKFIYAT,
AVG(LINENET) AS ORTALAMASATISFIYATI
from SALES
WHERE BRANCH = 'Kocaeli Subesi'
"""
# Dersem hata verir(Bu aggregate function değil ya GROUP BY cümlesi değil)
# O yüzden en sona GROUP BU yazıyorum.

"""
select BRANCH,
sum(LINENET) AS TOPLAMSATIS,
count(*) AS SATIRSAYISI,
MIN(LINENET) ENDUSUKFIYAT,
MAX(LINENET) ENYUKSEKFIYAT,
AVG(LINENET) AS ORTALAMASATISFIYATI
from SALES
WHERE BRANCH = 'Kocaeli Subesi'
GROUP BY BRANCH
"""
# Sadece kocaeli geldi, eğer where şartını kaldırırsam 81 şehri görürüm.
# ya da comment e alırım. NOT : SQL de yorum satırı için en başa -- yaz

"""
select BRANCH,
sum(LINENET) AS TOPLAMSATIS,
count(*) AS SATIRSAYISI,
MIN(LINENET) ENDUSUKFIYAT,
MAX(LINENET) ENYUKSEKFIYAT,
AVG(LINENET) AS ORTALAMASATISFIYATI
from SALES
--WHERE BRANCH = 'Kocaeli Subesi'
GROUP BY BRANCH
"""

# SORU: en çok satış yapan şubelerimiz satış tutarına göre sıralayarak getir.

"""
select BRANCH AS SUBEADI, SUM(LINENET) AS TOPLAMSATIS
from SALES
GROUP BY BRANCH
ORDER BY SUM(LINENET) DESC
"""

# Peki şu soruyu sorsaydık. En çok satış yapan 10 şubeyi göster

"""
select TOP 10 BRANCH AS SUBEADI, SUM(LINENET) AS TOPLAMSATIS
from SALES
GROUP BY BRANCH
ORDER BY SUM(LINENET) DESC
"""

# Toplam satışı 50000 den büyük olan mağazaları getirelim.
# ÖNEMLİ NOT: Şimdi burada yapılan bir hatadan da bahsedelim(Aşağıdaki kod hata verir.)
"""
select BRANCH, SUM(LINENET) AS TOPLAMSATIS
from SALES
WHERE SUM(LINENET)>50000
GROUP BY BRANCH
"""
# Hata. Çünkü. GROUP BY yaptığımız şey de HAVING kullanmalıyız(KURAL!)
#.. ve bunu GROUP BY dan sonra kullanmalıyız.

"""
select BRANCH, SUM(LINENET) AS TOPLAMSATIS
from SALES
GROUP BY BRANCH
HAVING SUM(LINENET)>50000
(ORDER BY 2 DESC)
"""

#%% 4. VİDEO- GROUP BY KULLANIMI 2

# Seçtiğimiz herhangi bir mağazanın o gün içerisindeki toplam yaptığı satış

"""
select * from sales where BRANCH = 'BURSA SUBESİ' AND DATE_ = '2017-01-05'
""" 

# Bu datayı excel de incelemek istersek: altta çıktıda rakamla 1 yazan yerin üstünde
# ... bi boşluk var. oraya tıkla hepsini seçiyor.
# dataya sağ tıkla "copy with headers" diyelim.
# Bi excel açıp yapıştırıyorum.

# Excel de ÖZET TABLO(PİVOT TABLE) diye bir kavram var.(HOCA: Bizim group by ın aynısı aslında)
# Ekle - Pivot table- PivotTable tıkla. Gelen yerde tamam diyelim.
# Sağdaki "DATE" i tutup - sağ altta "Satır Etiketleri(sütunlar)" alanına sürüklüyorum.
# Bu ne demek?. Sol tarafta DATE(Tarihler) gelsin şeklinde işaretliyorum.
# Eğer tarih şeklinde format gelmezse .Bunun formatını düzeltelim. 
# sağ altta DATE E tıkla - alan ayarları - sayı biçimleri(bizim bilg. daki excelde çıkmıyor)
# -tarih - Türden bi şekil seç (2017-05-15) formatında
# ...
# Yan tarafada toplam satışı getirmek istiyorum.
# ...Sağdaki LINENET i de alttaki Değerler yerine sürükle. 
# Bi tanede COUNT aldıralım(say diyelim) --> LOGICALREF i 
# ... Değerler e sürükle sonra LOGICALREF deki ok a tıkla
# ... - değer ayarları - SAY a bas.
# BRANCH i de satır etiketlerine(sütunlara) at. Bu şekilde incele.
# Bizim SQL de yapmaya çalıştığımız şey tam da bu aslında.
# Şimdi Exceldeki görüntü gibi bir görüntü elde edelim.
# Sol tarafa BRANCH ve DATE i getirmeliyim. Sağ tarafa diğerleri

"""
select BRANCH AS SUBE, DATE_ AS TARIH, SUM(LINENET) TOPLAMSATIS
FROM SALES WHERE BRANCH='BURSA SUBESİ' AND DATE_ = '2017-01-05'
"""
# HATA VERİYOR. SALES bi aggregate function ın içinde geçmiyor(sum, avg gibi)
# Group by yapacağız.

"""
select BRANCH (AS) SUBE, DATE_ (AS) TARIH, SUM(LINENET) TOPLAMSATIS
FROM SALES WHERE BRANCH='BURSA SUBESİ' AND DATE_ = '2017-01-05'
GROUP BY BRANCH, DATE_
"""
# Bu seferde Date i group by a koyman gerekiyor diyor.

"""
select BRANCH SUBE, DATE_ TARIH, SUM(LINENET) TOPLAMSATIS,
FROM SALES WHERE BRANCH='BURSA SUBESİ' AND DATE_ = '2017-01-05'
GROUP BY BRANCH,DATE_
"""
# 703.85 i getirdik. HATTA SATIR SAYISINI DA GETİRELİM.

"""
select BRANCH SUBE, DATE_ TARIH, SUM(LINENET) TOPLAMSATIS, COUNT(*) SATIRSAYISI
FROM SALES WHERE BRANCH='BURSA SUBESİ' -- AND DATE_ = '2017-01-05'
GROUP BY BRANCH,DATE_
ORDER BY DATE_
"""

# Bursanın tüm tarihlere göre satışları
# Exceldeki ilk satır oluştu.
# tarih filtresini kaldırıp tek bir gün yerine tüm tarihlere bakalım sırayla.

"""
select BRANCH SUBE, DATE_ TARIH, SUM(LINENET) TOPLAMSATIS, COUNT(*) SATIRSAYISI
FROM SALES WHERE BRANCH='BURSA SUBESİ' AND DATE_ = '2017-01-05'
GROUP BY BRANCH,DATE_
"""

#%% 5. Video - GROUP BY KULLANIMI 3
# Bizim sorumuz neydi önceden? Bir mağazanın gün bazlı satış rakamları
# Bunun tersini düşünelim bir de
# Bir günün mağaza bazlı satış rakamları.

"""
select DATE_,BRANCH, SUM(LINENET) FROM SALES
WHERE DATE_ = '20170105'
GROUP BY DATE_,BRANCH
ORDER BY SUM(LINENET) DESC
"""

# YANİ group by da çarpraz gruplamalar yapabiliriz.
#%% 6. video - GROUP BY KULLANIMI 4

# GROUP by örnekleriyle devam ediyoruz. Çünkü bu SQL programlama için çok önemli
# Özellikle Büyük verilerde. Bizden istenilen sonuçları sorgu diline çevirip,
# ... istenilen şekilde getirmek için sular seller gibi bilmeliyiz.

# Ürün kategorilerine göre satış rakamları diyelim.(NULL ları göstermesin)
# ...(Yani o şartıda ekleyelim)
"""
select CATEGORY_NAME1, SUM(LINENET) FROM SALES 
WHERE CATEGORY_NAME1 IS NOT NULL
GROUP BY CATEGORY_NAME1
ORDER BY 2 (SUM(LINENET)) DESC
"""

# BUNUN altına bir tane de marka değerini getirmek istiyorum.

"""
select CATEGORY_NAME1,BRAND, SUM(LINENET) FROM SALES 
WHERE CATEGORY_NAME1 IS NOT NULL
GROUP BY CATEGORY_NAME1,BRAND
ORDER BY SUM(LINENET) ((2)) DESC
"""
# NOT: sum(linenet) yerine sadece "2" de yazabiliriz.

# SADECE GIDA OLSUN CATEGORİMİZDE

"""
select CATEGORY_NAME1,BRAND, SUM(LINENET) FROM SALES 
WHERE CATEGORY_NAME1 IS NOT NULL AND CATEGORY_NAME1='GIDA'
GROUP BY CATEGORY_NAME1,BRAND
ORDER BY SUM(LINENET) DESC
"""
# Yani categorinin altına markayı getirmiş olduk.

# Tersten düşünelim. Bir üretici birden fazla markada üretim yapabiliyor.
# ürün markasına göre satışlar
"""
select BRAND, SUM(LINENET) FROM SALES 
WHERE BRAND IS NOT NULL
GROUP BY BRAND
ORDER BY SUM(LINENET) DESC
"""

# ülkerin altında en çok ne satıyormuşum bakalım

"""
select BRAND, CATEGORY_NAME1, SUM(LINENET) FROM SALES 
WHERE BRAND IS NOT NULL AND BRAND = 'ÜLKER'
GROUP BY BRAND, CATEGORY_NAME1
ORDER BY SUM(LINENET) DESC
"""

# DAHA DETAYLI İSTERSEK(KATEGORY NAME 2 VE SIRALI VS)

"""
select BRAND, CATEGORY_NAME1, CATEGORY_NAME2, SUM(LINENET) FROM SALES 
WHERE BRAND IS NOT NULL AND BRAND = 'ÜLKER'
GROUP BY BRAND, CATEGORY_NAME1, CATEGORY_NAME2
ORDER BY BRAND, CATEGORY_NAME1, CATEGORY_NAME2
"""

#%% 7. VIDEO - GROUP BY KULLANIMI 5

# SORU MAĞAZALARIN MÜŞTERİ SAYISINI HESAPLAMA

"""
SELECT BRANCH, COUNT(CLIENTNAME)
FROM SALES
GROUP BY BRANCH
"""
# aDANA 15858 TANE SATIRI VARMIŞ. üstte CLIENTNAME YERİNE , * ya da ITEMCODE
# ... da yazabilirdik.O zaman bizim burada farklı bir şey yapmamız gerekiyor.

"""
select DISTINCT CLIENTNAME
FROM SALES WHERE BRANCH = 'ADANA SUBESİ'
"""

# Şimdi Adana şubesinde 3592 tane müşteri varmış.
# ilk sorguda Adana karşısına 15858 yerine 3596 yı getirmem gerekiyor.
# Yani mağazamdaki müşteri sayısını bulalım. Onu da şöyle yapacağız.

"""
SELECT BRANCH, COUNT(DISTINCT CLIENTNAME)
FROM SALES
GROUP BY BRANCH
"""

# PEKİ ; Bir müşteri birden fazla mağazadan alışveriş yapmış olabilir mi ?
# Alttaki çıktıyı kopyalıyorum excel e yapıştırıyorum.
# sağdaki sütuna tıkladım toplamı görmek için : 127633
# Yani herkes kendi mağazasından alışveriş yapıyor olsa 127633 müşterim
# ... olması gerekir.
# Gerçekte o kadar mı teyit edelim .

"""
SELECT COUNT(DISTINCT CLIENTNAME)
FROM SALES
"""
# 49205 yani bazı müşteriler başka şubelere de gitmiş.

# Şimdi 1 müşterinin gittiği mağaza sayısını bulalım.

"""
select CLIENTNAME, COUNT(DISTINCT BRANCH)
FROM SALES
GROUP BY CLIENTNAME
ORDER BY 2 DESC
"""

# Bir tane isim için bi kontrol yapalım.

"""
select * from SALES WHERE CLIENTNAME='Levent Alperen'
"""

# 37 kere alışveriş yapmış bu kişi
# city den de nerelerden yaptığını görüyoruz.
# ama cıty yi direk görmek istersek

"""
select DISTINCT BRANCH from SALES WHERE CLIENTNAME='Levent Alperen'
"""

# 5 ten fazla mağazaya giden müşterileri listeleyelim

"""
select CLIENTNAME, COUNT(DISTINCT BRANCH)
FROM SALES
GROUP BY CLIENTNAME
HAVING COUNT(DISTINCT BRANCH) >10

select DISTINCT BRANCH 
from SALES 
WHERE CLIENTNAME='Arzu ALPER'
"""

# 2 sorguyu birlikte görelim.
# 3 TANE müşteri 10 dan fazla mağazadan alışveriş yapmış.
# .. ve Arzu Alper nerelerden alışveriş yapmış görüyoruz.

# ilişkisel veritabanına geldiğimizde daha karmaşık yapılar göreceğiz.

#%%son video
# Aşağıdaki soruları bilmeniz bekleniyor.

"""
1.SQL Server'a' bir database nasıl restore edilir.
2.Aggregate function ne demektir? Hangi çeşitleri vardır?
3.Group By ne amaçla ve nasıl kullanılır?
4.MIN,MAX,AVG,COUNT;COUNT DISTINCT komutları hangi amaçla ve nasıl kullanılır?
5.HAVING komutu hangi amaçla ve nasıl kullanılır?
6.Group By kullanılan sorguda Order By nasıl kullanılır?
"""
