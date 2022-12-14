# To Do List

Link aplikasi di Heroku : [Link](https://pbp-tugas-2-insta-x.herokuapp.com/todolist)

## Inline, Internal, dan External CSS
### Inline CSS
Inline CSS dilakukan dengan menggunakan attribut `style` pada tag HTML yang ingin diubah. Inline CSS juga memiliki prioritas tertinggi sehingga akan meng-override CSS lain. Karena kita langsung mengubah di tag yang kita inginkan, cara ini sangat cepat untuk dilakukan dibandingkan cara lain. Namun, kelemahannya adalah kita perlu menambahkan `style` pada setiap tag HTML yang ingin kita ubah sehingga akan memakan waktu yang sangat lama jika kita ingin mengubah banyak tag. Dengan karakteristik yang sudah disebutkan, Inline CSS paling berguna ketika kita ingin mengetes atau mencoba CSS secara langsung dan cepat, tetapi akan sangat tidak efisien jika menjadi cara utama kita menggunakan CSS.

### Internal CSS
Internal CSS dilakukan di dalam tag `<head>` dengan memasukkan code CSS di dalam tag `<style>`. Karena code CSS ini hanya berada pada 1 html, maka CSS ini hanya akan aktif pada html tersebut. Selain itu, karena HTML dan CSS berada pada 1 file, kita tidak perlu mengirimkan banyak file untuk menampilkan halaman. Salah satu kasus hal ini akan berguna jika kita hanya ingin menunjukkan hasil halaman pada seseorang. Namun, karena CSS berada pada file html, maka load time tentunya akan meningkat. Selain itu, karena CSS hanya mempengaruhi 1 html, maka sangat tidak efisien menggunakan cara ini pada project dengan banyak file html.

### External CSS
External CSS dilakukan dengan memasukkan code CSS pada file yang terpisah dari html dan menyuruh html mengambil file CSS tersebut. Karena code CSS terpisah dari html, maka CSS bisa mempengaruhi semua html tergantung pada selector yang digunakan. Karena itu, cara ini yang paling sering digunakan dalam pengembangan website karena paling efisien. Selain itu, dengan memisahkan html dengan CSS, file menjadi lebih rapi dan load time menjadi lebih pendek untuk html. Kelemahannya adalah ketika html diload lebih cepat daripada CSS, maka ada selang waktu html tersebut dirender dengan browser default sehingga terlihat tidak sesuai yang kita inginkan.

## Tag HTML5
- `<p>` tag element untuk memasukkan paragraf atau text.
- `<div>` tag element untuk mendefinisikan suatu division.
- `<h1> <h2> <h3> <h4> <h5> <h6>` tag element untuk berbagai ukuran header.
- `<a>` tag element untuk memasukkan hyperlink.
- `<form>` tag element untuk mendefinisikan sebuah form. Form akan berisi tag `<input>` untuk menyimpan data input dari user yang akan dikirimkan.
- `<input>` tag element agar user dapat memberikan input.
- `<head>` tag element yang berisi metadata dari html.
- `<body>` tag element yang berisi data dari html.
- `<ul>` tag element untuk unordered list. Item akan ditunjukkan dengan bullet point.
- `<ol>` tag element untuk ordered list. Item akan terurut dengan angka.
- `<li>` tag element untuk item dari list `<ul>` ataupun `<ol>`.
- `<img>` tag element untuk memasukkan gambar dari suatu source.

## Jenis CSS Selector
- `.class` menselect semua element dengan attribut `class="class"`.
- `.class1 .class2` menselect semua element dengan attribut `class="class2"` yang berada dalam element dengan attribut `class="class1"`.
- `#id` menselect semua element dengan atribut `id="id"`.
- `*` menselect semua element.
- `a:hover` menselect element tag `<a>` yang sedang di-hover mouse.

## Penjelasan langkah
- Memasukkan framework Bootstrap pada semua html dengan menggunakan `<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">` pada `base.html`
- Membuat form manual karena tidak dapat mengubah CSS dari element yang telah digenerate secara otomatis dengan `{{ form.as_table }}`. Kemudian menggunakan bantuan Bootstrap untuk membuat form berada di tengah halaman. Juga menggunakan `style.css` untuk mengatur `max-width` agar tidak terlalu lebar memenuhi 1 halaman.
- Membuat card dengan menggunakan attribut `class="card"` pada tag `<div>`. Kemudian memformat data dari task agar ditampilkan dengan bagus pada card tersebut.
- Menggunakan media query untuk menetapkan breakpoint CSS dimana CSS akan berubah ketika resolusi layar mencapai breakpoint tersebut. Kemudian menggunakan `CTRL + SHIFT + M` untuk mengecek apakah halaman sudah responsive. Jika belum responsive, maka melakukan pengaturan lagi terhadap CSS dan class yang digunakan dari Bootstrap agar responsive.
- Menambahkan efek hover dengan menggunakan selector CSS `:hover` untuk menselect suatu element yang sedang di-hover mouse.