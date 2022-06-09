# 7. Bölüm - Join işlemleri
# 1. Video
# Bir önceki derste elimizdeki datayı nasıl doldurabileceğimizi öğrenmiş olduk.
# Artık RDMS tabanının kodlama kısmına geleceğiz. Daha sonra da daha büyük
# datalarla bu sql kodlamayı canlı data üzerinde kodluyo olacağız.

# Şimdi elimizde USER tablosu var
"""
select * from USER_ WHERE ID=1
"""
# Nazlıcan Özsimitçi
# Bu Nazlıcan Özsimitçiye ait ne kadar adres var acaba
"""
select * from ADDRES WHERE USERID=1
"""
# Burada bu kullanıcıya ait 4 tane adres var
# Ben istiyorum ki ben bir tablo oluşturayım
# Bana kullanıcı adı - ad soyad - email- tel1- tel2-adres bilgisini getirsin.
# Böyle bir bilgi çekmek isteyeyim.
# Zaten büyük kısmı bu tabloda var.
"""
select USERNAME_, NAMESURNAME, EMAIL, TELNR1, TELNR2 from USER_ WHERE ID=1
"""
# ya da 
"""
select USERNAME_, NAMESURNAME, EMAIL, TELNR1, TELNR2 from USER_ WHERE USER_.ID=1
"""
# Burada sadece adres eksik.
# Yani 4 adresi benim yandaki kolona yazdırmam gerekiyor.
# İşte burada ilişkisel veritabanı ortaya çıkıyor.
# Yani ADDRES tablosu ile USER_ tablosu arasında ne tarz bi ilişki var.
# ADDRES tablosundaki USERID ile 
# USER_ tablosundaki ID alanına eşit.
# Bu 2 tabloyu bağlayarak bu işi halledebilirim.
# Burada da join mantığını öğreneceğiz.
# Standart kullanım şekli şu şekilde

"""
select USERNAME_, NAMESURNAME, EMAIL, TELNR1, TELNR2 from USER_ WHERE ID=1
JOIN ADDRES ON USER_.ID=ADDRES.USERID
WHERE ID=1
"""
# Hangi tablo ile bağlamak istiyorsak sonradan o tablonun(ADDRES) ismini yazıyoruz.
# ... ve neye göre bağlayacağıma "ON USER_.ID=ADDRES.USERID" bu kodla karar veriyorum.
# Sonra

"""
select USER_.USERNAME_, USER_.NAMESURNAME, USER_.EMAIL, USER_.TELNR1, USER_.TELNR2 
from USER_
JOIN ADDRES ON USER_.ID=ADDRES.USERID
WHERE USER_.ID=1
"""

# şeklinde yapıyorum.
# Başlarına USER_. yazdık çünkü aynı alan başka yerlerde de tekrar ediyor olabilir.
# ... JOIN kullanacağımız için yazmak daha iyi. O yüzden başına tablo adını yazıyorum.
# EN SON bi de ADDRES.ADRESSTEXT alanını da buraya getir diyorum.

"""
select USER_.USERNAME_, USER_.NAMESURNAME, USER_.EMAIL, USER_.TELNR1, USER_.TELNR2 , ADDRES.ADDRESSTEXT
from USER_
JOIN ADDRES ON USER_.ID=ADDRES.USERID
WHERE USER_.ID=1
"""

# başlarına USER_. yazmasam ne olurdu.
"""
select USERNAME_, NAMESURNAME, EMAIL, TELNR1, TELNR2 , ADDRES.ADDRESSTEXT
from USER_
JOIN ADDRES ON USER_.ID=ADDRES.USERID
WHERE USER_.ID=1
"""
# Bu da çalıştı . En alttaki USER ı da kaldırırsam ?
"""
select USERNAME_, NAMESURNAME, EMAIL, TELNR1, TELNR2 , ADDRESSTEXT
from USER_
JOIN ADDRES ON USER_.ID=ADDRES.USERID
WHERE ID=1 
"""
# HATA
# Ambigious column name "ID" (Buradaki ID alanının hangi tabloya ait olduğu belirsiz)
# Üsttekileri kaldırdığımda neden hata olmadı. Çünkü
# USERNAME sadece USER tablosunda geçiyor ya da email ya da telnr1
# ADRESSTEXT de sadece ADRESS tablosunda geçiyor. O yüzden bi belirsizlik yok.
# Ama ID hem ADRESS tablosunda hem USER_ tablosunda olduğu için sorun çıktı.

