import json
import os

GOREV_YOLU = "veritabani/gorevler.json"
RUTIN_YOLU = "veritabani/rutinler.json"

# Görevleri yükle
def veri_yukle():
    if not os.path.exists(GOREV_YOLU):
        return {"gorevler": []}
    try:
        with open(GOREV_YOLU, "r", encoding="utf-8") as dosya:
            return json.load(dosya)
    except json.JSONDecodeError:
        return {"gorevler": []}

# Görevleri kaydet
def veri_kaydet(veri):
    os.makedirs(os.path.dirname(GOREV_YOLU), exist_ok=True)
    with open(GOREV_YOLU, "w", encoding="utf-8") as dosya:
        json.dump(veri, dosya, indent=2, ensure_ascii=False)

# Rutinleri yükle
def rutin_yukle():
    if not os.path.exists(RUTIN_YOLU):
        return {"rutinler": []}
    try:
        with open(RUTIN_YOLU, "r", encoding="utf-8") as dosya:
            return json.load(dosya)
    except json.JSONDecodeError:
        return {"rutinler": []}

# Rutinleri kaydet
def rutin_kaydet(veri):
    os.makedirs(os.path.dirname(RUTIN_YOLU), exist_ok=True)
    with open(RUTIN_YOLU, "w", encoding="utf-8") as dosya:
        json.dump(veri, dosya, indent=2, ensure_ascii=False)
