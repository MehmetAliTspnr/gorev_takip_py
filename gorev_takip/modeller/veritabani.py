import json
import os

VERI_YOLU = "veritabani/veri.json"

# JSON'dan veriyi oku
def veri_yukle():
    if not os.path.exists(VERI_YOLU):
        return {"gorevler": []}
    try:
        with open(VERI_YOLU, "r", encoding="utf-8") as dosya:
            return json.load(dosya)
    except json.JSONDecodeError:
        print("HATA: JSON dosyası bozuk veya boş. Varsayılan veri yükleniyor.")
        return {"gorevler": []}

# JSON'a veri kaydet
def veri_kaydet(veri):
    # Dosya klasörü yoksa oluştur
    os.makedirs(os.path.dirname(VERI_YOLU), exist_ok=True)
    with open(VERI_YOLU, "w", encoding="utf-8") as dosya:
        json.dump(veri, dosya, indent=2, ensure_ascii=False)
