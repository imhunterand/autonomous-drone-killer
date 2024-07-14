# Panduan Instalasi

## Persiapan Hardware
- Arduino board
- Motor driver
- Kamera
- Modem WiFi
- Sensor panas (thermal sensor)
- Komponen lainnya yang diperlukan (kabel, baterai, dll.)

## Langkah-langkah Instalasi
1. **Clone Repository**

```sh
git clone https://github.com/imhunterand/autonomous-drone-killer.git
cd autonomous-drone-killer
```
2. Install Dependensi Python

```
cd python
pip install -r requirements.txt
```
3. Upload Kode ke Arduino
 * Buka `drone_ai.ino` di Arduino IDE.
 * Unggah ke board Arduino Anda.

4. Konfigurasi File `config.json`
Sesuaikan parameter dalam `config.json` sesuai dengan setup Anda.

## Menjalankan Project
1. Jalankan Script Python

```
python python/ai_targeting.py
python python/thermal_detection.py
python python/night_mode.py
python python/control_interface.py
```
2. Kontrol Drone
Gunakan antarmuka pengguna untuk mengontrol drone dan mengaktifkan berbagai fitur.


