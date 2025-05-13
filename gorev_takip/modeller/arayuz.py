import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from gorev_yonetimi import gorevleri_listele, gorev_ekle, gorev_sil, gorev_tamamla
from datetime import datetime

def arayuz():
    pencere = tk.Tk()
    pencere.title("Görev ve Alışkanlık Takibi")
    pencere.geometry("650x500")
    pencere.configure(bg="#f5f5f5")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview", background="#ffffff", foreground="#000000", rowheight=30, fieldbackground="#ffffff", font=('Segoe UI', 10))
    style.configure("Treeview.Heading", font=('Segoe UI', 11, 'bold'), background="#e1e1e1")

    # Başlık
    title_label = tk.Label(pencere, text="Görev ve Alışkanlık Takibi", font=("Segoe UI", 16, "bold"), bg="#f5f5f5", fg="#333")
    title_label.pack(pady=10)

    # Görev Listesi (Treeview)
    kolonlar = ("Tarih", "Görev", "Durum")
    tree = ttk.Treeview(pencere, columns=kolonlar, show="headings")
    for col in kolonlar:
        tree.heading(col, text=col)
        tree.column(col, width=200 if col != "Durum" else 80, anchor="center")

    tree.pack(pady=10)

    def listele():
        for i in tree.get_children():
            tree.delete(i)
        gorevler = gorevleri_listele()
        for g in gorevler:
            durum = "✓" if g["tamamlandi"] else "✗"
            tree.insert("", tk.END, values=(g["tarih"], g["ad"], durum))

    def gorev_ekle_func():
        ad = simpledialog.askstring("Görev Ekle", "Görev adı:")
        if not ad:
            return
        aciklama = simpledialog.askstring("Görev Ekle", "Açıklama:")
        # Tarih sorulmasın isteniyordu, otomatik olarak bugünün tarihi veriyoruz
        tarih = datetime.now().strftime("%d/%m/%Y")
        gorev_ekle(ad, aciklama, tarih)
        listele()
        messagebox.showinfo("Başarılı", "Görev eklendi.")

    def gorev_sil_func():
        secili = tree.selection()
        if not secili:
            messagebox.showwarning("Uyarı", "Lütfen silmek için bir görev seçin.")
            return
        index = tree.index(secili[0])
        silinecek = gorev_sil(index)
        listele()
        messagebox.showinfo("Silindi", f"{silinecek} görevi silindi.")

    def gorev_tamamla_func():
        secili = tree.selection()
        if not secili:
            messagebox.showwarning("Uyarı", "Lütfen bir görev seçin.")
            return
        index = tree.index(secili[0])
        gorev_tamamla(index)
        listele()
        messagebox.showinfo("Tamamlandı", "Görev tamamlandı olarak işaretlendi.")

    def aliskanlik_ekle():
        ad = simpledialog.askstring("Alışkanlık Ekle", "Alışkanlık adı:")
        if not ad:
            return
        gorev_ekle(ad, "Alışkanlık", datetime.now().strftime("%d/%m/%Y"))
        listele()
        messagebox.showinfo("Eklendi", "Alışkanlık eklendi.")

    # Butonlar
    buton_frame = tk.Frame(pencere, bg="#f5f5f5")
    buton_frame.pack(pady=10)

    ttk.Button(buton_frame, text="Görev Ekle", command=gorev_ekle_func).grid(row=0, column=0, padx=5)
    ttk.Button(buton_frame, text="Görev Sil", command=gorev_sil_func).grid(row=0, column=1, padx=5)
    ttk.Button(buton_frame, text="Tamamla", command=gorev_tamamla_func).grid(row=0, column=2, padx=5)
    ttk.Button(buton_frame, text="Alışkanlık Ekle", command=aliskanlik_ekle).grid(row=0, column=3, padx=5)

    listele()
    pencere.mainloop()

if __name__ == "__main__":
    arayuz()