# Bu JOIN in en temel kullanım şekli.
# Farklı JOIN leri kullanarak öğrenmeye devam edeceğiz.

#%% 2.Video
# Bir önceki derste ilişkisel 2 tabloyu nasıl bağladığımızı görmüş olduk.
# JOIN lerin de kullanım alanı ve data tipine göre farklı kullanım şekilleri var
# Önce teorik bakalım sonra uygulama bakalım.
# En temel JOIN , JOIN in kendisi ya da INNER JOIN dediğimiz yapı
# Burada video nun 45 inci saniyesinden itibaren bak. 2 küme var
# Bir küme USER tablosu, diğer küme ADRESS tablosu
# Bunların kesişimlerine bakıcam
# Her 2 tabloda da olanları getirmesi lazım.
# 1 e 1 eşleşme, 1 e n eşleşme ( videoya bak)
# ......
# Birkaç canlı örnek ile anlamaya çalışalım.

#%%3.Video

# Şimdi inner join uygulamasını yapalım.

"""
select * from USER_ WHERE USER_.ID=1
"""
# 1 satır geldi

"""
select * from ADDRES 
WHERE USERID=1
"""

# Bunların kesişiminden bana 4 satır gelmesini beklerim

"""
select * from USER_
JOIN ADDRES ON ADDRES.USERID=USER_.ID
WHERE USER_.ID=1
"""
# Önce * diyip USER_ dediğim için önce USER_ ın tamamını sonra ADDRES in tamamını getirdi.
# Ben bunların içerisinden istediklerimi getirebilirim.(Bi önceki dersteki gibi)

"""
select USER_.NAMESURNAME, ADDRES.* from USER_
JOIN ADDRES ON ADDRES.USERID=USER_.ID
WHERE USER_.ID=1
"""
# USER_ dan sadece NAMESURNAME, ADDRES den hepsi geldi * dediğimiz için.

# Şimdi ADDRES tablosundan 2 numaralı kullanıcıyı sileyim.(ADDRES den)

"""
DELETE FROM ADDRES
WHERE USERID=2
"""
# Şimdi kesişiminden ne gelecek?
"""
select USER_.NAMESURNAME, ADDRES.* from USER_
JOIN ADDRES ON ADDRES.USERID=USER_.ID
WHERE USER_.ID=2
"""
# Boş geldi. Oysa burada USER_ tablom dolu ama JOIN le birlikte boş getirdi.
# Tersini yapalım 4 nolu kullanıcı için. 4 nolu kullanıcının 2 tane adresi varmış
# 4 nolu kullanıcıyı silelim.(USER_ dan)

"""
delete from USER_ WHERE ID=4
"""
# 2 satır geliyordu normalde ama aşağıda sildikten sonra bakarsak kesişim e

"""
select USER_.NAMESURNAME, ADDRES.* from USER_
JOIN ADDRES ON ADDRES.USERID=USER_.ID
WHERE USER_.ID=4
"""

# Boş gelir. Çünkü JOIN 2 kümenin kesişim noktasıydı. Kesişecek durum kalmadı.
# NOT: JOIN yerine INNER JOIN de yazabiliriz.

#%%4. Video - Left Join
# Sol taraftaki kümeden Join alma işlemi

# Sol tarafta USER_ da 7 kullanıcı var
# Sağ tarafta ADDRES de 6 bilgi var.
# Sol dan bi kişinin adresi yok.
# o kişiyi es geçmeden karşısına NULL yazar (INNER JOIN de böyle değildi)
# Left JOIn left i referans alır ve 7 tanesini de es geçmeden getirir.

