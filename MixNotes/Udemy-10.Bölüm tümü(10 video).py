# 10. Bölüm - String İşlemleri
# 1. Video

# Bu bölümde SQL server üzerinde string işlemlerinden bahsediytor olacağız.
# Sql server üzerinde sadece sql dili ile değil, Transact SQL dediğimiz,
# ... sql server için özelleştirilmiş bir dil olan t-sql ile bir 
# ... programlama dilinde yapabileceiğimiz hemen hemen her şeyi yapabiliriz.
# ... Bunlar içinde string operasyoları, matematiksel opersayonlar, döngüler,
# ... değişken atamalar vs sadece t-sql komutları kullanarak yapabiliriz.
# Bu anlamda gelişmiş bir string işlemleri fonksiyonları listesi var.
# Bunlar üzerinde konuşuyor olacağız.

# videonun sonunda o fonksiyonları gösteriyor.

#%%2. video -ASCII(Aski) - CHAR
# Alfabetik sıraya göre gidelim. String fonksiyonlarımızdan ilk fonksiyonumuz ASCII

# ASCII: İçerisine aldığımız karakterin ASCII türünden değerini verir.
# Yani bizim byte olarak neye karşılık geliyorsa onun değerini verir.
# Şu şekilde çalıştıralım. Örneğin A harfinin ASCII değeri

"""
select ASCII ('A')
"""

# Alfabetik karakterler 0 dan 255 e kadar değerler alır.
# A nın karşılığı 65 miş
# Ö nün karşılığı 214
# 1 in karşılığı 49
# ? nin karşılığı 63 müş ...

# BİLGİ : seri port üzerinde çalışanlar var mı ama mesela seri porttan gelen
# ...datayı dinlerken ASCII formatında dinleriz.
# ...1 e basıyoruz 49 değeri gelir 
# ...2 ye basarız 50 gelir falan.

# ASCII ye bağlı bi de Char fonk var , char da bunun tam tersi
"""
select char(214)
"""
# Ö harfi geldi.
# Bunu iç içe kullanırsam aynı değeri görmem lazım.
# Fonksiyonları iç içe kullanabiliriz.

"""
select ASCII(CHAR(49))
"""
# Bana 49 u getirdi.

# Tam tersiniz yapalım.

"""
select CHAR(ASCII('Ö'))
"""

# Bana Ö yü getirdi.

#%%3. video - Substring

# Bu çok kullanılan bir fonksiyon ve diğerlerini anlatırken bundan yararlanacağımız için
# ... alfabetik sıra burada bozulsun biraz sonra alfabetik devam edelim.
# Substring: bir string in içerisinde belli bir noktadan belli bir noktaya kadar olan alanı
# ...almamızı sağlar. Genel olarak şu şekildedir.

"""
select SUBSTRING('ÖMER FARUK ÇOLAKOĞLU',1,4)
""" 
# select SUBSTRING(  dediğimiz anda alta yazı gelir zaten. "expression: üzerinde çalışacağım script")
# Yani bu string işlemlerinde alta açıklama gelir hep ve açıklamada sırayla koyu harf yazılı
# ... yerde ne yapmak istiyorsun u yazar.
# Buradaki 1: starting position - kaçıncı karakterden itibaren alacak. (Diyelim ki 1 olsun)
# buradaki 4: kaç karakter alacak - diyelim 4
# birinci karakterden itibaren(Ö den itibaren) 4 karakter al demek Ö - M - E - R.
# Yani ÖMER i bana verecek.
# Şimdilik bu kadar bilmemiz yeterli.


#%%4. video - CharIndex

# CharIndex : Bir string in içerisinde başka bir string i buldurup onun pozisyonunu bize söyler.

"""
select CHARINDEX('F', 'ÖMER FARUK ÇOLAKOĞLU',1)
"""

# F harfini aramak istiyorum.
# Nerede aramak istiyorum. 'ÖMER FARUK ÇOLAKOĞLU' nun içerisinde
# Nereden başlayarak arayayım. 1 den başla
# Bana 6 yı getirdi. Çünkü F harfi 6. karakter.

# Peki burada 1 den değil de 7 den başlayarak say deseydi
# Sıfır sonucu gelecekti. Yani bulamadı.
# Peki F yi değil de FARUK u bul desem

