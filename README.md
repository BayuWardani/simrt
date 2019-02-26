# SIMRT
Sistem Informasi Management RT. sistem yang ditunjukan kepada semua ibu/bapak rt yang ingin semua data kependudukan maupun pelayanan tertata dengan rapi dalam bentuk sebuah sistem.

![alt text](https://github.com/BayuWardani/simrt/blob/master/127.0.0.1_8000_kependudukan_warga_%20(1).png?raw=true)

## FITUR
<ul>
  <li><strong>Kependudukan</strong>
    <ul>
      <li>Warga</li>
      <li>Warga Sementara</li>
      <li>Surat Pengantar</li>
      <li>Cetak Surat Pengantar dalam bentuk PDF</li>
    </ul>
  </li>
  <li><strong>Konfigurasi Sistem</strong>
    <ul>
      <li>Setting Kabupaten, Kecamatan, Desa, Dusun, RT & RW, Ketua RT, Ketua RW</li>
    </ul>
   </li>
  <li><strong>Accounts</strong>
    <ul>
      <li>Admin</li>
    </ul>
   </li>
</ul>


## ISTALASI LINUX
1. Install Python 3.* [Python 3.*](https://www.python.com) 
2. Install Virtualenv ``` pip3 install virtualenv ```
3. Buat Folder ```mkdir simrt```
4. arahkan ke folder env simrt ``cd simrt``
5. ``virtualenv simrt``
6. ketik ``./simrt/bin/active`` 
7. arahkan ke folder home ```cd ~/```
8. clone project simrt ``git clone https://github.com/BayuWardani/simrt.git``
9. masuk ke project simrt ``` cd simrt && pip3 install -r requirments.txt```
10. migrate database simrt tapi sebelumnya sudah dibuatkan database dan install postgresql, untuk cara instalasi postgresql dan  cara buat databasenya bisa ke sini [How To Use PostgreSQL with your Django Application on Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04) ``python manage.py makemigrations && python manage.py migrate ``
11. lalu jalankan perintah `` python manage.py runserver``
12. Jika ingin menjalankan ke dalam sebuah server bisa mengikuti langkah2 deploy django link tutorial [How To Deploy a Local Django App to a VPS](https://www.digitalocean.com/community/tutorials/how-to-deploy-a-local-django-app-to-a-vps)

### TERIMAKASIH UNTUK
~ [Python](https://www.python.com) Bahasa Pemograman <br />
~ [Django](https://www.djangoproject.com/) Web Framework <br />
~ [Stisla](https://github.com/stisla/stisla) Template Admin <br />
~ dan semua Python library yang saya gunakan.

### NOTE
SIMRT ini masih belum selesai 100% karena masih ada beberapa template dan fitur yang belum saya selesaikan.
