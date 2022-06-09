# SQL = Structural Query Language = Yapısal sorgulama Dili
# Her şeyden önce bu bir DİL. C# gibi Java gibi
# Veritabanlarındaki verileri yönettiğimiz bir çeşit sorgulama dili
# Veri tabanı: temel anlamda içerisinde veri barındıran yazılımlar.
# Verileri listeler halinde tablo ve satırlar halinde tutan yapılar.(Excel vs)
# Veri tabanları nelerden oluşur: tablolar,kolonlar(isim,yaş,..), satırlar, indexler 
# Veri tabanı sunucu nedir? Bir yazılımdır.
# .. Network üzerinde bir porttan sistemi dinler ve gelen komutlara göre istenilen,
# .. veriyi gönderir. 
# .. SQL Server, MYSQL, PostgreSQL, Oracle gibi sistemler veritabanı sunucusudur.
# .. Yani, gelen komutlarla işlem gerçekleştirir. Bu işlemleri gerçekleştirirken,
# .. kendi CPU sunu vs kullanır.
# NOT: Access, Excel gibi yapılar ise bir sunucu değildir.
# .. Mesela bir excel dosyasını açmak istediğimizde kendi bilg kaynaklarını kullanırız.
# .. Bu yüzden bunlar veri tabanı SUNUCUSU değillerdir.
# İstemci bilgisayar, veritabanı sunucusundan bir müşteri listesi çekmek istesin.
# Bunun için fiziksel bir bağlantı ŞART. Arada bir firewall vs varsa bu bağlantı gerçekleşemez.
# Bir kullanıcı adı ve şifre olmalı.
# Veritabanı sunucusu kullanıcı adı ve şifreyi kontrol eder yanlışsa girmesini engeller.
# Müşteri listesini istemci bilgisayarımıza getirmek için bir SQL komutu 
# .. gönderiyorum veritabanı sunucusuna
# Yapmak istediğimiz şeyleri SQL diliyle anlatmalıyız.
# SQL DİLİ BÜTÜN VERİTABANLARI İÇİN ORTAK BİR DİLDİR:
# BUNUNLA BİRLİKTE HER VERİTABANI KENDİ İÇERİSİNDE BAZI KOMUTLAR GELİŞTİRMİŞTİR.
# AMA TEMEL SQL KOMUTLARI AYNIDIR.(mesela SELECT*FROM MUSTERILER)
# Veri tabanından sadece veri çekmeyiz. başka neler yaparız?
# veriyi değiştirme: yeni kayıt, mevcut kaydı değiştirme, mevcut kaydı silme.
# (Örnek: INSERT INTO MUSTERILER(AD,SOYAD) VALUES("OMER COLAKOGLU"))

# Biz bu kursumuzda veritabanı sunucus olarak Microsoft SQL Server ı kullanacağız.
# Neden? Çünkü şu anda Türkiyede en çok kullanılan ticari veri tabanı.
# MSSQL de öğreneceklerimiz 2 tane:
"""1. SQL SERVER PROGRAMMING                 -  2.SQL SERVER ADMINISTRATING
-TEMEL SQL DİLİ(SELECT,INSERT,VS)            - TEMEL YÖNETİM(KURULUM, YAPILANDIRMA VS)
-SQL SERVER PROGRAMLAMA(STORED PROC,          - ILERI SEVIYE YONETIM(PERFORMANS YÖNETİMİ
         ...TRIGER,FUNCTION,WIEW,...)         SİSTEM İZLEME, HIGH AVAILABILITY, ALWAYS ON,..) 
-TSQL(CURSOR,DYNAMIC WİEW,TEMP TABLE,PIVOT..)  - TSQL(DBCC KOMUTLARI, DMV LER, 
                                                DDL TRIGGER, SERVER TRIGGER,...)
"""

# 0 dan bu işi yapacak olsak nelere ihtiyacımız var bu onları gösteriyor.
# TSQL aşaması, ileri seviye sql cümleleri yazmak.
# Yönetimde de temel anlamda bilmemiz gerekenden ileri seviyeye bilmemiz gerekenler var.
# ... (Uçtan uca SQL server da 2. kısımdan çokça bahsedildi.(SQL Server administrating.))

#%%2. video
# RDMS = Relational Database Management Systems = İlişkisel veritabanı sistemleri
# Popüler olan veritabanları ilişkisel veritabanı sistemleridir.(Postgresql, Mysql, Oracle vs)
# RDMS : Tekrar eden verileri tekilleştirmek amacı ile yapılandırılan veritabanı sistemleri.
# Teorik tanım yerine, biraz uygulamada anlamaya çalışalım.
# Mesela bir firmasınız bir fatura keseceksiniz,
# faturada başlık bilgisi, müşteri bilgisi, tahsilat tarihi, işlem tarihi, 
# altta da ürünlerimiz var fiyatı miktarı var vs.
# üsttekiler (fatura ile alakalı yerler) bir kere yazılacak yerler.
# diğer taraftan mesela müşteri kısmında müşteri seçerek müşteri bilgileri geliyor.
# Tekrar bilgileri girmek yerine mevcut kayıttan görüyorum.
# Aşağıda yeni satır ekle diyerek ürün seçiyorum.(miktarı elle girdim, Toplamı otomatik hesapladım)
# Yani fiyatı elle yazmak yerine ürün seçten ürünü seçtim. diğer bilgileri otomatik olarak getiriyoruz)
# Burada 1.fatura bilgileri 2.Müşteri tablosu bilgileri
# 3. ürünler tablosu bilgileri 4.fatura satırlarına elle girdiğim bilgiler.
# Şimdi Müşterinin kodu değişir mi? değişmez, adı değişir mi? değişmez,
# burada belki adres tel vs değişir. onlarda adres ve tel tablosunda tutulur zaten.
# ürün adı kodu da değişmez. Bu şekilde değişmeyecek şeyleri satır satır tutmak yerine,
# ürünün sadece kodunu yani referans edecek bir bilgiyi tutmam yeterli.
# Yani bilgi tekrarından kaçınmış olurdum.
# SONUC OLARAK: İlişkisel veritabanında tekrar eden veriyi engellemek 
# ..ve veri bütünlüğünü sağlamak temel amaçtır.

#%% 3. video - kurulum
# 4. video 
# Üstteki bilgilere ve 3. videoya göre bilmemiz beklenmekte
"""
1. Veritabanı nedir?
2. Veritabanı Yönetim Sistemi nedir? # Kurulum, yapılandırma, performans, bakım vs ...
3. Veritabanı Sunucusu nedir?
4. Client-Server Mimarisi nasıl çalışır?
5. İlişkisel veritabanı nedir?
6. SQL Server 2017 sürümleri nelerdir?
7. SQL Server 2017 nasıl kurulur?
"""