"""
select CHARINDEX('FARUK','ÖMER FARUK ÇOLAKOĞLU',1)
"""
# 6 sonucunu getirdi yine.

# Çolak desem .. 12 yi getirecekti.

#%%5. video - Concat, Concat_WS

# CONCAT: 2 veya daha fazla string in yan yana birleştirilmesini sağlar.
# İki string i yan yana yazdırmak istersek + işaretini kullanabiliriz.

"""
select 'ÖMER' + 'FARUK' +'ÇOLAKOĞLU'
"""

# çıktı : ÖMERFARUKÇOLAKOĞLU
# Bunun bir yolu da şu 
"""
select CONCAT('OMER','FARUK', 'COLAKOGLU')
"""
# çıktı : ÖMERFARUKÇOLAKOĞLU
# Aralarında boşluk olmasını istersem.
"""
select CONCAT('OMER','','FARUK','', 'COLAKOGLU')
"""

# çıktı: ÖMER FARUK ÇOLAKOĞLU
# Yalnız burada fonksiyon karmaşıklaşıyor. Bu ihtiyacı karşılamak için sanırım.
# Yeni bir fonksiyon koymuşlar. O da, CONCAT_WS

"""
select CONCAT_WS('','OMER','FARUK','COLAKOĞLU')
"""

# çıktı: OMER FARUK ÇOLAKOGLU

# Peki bu fonksiyonlar bir table üzerinde nasıl çalışıyor ona bakalım.
# Kullanıcı adı ve password ü yan yana yazdırmak isteyeyim.
# Bunun 2 yolu var.

"""
select
USERNAME_+' '+PASSWORD_+' '+NAMESURNAME, 
* from USER_
"""

# 2. yol CONCAT ile

"""
select
USERNAME_+' '+PASSWORD_+' '+NAMESURNAME, 
CONCAT(USERNAME_,' ',PASSWORD_,' ',NAMESURNAME),
* from USER_
"""

# 2. kolonda gördüğümüz gibi aynı sonucu getirdi.
# Bir de CONCAT_WS ile yapalım.

"""
select
USERNAME_+' '+PASSWORD_+' '+NAMESURNAME, 
CONCAT(USERNAME_,' ',PASSWORD_,' ',NAMESURNAME),
CONCAT_WS(' ',USERNAME_,PASSWORD_,NAMESURNAME),
* from USER_
"""

# Bakınız 3. kolonda aynı sonucu gördük.

#%%6. video - Format
# sayı ya da tarih türündeki (geneldde tarih için kukllanırız) değerleri
# ... local olarakl istediğimiz dormatta yazdırmamızı sağlar.

"""
select FORMAT(GETDATE) ,'d', 'en-us')
"""
# not: getdate bugünün tarihini getirir.

# çıktı : 10/18/2018

# Eğer büyük D olsaydı

# çıktı :Thursday, October 18, 2018
# haftanın gününü, günü ayı yılı getirdi.

# Başka hangi dillerde gösterebiliryoruz.
# ...(Hoca burada microsofttan aldığı bi alıntıyı gösteriyor.)
# Tarih alanını string olarak yazdırmak istiyorsak bu format fonk kullanıyoruz.

#%%7. video - Left, Right, Len
# left ve right fonk : bi tanesi soldan, bi tanesi sağdan karakter almamızı sağlar.

"""
select LEFT('OMER ÇOLAKOĞLU',4)
"""
# çıktı:OMER
# Gitti soldan 4 karakteri aldı.

"""
select RIGHT('OMER ÇOLAKOĞLU',4)
"""
#çıktı: OĞLU

# LEN: bir string in uzunluğunu alır

"""
select LEN('1234567890')
"""
# çıktı: 10

# adımı ve soyadımı ayrı ayrı yazdırmak istiyorum.

"""
select left('OMER ÇOLAKOGLU', 4)
select right('OMER COLAKOĞLU', 10)
"""

# Burada 4 ü ve 10 u elle girdik. Böyle yapmadan nasıl yapabilirimç.

"""
select LEFT('OMER ÇOLAKOĞLU', CHARINDEX(' ','OMER ÇOLAKOGLU'))
"""
# çıktı: ÖMER
# Boşluğun yeri olan 4 ü buldu daha sonra ÖMER ÇOLAKOĞLU nun içinden LEFT ile
# ... 4 ü aldı.
# RIGHT ile de 10 u bulduralım.


