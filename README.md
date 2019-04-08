# Steam Crawler

Ta repozitorij vsebuje dve datoteki, eno za zbiranje in eno za analizo podatkov uporabnikov spletne platforme Steam.
Steam je brezplačna igričarska platforma kjer uporabniki primarno kupujejo in igrajo računalniške igre, omogoča pa tudi povezovanje in komuniciranje med posamezniki, ocenjevanje in komentiranje objavljenih vsebin. Prav tako lahko igralci posnamejo in delijo svoje videje ali posnetke zaslona. Vse to so hrani na njihovem profilu. 

Ideja programa ja, da bi na podlagi vpisane starosti profila, s pomočjo predvidevanja izračunal predvidene vrednosti teh lastnosti glede na vzorcec, ki ga predhodno sam zgenerira.

**Primer profila:**
![steam_profile](steam_profile)

## knjižnice, ki so potrebne za delovanje
+ numpy
+ tkinter
+ matplotlib
+ request
+ re

## crawler.py
Datoteka vsebuje skripto za zbiranje podatkov o uporabnikih. Podati je potrebno profil, kjer želimo začeti naključni sprehod in dolžino sprehoda (koliko uporabnikov bomo pregledali). Program s pomočjo paketa requests dobi izvorno kodo strani iz katere poišče določene podatke. Nekateri podatki pa so pridobljeni s pomočjo že narejenih API poizvedb s strani razvijalvec na Steam platformi. 
Te podatke se nato združi v uporabniku berljivo strukturo in zapiše v tekstkovno datoteko.
Podanih je več tekstovnih datotek, kjer je vsakič naredil sprehod čez 1000 uporabnikov a pri tem spustil vse privatne profile (profil, ki ne razkriva nobenih podatkov). Zato je v vsaki datoteki približno 850 uporabnikov.

## analysis.py
Datoteka sprva prebere tekstkovno datoteko, ki jo je zgenerirala skripta crawler.py. Podatke si shrani tako, da lahko zatem naredi z vsakim posebaj regresijo od odvisnosti od starosti profila. Za vsak podatek posebaj, izriše tudi sliko in pa premico, ki predstavla rezultat linearne regresije. 

Nato program odpre uporabniški vmesnik, v katerem lahko sam uporabnik vpisuje različne starosti in program mu vrne izračunane pričakovane vrednosti vseh lastnosti, ko ta doseže vpisano starost. Zraven pa se tudi izrišejo vse slike, ki predstavlajo regresije raznih lastnosti.

**Izgled končnega programa**
![gui_example](gui_example)
