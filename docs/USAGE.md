#### Panduan penggunaan. Menggunakan Antarmuka Pengguna
1. Jalankan `control_interface.py`:
```sh
   python python/control_interface.py
```
2. Gunakan tombol di antarmuka untuk mengontrol drone dan mengaktifkan fitur penembakan.

### Mode AI Targeting
1. Jalankan `ai_targeting.py` untuk mendeteksi dan mengunci target menggunakan AI:
```
python python/ai_targeting.py
```
### Mode Deteksi Panas
1. Jalankan `thermal_detection.py` untuk mengaktifkan deteksi panas tubuh:
```
python python/thermal_detection.py
```
### Mode Malam
1. Jalankan `night_mode.py` untuk mengaktifkan mode malam:
```
python python/night_mode.py
```
### Pencatatan Data
1. Semua data penerbangan dan deteksi akan dicatat dalam `logs/flight_data.log`.

### Penutupan
Tutup semua koneksi serial dengan menjalankan c`lose_connection()` dari `communication.py`:
```
Tutup semua koneksi serial dengan menjalankan close_connection() dari communication.py:
```
