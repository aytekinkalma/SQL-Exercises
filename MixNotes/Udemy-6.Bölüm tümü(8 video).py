# 6. Bölüm
# 1. Video - İlişkisel veritabanı oluşturma
"""
Bu zamana kadar SQL dilinin temellerini öğrendik. Daha önce tek bir tablo üzerinde,
bütün verilerin tekrar ettiği tek bir tablo üzerinde durduk. Şimdi gerçek bir sistem 
üzerinde bu iş nasıl yürüyor. Gerçek bir veritabanı nasıl tasarlanır ve önceki 
senaryolarda tek tablodan çekmiş olduğumuz örnekler ilişkisel veritabanlarında
(birden fazla tablonun olduğu veritabanlarında) nasıl çekilir bunu göreceğiz.
İlişkisel veritabanı modern veritabanı mimarilerinin temelidir.(son 20-30 yıldır
kullanılan veritabanları rdms özelliğini desteklemektedir)

Buradaki örnek bir e-ticaret sistemi olacak.
Hepimiz internet üzerinden alışveriş yapıyoruz. Üye oluyoruz. Sonra Login oluyoruz.
Kullanıcı seçtiği ürünleri sepete ekler - ödeme ekranına geçer - adresi seçer
sonra ürün faturası kesilerek kargoya verilir son kullanıcıya gider.
Bu süreç geri planda nasıl işliyor. Bunu öğreneceğiz.
"""
#%% 2. Video - Veritabanı Oluşturma - 1
# ilk yapacağımız şey ne olacak.
# 1. KULLANICI SISTEME LOGIN OLUR
# Yani benim 1 tane kullanıcı tablomun olması lazım.
# Yeni kullanıcı kayıt olurken bu tabloya kayıt eklenmesi
# Mevcut kullanıcı login olurken de kullanıcı adı ve şifre kontrolü yaparken,
# ... bu tabloda olup olmadığına bakılması.
# Sonuç olarak burada benim 1 tane kullanıcı tablom olması lazım.
# Bunu bir excel formatında oluşturalım.
# Exceli açıyoruz.

# Sol üst kutucuğa USER_ yazdık(USER normalde "dedike" edilmiş kelime. SQL de
# ...yazarken normalde sorun olmaz ama renkler vs ler karışabilir o yüzde USER ın sonuna
# ... bi tane (alttire)_) yazdık)
# otomatik artan bi bölümümüz olması gerekir. ID diyelim
# USER ın altına ID yazdık. ID nin yanına(sağına) INT yazdık
# ID altına USERNAME_ . sağına VARCHAR(50)
# USERNAME_ altına PASSWORD_ . sağına VARCHAR(50)
# PASSWORD_ altına NAMESURNAME . sağına VARCHAR(100)
# EMAIL. VARCHAR(100)
# GENDER. VARCHAR(1)
# CREATEDDATE. DATETIME
# BIRTHDATE. DATE
# TELNR1. VARCHAR(15)
# TELNR2. VARCHAR(15)


# Şimdi kullanıcı tablomu oluşturdum. Kullanıcımla ilgili bilgileri burada tutuyorum.
# Kullanıcı sisteme kayıt olduktan sonra Adres-Telefon-Email gibi bilgileri sisteme
# .. kayıtlıdır. AMA;

# Şimdi yukarda adres yazmadık çünkü mesela tel no çok sık değişen bir şey değil.
# .. ama adres için şunu söyleyebiliriz. Kişi ürünü evine - işine - arkadaşının adresine
# .. eşinin işyerinin adresine vs isteyebilir.
# O yüzden adresin farklı bir tabloda tutulması benim için çok daha faydalı.
# e-ticaret sitelerinde mantık budur. Siz adres seçersiniz oradan hangisine isterseniz.
# Eğer orada değilse istediğiniz adres bi adres daha eklersiniz.
# Adresler için farklı bir tablo tutmak ihtiyaçtır.

