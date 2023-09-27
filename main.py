import tkinter
from PIL import ImageTk
from PIL import Image
from cryptography.fernet import Fernet
import os

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
def sıfreEntry():
    global girilecekSifre
    girilecekSifre = tkinter.Entry()

    girilecekSifre = tkinter.Entry()
    girilecekSifre.config(width=24,
                       bd=3,
                       fg="black",
                       justify="center",
                       font=("Times New Roman",14))
    girilecekSifre.place(x= 90, y=505)

sıfreEntry()



def CozumleButonu():
    cozumButonu = tkinter.Button()
    cozumButonu.config(text="Çözümle",
                       width=25,
                       font=("Arial",9,"bold"),
                       bg="yellow")
                       #command=#islemyapılacakfonksiyon)

    cozumButonu.place(x=108, y=585)
CozumleButonu()


def sifreleVeKaydetButonu():

    konuMetniniGetir = baslikIcerigi.get()
    with open(r"C:\Users\VICTUS\PycharmProjects\SecretNotes\Sifreli_Icerik.txt", mode="a") as dosyaYazma:
        dosyaYazma.write(konuMetniniGetir +"\n")

def KayıtButonu():
    kayitButonu = tkinter.Button()
    kayitButonu.config(text="Şifrele ve Kaydet",
                       width=25,
                       font=("Arial",9,"bold"),
                       bg="yellow",
                       command=sifreleVeKaydetButonu)

    kayitButonu.place(x=108, y=545)

KayıtButonu()

sifreleVeKaydetButonu()






tkinter.mainloop()