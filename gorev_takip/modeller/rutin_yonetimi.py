from veritabani import rutin_yukle, rutin_kaydet

def rutinleri_listele():
    veri = rutin_yukle()
    return veri["rutinler"]

def rutin_ekle(ad):
    veri = rutin_yukle()
    veri["rutinler"].append({
        "ad": ad,
        "tamamlandi": False
    })
    rutin_kaydet(veri)

def rutin_tamamla(ad):
    veri = rutin_yukle()
    for r in veri["rutinler"]:
        if r["ad"] == ad:
            r["tamamlandi"] = True
            break
    rutin_kaydet(veri)