# Şimdi ADRESS isimli bir tablo tutalım. Altına
# ID -- INT
# COUNTRY - varchar(100)
# CITY - varchar(100)
# TOWN - varchar(100)
# DISTRICT - varchar(100)
# POSTALCODE - varchar(10)
# ADRESSTEXT - varchar(250)

# Şimdi bu adress tablosu iyi bilgileri girdik ama kullanıcı ile nasıl bağlanacak ?
# Bi sütun daha ekleyip name surname le bağlayabilirim.Ama aynı isim soyisime sahip insanlar?
# Tamam username yapayım. Ama bu da değişebilir. Hiç bir şekilde tekrar etmeyecek 
# .. ya da değişmeyecek bir şey bulmalıyım. Bu da ID alanıdır. ID lerin hepsi farklıdır.
# O zaman oradaki sütuna USERID diyip ID ye 1 yazdığım zaman Ömer Çolakoğlunun
# ... bilgilerini getirir.
# Ömer Çolakoğlunun bilgilerini ve yanına da adres bilgilerini getirmek istediğim zaman
# ... ne yaparım ? (Yani ilk USER tablosunun sütunlarının yanına Adress bilgilerini
# ... de getirmek istiyorum.
# En sona diyelim ki ADRESSTEXT  sütununu getirdim diyelim.
# Bana kullanıcı bilgisini adresiyle çek dediği zaman.
# Önce USER bilgilerini çekicem.
# ADRESS den de USERID si 1 olan adres bilgilerini getiricem
# Kolon isimlerinden de hangisini istiyorsam(ADDRESSTEXT) onu USER tablosunun yanına
# ... yazdıracağım.
# Böylelikle bir veri tekrarının önüne geçeriz.
# Temel anlamda ilişkisel veritabanı mimarisi bu şekildedir.

# USER tablomuz bizim MASTER(ANA) tablomuzdur. Çünkü ID alanı hiç tekrar etmediği
# ... için benim için master dır.
# ADRRESS tablomuzda birden fazla adress olacağı için tekrar edebilir.
# ...ve bu şekilde aralarında bir bağlantı vardır.
# ADRESS tablosuna biz DETAIL(DETAY) tablosu diyoruz.
# Şimdi başka tablolar oluşturarak veritabanımızı oluşturmaya devam edelim.


#%% 3. Video - Veritabanı Oluşturma - 2

# Burada ADRESS tablosuna bakacak olurrsak country, city(81 şehir), town(20 ilçe) , 
# district gibi string alanlar var burada.
# Burada her bir Istanbul şehri için tekrar ettiğini düşünecek olursak,
# ...ve bizim 1 milyon müşterimiz varsa ve her müşterimizin ortalama 3 tane
# .. adresi varsa ve her birinde istanbul şehri tekrar edecek.
# .. aynı şey ilçe ve semt içinde geçerli.
# Bu bizim için fazladan bir veri tutmak demektir. ya da 
# yanlış yazılan "İstanbul" yerine "Istanbul" yazılması ..
# Oysa burada master olan şey nedir. Şehir bilgisidir.
# Ben burada city yi varchar olarak yazmaktansa başka bir tablodan tutsam getirsem
# COUNTRY diye 3. bir tablo oluşturalım altına ID- int Identity(1,1)(integer),
# ... COUNTRY - varchar(100)
# CITY diye 4. bir tablo oluşturalım altına ID- int Identity(1,1)(integer) (Buradaki,
# identity(1,1) = 1 den başlayıp 1 er 1 er artsın anlamında) ,CITY - varchar(100)
# ve ben artık ADRESS tablomdaki COUNTRY ve CITY yerlerine, COUNTRYID ve CITYID yazıyorum.
# ve bunların veri türü de "int" olacaka
# Aynı şekilde TOWN diye bir tablo oluşturalım. ADRESS tablosunda TOWNID olsun.(Türü "int")
# Aynı şekilde DISTRICT için yapalım.

