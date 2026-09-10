# QR Absen Harian

Website absen QR harian: dua kartu (QR Datang hijau + QR Pulang biru) yang payload JSON-nya dibuat live oleh Python (Flask) dalam zona Asia/Jakarta dan berganti otomatis tiap tanggal baru. Siap deploy ke Vercel. Tanpa database, tanpa login, tanpa build step.

## Cara jalan lokal

Butuh Python 3.12 dan Node.js (untuk Vercel CLI).

```bash
pip install -r requirements.txt
```

Untuk API saja (cepat, tanpa login):

```bash
python -m flask --app api/index run --port 5000
# cek: curl localhost:5000/api/qr-datang
```

Untuk full stack (halaman + API bersamaan, butuh login Vercel sekali):

```bash
npx vercel login
npx vercel dev --listen 3000
# buka http://localhost:3000/
```

Alternatif tanpa Vercel CLI: jalankan Flask di port 5000 (perintah di atas) lalu sajikan folder `public/` sebagai statis di port lain, misal:

```bash
cd public && python -m http.server 8000
# buka http://localhost:8000/index.html
```

Catatan: halaman memanggil `fetch("/api/...")` relatif, jadi saat dipisah port seperti di atas, fetch API hanya jalan bila halaman disajikan lewat server yang juga meneruskan `/api/*` (misal `vercel dev`). Untuk cek tampilan statis saja, halaman tetap tampil dengan status loading/error yang jelas.

## Cara deploy

```bash
npx vercel --prod
```

Fungsi Python dibatasi `maxDuration: 10` (lihat `vercel.json`). Runtime Python 3.12 (lihat `.python-version`).

## Kontrak endpoint

- `GET /api/qr-datang` -> `{"id": int, "lemdikId": 4, "createdAt": "YYYY-MM-DD HH:MM:SS", "type": "QR Datang"}`
- `GET /api/qr-pulang` -> sama dengan `"type": "QR Pulang"`
- `GET /api/health` -> `{"status": "ok"}`

Contoh respons nyata (terverifikasi lokal):

```json
{"createdAt": "2026-09-10 21:54:41", "id": 3542, "lemdikId": 4, "type": "QR Datang"}
{"createdAt": "2026-09-10 21:54:41", "id": 3626, "lemdikId": 4, "type": "QR Pulang"}
```

`createdAt` selalu waktu request dalam WIB.

## ID deterministik + param ?date=

ID dihitung dari tanggal WIB, bukan dari database (tahan cold-start):

- `days = (tanggal_wib - 2026-01-01).days`
- `id_datang = 3290 + days`
- `id_pulang = 3374 + days`

Jadi tiap tanggal baru ID naik tepat 1. Param `?date=YYYY-MM-DD` hanya alat uji rollover (mengubah tanggal dasar, jam tetap waktu live). Contoh:

```bash
curl "localhost:5000/api/qr-datang?date=2026-09-18"
curl "localhost:5000/api/qr-datang?date=2026-09-19"
# id hari kedua tepat +1 dari hari pertama
```

`?date=` yang tidak valid mengembalikan 400 JSON `{"error": ...}`.

## Troubleshooting

- 404 di `/` tapi `/api/*` jalan: pastikan folder `public/` ada dan `vercel.json` tidak menimpa routing statis. Config bawaan repo sudah benar, jangan tambah `routes` manual.
- 404 di `/api/*` tapi `/` jalan: pastikan file entrypoint bernama `api/index.py` dan variabelnya bernama `app` (wajib untuk runtime Python Vercel).
- Versi Python: Vercel memakai `.python-version` (`3.12`). Bila deploy gagal dengan error runtime, samakan versi lokal dengan file itu.
- `vercel dev` minta login: normal, jalankan `npx vercel login` sekali di mesin itu.
- QR tidak tampil tapi JSON tampil: CDN qrcodejs terblokir (offline). Data JSON tetap tampil dan halaman tidak kosong.