# RIGHT JOIN
# Aynı mantık
# Sol tarafta USER_ da 6 kullanıcı var
# Sağ tarafta ADRESS de 7 bilgi var.
# Sağ tarafta adresin birisinin kullanıcısı yok.
# right Join de sağ taraftaki 7 tanesini es geçmeden getirir.
# ve o boş olan USERNAME bilgisine NULL değer getirir(sol tarafta)
# Diğer taraftan baktığımız zamanda 1 numaradaki Ömer kullanıcısına ait
# .. 2 adres var, bi de 7 numaralı denizli adresinin kullanıcısı yoktu.
# Right Join şunu yapacak. hem denizliye ait olan kullanıcı kaydını.
# ... Hem de Ömer e ait olan "Mersin"(2. adresi) kaydını getirir
# Sonuç olarak buradan 7 satırlık sonuç döndürür.

# FULL JOIN
# Sol da USER_ da 7 numaraları esranın sağ da(ADDRES) de adresi yok
# Sağ da da ADDRES de 2 tane Ömer(USER_ daki) kullanıcısına ait adres var
# Burada FULL JOIN ne yapıyor?
# Sağdan Mersin bilgisi Soldan da Esra bilgisi gelecek.
# Toplamda satır sayımız 8 satır sonuç gelmiş olacak (6+2 den)

#%% 5. Video - JOIN uygulamaları
# Şimdi uygulamalarını yaparak öğrenelim.

# INNER JOIN, LEFT Join ve right join arasındaki farkları anlamaya çalışalım.
# Bunun için 3 tane kullanıcının adres bilgisine bakmak istiyorum.
# Bunlar 100 , 101 ve 102 nolu kullanıcılar olsun.

"""
SELECT USER_.NAMESURNAME, ADDRES.* from USER_
INNER JOIN ADDRES ON ADDRES.USERID=USER_.ID
WHERE USER_.ID IN (100,101,102)
"""

# Biz de 8 adres gözüküyorda , Hoca da 3 tane gözüktü (Belki derste ekledi adres. Bilmiyoruz)
# Ben şimdi 102 numaranın adresini silmek istiyorum

"""
delete from ADDRES WHERE USERID=102
"""
# Silince 2 satıra düştü( bi üstteki kodu yeniden çalıştırınca)
# Ama benim kullanıcılar tablosunda 102 nolu kullanıcı mevcut
# Inner Join ile çağırdığım zaman gelmiyor. Neden? Çünkü Kesişme
# Sol taraftaki kümemde olup sağ taraftaki kümemde de olması lazım.
# sol u sağ yı nasıl anlıyorum ? 
# Kodda bi bölüm var ..... ON ADDRES.USERID=USER_.ID bölümü
# Eşittir in sol tarafındaki sol , sağ tarafındaki sağ kümem.
# O kodda inner Join değil de Left Join desek ne olurdu?

"""
SELECT USER_.NAMESURNAME, ADDRES.* from USER_
LEFT JOIN ADDRES ON ADDRES.USERID=USER_.ID
WHERE USER_.ID IN (100,101,102)
"""
# Bu sefer 3 satır geldi ama NULL değerlerle(ADDRES in altındaki değerler NULL farkettiysek)
# Çünkü kodda USER_ dan sadece NAMESURNAME i , ADDRES den * ı yani hepsini çağırmıştık.
# NAMESURNAME NULL değil, diğerleri NULL

# Peki right JOIN deseydim.
"""
SELECT USER_.NAMESURNAME, ADDRES.* from USER_
RIGHT JOIN ADDRES ON ADDRES.USERID=USER_.ID
WHERE USER_.ID IN (100,101,102)
"""

# 2 sonuç getirdi sadece. Çünkü eşittirin sağ tarafında USER_.ID var
# .. ancak sol tarafında ADDRES.USERID var ama bu ADDRES de kayıt olmadığı için
# ... onu getirmedi.