# Yani COUNTRYID ile COUNTRY tablosundaki ID 
# CITYID ile CITY tablosundaki ID
# TOWNID ile .....
# .....bağlantılı olsun.
# USER_ tablosundaki ID ile de ADRESS tablosundaki USERID bağlantılı olsun.
# Temel anlamda 6 tane tablomu oluşturdum(USER_, ADRESS, COUNTRY,CITY,TOWN,DISTRICT)
# ... ve birbirine bağladım. Şimdi uygulamamıza geçelim.

# Bizim 1. maddemiz neydi # 1. KULLANICI SISTEME LOGIN OLUR
# 2.KULLANICI SEÇTİĞİ ÜRÜN YA DA ÜRÜNLERİ SEPETE EKLER
# Sepete eklemeden önce bi ürün listemiz olacak. Yani benim malzemeyi tanımlayan
# ... bir tablom olması lazım.
# Bu tablomada "ITEM" diyorum.
# Bununda bir ID si var - int IDENTITY(1,1)
# ITEMCODE - varchar(20)
# ITEMNAME - varchar(100)
# PRICE - FLOAT
# Bu arada bu ürünü genelde kategoriler altında değerlendiririz.
# CATEGORY1 - varchar(50)
# CATEGORY2 - varchar(50)
# CATEGORY3 - varchar(50)
# Şimdilik ürünün bu bilgileri yeterli. Bu tabloda herhangi bir bağlantı yok.
# Yapmaya çalıştığımız neydi. "Kullanıcı seçtiği ürün ya ürünleri sepete ekler"
# USER_ tablomuzda Kullanıcı bilgileri var(ID(USER_ daki)),
# ... ITEM dan da ürün bilgim var(ID(ITEM))
# Bu bilgiler birleşip bi sepet oluşturacak.
# Biz bi sitede ürünü sepete ekle diyince ürünü spete ekliyor.
# Başka bir ürün ekleyince sepette 2 tane ürün oluyor.
# vs vs.
# Sepetimde toplam 981 tl dedi 3 ürün olsun. Sepete tıkladığımda detayları görüyorum.
# Aynı mantıkta yapacağız.Sepet dediğimiz şey bana ait olan bir yapı bi de içinde malzemeler
# .. var. Benim bi tane BASKET tablom olacak kullanıcının bilgilerini tutan.
# .. bi de BASKETDETAIL tablosu olacak. İçerde ürünleri tutacak.

# BASKET tablosunu oluşturalım.
# ID - int indentity(1,1)
# Bunu USER_ daki ID ile bağlayacağım o yüzden,
# USERID - int 
# CREATEDDATE - DATETIME
# LASTMODIFIEDDATE - DATETIME
# ITEMCOUNT - INT (ÜRÜN sayısı)
# TOTALPRICE - FLOAT
# STATUS_ -  int
# Şimdi Status un integer ı 0-1-2 değerlerini alacak.
# Siparişe çevrilmedi - ödemesi yapılmadı = 0
# Siparişe çevrildi - ödemesi yapılmadı = 1
# Siparişe çevrildi - ödemesi yapıldı = 2

# Bi de BASKETDETAIL tablom var. Bunun da otomatik artan bi alanı olacak.
# ID - int identity(1,1)
# Bu da BASKETID olacak (BASKET - ID ile bağlı) - int
# ITEMID - INT
# AMOUNT - FLOAT (Sepetin içerisinde kaç tane olduğunu yazıyorduk o yüzden AMOUNT yazdık)
# Not: bu ondalıklı rakam olabilir. Her zaman adet gibi düşünmeyin.
# PRICE - FLOAT (Birim fiyat)
# TOTALPRICE - FLOAT
# Birde sepete eklenme tarihi..,
# DATE - DATETIME

# Burada neler bağladık. USER_-ID ile BASKET-USERID yi bağladık.
# BASKET-ID ile BASKETDETAIL-BASKETID yi bağladık.
# ITEM - ID ile BASKETDETAIL- ITEMID alanını bağladık.