# ŞİMDİ : select RIGHT('OMER ÇOLAKOĞLU', CHARINDEX(' ','OMER ÇOLAKOGLU')) dediğimizde...
# sağdaki CHARINDEX(' ','OMER ÇOLAKOGLU') ne idi 4 tü.
# Burada soldaki 'OMER ÇOLAKOĞLU' nun uzunluğu 14. Yani bundan üsttekini çıkaracağım.

"""
select RIGHT('OMER ÇOLAKOĞLU',LEN('OMER ÇOLAKOĞLU') - CHARINDEX(' ','OMER ÇOLAKOGLU'))
"""

# çıktı: ÇOLAKOĞLU

# Şimdi bunları yanyana yazdıracak olursam

"""
select LEFT('OMER ÇOLAKOĞLU', CHARINDEX(' ','OMER ÇOLAKOGLU')),
RIGHT('OMER ÇOLAKOĞLU',LEN('OMER ÇOLAKOĞLU') - CHARINDEX(' ','OMER ÇOLAKOGLU'))
"""
# Böyle yaparım.
# Şimdi bunu database imiz üzerinde gerçekleştirelim.

"""
select 
LEFT(NAMESURNAME, CHARINDEX(' ','OMER ÇOLAKOGLU')),
RIGHT(NAMESURNAME,LEN('OMER ÇOLAKOĞLU') - CHARINDEX(' ','OMER ÇOLAKOGLU'))
from USER_
"""

# Adı ve soyadı ayrı ayrı yazdırdı.

#%%8. video - Trim, LTrim, RTrim
# TRIM: boşlukları temizlemek anlamına geliyor.
# L = left , R=Right

"""
select TRIM(' OMER ÇOLAKOĞLU ')
"""
# bir başa  bi sona boşluk koyduk.
# çıktı : ÖMER ÇOLAKOĞLU (ortadaki ve diğer yerlerdeki boşluklara dokunmadı)
"""
select LTRIM(' OMER ÇOLAKOĞLU ')
"""

# çıktı :ÖMER ÇOLAKOĞLU (Şimdi sql de bunu kopyalarsak bi yere yapıştırırsak cursor ün
# .. yandığı yere göre nerede ne oluyo görebiliriz.)
# Bazen başında boşluk olmaması gereken bilgiler girilir veritabanlarına. Bu tarz
# ... sorunlar olunca TRIM fonk kullanırız.
# Yaygın kullanılan başka şekli de şudur.

"""
select LTRIM(RTRIM(' OMER ÇOLAKOĞLU '))
"""

# çıktı: ÖMER ÇOLAKOĞLU
# Yine bana aynı sonucu getirmiş oldu (TRIM örneğindeki ile(En üstteki))

#%%9. video - Lower, Upper, Reverse, Replicate
# LOWER ve UPPER : büyük harf - küçük harf fonksiyonları
"""
select LOWER('OMER')
"""
# çıktı: omer

"""
select UPPER('Omer')
"""
# Çıktı : OMER

# Bazen veribütünlüğü olsun diye kimisi tamamen küçük , kimisi tamamen büyük yazar.

# REVERSE : Tersten yazdırma fonksiyonudur.

"""
select REVERSE('ÖMER FARUK')
"""

# çıktı: KURAF REMÖ

# Replicate: 1 den fazla tekrar etmesini sağlar.
"""
select REPLICATE('0',10)
"""

# Bu genelde belli bir karakter sayısını tutturmamız gereken yerlerde kullanırız.
# Elimde 178 olsun. bunu 8 karaktere tamamlayıp 00000178 yapmak istiyorum.
# Bi de başka bi rakam var 1187 yi . 00001187 yapmak istiyorum.
# Bunu programatik olarak çeşitli döngüler içerisinde çeşitli sorgularla yapmam gerekebilir.
# Bunun için bi tablo oluşturalım. new table
"""
SIRANO  int
SIRANO2 varchar(50)
"""
# Bu tabloyu da TEST olarak kaydedelim. TEST e sağ tıkla --> edit top 200 rows