# NOT: Biraz düşünerek anlaşılabilecek bir şey dikkatli okursak-izlersek- zor değil.

# Full Join deseydik
# Left Join le aynı sonucu getirecek bana

# Left JOIN = LEFT OUTER JOIN
# RIGHT JOIN = RIGHT OUTER JOIN
# FULL JOIN = FULL OUTER JOIN
# DIKKAT: INNER JOIN  =! INNER OUTER JOIN (HATA)
# Başka veritabanlarında kullanıma göre bu yazılır ya da yazılmaz.
# OUTER yazsanızda yazmasanızda çalışır kod.
# NOT: HOCA: Biz genelde sorgu yazarken veri bürtünlüğü bozulmaması adına,
# ... standart kullanımda left Join kullanırız. sizin de eliniz alışsın.

# Örnekler üzerinde Join uygulamalarımızı pekiştirelim.

#%%6. video - ALLIAS kullanımı

# Biz hep 2 tane tabloyu birleştirerek işlemler gerçekleştirdik ancak
# JOINLER genelde 10 tablo - 15 tabloya kadar çıkabilir.
# Sonuçta RDMS kullanıyoruz.
# Uzun karakterli isme sahip olan tablolar bizim SQL sorgularımızın karışık
# ... olmasına sebep olur. Bunun önüne geçmek adına "ALLIAS" dediğimiz yapılar kullanılır.
# ALLIAS bir tabloya kısaltma isim verilmesi işlemidir.
# Nasıl kullanılır bakalım.

"""
select * from USER_
WHERE ID=1
"""
# Burada USER_ ı kısaltma olarak: U demek istiyorum.

"""
select * from USER_ U
WHERE U.ID=1
"""
# Böyle yapabilirim.
# Buraya bi JOIN atalım arasına

"""
select U.*, A.ADDRESSTEXT from USER_ U
JOIN ADDRES A ON U.ID=A.USERID
WHERE U.ID=1
"""
# Önce Aşağıda Join kısmında ADDRES A yazıyorum sonra üstte select in yanına yazıyorum
# ALLIAS kullandığım zaman tertemiz kodlar yazabiliyorum.
# Şimdi bunun kolaylığını daha çok görelim.
# 1 den fazla tablo için Join yapalım.
# Şu sonucu istiyorum. USER tablosundan Kullanıcı adı.
# ADDRES tablosunda Adres
# CİTY tablosundan İL
# TOWN dan İLÇE
# DISTRICT tablosundan MAHALLE yi almak istiyorum.
# Zaten ADDRES in içinde CITYID, TOWNID; DISTRICTID vs var.
# Şimdi kodu yazalım.

"""
select U.*, A.* ,C.CITY, T.TOWN, D.DISTRICT
from USER_ U
JOIN ADDRES A ON U.ID=A.USERID
JOIN CITY C ON C.ID=A.CITYID
JOIN TOWN T ON T.ID=A.TOWNID
JOIN DISTRICT D ON D.ID = A.DISTRICTID
WHERE U.ID=1
"""

# Şimdi istediğimiz formatta yazdıralım bunu

"""
select U.USERNAME_, U.NAMESURNAME,U.EMAIL, U.TELNR1, U.TELNR2,C.CITY, T.TOWN, D.DISTRICT
from USER_ U
JOIN ADDRES A ON U.ID=A.USERID
JOIN CITY C ON C.ID=A.CITYID
JOIN TOWN T ON T.ID=A.TOWNID
JOIN DISTRICT D ON D.ID = A.DISTRICTID
WHERE U.ID=1
"""

# İstediğim formatta oldu.
# Burada 5 tabloyu birbirine Joinliyerek sonucumuzu döndürdük.
# 4 tanesi Join lerden sonra birleştirildi.
# Hangi tabloya? ---> from USER_ U  daki USER tablosuna.
# from dan sonra o yüzden sadece USER_ yazdım, diğerlerini birleştirdim.

# Bir de kolonlara verilen ALLIAS var.(daha önce görmüştük)