# Şimdi ITEM kısmındakileri excel de sütuna çevirelim bir kaç bilgi girelim.
# (Önceden USER tablosu ve ADRESS tablosu bilgilerini girmiştik)
# ID = 1 olsun
# ITEMCODE = p1551242
# ITEMNAME = Dior SAUVAGE EDT 100 ml
# PRICE = 509
# CATEGORY1 = Kozmetik
# CATEGORY2 = Parfüm&Deodorant
# CATEGORY3 = Parfüm

# Bi tane daha ürün ekleyelim

# ID = 2 olsun
# ITEMCODE = p7281242
# ITEMNAME = Dufy Gömlek
# PRICE = 20
# CATEGORY1 = Giyim
# CATEGORY2 = Erkek Giyim
# CATEGORY3 = Gömlek

# Böyle binlerce ürün olabilir. Şimdi sepete ekleme işine bakalım.

# BASKET tablomu da atalım 4. olarak.
# BASKET da neler var
# ID = 1
# USERID = 1
# CREATEDDATE = 11-10-2018 12:11
# LASTMODIFIEDDATE = 11.10.2018 12:15
# ITEMCOUNT = 1
# TOTALPRICE = 509
# STATUS_ = 0 (Yani siparişe çevrilmedi)

# Sonra BASKETDETAIL tablomu getireyim.
# ID = 1
# BASKETID = 1
# ITEMID = 1
# AMOUNT = 1
# PRICE = 509
# TOTALPRICE = (AMOUNT) x (PRICE) = 529 
# DATE_ = 11.10.2018 12:11

# Başka bi ürün daha ekleyelim.
# ID = 2
# BASKETID = 1
# ITEMID = 2
# AMOUNT = 2
# PRICE = 20
# TOTALPRICE = (AMOUNT) x (PRICE) = 40 
# DATE_ = 11.10.2018 12:13 (2 dk sonra eklemiş olayım)

# En sonra toplam fiyatım yani BASKET tablosundaki PRICE = 549 tl olacak
# ITEMCOUNT da 2 olmuş olacak.
# Sepete ekleme işide bu şekilde.
# Bir sonraki aşamada ödemesini gerçekleştiricem. Daha sonra 
# Sipariş oluşacak ve ilgili kişilerin önüne yeni bir sipariş olarak düşecek.

#%% 4.VIDEO - Veritabanı oluşturma 3
# 3. aşama ÖDEME GERÇEKLEŞTİRME

# SEPETE GİT - ÖDEMEYE GEÇ- ÖDEME SEÇENEKLERİ VAR ORADA(n11.com)
# Kredi kartı ile ödeme yapmak istiyorum. 
# Bilgileri giriyorum.
# Bu sırada sistem benim kredi kartı bilgilerimle ssl üzerinden ödemeyi gerçekleştiriyor.
# Sonra ÖDEMELER tablosuna bu kayıtla ilgili bilgiyi gönderiyor.
# Eğer bir hata alırsa "limit yetersiz" gibi. Hata olarak logluyo. Almazsa;
# İşlem gerçekleşmiştir diyerek kredi kartından gelen onay koduyla kayıt gerçekleştiriyor.
# Bundan sonra sistem STATUS ü 1 olarak güncelliyor(Önceden 0 dı)
# Daha sonra SİPARİŞ tablosuna benim sepetimdeki kayıtları atıyor.
# Attıktan sonra otomatik olarak BASKET tablomdaki STATUS ü 2 ye çevrildi olarak işaretliyor.