"""
SIRANO    SIRANO2
1
2
3
4
5
6
7
8
9
10
11
12
13
118
877
1198
"""
# Sola rakamlar yazıcam . amacım sağdaki yere 8 karaktere tamamlatmak.
# Şimdi tamamlatmak için bunu otomatik olarak UPDATE cümlesiyle nasıl yaparım?

"""
select *,
REPLICATE('0',8-LEN(SIRANO))
from TEST
"""
# Böyle kaç tane 0 ekleyeceğini yanına getirdi çıktı da 
"""çıktı :  1        0000000
            2        0000000
            .
            .
            1198     0000
"""


"""
select *,
REPLICATE('0',8-LEN(SIRANO)+CONVERT(VARCHAR,SIRANO) FROM TEST
UPDATE TEST SET SIRANO2=REPLICATE('0',8-LEN(SIRANO)+CONVERT(VARCHAR,SIRANO)
"""
# Convert ile convert ettik. bi de update edelim bunları dedik ettik.
# Gördüğünüz gibi düzgün şekilde update etti tablomuz.

#%%10. video - Replace
# REPLACE : başka bi değerle REPLACE ettiren bir fonksiyon.
# Biz burada string ifadeyi konuşuyorsak. Burada aradığımız herhangi bir değeri
# ... set ettiğimiz başka bir değer ile değiştirme işlemi.

"""
select 'OMER ÇOLAKOĞLU'
""" 
# Burda OMER yerine OMER FARUK yazmak(yer değiştirmek istiyorum)

"""
select 'OMER ÇOLAKOĞLU'
select REPLACE('ÖMER ÇOLAKOĞLU', 'ÖMER', 'ÖMER FARUK')
"""
# Yukarıdaki kodun özeti :
# Neyin içerisinde? 'ÖMER ÇOLAKOĞLU'
# Neyi değiştireceksin 'ÖMER'
# Neyle değiştireceksin 'ÖMER FARUK'

# Akılda kalması adına başka bir örnek verelim. 
# Bir string in içerisinde bir kelime kaç kere geçiyor onu bulalım.

"""
'Delikanlı evine döndü, kendisini merakla bekleyen annesiyle babasına neler olduğunu anlattı.
Anlattıkça anlattı da kendine çok anlamsız gelen bu hareketi soğuk konuşması nedeniyle
kızdığı ustaya
'Nasıl olurda böyle budalaca bir şey yapmamı ister-
Birde ülkenin en iyi mücevhercisi olacak -
Bu saçmalığa bir yıl boyunca nasıl katlanırım, böyle bir eziyetle nasıl yaşarım?...
Bu ne biçim ustalık?...Ustalık kaprisi yapacaksa bari başından yapmasaydı..'
Devamlı söyleniyor, her önüne gelene ustadan yakınıyor, ama avucunu açmıyordu. Avucu kapalı uyuyor, 
Böylece bir yıl geçti, her günkü zorluklarla dolu, her gecesi yarım uykuyla yaşanmış bir yıl
Ve o gün geldi. Genç tam bir yıl sonra büyük ustanın karşısına çıktı. Usta onu bir süre bekle
"""

# Yukardaki metin tam değil de neyse ... 
# Elimizde bir paragraf var. Bir kelimenin ne kadar geçtiğini bulacağım.
# Paragraf uzun olunca SQL serverda bu şekilde kullanmak biraz sorgumuzu karmaşıklaştırıyor.
# .. Keşke buna bi değişken atasaydım da sorgunun içerisine doğrudan değişkeni çağırsaydım.
# Evet.. SQL server içerisinde değişken tanımlayabiliriz.
# DECLARE diyerek değişkeni tanımlarız ve değişken olduğunu belirtmek için @ deriz
# ... Sonra da buna bir isim veririz . Mesela "CUMLE" diyelim.
# ... Sonra tipini belirleriz. AS varchar(MAX)
# ... Sonra bu değişkene bir değer atarız. SET @CUMLE =  şeklinde

