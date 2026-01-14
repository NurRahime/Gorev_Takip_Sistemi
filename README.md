# 📝 Görev Takip Sistemi 
Django altyapısı kullanılarak geliştirilmiş, kullanıcıların kişisel görevlerini planlayabileceği, ilerlemelerini takip edebileceği ve profil yönetimini yapabileceği web tabanlı bir görev yönetim uygulamasıdır.

## 🚀 Proje Özellikleri

* **Kullanıcı Sistemi:**
    * Kullanıcı Kayıt (Register) ve Giriş (Login) işlemleri.
    * Güvenli çıkış (Logout) ve oturum yönetimi.
* **Profil Yönetimi:**
    * Kullanıcıların profil bilgilerini (Ad, Soyad, E-posta) görüntülemesi.
    * Profil bilgilerini güncelleyebilmesi.
* **Modern Arayüz:**
    * Bootstrap 5 kütüphanesi ile tamamen responsive (mobil uyumlu) tasarım.
    * Kullanıcı dostu form tasarımları ve kart (card) yapıları.
* **Görev Yönetimi (Geliştirilme Aşamasında):**
    * Kişisel görevlerin listelenmesi ve yönetilmesi için Dashboard altyapısı.
## Grup üyeleri Ve Oluşturması Gereken Appler:
    Büşra Çakmak : Dashboard 
    Nagihan Şahiner:tasks 
    Nuriye Rahime :accounts
    Zeynep Duyar:categories
    Ayşe Temel: archive
## 🛠️ Kullanılan Teknolojiler

* **Backend:** Python , Django
* **Frontend:**  Bootstrap 5
* **Veritabanı:** SQLite (Geliştirme ortamı için)
gorev_takip_sistemi/
├── accounts/          # Kullanıcı giriş/kayıt ve profil işlemleri
├── dashboard/         # Ana sayfa ve görev paneli
├── gorev_takip_sistemi/ # Ana proje ayarları (settings, urls)
├── templates/         # HTML dosyaları (base.html burada)
├── manage.py          # Django yönetim dosyası
└── db.sqlite3         # Veritabanı dosyası


### 1. Proje linki:
```bash
git clone https://github.com/NurRahime/Gorev_Takip_Sistemi.git
cd gorev-takip-sistemi