# Şimdi PAYMENT tablosuna bakalım
# ID - int - identity(1,1)
# BASKETID - int (Ödeme bilgisinin hangi sepet üzerinden gerçekleştirildiğini bulmak için)
# TOTALRPICE - FLOAT (fiyatı ne kadar tuttu)
# PAYMENTTYPE - int (Kredi kartı = 1, Akbank Direct = 2 , Garanti=3...)
# ... Biz default olarak Kredi kartı kullanacağız.
# İşlem tarihi .. DATE - DATETIME
# ISOK - BIT (ödeme sonrası onay kodu geldi mi? IS OK? -- türü BIT(BOOLEAN))
# APPROVECODE - varchar(20) (Onay kodu)
# ERROR_ - varchar(1000) (1000 çünkü uzun bir hata mesajı geliyor olabilir.)

# PAYMENT tablomda bu şekilde.
# Bunu da ekleyelim şimdi yazılanları (ID, BASKETID,...) sütun yapalım. Örnek yapalım.
# ID = 1
# BASKETID = 1
# TOTALPRICE = 549
# PAYMENTTYPE = 1
# DATE_ = 11.10.2018
# ISOK = 1 (Ödeme hatasız gerçekleşti- TRUE)
# APPROVECODE =2821952
# ERROR = (BOŞ) (BU alan boş çünkü herhangi bi hata gerçekleşmedi.)

# Bu arada ödeme gerçekleştiği için BASKET tablomdaki STATUS = 1 olarak güncellenecek.
# Bundan sonra sepet bittiği için bu kullanıcı adına otomatik olarak bir sipariş açılacak.
# Sonra Faturasıyla birlikte sevkedilecek.
# Bunun için bi tanede sipariş tablosuna ihtiyacım var. ORDER-BASKET tablomla aynı şekilde
# Farklı olarak BASKETID var.

# ORDER
# ID - int identity(1,1)
# USERID - int
# BASKETID - int
# CREATEDDATE - datetime
# ITEMCOUNT - int
# TOTALPRICE - float
# STATUS_  - int

# Birde ORDERDETAIL var
# ID - int identity(1,1)
# ORDERID - int
# BASKETDETAILID - int (BASKETDETAIL tablosunun hangi satırına denk geliyor. O bilgiyi tutuyor.)
# ITEMID - INT
# AMOUNT - float
# PRICE - float
# TOTALPRICE - float
# DATE_ - datetime


# Şimdi bu kaydı da ekleyelim. ORDER
# ID = 1
# USERID = 1
# BASKETID = 1
# CREATEDDATE = 11.10.2018 12:25
# ITEMCOUNT = 2 (2 tane malzeme var)
# TOTALPRICE = 549
# STATUS_  = 2 (Ödemesi gerçekleşti)

# Bide ORDERDETAIL i var bunun. (BASKETDETAILDAN 1. satıra bakarak doldurduk)
# Ne-Neye denk geliyor diye bakarak.
# ID = 1
# ORDERID = 1
# BASKETDETAILID = 1
# ITEMID = 1
# AMOUNT = 1
# PRICE  = 509
# TOTALPRICE = 509
# DATE_ = 11.10.2018 12:25

# Yine 2. satırı dolduralım
# ID = 2
# ORDERID = 1
# BASKETDETAILID = 2
# ITEMID = 2 (ikinci item)
# AMOUNT = 2
# PRICE  = 20
# TOTALPRICE = 40
# DATE_ = 11.10.2018 12:25 (Tarih aynı)

# Baştan ne yaptık bakalım.
# Ürünleri sepetime ekledim.
# Sepetime eklediğim ürünlerin ödemesini gerçekleştirdim.
# Sepetime eklediğim ürünlerin sipariş ve siparişsatırlarının tutulduğu,
# ... ORDER ve ORDERDETAIL tablolarına kayıt attım.
# ve son aşamada artık bu hale gelen ürünler mağazaların önüne düştü.
# ... (Artık sen bunları sevketmelisin diye)
# Son olarak da ne kalacak. Sistemin bana fatura kesmesi kalacak.
# Bunun içinde bir FATURA tablomuz olmalı

