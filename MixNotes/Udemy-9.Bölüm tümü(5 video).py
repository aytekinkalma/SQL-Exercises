# 9. Bölüm - SUBQUERY

# Gerek bir tablodan gerekse birden fazla tablodan JOIN leyerek,
# ... alan isimlerini yazarak datamızı kolonlar ve satırlar olarak döndürüyoruz.
# Ancak bazen, bu kolonlar bizim işimizi görmez
# Bunun için parantez içinde yazdığımız yapı tek bir kolonu döndürür.
# Bu yapıya subquery deriz.

# Kolay anlaşılması açısından bi uygulama yapalım.
# USER_ tabloma bakalım.

"""
SELECT U.NAMESURNAME
FROM USER_ U
"""
# 9999 tane kaydım geldi. İstiyorum ki bir müşterimin benden kaç kez alışveriş yapmış.
# Normalde Group by ve join le şu şekilde yapardık.

"""
SELECT U.NAMESURNAME, COUNT(B.ID)
FROM USER_ U
JOIN BASKET B ON B.USERID=U.ID
GROUP BY U.NAMESURNAME
"""
# NOT:Şu anda bizde BASKET boş o yüzden sorguda bişey göremezsin.
# JOIN yerine LEFT JOIN yazsaydık 9999 sonuç getirirdi.
# ... Alışveriş yapmayanların yanına da 0 yazardı.
# Şimdi bunun başka bir yolu daha var.

"""
SELECT U.NAMESURNAME,
(SELECT COUNT(*) from BASKET WHERE USERID=U.ID)
from USER_ U
"""
# Araya yazdığımız subquery(Parantez içindeki)
# INNER JOIN de ne yapmıştık biz?
# Sadece sepete en az bir kere ürün eklemiş kullanıcıları getirmek istemiştim.
# Burada şimdi 9999 sonuç geldi.
# Ben en az 1 ürün eklemiş kullanıcıları görmek istersem oraya bir şart yazabilirim.

"""
SELECT U.NAMESURNAME,
(SELECT COUNT(*) from BASKET WHERE USERID=U.ID)
from USER_ U
WHERE (SELECT COUNT(*) from BASKET WHERE USERID=U.ID)>0
"""

# Şimdi akla şu soru gelebilir. JOIN mi kullanmak mantıklı subquery mi ?
# Bu örnek için JOIN li olan kod daha temiz görünüyordu.
# Başka bir soru: Bunlardan hangisi daha hızlı çalışır?

# SQL de yapılan işlem IO okuma işlemi. Ne kadar fazla IO yaparsa o kadar yoruluyordur sistem.
# SQL server da datalarımız 8kb lık page ler halinde tutulur ve şimdi yazacağımız sorgu
# ... kaç tane page okuduğunuz söyleyebilir.
# Şimdi her 2 kod içinde bakalım hangisi daha hızlı çalışıyor diye


"""
SET STATISTICS IO ON
SELECT U.NAMESURNAME, COUNT(B.ID)
FROM USER_ U
JOIN BASKET B ON B.USERID=U.ID
GROUP BY U.NAMESURNAME
"""
# Çıktı da "logical reads 5" ve "logical reads237" yazıyor ayrı satırlarda
# Toplamda 242 page okumuş

"""
SELECT U.NAMESURNAME,
(SELECT COUNT(*) from BASKET WHERE USERID=U.ID)
from USER_ U
WHERE (SELECT COUNT(*) from BASKET WHERE USERID=U.ID)>0
"""

# Çıktı da "logical reads 237" ve logical reads 10" yazıyor
# Toplamda 247 tane page okumuş

# Yani 2 query arasında performans farkı yok denecek kadar az.
# O zaman ben hangisinin kod yazımı kolaysa onu yazarım.

# Ancak bazı örnekler varki onu JOIN le değil sadece subquery ile yapabilirsiniz.
# Onlara bakalım

#%%2. Video
# Subquery ile Müşteri bilgisi getirme
# select ID.NAMESURNAME den sonra  kod yazıp
# ...bu kullanıcının en son sepete ekleme tarihini getirelim.

"""
select ID,NAMESURNAME,
(select MAX(CREATEDDATE) from BASKET WHERE USERID=U.ID) as LASTBASKETDATE
from USER_ U
"""

