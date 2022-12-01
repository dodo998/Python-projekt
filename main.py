import sqlite3
import tkinter
from tkinter import *
import funkciok

def hozzaad():
    lada_liasta.delete(0, END)
    funkciok.beilleszt(szama.get(), kodja.get(), neve.get(), megyeje.get(), szelessege.get(), hossza.get(), telj.get())
    lada_liasta.insert(END, szama.get(), kodja.get(), neve.get(), megyeje.get(), szelessege.get(), hossza.get(), telj.get())
    szam_e.delete(0, END)
    kod_e.delete(0, END)
    nev_e.delete(0, END)
    megye_e.delete(0, END)
    hossz_e.delete(0, END)
    szel_e.delete(0, END)

def megnez_osszes():
    lada_liasta.delete(0, END)
    for sor in funkciok.megnez():
        lada_liasta.insert(END, sor)


def keres():
    lada_liasta.delete(0, END)
    for sor in funkciok.kereses(szama.get(), kodja.get(), neve.get(), megyeje.get(), szelessege.get(), hossza.get(), telj.get()):
        lada_liasta.insert(END, sor)


def sor_kivalasztas(event):
    hanyadik = lada_liasta.curselection()[0]


def torles():
    lada_liasta.delete(tkinter.ANCHOR)


def modosit():
    for sor in lada_liasta.curselection():
        print(lada_liasta.get(sor))

ablak = Tk()
ablak.title('Geocatching')
ablak.minsize(width=600, height=400)


l_szam = Label(ablak, text="Szám:")
l_szam.grid(row=0, column=0)

l_kod = Label(ablak, text="Kód:")
l_kod.grid(row=1, column=0)

l_nev = Label(ablak, text="Név:")
l_nev.grid(row=2, column=0)

l_megye = Label(ablak, text="Megye:")
l_megye.grid(row=0, column=2)

l_szel = Label(ablak, text="Szélesség:")
l_szel.grid(row=1, column=2)

l_hossz = Label(ablak, text="Hosszúság:")
l_hossz.grid(row=2, column=2)

szama = StringVar()
szam_e = Entry(ablak, textvariable=szama)
szam_e.grid(row=0, column=1)

kodja = StringVar()
kod_e = Entry(ablak, textvariable=kodja)
kod_e.grid(row=1, column=1)

neve = StringVar()
nev_e = Entry(ablak, textvariable=neve)
nev_e.grid(row=2, column=1)

megyeje = StringVar()
megye_e = Entry(ablak, textvariable=megyeje)
megye_e.grid(row=0, column=3)

szelessege = StringVar()
szel_e = Entry(ablak, textvariable=szelessege)
szel_e.grid(row=1, column=3)

hossza = StringVar()
hossz_e=Entry(ablak, textvariable=hossza)
hossz_e.grid(row=2, column=3)

telj = BooleanVar()
l_pipa = Checkbutton(ablak, text="Teljesített?", variable=telj)
l_pipa.grid(row=0, column=4)

lada_liasta=Listbox(ablak, height=12, width=50)
lada_liasta.grid(row=5, column=0, rowspan=7, columnspan=3)

lista_sb=Scrollbar(ablak)
lista_sb.grid(row=7, column=3)

lada_liasta.bind("<<kivalasztva>>", sor_kivalasztas)

lada_liasta.configure(yscrollcommand=lista_sb.set)
lista_sb.configure(command=lada_liasta.yview)

gomb_hozzaad = Button(ablak, text="Láda hozzáadása", width=20, command=hozzaad)
gomb_hozzaad.grid(row=4, column=4)

gomb_osszes = Button(ablak, text="Összes láda", width=20, command=megnez_osszes)
gomb_osszes.grid(row=5, column=4)

gomb_keres = Button(ablak, text="Keresés", width=20, command=keres)
gomb_keres.grid(row=6, column=4)

gomb_mod = Button(ablak, text="Kijelölt adat módosítása", width=20, command=modosit)
gomb_mod.grid(row=7, column=4)

gomb_torol = Button(ablak, text="Kijelölt adat törlése", width=20, command=torles)
#gomb_torol = Button(ablak, text="delete", command=lambda listbox=lada_liasta: listbox.delete(ANCHOR))
gomb_torol.grid(row=8, column=4)


gomb_kilep = Button(ablak, text="Kilépés", command=ablak.destroy, width=20)
gomb_kilep.grid(row=9, column=4)
"""
menusor.add_cascade(label='Felvétel', menu=felvetel)
felvetel.add_command(label='Kilépés', command=ablak.destroy)
"""

ablak.mainloop()