# INVOICE tablomuz
# ID - int identity(1,1)
# ORDERID - int
# INVOICENO - varchar(50)
# DATE_ - DATETIME (Faturanın kesildiği tarih.)
# CARGOFICHENO(FAturayı kargoya bir fiş numarasıyla veriyoruz) - varchar(50)
# STATUS - int (Ben ürünü gönderdikten sonra faturayı kabul etti ya da iade etti)

# Bi de faturanın satır bilgilerini tuttuğum yer.INVOICEDETAIL
# ID - int identity(1,1)
# INVOICEID - int (Hangi faturanın satırı olduğu bilgisi)
# ORDERDETAIL - int (Hangi siparişin satırı olduğu bilgisi)
# ITEMID - int (Hangi malzeme)
# AMOUNT - float
# PRICE - float
# TOTALPRICE - float

# Şimdi burada akla şu soru gelebilir ORDERDETAIL ı tekrardan burada tekrar ettirmenin
# ... ne anlamı var. Evet sistem performansı açısından doğru değil fakat resmi
# ... işlemlerde asıl olan şey fatura olduğu için siparişi düzeltmeden faturayı 
# ... düzeltmemiz gereken işlemler olabilir.

# Şimdi bununda bilgilerini girelim. INVOICE
# ID = 1
# ORDERID = 1
# INVOICENO = INV001
# DATE_ = 12.10.2018 15:25:00(Ürün ertesi gün gönderiliyor olsun)
# CARGOFICHENO = KRG001
# STATUS = 0 (Buradan çıktı)

# Bi de bunu detayları var. INVOICEDETAIL
# ID = 1
# INVOICEID = 1
# ORDERDETAIL = 1
# ITEMID = 1
# AMOUNT = 1
# PRICE = 509
# TOTALPRICE = 509

# 2. satır için.
# ID = 2
# INVOICEID = 1
# ORDERDETAIL = 2
# ITEMID = 2
# AMOUNT = 2
# PRICE = 20
# TOTALPRICE = 40

# Kullanıcı bu ürünü teslim aldım dediğinde INVOICE daki STATUS alanı 1 olarak değişecek.
# Üründe problem var dediğinde 2 olarak değişecek (iade anlamında)

# Genel olarak veritabanı tasarımımız excel üzerinde bu şekilde. SQL serverda nasıl yapacağız
# Buna bakalım.

#%%5.VİDEO- Veritabanı oluşturma 4

# Bu tablo ve alanları SQL serverda oluşturalım.
# ETRADE - Tables -New table - Tabloları sırayla oluşturalım. Önce USER_
# Bu arada tasarımı önce excelde yaptık. Çünkü değişiklikle yapmak genel yapıyı
# ... oluşturmak için. SQL de bu daha zor olurdu.
# SQL de önce hoca tek tek girdi ID- int , USERNAME - ... vs diye
# Peki bunu excelden almanın bir yolu var mı ?
# Bunun için şunu düşünmeliyiz önce. SQL sadece SQL dilinden anlar.
# Buraya ben new table dan sonra ID-int falan yazdım ama aslında SQL arka planda
# .. kodu otomatik yazıyor. Peki nasıl?
# USER ın üzerine sağ tıkla - Script Table As - Create to - New Query Editor Window
# ... a tıkladığımız zaman aşağıda CREATE TABLE metoduyla bir tablo yapılmış 
# Ben bunu excelden yaparsam... (Sonra exceldeki CREATE TABLE kodlarını ve altını kodları incele)

# Sonra o sütünu komple kopyalayıp çalıştırdığımda . tables a gelip refresh dersem.
# Tablom artık görünür hale gelecek ve ID yi primary key yapacak.(Aşağıdaki kod)
# NOT: Excell de neden ID - int identity(1,1) şeklinde yazdığımızı anlamış olduk.

