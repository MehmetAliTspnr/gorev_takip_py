from veritabani import veri_yukle, veri_kaydet
from datetime import datetime

# Görevleri listele
def gorevleri_listele():
    veri = veri_yukle()
    veri["gorevler"].sort(key=lambda g: datetime.strptime(g["tarih"], "%d/%m/%Y") if g["tarih"] else datetime.max)
    return veri["gorevler"]

# Görev ekleme
def gorev_ekle(ad, aciklama, tarih):
    veri = veri_yukle()
    veri["gorevler"].append({
        "ad": ad,
        "aciklama": aciklama,
        "tarih": tarih,
        "tamamlandi": False,
        "tip": "gorev"
    })
    veri_kaydet(veri)

# Görev silme
def gorev_sil(index):
    veri = veri_yukle()
    silinecek = veri["gorevler"][index]["ad"]
    del veri["gorevler"][index]
    veri_kaydet(veri)
    return silinecek

# Görev tamamla
def gorev_tamamla(index):
    veri = veri_yukle()
    veri["gorevler"][index]["tamamlandi"] = True
    veri_kaydet(veri)