"""
DECLARE @CUMLE AS varchar(MAX)
SET @CUMLE='Delikanlı evine döndü, kendisini merakla bekleyen annesiyle babasına neler olduğunu anlattı.
Anlattıkça anlattı da kendine çok anlamsız gelen bu hareketi soğuk konuşması nedeniyle
kızdığı ustaya
Nasıl olurda böyle budalaca bir şey yapmamı ister-
Birde ülkenin en iyi mücevhercisi olacak -
Bu saçmalığa bir yıl boyunca nasıl katlanırım, böyle bir eziyetle nasıl yaşarım?...
Bu ne biçim ustalık?...Ustalık kaprisi yapacaksa bari başından yapmasaydı..
Devamlı söyleniyor, her önüne gelene ustadan yakınıyor, ama avucunu açmıyordu. Avucu kapalı uyuyor, 
Böylece bir yıl geçti, her günkü zorluklarla dolu, her gecesi yarım uykuyla yaşanmış bir yıl
Ve o gün geldi. Genç tam bir yıl sonra büyük ustanın karşısına çıktı. Usta onu bir süre bekle'
"""

# Kontrol edelim.

"""
DECLARE @CUMLE AS varchar(MAX)
SET @CUMLE='Delikanlı evine döndü, kendisini merakla bekleyen annesiyle babasına neler olduğunu anlattı.
Anlattıkça anlattı da kendine çok anlamsız gelen bu hareketi soğuk konuşması nedeniyle
kızdığı ustaya
Nasıl olurda böyle budalaca bir şey yapmamı ister-
Birde ülkenin en iyi mücevhercisi olacak -
Bu saçmalığa bir yıl boyunca nasıl katlanırım, böyle bir eziyetle nasıl yaşarım?...
Bu ne biçim ustalık?...Ustalık kaprisi yapacaksa bari başından yapmasaydı..
Devamlı söyleniyor, her önüne gelene ustadan yakınıyor, ama avucunu açmıyordu. Avucu kapalı uyuyor, 
Böylece bir yıl geçti, her günkü zorluklarla dolu, her gecesi yarım uykuyla yaşanmış bir yıl
Ve o gün geldi. Genç tam bir yıl sonra büyük ustanın karşısına çıktı. Usta onu bir süre bekle'


select @CUMLE
"""

# Yukarda artık bir kere atadıktan sonra @CUMLE üzerinden işlem gerçekleştirebilirim.
# Örneğin Delikanlı yazısını Genç ile replace ettireyim.

"""
DECLARE @CUMLE AS varchar(MAX)
SET @CUMLE='Delikanlı evine döndü, kendisini merakla bekleyen annesiyle babasına neler olduğunu anlattı.
Anlattıkça anlattı da kendine çok anlamsız gelen bu hareketi soğuk konuşması nedeniyle
kızdığı ustaya
Nasıl olurda böyle budalaca bir şey yapmamı ister-
Birde ülkenin en iyi mücevhercisi olacak -
Bu saçmalığa bir yıl boyunca nasıl katlanırım, böyle bir eziyetle nasıl yaşarım?...
Bu ne biçim ustalık?...Ustalık kaprisi yapacaksa bari başından yapmasaydı..
Devamlı söyleniyor, her önüne gelene ustadan yakınıyor, ama avucunu açmıyordu. Avucu kapalı uyuyor, 
Böylece bir yıl geçti, her günkü zorluklarla dolu, her gecesi yarım uykuyla yaşanmış bir yıl
Ve o gün geldi. Genç tam bir yıl sonra büyük ustanın karşısına çıktı. Usta onu bir süre bekle'

select @CUMLE=REPLACE(@CUMLE, 'Delikanlı','Genç')
select @CUMLE
"""

#"Evine" yazan yere "Yuvasına" yazalım.

"""
DECLARE @CUMLE AS varchar(MAX)
SET @CUMLE='Delikanlı evine döndü, kendisini merakla bekleyen annesiyle babasına neler olduğunu anlattı.
Anlattıkça anlattı da kendine çok anlamsız gelen bu hareketi soğuk konuşması nedeniyle
kızdığı ustaya
Nasıl olurda böyle budalaca bir şey yapmamı ister-
Birde ülkenin en iyi mücevhercisi olacak -
Bu saçmalığa bir yıl boyunca nasıl katlanırım, böyle bir eziyetle nasıl yaşarım?...
Bu ne biçim ustalık?...Ustalık kaprisi yapacaksa bari başından yapmasaydı..
Devamlı söyleniyor, her önüne gelene ustadan yakınıyor, ama avucunu açmıyordu. Avucu kapalı uyuyor, 
Böylece bir yıl geçti, her günkü zorluklarla dolu, her gecesi yarım uykuyla yaşanmış bir yıl
Ve o gün geldi. Genç tam bir yıl sonra büyük ustanın karşısına çıktı. Usta onu bir süre bekle'

select @CUMLE=REPLACE(@CUMLE, 'Delikanlı','Genç')
select @CUMLE=REPLACE(@CUMLE, 'Evine','Yuvasına')
select @CUMLE
"""
# Bu arada Evine yazarken küçük de yazabilirim. Çünkü biz kurarken büyük küçük harfe
# ...duyarsız olacak şekilde kurmuştuk.