# Null gelenler sepete hiç ürün eklemeyenler.
# Dolu gelenler ise bu kullanıcının en son sepete ekleme zamanı.
# Peki bu kullanıcı kaç kere sepete eklemiş ona bakalım.

"""
select ID,NAMESURNAME,
(select COUNT(*) from BASKET WHERE USERID=U.ID) as BASKETCOUNT,
(select MAX(CREATEDDATE) from BASKET WHERE USERID=U.ID) as LASTBASKETDATE
from USER_ U
WHERE (select COUNT(*) from BASKET WHERE USERID=U.ID)>0
"""
# 953 kişi geldi

# Bir tane de bunun ilk alışveriş zamanını getirelim.

"""
select ID,NAMESURNAME,
(select COUNT(*) from BASKET WHERE USERID=U.ID) as BASKETCOUNT,
(select MIN(CREATEDDATE) from BASKET WHERE USERID=U.ID) as FIRSTBASKETDATE,
(select MAX(CREATEDDATE) from BASKET WHERE USERID=U.ID) as LASTBASKETDATE
from USER_ U
WHERE (select COUNT(*) from BASKET WHERE USERID=U.ID)>0
"""

# Kişi ne kadar bizden alışveriş yapmış(TL olarak)
# Bu bilgi BASKETDETAIL tablosunda yer alıyor.(user la alakalı bilgi yok)
# Aşağıdaki kodu yazalım. Sonra anlatacağız.

"""
select ID,NAMESURNAME,
(select COUNT(*) from BASKET WHERE USERID=U.ID) as BASKETCOUNT,
(select MIN(CREATEDDATE) from BASKET WHERE USERID=U.ID) as FIRSTBASKETDATE,
(select MAX(CREATEDDATE) from BASKET WHERE USERID=U.ID) as LASTBASKETDATE,
(select SUM(TOTAL) from BASKETDETAIL WHERE BASKETID IN (SELECT ID FROM BASKET WHERE USERID=U.ID)) AS TOTAL
from USER_ U
"""

# WHERE şartında IN komutunu kullanmıştık.
# IN komutunda; WHERE ID IN(101,102,103) gibi ayırt ettiriyorduk.
# Oysa burada IN komutunu tablodan dönen bir  değer için kullandım.

# Ben şimdi bakıyorum "Selahattin Sukusturan" isimli kullanıcıma bakıyorum.
# Bunun ID si 127 (Bizde 126 da)

"""
select ID from BASKET WHERE USERID=127
"""

# Bu kullanıcının 2 tane basket tablosunda kaydı var.

"""
select * from BASKETDETAIL WHERE BASKETID IN (1062,1233)
"""

# 1062 den 4 tane 1233 den 6  tane kayıt mevcut.Peki şunu desem ne olur
# Böyle yapmak yerine parantez içine bi subquery göndersem.
# subquery yi bir kolon ya da bir değer gibi kullanabiliyoruz ya o yüzden.

"""
select SUM(TOTAL) from BASKETDETAIL WHERE BASKETID IN (select ID from BASKET WHERE USERID=127)
"""
# 10066.12

# Bi de Count unu aldıralım. Toplam Kaç ürün almış benden.

"""
select ID,NAMESURNAME,
(select COUNT(*) from BASKET WHERE USERID=U.ID) as BASKETCOUNT,
(select MIN(CREATEDDATE) from BASKET WHERE USERID=U.ID) as FIRSTBASKETDATE,
(select MAX(CREATEDDATE) from BASKET WHERE USERID=U.ID) as LASTBASKETDATE,
(select SUM(TOTAL) from BASKETDETAIL WHERE BASKETID IN (SELECT ID FROM BASKET WHERE USERID=U.ID)) AS TOTAL,
(select COUNT(*) from BASKETDETAIL WHERE BASKETID IN (SELECT ID FROM BASKET WHERE USERID=U.ID)) AS ITEMCOUNT
from USER_ U
"""
# BasketCounttan kaç sefer de, ItemCOUNT tan da kaç tane ürün eklediğini görüyorum.
# BASKETCOUNT = 2 , ITEMCOUNT=6 ise 2 seferde toplam 6 ürün eklemiş diyeceğim.
# Bu sorguyu JOIN le yapabilir miydik? Yapardık.