"""
CREATE TABLE USER_(
ID INT IDENTITY(1,1),
USERNAME_ VARCHAR(50),
PASSWORD_ VARCHAR(50),
NAMESURNAME VARCHAR(100),
EMAIL VARCHAR(100),
GENDER VARCHAR(1),
CREATEDDATE DATETIME,
BIRTHDATE DATE,
TELNR1 VARCHAR(15),
TELNR2 VARCHAR(15)
CONSTRAINT [PK_USER_] PRIMARY KEY CLUSTERED (ID ASC))
"""
# Excel de sonra sadece tablo isimlerini değiştireceğiz diğer tablo isimlerini yazacağız.
# Yani en üstteki USER olan yeri "A1" yerine artık "D1" deki ADRESS yapıyorum(MESELA)
# Aynı şekilde altta yazan USER yerini de.

# Yani bu şekilde bu tabloların create scriptlerini oluşturarak SQL serverda bu tabloları
# ... oluşturabilirim.
# Bu arada yukardaki kodu gidip excell de ADRESS tablosunun yanına yapıştırırsam
# ... Adress tablosundaki bilgilere göre kodu yazıyor kendisi yani yukardaki kodu
# ... yapıştırıyoruz ama aşağıdaki tablo oluşuyor otomatik.

"""
CREATE TABLE ADDRESS(
ID INT IDENTITY(1,1),
COUNTRYID INT,
CITYID INT,
TOWNID INT,
DISTRICTID INT,
POSTALCODE VARCHAR(10),
ADDRESSTEXT VARCHAR(250),
USERID INT,
CONSTRAINT [PK_ADDRESS] PRIMARY KEY CLUSTERED (ID ASC))
"""

# Sonra bunların hepsini SQL e yazıp çalıştırıyoruz.
# ORDER da sıkıntı çıkardı kod çünkü ORDER dedike bi kelime o yüzden ORDER_ 
# ...şeklinde yazıyoruz.
# Tüm tabloları doldurduktan sonra artık tabloların içini doldurup sorgular yazmaya
# ... başlayalım.


#%%6.Video- Veri Oluşturma - 1

# Bunları kodla excelden çektik ama el alışkanlığı olması adına
# SQL new table a bas ve tek tek tabloları oluştur ID- int ... gibi
# Hoca bunu tavsiye ediyor.
# Hoca: ben gerçek bir data oluşturdum. Bundan sonra SQL sorguları yazmaya başlayacağız.
# Yeni datayı restore edip, o data üzerinde çalışmaya başlayacağız.
# Mevcut database imizi siliyoruz. (close existing connections ı işaretleyerek)

# Databases sağ tıkla - restore database - device- [...] - add - 

# COUNTRY için TÜRKİYE yi aldım (Hoca)
# 53.145 tane semt(DISTRICT) varmış. (Burada TOWNID ile bağlı (diğerlerine))
# 957 tane ilçe(TOWN) varmış.
# Hoca : DISTRICTSTREET i de internetten buldum Türkiyedeki sokakların mahallelerin yazdığı
# Bunun üzerinden birazdan random adresler, random veriler oluşturacağız.
# INVOICE ve INVOICEDETAIL tablolarımın içi boş şu anda
# ITEM tablom var
# ITEMCATEGORY VAR ama bunu kullanmayacağız.
# PASSWORDLIST kullanıcılara random şifre oluşturmak için kullandığım bir tablo
# PAYMENT içi boş
# Bir de USER bölümümüz var burası önemli. 10000 tane kullanıcı açtık sisteme
# USER- CREATEDDATE . kullanıcının sisteme giriş tarihi (Bilgiler tamamen sallamadır.)
# username i ve email i isim soyisimi kullanarak oluşturdum.
# Sistem üzerinde canlı çalışabileceğimiz 10000 tane kullanıcımız var.
# Her kullanıcı için de bir den fazla adres oluşturdum.
"""
WHERE USERID = 1
"""
# 1 nolu kullanıcı(Nazlıcan Özsimitçi) için 4 tane adres tanımlamışım.
# 2 nolu kullanıcının mesela 1 tane adresi varmış.
# Toplamda bakalım

