# 3000 Kalimat Bahasa Arab Populer — Level A2 (kalimat 751–1500)

Buka `index.html`. Isi: menu utama → daftar 24 topik → pelajaran, dan kuis (`quiz-1.html` … `quiz-24.html`).

## Suara
1. Pasang Python, lalu: `pip install edge-tts`
2. Taruh `make_audio.py` dan `audio_list.csv` di folder yang sama dengan `index.html`
3. Jalankan: `py make_audio.py` → folder `audio/` berisi 2342 file mp3
   (skrip ini melewati file yang sudah ada; ubah `OVERWRITE = True` untuk membuat ulang semuanya)
4. Unggah folder `audio/` bersama file lainnya.

Nama file: `NOMOR.mp3` (kalimat), `NOMORf.mp3` (bentuk perempuan), `NOMORa.mp3` / `NOMORb.mp3` (dialog A/B).
Nomor kalimat Level A2 adalah 751–1500, jadi tidak bertabrakan dengan Level A1 (1–750); kedua level boleh memakai folder `audio/` yang sama.

## GitHub Pages
Unggah seluruh isi folder ke repo → Settings → Pages → Deploy from branch → `main` / root.
Untuk Level A2 sebaiknya buat repo terpisah (atau subfolder, misalnya `a2/`).
