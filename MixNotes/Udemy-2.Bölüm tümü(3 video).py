# 1.video
# Management studio ya girdiğimizde,
# Windows Aut... : Bizim makinamız bağlanabiliyor. 
# SQL Server Auth... : Kurulumda belirlediğimiz şifre ile bağlanabiliyoruz.
# Şimdi Windows Aut... ile bağlanalım.

# SQL eğitim yazarak bağlanılmıyor hoca gibi çünkü...
# Kendi makinanızın adını yazarak bağlanabilirsiniz.
# Bilgisayar adı için bilgisayar-özelliklerden bak. Ya da CMD ye gir. -HOSTNAME yaz
# Ya da kendi makinama "." , "local", ya da "127.0.0.1" diyerek de bağlanabilirim.
# Ya da cmd ye "ipconfig yazınca" IPv4 Adress" yazanı yazınca bağlanabiliriz.
# .. Ama bunda bir domain içinde olmadığımız için bağlanmayabilir.
# ...Sql Automatication a girip parola girince "IPv4 Adress" numarasıyla bağlanabiliriz yine.

# Şimdi girdik. Bi tane database oluşturacağız.
# Databases yazan yere sağ tıkla "new database" diyelim.
# İsmine "ETRADE" diyelim ok diyelim.

#%% 2. video
# Şimdi bir tablo oluşturarak işe başlayalım.
# Oluşturduğum ETRADE in altında "Tables" sağ click "New"->"Table" diyorum.
# Column name :ID olsun , Data Type:int(integer) olsun.
# NOT:Sistemin daha perforsmanlı çalışması adına Database inizde kullanın ya da kullanmayın...
# ... otomatik artan bir alan mutlaka olsun. Bunuda primary key olarak işaretleyin.
# Bu ifadeler (otomatik artan ve primary key) ile ilgili bi ders yapacağız ilerde.
# Sadece bahsetme adına otomatik artan bi alandan bahsettik.
# Buna da genelde ID ismini veririz.
# ID yi işaretledik. tipini de integer seçtik.
# Peki nerede hangi veritipini seçeceğiz? Bunu ilerde göreceğiz.
# int: sayısal, date:tarih ,datetime:tarih-zaman, varchar(MAK): text tipleri için
# Şimdilik bu 4 ünü bilsek yeterli. ilerleyen derslerde göreceğiz diğerlerini.
# Peki otomatik artan ı nereden işaretliyoruz?
# Alt kısımda Identity Specification- Is Identity nin sağındaki "oka" gelip - "Yes" diyoruz.
# Identity Specification ve is identity "Yes" oldu
# Sonra ID ye sağ tıklayıp "set primary key" e tıklayı onu primary key yapıyoruz.
# Primary Key: Bir tabloda tekrar etmeyen alan(otomatik artan olacağı için ..)
# ...Mesela : müşteriler tablosunda TC numarasını da primary key olarak işaretleyebilirdik. 
# Ancak oromatik artanın primary key olarak işaretlenmesi performans açısından daha iyidir.
# Müşteriler tablosu oluşturmak istiyorum. ID nin altına "CUSTOMERNAME" diyelim. datatype varchar(100)
# ...neden 100? 100 karakterden az olacak şekilde olsun ismi diye.
#  Sonra onun altına Müşterinin başka neyi olur
# ... "CITY"(varchar(50)), "DISTRICT"(varchar(50)), "BIRTHDAY"(date), "GENDER"(varchar(1)) diyelim.
# Sonra makinanın isminin yazılı olduğu sekmedeki çarpıya bas - "yes" de sonra "CUSTOMER"
# ... olarak kaydet. sol tarafta tables a gel "CUSTOMER" ı göreceksin orada.
# ... Göremezsek tables a sağ tıkla "refresh"
# Üzerine gelip sağ click "edit top 200 rows" dersem onun içerisine bilgi girebilirim artık.
# Denemek için bi kaç satır rasgele bilgilerle doldurduk.
# NOT: date e yazarken: 1993-07-15 şeklinde yazdık.
# ID otomatik doldu farkettiysek ve o alana müdahale edemiyorum. Diğer alanları değiştirebilirim.
# Artık veritabanında bu değerleri (SQL dili ile) sorgulamaya başlayabiliriz.

#%%3. video
"""
Aşağıdaki bilgileri bilmeniz beklenmektedir.
1.Management studio da bağlantıyı nasıl yapabiliriz?
2.Yeni bir database nasıl oluşturabiliriz?
3.Yeni tablo nasıl oluştururuz?
4.Bilmemiz gereken 4 tane veri tip hangileridir?
5.Bir sütun ismi oluşturduk diyelim ki "ID" bunu otomatik artan nasıl yaparız?
6.Primary key nasıl yaparız?
7.ID haricinde başka sütunlar oluştur ve bunu CUSTOMER olarak kaydet?
8.Bu tabloya yeni bilgileri nasıl gireceğiz?
9.Date veri tipli olana veriyi nasıl giriyoruz?

1.Management Studio kullanımı?
2.SQL Server Authentication türleri?
3.SQL Server üzerinde tablo oluşturma?
4.SQL Server ın geri planda sadece TSQL komutları çalıştırıyor olması?
Bunları biliyor muyum diye kendinize sorun.
"""