# Soru : Bu cümlenin içerisinde kaç tane nasıl kelimesi geçiyor?
# Videoyu durdurup düşünün. Bunu SQL sorgusuyla nasıl getirebilirim.
# Aslında basit bir yolu var

"""
select LEN(@CUMLE)
"""
# Cümlemin uzunluğu: 745 karaktermiş. Ben bunun içerisinden nasıl kelimelerini temizlersem.
# Yani boşlukla yer değiştirirsem...

"""
DECLARE @CUMLE AS varchar(MAX)
SET @CUMLE='Delikanlı evine döndü, kendisini merakla bekleyen annesiyle babasına neler olduğunu anlattı.
Anlattıkça anlattı da kendine çok anlamsız gelen bu hareketi soğuk konuşması nedeniyle
kızdığı ustaya
Nasıl olurda böyle budalaca bir şey yapmamı ister-
Birde ülkenin en iyi mücevhercisi olacak -
Bu saçmalığa bir yıl boyunca nasıl katlanırım, böyle bir eziyetle nasıl yaşarım?...
Bu ne biçim ustalık?...Ustalık kaprisi yapacaksa bari başından yapmasaydı..
Devamlı söyleniyor, her önüne gelene ustadan yakınıyor, ama avucunu açmıyordu. Avucu kapalı uyuyor, 
Böylece bir yıl geçti, her günkü zorluklarla dolu, her gecesi yarım uykuyla yaşanmış bir yıl
Ve o gün geldi. Genç tam bir yıl sonra büyük ustanın karşısına çıktı. Usta onu bir süre bekle'


select Len(@CUMLE)
SET @CUMLE=REPLACE(@CUMLE,'Nasıl','')
select LEN(@CUMLE)
"""

# 745 ten 730 a düştü

"""
select (745-730)/5
"""

# Nasıl kelimesi 5 harfli olduğu için 5 e böldüm. 
# şimdi değişken tanımlamayı öğrendik.
# bir değişken daha tanımlayalım buraya

"""
DECLARE @CUMLE AS varchar(MAX)
SET @CUMLE='Delikanlı evine döndü, kendisini merakla bekleyen annesiyle babasına neler olduğunu anlattı.
Anlattıkça anlattı da kendine çok anlamsız gelen bu hareketi soğuk konuşması nedeniyle
kızdığı ustaya
Nasıl olurda böyle budalaca bir şey yapmamı ister-
Birde ülkenin en iyi mücevhercisi olacak -
Bu saçmalığa bir yıl boyunca nasıl katlanırım, böyle bir eziyetle nasıl yaşarım?...
Bu ne biçim ustalık?...Ustalık kaprisi yapacaksa bari başından yapmasaydı..
Devamlı söyleniyor, her önüne gelene ustadan yakınıyor, ama avucunu açmıyordu. Avucu kapalı uyuyor, 
Böylece bir yıl geçti, her günkü zorluklarla dolu, her gecesi yarım uykuyla yaşanmış bir yıl
Ve o gün geldi. Genç tam bir yıl sonra büyük ustanın karşısına çıktı. Usta onu bir süre bekle'

declare @len1 as INT
set @LEN1=LEN(@CUMLE)
declare @len2 as INT
set @CUMLE=REPLACE(@CUMLE,'Nasıl','')
set @LEN2=LEN(@CUMLE) # nasıllar temizlendikten sonra mevcut uzunluğunu aldırıyor

select (@LEN1-@LEN2)/LEN('Nasıl')
"""


#%%11. video - Ders sonu -SORULAR

"""
1.ASCII,CHAR, ..... fonksiyonları ne işe yarar nasıl kullanılır, nerede kullanılır?

"""