# Argo Programming Language

## About the Project

Bahasa Pemrograman Argo (Argo Programming Language) adalah sebuah bahasa pemrograman interpreter yang dibangun menggunakan bahasa Python.

## Acknowledgment

Bahasa pemrograman ini dibuat dengan mengikuti tutorial yang disediakan oleh CodePulse pada [tautan berikut](https://www.youtube.com/playlist?list=PLZQftyCk7_SdoVexSmwy_tBgs7P0b97yD)

## Getting Started

### Prerequisite

Karena bahasa ini ditulis menggunakan bahasa python versi 3, pastikan sudah terinstall python 3 di perangkat kalian. Bahasa Python versi 3 dapat kalian unduh pada [tautan berikut](https://www.python.org/downloads/).

### Installation
1. Lakukan clone terhadap repo
   ```
   git clone https://github.com/AldyAkbarrizky/ArgoLanguage.git
   ```
2. Untuk menjalankan shell, buka cmd kemudian ketikkan
   ```
   argo
   ```
   atau
   ```
   python argo.py
   ```
3. Untuk menjalankan script, buka cmd kemudian ketikkan
   ```
   argo <script_name>.argo
   ```
   atau
   ```
   python argo.py <script_name>.argo
   ```
   Note: Pastikan file script berada di folder yang sama dengan file ```argo.py```

## Features
Berikut ini adalah beberapa fitur yang sudah terimplementasikan kepada bahasa ini:
- Melakukan operasi aritmatika
- Comparisons dan logical operator
- Support untuk IF statement
- Support untuk loop statement (For dan While)
- Support untuk membuat modul (fungsi)
- Support terhadap tipe data string
- Support untuk tipe data list
- Beberapa built-in module sederhana
    - print()
    - input()
    - input_int()
    - clear()
    - quit()
    - is_number()
    - is_string()
    - is_list()
    - is_module()
    - append()
    - pop()
    - extend()
    - len()
- Support untuk multi-line statement
- Support untuk keyword return, break, dan continue

## Example
Berikut ini adalah contoh script untuk bahasa pemrograman argo
```
# Ini adalah komentar

module tambah(angka1, angka2)
    var hasil = angka1 + angka2
    return hasil
end

module kurang(angka1, angka2)
    var hasil = angka1 - angka2
    return hasil
end

module bagi(angka1, angka2)
    var hasil = angka1 / angka2
    return hasil
end

module kali(angka1, angka2)
    var hasil = angka1 * angka2
    return hasil
end

print("Ini adalah bahasa pemrograman argo!")
var angka1 = 3
var angka2 = 4
var hasil_operasi = tambah(angka1, angka2)
print("Hasil operasi: ")
print(hasil_operasi)
```
## Author
Aldy Akbarrizky, 2022

## Future Plans
Berikut ini adalah rencana pengembangan yang akan dilakukan kedepannya terhadap bahasa pemrograman argo
- Melakukan refactoring code secara keseluruhan
- Menambah beberapa built-in module baru
- Support untuk melakukan import/include file
- Mengembangkan built-in module print
- Support untuk keyword dengan Bahasa Indonesia
- Support untuk Object-Oriented Programming
- Support untuk Computer Graphic