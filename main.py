import tkinter
from PIL import ImageTk
from PIL import Image
from tkinter import messagebox
import base64


def Arayuz():

    arayuz = tkinter.Tk()
    arayuz.title("Secret Notes")
    arayuz.config(bg="#c0c0c0")
    arayuz.wm_minsize(400,640)

Arayuz()
def ImageArayuz():
    global img
    resim = Image.open(r"C:\Users\VICTUS\OneDrive\Masaüstü\PROJE ÇİZİMLERİ\DOSYA ŞİFRELEME\güvenlikImage.png")
    yenigenislik = 100
    yeniyukseklik = 100
    resim = resim.resize((yenigenislik, yeniyukseklik), Image.BILINEAR)
    img = ImageTk.PhotoImage(resim)
    imgCercevesi = tkinter.Label(image=img,borderwidth=0)
    imgCercevesi.anchor("center")
    imgCercevesi.place(x=160, y=30)

ImageArayuz()

def BaslıkLabel():
    baslikLabel = tkinter.Label()
    baslikLabel.config(bg="#c0c0c0",
                  text="Konu Başlığını Giriniz",
                  font=("Times New Roman", 17))
    baslikLabel.place(x=100, y=140)

BaslıkLabel()

def BaslikEntry():
    global baslikIcerigi
    baslikIcerigi = tkinter.Entry()
    baslikIcerigi.config(width=24,
                       bd=3,
                       fg="black",
                       justify="center",
                       font=("Times New Roman",14))
    baslikIcerigi.focus()
    baslikIcerigi.place(x=90, y=175)

BaslikEntry()

def KonuLabel():
    konuLabel = tkinter.Label()
    konuLabel.config(bg="#c0c0c0",
                    text="Konu İçeriğini Giriniz",
                    font=("Times New Roman", 17))
    konuLabel.place(x=100, y=215)

KonuLabel()

def IcerikText():
    global icerikText
    icerikText = tkinter.Text()
    icerikText.config(width=24,
                      height=10,
                       bd=3,
                       fg="black",
                       font=("Times New Roman",14))

    icerikText.place(x=90, y=245)

IcerikText()

def sıfreLabel():
    konuLabel = tkinter.Label()
    konuLabel.config(bg="#c0c0c0",
                    text="Şifrenizi Giriniz",
                    font=("Times New Roman", 17))
    konuLabel.place(x=130, y=475)

sıfreLabel()

def UyarıArayuz():

    messagebox.showwarning(title="Geçersiz Değer", message="Değerleri Kontrol Edin")

def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

def sifreleVeKaydetButonu():

    global sifrelenmisMesaj
    sifre = girilecekSifre.get()
    konuMetniniGetir = baslikIcerigi.get()
    textMetniniGetir = icerikText.get("1.0", "end-1c")



    if len(konuMetniniGetir) !=0 or len(textMetniniGetir) !=0 or len(sifre) !=0:

        sifrelenmisMesaj = encode(textMetniniGetir, sifre)

        try:

            with open(r"C:\Users\VICTUS\PycharmProjects\SecretNotes\Sifreli_Icerik.txt", mode="a") as dosyaYazdır:
                    dosyaYazdır.write(konuMetniniGetir + "\n" + "\n")

            with open(r"C:\Users\VICTUS\PycharmProjects\SecretNotes\Sifreli_Icerik.txt", mode="a") as dosyaYazma:
                        dosyaYazma.write((sifrelenmisMesaj) + "\n" + "\n")

        except FileNotFoundError:
            UyarıArayuz()
        finally:
            baslikIcerigi.delete(0,"end")
            icerikText.delete(1.0,"end")
            girilecekSifre.delete(0,"end")

    else:
        UyarıArayuz()

def sıfreEntry():
    global girilecekSifre

    girilecekSifre = tkinter.Entry()
    girilecekSifre.config(width=24,
                          bd=3,
                          fg="black",
                          justify="center",
                          font=("Times New Roman",14))
    girilecekSifre.place(x= 90, y=505)

sıfreEntry()


def sifreCoz():

    sifrelenmisIcerik = icerikText.get("1.0", "end-1c")
    sifrelenmisSifre = girilecekSifre.get()

    if len(sifrelenmisIcerik) == 0 or len(sifrelenmisSifre) == 0:
        UyarıArayuz()
    else:
        try:
            cozumlenmisMesaj = decode(sifrelenmisIcerik, sifrelenmisSifre)
            icerikText.delete("1.0", "end")
            icerikText.insert("1.0", cozumlenmisMesaj)
        except Exception as e:
            print("Hata:", e)
            UyarıArayuz()

def CozumleButonu():
    cozumButonu = tkinter.Button()
    cozumButonu.config(text="Çözümle",
                       width=25,
                       font=("Arial", 9, "bold"),
                       bg="yellow",
                       command=sifreCoz)

    cozumButonu.place(x=108, y=585)
CozumleButonu()

def KayitButonu():

    kayitButonu = tkinter.Button()
    kayitButonu.config(text="Şifrele ve Kaydet",
                       width=25,
                       font=("Arial",9,"bold"),
                       bg="yellow",
                       command=sifreleVeKaydetButonu)

    kayitButonu.place(x=108, y=545)
KayitButonu()


tkinter.mainloop()