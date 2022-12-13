'''
n�v        ;els�;utols�;s�ly;magass�g
Jim Abbott  ;1989-04-08;1999-07-21;200;75
Kyle Abbott ;1991-09-10;1996-08-24;200;76
'''

import sqlite3


con = sqlite3.connect(":memory:")
cur = con.cursor()

class Bal:
  def __init__(self, sor):
    nev, elso, utolso, suly, magassag = sor.strip().split(";")
    self.nev = nev
    self.elso = elso
    self.utolso = utolso
    self.suly = suly
    self.magassag = magassag
    
#2
    
with open("balkezesek.csv", encoding="latin2") as f:
  elso_sor = f.readline()
  lista = [Bal(sor) for sor in f]


cur.execute("DROP TABLE IF EXISTS balkez")
cur.execute("""
    CREATE TABLE IF NOT EXISTS balkez
    (nev    TEXT,
    elso  TEXT,
    utolso    TEXT,
    suly      INTEGER,
    magassag     INTEGER)
    """)
con.commit()

for i in lista:
  lista = [(i.nev, i.elso, i.utolso, i.suly, i.magassag)]
  cur.executemany("INSERT INTO balkez VALUES(?, ?, ?, ?, ?)", lista)

con.commit()

#3

darab = cur.execute("SELECT COUNT() FROM balkez")
print(f"3. feladat: {darab.fetchall()[0][0]}")

#4
print(f"4. feladat: ")
negyes = cur.execute("SELECT nev,magassag*2.54 FROM balkez WHERE utolso LIKE '1999-10%'")
for sor in negyes:
  finom = f"{sor[1]:.1f}"
  finom = str(finom).replace(".", ",")
  print(f"\t{sor[0]}, {finom} cm")


#5
print(f"5. feladat: ")
bekeres = int(input("Kérek egy 1990 és 1999 közötti évszámot: "))
while True:
  if 1990 <= bekeres <= 1999:
    break
  else:
    bekeres = int(input("Hibás adat, kérek egy 1990 és 1999 közötti évszámot!: "))

#6

atlag = cur.execute(f"SELECT avg(suly) FROM balkez WHERE utolso LIKE '{bekeres}%'")

ves = f"{atlag.fetchall()[0][0]:.2f}"
ves = str(ves).replace(".", ",")
print(f"6. feladat: {ves} font")