"""
select U.USERNAME_ KULLANICIADI, 
U.NAMESURNAME AS ADSOYAD,U.EMAIL AS EMAIL, U.TELNR1 AS TELEFON1, U.TELNR2 AS TELEFON2,
C.CITY AS ŞEHİR, T.TOWN AS İLÇE, D.DISTRICT AS MAHALLE
from USER_ U
JOIN ADDRES A ON U.ID=A.USERID
JOIN CITY C ON C.ID=A.CITYID
JOIN TOWN T ON T.ID=A.TOWNID
JOIN DISTRICT D ON D.ID = A.DISTRICTID
WHERE U.ID=1
"""

# Bundan sonra daha farklı verilerle daha farklı senaryolar üzerinden bu Joın
# .. meselesini pekiştirerek gideceğiz.

#%%7. Video - GROUP BY KULLANIMI

# GROUP BY, SUM, COUNT .... gibi aggregate functionları işlemiştik.
# Ancak tek tablodan sorgu çektiğimiz yapıda işlemiştik.
# Şimdi benzer GROUP BY sorgularını JOIN ile bağladığımız 1 den fazla tablo
# ... üzerinde nasıl kullanırız onu göreceğiz.

# Sorumuz şu olsun "her bir kullanıcının kaç tane adresi var onu listele"
# Biz ID=1 için yapmıştık 4 satır getirmişti bize. 
# Ben şunu istiyorum kullanıcıadısoyadı, email i tel1, tel2 ve adress sayısı

"""
select U.USERNAME_ KULLANICIADI, 
U.NAMESURNAME AS ADSOYAD,U.EMAIL AS EMAIL, U.TELNR1 AS TELEFON1, U.TELNR2 AS TELEFON2,
COUNT(A.ID) AS ADRESAYISI
from USER_ U
JOIN ADDRES A ON U.ID=A.USERID
JOIN CITY C ON C.ID=A.CITYID
JOIN TOWN T ON T.ID=A.TOWNID
JOIN DISTRICT D ON D.ID = A.DISTRICTID
WHERE U.ID=1
GROUP BY U.USERNAME_, U.NAMESURNAME ,U.EMAIL, U.TELNR1, U.TELNR2
"""

# ÖNEMLİ NOT: Bir AGGREGATİON function kullandığımız zaman (üstte COUNT)
# ... GROUP BY kullanmak zorundaydık.

# A.ID yerine A.* da yazabilirdik çünkü her kolonda 4 satır var sonuçta

# Şimdi WHERE şartını kaldırıp bütün kullanıcılar için çalıştıralım bu sorguyu
# Bir de ORDER BY ekleyelim.
"""
select U.USERNAME_ KULLANICIADI, 
U.NAMESURNAME AS ADSOYAD,U.EMAIL AS EMAIL, U.TELNR1 AS TELEFON1, U.TELNR2 AS TELEFON2,
COUNT(A.ID) AS ADRESAYISI
from USER_ U
JOIN ADDRES A ON U.ID=A.USERID
JOIN CITY C ON C.ID=A.CITYID
JOIN TOWN T ON T.ID=A.TOWNID
JOIN DISTRICT D ON D.ID = A.DISTRICTID
GROUP BY U.USERNAME_, U.NAMESURNAME ,U.EMAIL, U.TELNR1, U.TELNR2
ORDER BY COUNT(A.ID) DESC
"""

# En fazla olan adres sayısı 4 taneymiş.

# Şimdi Adres sayısı 1 tane olanlar kaç taneymiş ona bakalım.
# Şimdi şart için HAVING kullanmalıyız