"""
select count(*)
from [ETRADE2].[dbo].[ADDRES]
"""
# Toplamda 10000 kullanıcı vardı. 24945 tane adres varmış.
# Şimdi bi script imiz var. onu yazarak rasgele satışlar gerçekleştireceğiz.
# Yani- sepete ekleme- ödeme gerçekleştirme- siparişe ekleme- faturasını kesme (Rasgele)

#%%7.Video - Veri Oluşturma 2
# Yavaş yavaş kod yazma kısmına geliyoruz ama bizim neye ihtiyacımız var, dataya ihtiyacımız var.
# Örnek sipariş örnek satış örnek malzeme gibi datalar oluşturacağız rasgele olarak.
# Hocanın  yazdığı Script tam da bu işi yapıyor.
# Script: Birden fazla sql komutunun bir arada kullanıldığı komutlar bütünü.
# Bu komut şunu yapıyor.
# Rasgele bir kullanıcı seçiyor. rasgele bir zamanda sepetine ürün ekliyor
# ...sepetine eklediği ürün sayısı da rasgele (3 tane de ürün alabilir 5 tane de)
# Sonra bir kaç dakika sonrasında PAYMENT tablosuna kayıt atıyor.
# Otomatik olarak da sipariş tablolarını oluşturuyor.
# Sonrasında yine bir kaç gün sonra(bu bir kaç gün de random olarak belirleniyor)
# ...ürünün faturasını kesiyor - ürünü müşteriye sevk ediyor.

# Şu an BASKET, BASKETDETAIL,PAYMENY,ORDER,ORDERDETAIL,INVOICE,INVOICEDETAIL
# ... tablolarımın içi boş ve hiç bir kayıt yok.
# ve ben sadece 1 tane sepet ekle oluşturmak istiyorum.
# Script imi çalıştırıyorum.
# Sonra tekrar bakıyorum BASKET ın içine falan. sepet te 1 tane ürünüm var.
# .(1278 NOLU kullanıcı rasgele geldi)
# Burada teyit edelim bakalım hangi user a bağlanmış.
"""
select * from USER_ WHERE ID = 1278
"""
# Tuana Köle isimli kullanıcı
# Sepete neler eklemiş bakalım.
"""
select * from BASKETDETAIL
"""
# 9 tane ürün var. Toplamları 178.75 tl lik ürün satın almış. Bu kadarlıkta 
# ...ödeme gerçekleştiriyor olması gerekiyor
"""
select * from PAYMENT
"""

# ISOK=1 onay gelmiş.
# Sipariş tablosuna bakalım

"""
select * from ORDER
"""
# 1 tane sipariş var . Şimdi ADDRESSID den bakalım bu sipariş nereye gidiyormuş?
# ADRESSID = 3169 burada (Rasgele)

"""
select * from ADDRES WHERE ID =3169
"""

# ORDERDETAIL da BASKETDETAIL in aynısı var
# INVOICE da 
# 3 gün sonra ürün kargoya verilmiş (random bunlar hep). STATUS = 1

# Ürünlerden bir tanesine de bakalım hangi ürünmüş(Örnek olsun diye bakalım)

"""
select * from ITEM WHERE ID = 13454
"""

# Perwoll yenilenen siyahlar 450 ml ....

# Bu şekilde siparişi geçilmiş ve sevkedilmiş şekilde tüm operasyonlarını gerçekleştirmiş olduk.
# Şimdi yavaş yavaş SQL cümlelerimizi yazmaya ve rdms kullanmaya başlayabiliriz.

#%%8. video- Sorular

"""
1.İlişkisel veritabanı ne demektir?(RDMS)
2.RDMS sistemine sahip bir yapı temel anlamda nasıl çalışır?(Fatura örneğinden bahsetmiştik
... onun mantığını anladık mı ? soru bu)
3.Bir e-ticaret sistemi temel olarak nasıl çalışır?
4.RDMS bir yapıda veritabanı mimarisi nasıl oluşturulur ?
"""
 











