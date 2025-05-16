import tkinter as tk
from tkcalendar import Calendar
from tkinter import ttk, messagebox, simpledialog
from gorev_yonetimi import gorevleri_listele, gorev_ekle, gorev_sil, gorev_tamamla
from rutin_yonetimi import rutinleri_listele, rutin_ekle, rutin_tamamla

def arayuz():
    pencere = tk.Tk()
    pencere.title("Görev ve Alışkanlık Takibi")
    pencere.geometry("900x600")
    pencere.configure(bg="#f5f5f5")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview", background="#ffffff", foreground="#000000", rowheight=30, fieldbackground="#ffffff", font=('Segoe UI', 10))
    style.configure("Treeview.Heading", font=('Segoe UI', 11, 'bold'), background="#e1e1e1")

    tk.Label(pencere, text="Görev ve Alışkanlık Takibi", font=("Segoe UI", 16, "bold"), bg="#f5f5f5", fg="#333").pack(pady=10)

    tk.Label(pencere, text="Tarih Seç:", font=("Segoe UI", 11), bg="#f5f5f5").pack()
    takvim = Calendar(pencere, selectmode='day', date_pattern='dd/mm/yyyy', font=("Segoe UI", 10))
    takvim.pack(pady=5)

    icerik_frame = tk.Frame(pencere, bg="#f5f5f5")
    icerik_frame.pack(pady=10, fill="both", expand=True)

    kolonlar = ("Tarih", "Görev", "Açıklama", "Durum")
    tree = ttk.Treeview(icerik_frame, columns=kolonlar, show="headings")
    for col in kolonlar:
        width = 200 if col in ["Tarih", "Görev", "Açıklama"] else 80
        tree.heading(col, text=col)
        tree.column(col, width=width, anchor="center")
    tree.pack(side="left", padx=10, fill="both", expand=True)

    rutin_kolonlar = ("Rutin", "Durum")
    rutin_tree = ttk.Treeview(icerik_frame, columns=rutin_kolonlar, show="headings", height=5)
    for col in rutin_kolonlar:
        width = 250 if col == "Rutin" else 100
        rutin_tree.heading(col, text=col)
        rutin_tree.column(col, width=width, anchor="center")
    rutin_tree.pack(side="right", padx=10, fill="y")

    def listele():
        for i in tree.get_children():
            tree.delete(i)
        gorevler = gorevleri_listele()
        for g in gorevler:
            durum = "✓" if g["tamamlandi"] else "✗"
            tree.insert("", tk.END, values=(g["tarih"], g["ad"], g["aciklama"], durum))

    def rutinleri_yenile():
        for i in rutin_tree.get_children():
            rutin_tree.delete(i)
        rutinler = rutinleri_listele()
        for r in rutinler:
            durum = "✓" if r["tamamlandi"] else "✗"
            rutin_tree.insert("", tk.END, values=(r["ad"], durum))

    def gorev_ekle_func():
        ad = simpledialog.askstring("Görev Ekle", "Görev adı:")
        if not ad:
            return
        aciklama = simpledialog.askstring("Görev Ekle", "Açıklama:") or "Açıklama girilmedi"
        tarih = takvim.get_date()
        gorev_ekle(ad, aciklama, tarih)
        listele()
        messagebox.showinfo("Başarılı", "Görev eklendi.")

    def gorev_sil_func():
        secili = tree.selection()
        if not secili:
            messagebox.showwarning("Uyarı", "Lütfen silmek için bir görev seçin.")
            return
        index = tree.index(secili[0])
        silinen = gorev_sil(index)
        listele()
        messagebox.showinfo("Silindi", f"{silinen} görevi silindi.")

    def gorev_tamamla_func():
        secili_gorev = tree.selection()
        secili_rutin = rutin_tree.selection()

        if secili_gorev:
            index = tree.index(secili_gorev[0])
            gorev_tamamla(index)
            listele()
            messagebox.showinfo("Tamamlandı", "Görev tamamlandı olarak işaretlendi.")
        elif secili_rutin:
            secili_item = secili_rutin[0]
            ad = rutin_tree.item(secili_item)['values'][0]
            rutin_tamamla(ad)
            rutinleri_yenile()
            messagebox.showinfo("Tamamlandı", "Rutin tamamlandı olarak işaretlendi.")
        else:
            messagebox.showwarning("Uyarı", "Lütfen bir görev veya rutin seçin.")

    def rutin_ekle_func():
        ad = simpledialog.askstring("Rutin Ekle", "Rutin adı:")
        if not ad:
            return
        rutin_ekle(ad)
        rutinleri_yenile()
        messagebox.showinfo("Eklendi", "Rutin eklendi.")

    buton_frame = tk.Frame(pencere, bg="#f5f5f5")
    buton_frame.pack(pady=10)

    ttk.Button(buton_frame, text="Görev Ekle", command=gorev_ekle_func).pack(side="left", padx=10)
    ttk.Button(buton_frame, text="Görev Sil", command=gorev_sil_func).pack(side="left", padx=10)
    ttk.Button(buton_frame, text="Tamamla", command=gorev_tamamla_func).pack(side="left", padx=10)
    ttk.Button(buton_frame, text="Rutin Ekle", command=rutin_ekle_func).pack(side="left", padx=10)

    listele()
    rutinleri_yenile()
    pencere.mainloop()

if __name__ == "__main__":
    arayuz()