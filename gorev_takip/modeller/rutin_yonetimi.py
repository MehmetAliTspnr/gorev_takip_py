import json
import os

DOSYA_ADI = "rutinler.json"

def rutinleri_yukle():
    if not os.path.exists(DOSYA_ADI):
        return []
    with open(DOSYA_ADI, "r", encoding="utf-8") as f:
        return json.load(f)

def rutin_kaydet(rutinler):
    with open(DOSYA_ADI, "w", encoding="utf-8") as f:
        json.dump(rutinler, f, ensure_ascii=False, indent=4)
