# 5. Bölüm VERİ TİPLERİ
# 1. Video 

# Tables a sağ tıklayıp new-table dediğimizde yeni tablo ekleyebiliyorduk.
# ID olsun COLUMN name , sayısal bir alan olduğu için, neler olabilir bakalım
# bigint, float, int, real, smallint, smallmoney tinyint
# Bunların aralarındaki farklar ne bunlara bakalım.
# Excel dosyasına bakarsak indirdiğimiz . 
# bigint : -2 üzeri 63 ile 2 üzeri 63 arasında değer alan 8 byte lık değer tutabilen yapılar.

# Müşteri sayım 32000 den büyükse int küçükse smallint , 2.000.000 dan büyükse,
# ... bigint kullanabilirim.

# Şimdi ID dedik. Buna şimdilik int(integer) diyelim. 
# Sonra alttan identity specification-is identity yi yes yapalım.
# Bu arada üstte "Allow Null" ı işaretlersek "boş değer girilmesine izin ver" demek.
# Sağ üstte de anahtar işareti var tıklayalım set primary key i miz olsun bu.

#%% 2. Video - Metin veri tipleri

# Müşterinin başka ad bilgisi olur. Bu string bi alan
# Mesela char olabilir. Parantez içinde ne kadar karakter vereceğimizi düşünelim.
# Bunun için karakter uzunluğuna 100 demek gerekir.
# Başka nchar, ntext olabilir.
# Peki char ile nchar arasındaki fark ne.
# Char: standart karakterler için tuttuğumuz alandır.
# nChar : international karakterler için tuttuğumuz (Arapça,Çince,Latince,İbranice vs)
# ...Yani bizim harflerimiz dışında harfler kullanılıyorsa...
# char : hafızada her bir karakter için 1 byte lık yer tutarken
# nchar: hafızada her bir karakter için 2 bytelık yer tutar.
# text : standart
# ntext: text in international olanı
# text vs char ? : text özellikle SQL 2005 ten sonra desteklenmeyen bir veri türü.
# ...çok kullanışlı değil. Geçmişe yönelik olmasıyla destekleniyor.
# char: max 8000 karakter büyüklüğünde olabilir.
# sql serverda bir satır max 8000 karakter olacak şeklinde tutulabilir.
# örneğin : (varchar(9000) YAZAMAM).
# nchar için 4000 dir sınır mesela . nchar(4500) YAZAMAM.
# Mesela word dosyasında daha çok olacağı için bunu tutmak istersek
# text türünde tutabiliriz ancak bu da artık desteklenen bi şey değil.
# Onun yerine başka özellikler çıkmış durumda.
# Bi de varchar var, nvarchar ı da var. nvarchar international karakterleri destekleyeni.
# varchar da ki durum şu: Biz char karakter tuttuğumuz zaman ben 100 digit demişsem.
# ..100 digitlik yazmasam bile hafızada 100 digitlik tutar.
# Ancak varchar : sadece girdiğim karakter kadar yer tutar.
# Örneğin ispanyolların 200 karakterlik isimleri olabilir. Ona göre oluşturabiliriz.
# varchar vs nvarchar a bakalım.
# varchar(50) vs nvarchar(50) olsun.
# Çince yazdığım zaman varchar türünde olursa SQL onu görmez ( ??? yazar )
# Uluslar arası dil desteği olan uygulama geliştiriyorsanız. Metin yerlerine nchar ,
# ... nvarchar vs yapmalısınız.
# Word dosyası meselesine tekrar gelelim. Alternatif olarak ne yapabiliriz.
# varchar(MAX) yazıp istediğim uzunlukta veri girebiliyorum.
# ANCAK : TEXT  varchar bir alan 900 karakterden büyükse, index işlemi çalışmaz hale geliyor.
#... son limitlerine kadar 1000,2000 vermek doğru değil.
#... Performansı doğru kullanmak istiyorsak en fazla 900 karakter olarak tanımlıyoruz.

#%% 3. Video - ondalıklı sayısal veri tipleri