"""
select U.USERNAME_ KULLANICIADI, 
U.NAMESURNAME AS ADSOYAD,U.EMAIL AS EMAIL, U.TELNR1 AS TELEFON1, U.TELNR2 AS TELEFON2,
COUNT(A.ID) AS ADRESAYISI
from USER_ U
JOIN ADDRES A ON U.ID=A.USERID
JOIN CITY C ON C.ID=A.CITYID
JOIN TOWN T ON T.ID=A.TOWNID
JOIN DISTRICT D ON D.ID = A.DISTRICTID
GROUP BY U.USERNAME_, U.NAMESURNAME ,U.EMAIL, U.TELNR1, U.TELNR2
HAVING COUNT(A.ID)=1
"""
# sağ altta 2492 çıktı.
# Böylelikle GROUP BY komutunu JOIN in içerisinde ALLIAS larla birlikte nasıl kullanıldığını
# ... öğrenmiş olduk.
# Başka bir örnek yapalım.

# Hangi şehirde kaç tane kullanıcımız var?

"""
select 
C.CITY, COUNT(U.ID)
from USER_ U
JOIN ADDRES A ON U.ID=A.USERID
JOIN CITY C ON C.ID=A.CITYID
JOIN TOWN T ON T.ID=A.TOWNID
JOIN DISTRICT D ON D.ID = A.DISTRICTID
GROUP BY C.CITY
ORDER BY 2 DESC
"""

# Biraz daha ilginç bir şey yapalım.
# Adress sayısını ekleyelim. Onun da yanına mesela 3 adresi var ama kaç farklı şehirde?
# COUNT DISTINCT kullanacağız.

"""
select U.USERNAME_ KULLANICIADI, 
U.NAMESURNAME AS ADSOYAD,U.EMAIL AS EMAIL, U.TELNR1 AS TELEFON1, U.TELNR2 AS TELEFON2,
COUNT(A.ID) AS ADRESAYISI, COUNT(DISTINCT C.CITY) AS SEHIRSAYISI
from USER_ U
JOIN ADDRES A ON U.ID=A.USERID
JOIN CITY C ON C.ID=A.CITYID
JOIN TOWN T ON T.ID=A.TOWNID
JOIN DISTRICT D ON D.ID = A.DISTRICTID
GROUP BY U.USERNAME_, U.NAMESURNAME ,U.EMAIL, U.TELNR1, U.TELNR2
"""

# Kontrol için U.ID yi select ten sonra eklersek, GROUP BY a da eklersek ID leride görünür.
# Farklı adressayısı ve şehir sayısı farklı olan bulduk bi tane ---> 4460
# Bunu teyit edelim doğruluğunu
"""
select * from ADDRES WHERE USERID=4460
"""

# Hatta Having e bunu koyalım.

"""
select U.USERNAME_ KULLANICIADI, 
U.NAMESURNAME AS ADSOYAD,U.EMAIL AS EMAIL, U.TELNR1 AS TELEFON1, U.TELNR2 AS TELEFON2,
COUNT(A.ID) AS ADRESAYISI, COUNT(DISTINCT C.CITY) AS SEHIRSAYISI
from USER_ U
JOIN ADDRES A ON U.ID=A.USERID
JOIN CITY C ON C.ID=A.CITYID
JOIN TOWN T ON T.ID=A.TOWNID
JOIN DISTRICT D ON D.ID = A.DISTRICTID
GROUP BY U.USERNAME_, U.NAMESURNAME ,U.EMAIL, U.TELNR1, U.TELNR2
HAVING COUNT(A.ID)<>COUNT(DISTINCT C.CITY)
"""

# <> = "FARKLI" demek
# 671 tane kayıdın aynı şehirde 1 den fazla kaydı varmış


#%%8.Video - son -sorular

"""
1.İlişkisel veritabanında birden fazla tablo nasıl birleştirilir?
2.JOIN kavramı ne demektir?
3.INNER JOIN, LEFT JOIN, RIGHT JOIN,FULL JOIN kavramları arasında ne farklar vardır?
4.Master Detay özelliğindeki tablolar nasıl bağlanarak soru çekilir?
5.ALIAS nedir?
6.JOIN kullandığımız tablolarda ALIAS kullanımı nasıl yapaılır?
7.JOIN kullandığımız tablolarda GROUP BY nasıl kullanılır?
"""






