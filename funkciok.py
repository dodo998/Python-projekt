import sqlite3

def adatbazis_kapcsolat():
    kapcsolat = sqlite3.connect("geoladak.db")
    kiad = kapcsolat.cursor()
    kiad.execute('CREATE TABLE IF NOT EXISTS geoladak (id INTEGER PRIMARY KEY, szam TEXT, kod TEXT, nev TEXT, megye TEXT, szelesseg TEXT, hosszusag TEXT, teljesitett BOLEAN)')
    kapcsolat.commit()
    kapcsolat.close()


def beilleszt(szam, kod, nev, megye, szelesseg, hosszusag, teljesitett):
    kapcsolat=sqlite3.connect("geoladak.db")
    kiad = kapcsolat.cursor()
    kiad.execute("INSERT INTO geoladak VALUES (NULL, ?,?,?,?,?,?,?)", (szam, kod, nev, megye, szelesseg, hosszusag, teljesitett))
    kapcsolat.commit()
    kapcsolat.close()


def megnez():
    kapcsolat = sqlite3.connect("geoladak.db")
    kiad = kapcsolat.cursor()
    kiad.execute("SELECT * FROM geoladak")
    sorok=kiad.fetchall()
    kapcsolat.close()
    return sorok

def kereses(szam="", kod="", nev="", megye="", szelesseg="", hosszusag="", teljesitett=""):
    kapcsolat = sqlite3.connect("geoladak.db")
    kiad = kapcsolat.cursor()
    kiad.execute("SELECT * FROM geoladak WHERE szam=? OR kod=? OR nev=? OR megye=? OR szelesseg=? ""OR hosszusag=? OR teljesitett=?",
                 (szam, kod, nev, megye, szelesseg, hosszusag, teljesitett))
    sorok = kiad.fetchall()
    kapcsolat.close()
    return sorok


def torol(id):
    kapcsolat = sqlite3.connect("geoladak.db")
    kiad = kapcsolat.cursor()
    kiad.execute("DELETE FROM geoladak WHERE id=?", (id,))
    kapcsolat.commit()
    kapcsolat.close()


def modosit(id, szam, kod, nev, megye, szelesseg, hosszusag, teljesitett):
    kapcsolat = sqlite3.connect("geoladak.db")
    kiad = kapcsolat.cursor()
    kiad.execute("UPDATE geoladak SET szam=?, kod=?, nev=?, megye=?, szelesseg=?, hosszusag=?, teljesitett=? WHERE id=?", (id, szam, kod, nev, megye, szelesseg, hosszusag, teljesitett))
    kapcsolat.commit()
    kapcsolat.close()




adatbazis_kapcsolat()