# Müşterinin borcu var diyelim. Vigüllü olacak bunlar. Neler olabilir.
# float, money, numeric, real, decimal olabilir.
# Aradaki farklara bakalım.
# Örnek decimal(18,0) yapalım veri türünü.
# 1500.388 dersek - bana 1500 yazar bırakır.
# decimal(18,2) deseydim 1500.38 diyecekti.
# buradaki 18 de vürgüldenn önceki sayı sayısı.
# eğer değer tam ise . virgülden sonra otomatik 00 atacaktı.

# money: bunun yerine decimal ya da float kullanılıyor.
# HOCA: bunun pek kullanıldığını görmedim(Bilgi için excele bak)

# float: Yine excele bak.
# float ne girdiysem onu tutar. 187.292312312 desek, aynısını yazar.
# real hafızada 4 byte lık yer tutar yine çok kullanılan bir veri tipi değil.

#%% 4. Video Tarih-saat - veri tipleri

# Müşterinin son hareket tarihi olsun.
# datatype tarihte olabilir. tarih saat de olabilir.
# date olabilir. Bunun içine sadece tarih girebilirim.
# datetime türünde olursa. tarih attığımda otomatik saat bilgisini gösteriyor.
# milisaniyeye kadar girebiliri.
# datetime2 : milisaniyeden microsaniye mertebesine getirdi. daha hassas data tutma
# ... imkanı veriyor.
# time olarak tutabilirim : sadece saat bilgisini getiriyor.
# Genel olarak bu şekilde.(Excel dosyasını inceleyin.)
# Elimden geldiği kadar en çok kullanılanları kullanıyoruz.

#%% 5. Video - Diğer veri tipleri

# geography: dünya üzerindeki kordinat bilgileri.
# geometry : bi takım geometrik şekillerin vektörel olarak şeklini tuttuğumuz veri tipi
# Hoca: bu 2 veri türünü ben hiç kullanmadım..... 
# hierarchyid: Müdür- Şef - Müdür yardımcısı olan bi ortamda bu tip hierarşik yapıları 
# ... tutmamıza yarayan bir veri tipi.
# image : resim jpg gibi formattaki datayı veritabanında tutmak adına 
# ... oluşturulan bir veri türü.
# ... Microsoft bunu önermiyor. Muhtemelen text gibi bu da zamanla kaybolacak.
# ... Onun yerine binary ya da varbinary dediğimiz datayı dosyaları veritabanında 
# ... tutmak adına ki 2 gb a kadar dosyayı tutabilirsiniz.
# xml : aslında string gibi ama xml formatındaki stringleri tutmaya yarıyor.
# ...Bir tablonun içerisinde(bir alanda) tuttuğunuz xml i sorgulayabiliyorsunuz.
# ..Yani tablonun içinde bir alanı xml sorgulayarak kendi içerisinde kıvrımlara 
# ...dökebiliyorsunuz
# uniqueidentifier: Dünya üzerinde öyle unique bir cümle üretmek istiyorsunuz
# ... ki başka örneği olmasın.
# ... Bunu tanımladım diyelim bi kolona. Veri Tipi uniqueidentifier olsun.
# ... select NEWID() yazarsak. unique bi kod gibi bişey çıkar altta.
# ... bi daha çalıştırsam başka bir şey çıkar. hep unique bir şey verir.
# ... Eğer veritabanınızda bu şekilde bir kayıt tutmak istiyorsanız.
# ... Bunun hiç bir yerde eşi benzeri olmasın diye.
# Bu genelde scala verilerini tuttuğumuz yerlerde veriyi sabitlemek adına otomasyon
# ... sistemlerinde kullanılan bir yapıdır. O zaman bu uniqueidentifier ı kullanabiliyoruz.

#%% 6. Video - Şunları bilmeniz beklenmektedir bu bölüm sonunda

"""
1. SQL serverda veritipi kavramı ne demektir.
2. Sayısal veritipleri nelerdir?
3. İnteger, Smallint, bigint,tinyint arasındaki farklar nelerdir?
4. Float, Decimal, Money, veri tipleri arasındaki farklar nelerdir?
5. Varchar, Char, Nchar, Nvarchar arasındaki farklar nelerdir?
6. Hangi veri tipi hafızada ne kadar yer tutar?
7. Hangi veritipini seçeceğimize neye göre karar veririz?
8. Date, Time ve Datetime arasında ne fark bulunmaktadır?
"""
