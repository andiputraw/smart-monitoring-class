# Tentang Project

<b>Smart class monitoring condition</b> adalah sebuah project untuk mendeteksi kebisingan kelas melalui dari tingkat kebisingan dan juga untuk memonitor kondisi kelas melalui Kamera.

Project ini menggunakan Rassbery-PI 4 dengan sensor suara dan juga kamera yang menggunakan handphone dengan aplikasi ipcam.

Note: Skala projek ini dalah miniatur prototype. tidak cocok untuk environtment production

# Cara pakai

1. clone repostory ini

   ```bash
   git clone
   ```

2. Ganti `.env.example` menjadi `.env`

3. Isi token yang diperlukan

   1. `UBIDOTS_TOKEN` bisa di dapat di https://help.ubidots.com/en/articles/590078-find-your-token-from-your-ubidots-account
   2. Sedangkan untuk `BOT_TOKEN` bisa di dapat dari https://core.telegram.org/bots/tutorial
   3. CAMERA_URL bi

4. install dependency
   ```bash
   pip install requests telepot python-dotenv
   ```
5. jalankan `app.py`

   ```bash
   python app.py
   ```
