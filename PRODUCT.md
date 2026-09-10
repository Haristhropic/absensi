# PRODUCT.md — QR Absen Harian (Skomda)

## Product truth
- Halaman absensi harian: menampilkan dua QR code yang dipindai pegawai/siswa untuk clock-in (Datang) dan clock-out (Pulang).
- Payload QR dibuat live oleh API Flask dalam zona Asia/Jakarta: `{"id":int,"lemdikId":4,"createdAt":"YYYY-MM-DD HH:MM:SS","type":"QR Datang"|"QR Pulang"}`.
- ID deterministik dari tanggal WIB: `id_datang = 3290 + days`, `id_pulang = 3374 + days` sejak 2026-01-01. Berganti tiap tengah malam WIB.
- Frontend statis tanpa build step: satu file `public/index.html`, inline CSS, satu CDN (qrcodejs). Deploy Vercel.

## Audience & scene
- Pengunjung utama: pegawai/siswa yang memindai QR dengan HP, pagi (datang) dan sore (pulang), sering terburu-buru.
- Admin: menampilkan halaman di layar/HP di pintu masuk; butuh status sekilas (jam, countdown QR berikutnya, error jelas).
- Bahasa: Indonesia (id-ID). Zona waktu: WIB.

## Content & function (must keep)
- Dua kartu: "QR Datang" (hijau) + "QR Pulang" (biru). JSON payload disembunyikan dari tampilan (keputusan pemilik).
- Jam live WIB, countdown ke tengah malam, auto-refetch saat tanggal berganti, timestamp "Diperbarui".
- Error state per kartu + tombol "Coba lagi". Skeleton loading.
- Endpoint: `GET /api/qr-datang`, `GET /api/qr-pulang`, `GET /api/health`.

## Constraints
- Tanpa build step, tanpa framework JS, tanpa database/auth. Inline CSS + qrcodejs CDN saja.
- Responsif 360px hingga desktop. Kontras AA. `prefers-reduced-motion` dihormati.
- Tanpa em-dash di UI.