"""
select U.ID, U.NAMESURNAME,
COUNT(B.ID) AS BASKETCOUNT ,
MIN(B.CREATEDDATE) AS FIRSTBASKETDATE,
MAX(B.CREATEDDATE) AS LASTBASKETDATE,
SUM(BD.TOTAL) AS TOTAL,
COUNT(BD.ID) AS ITEMCOUNT
FROM USER_ U 
INNER JOIN BASKET B ON B.USERID=U.ID
INNER JOIN BASKETDETAIL BD ON BD.BASKETID=B.ID
GROUP BY U.ID , U.NAMESURNAME
"""

# DAHA temiz bir kodla aynı değeri elde ettim.
# Aklımıza yine şu soru gelecek. subquery yi neden kullanıyoruz?
# JOIN le bağlamamıza gerek kalmayabilir bazen (Tam açıklama alamadık bence burada)
# Başka bir örnekle devam edelim.

#%%3. Video - SUBQUERY - 3

# Soru : Müşterinin sepetine eklediği son ürün.
# Bu standart JOIN ler ile gelebilecek bir şey değil.
# Mesela aşağıdaki kodda son eklediği ürünü görebiliyordum evet.

"""
select U.ID, U.NAMESURNAME, MAX(BD.DATE_) as LASTTIMEDATE
FROM USER_ U
INNER JOIN BASKET B ON B.USERID = U.ID
INNER JOIN BASKETDETAIL BD ON BD.BASKETID=B.ID
INNER JOIN ITEM I ON I.ID=BD.ITEMID
GROUP BY U.ID,U.NAMESURNAME
"""

# ...ama son eklediği ürün nasıl olacak?
# Bunun için subquery yazmaktan başka şansımız yok. ve biraz çetrefilli subquery yazacağız.

"""
select ID,NAMESURNAME,
(select COUNT(*) from BASKET WHERE USERID=U.ID) as BASKETCOUNT,
(select MIN(CREATEDDATE) from BASKET WHERE USERID=U.ID) as FIRSTBASKETDATE,
(select MAX(CREATEDDATE) from BASKET WHERE USERID=U.ID) as LASTBASKETDATE,
(select SUM(TOTAL) from BASKETDETAIL WHERE BASKETID IN (SELECT ID FROM BASKET WHERE USERID=U.ID)) AS TOTAL,
(select COUNT(*) from BASKETDETAIL WHERE BASKETID IN (SELECT ID FROM BASKET WHERE USERID=U.ID)) AS ITEMCOUNT,
(select ITEMNAME from ITEM WHERE ID IN (SELECT TOP 1 ITEMID FROM BASKETDETAIL WHERE BASKETID IN
    (
	SELECT ID FROM BASKETDETAIL WHERE BASKETID IN
         (
		 SELECT ID FROM BASKET WHERE USERID=U.ID
) 
)ORDER BY DATE_ DESC))
AS LASTTIMENAME
from USER_ U
"""

# ITEMCOUNT sütununda 1 den fazla malzeme gözükmemesi için, TOP 1 yazdık
# ve bunu DATE_ E GÖRE SIRALASIN DEDİK ORDER BY ile
# Aldıkları son ürün görünüyor.(Mesela Soner Ülgen)
# Kontrol için bakalım

"""
select U.ID, U.NAMESURNAME,BD.DATE_,I.ITEMNAME
FROM USER_ U
INNER JOIN BASKET B ON B.USERID = U.ID
INNER JOIN BASKETDETAIL BD ON BD.BASKETID=B.ID
INNER JOIN ITEM I ON I.ID=BD.ITEMID
WHERE U.ID=5
ORDER BY BD.DATE_
"""
# Doğru yapmışız.

# NOT: iç içe select = alt sorgu = subquery
# Bu tarz bi sorgu için bunu yapmamız gerekiyor.
# Bunu 1 kaç kere yapın. Bu zamana kadar gördüğümüz en karmaşık sorgulardan birisiydi bu

#%% 4. Video- sorular

"""
1. Management Studio kullanımını yeterince biliyor muyum?
2. SQL Server Authentication türleri hakkında bilgi sahibi miyim?
3. SQL Serverda tablo oluşturabiliyor muyum?
4. SQL Server'ın geri planda sadece TSQL komutları çalıştırıyor olmasını biliyor muyum?
"""















