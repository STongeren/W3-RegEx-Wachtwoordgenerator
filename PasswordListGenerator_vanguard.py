# Aangepaste wachtwoordgenerator - Vanguard Logistics context
# Gebaseerd op: https://github.com/utpalbalse/PasswordListGenerator

wachtwoordlijst = []
namen = []
tijdelijke_namen = []
telefoonnummer = ''

geboortedatum = input("Geboortedatum (DDMMJJJJ): ")
if len(geboortedatum) == 8:
    dag   = geboortedatum[:2]
    maand = geboortedatum[2:4]
    jaar  = geboortedatum[4:]
else:
    print("Fout: gebruik het formaat DDMMJJJJ (8 cijfers)")
    exit()

telefoonnummer = input("Telefoonnummer (zonder +31): ")

def BelangrijkeWoorden():
    """
    Verzamelt logistiek-relevante sleutelwoorden over het doelwit.
    Pentesters richten zich op persoonlijke info die mensen in wachtwoorden verwerken.
    """
    namen.append(input("Voornaam: "))
    namen.append(input("Achternaam: "))
    namen.append(input("Gebruikersnaam / bijnaam: "))
    print()
    namen.append(input("Naam partner: "))
    namen.append(input("Naam huisdier: "))
    print()
    # Vanguard-specifieke logistieke keywords
    namen.append(input("Bedrijfsnaam of afdeling (bijv. Vanguard, Operations): "))
    namen.append(input("Stad of haven (bijv. Rotterdam, Amsterdam): "))
    namen.append(input("Favoriete voetbalclub of hobby: "))
    print()
    # Vrije extra keywords
    print("Voeg extra keywords toe (lege regel om te stoppen):")
    while True:
        invoer = input("  > ")
        if invoer == '':
            break
        namen.append(invoer)
    # Verwijder lege strings
    while '' in namen:
        namen.remove('')

def permuteer(woord):
    """
    Genereert alle hoofdletter/kleine-letter combinaties van een woord.
    Werkt met bitmasking: voor elk karakter wordt bepaald of het hoofd- of
    kleine letter is via de bit op positie j in getal i.
    Voorbeeld: 'abc' → 'abc', 'Abc', 'aBc', 'ABc', 'abC', ... (2^3 = 8 varianten)
    """
    n = len(woord)
    mx = 1 << n          # 2^n combinaties
    woord = woord.lower()

    for i in range(mx):
        combinatie = list(woord)
        for j in range(n):
            if (i >> j) & 1:
                combinatie[j] = woord[j].upper()
        tijdelijke_namen.append("".join(combinatie))

def MaakWachtwoordlijst(lijst):
    """Combineert namen met geboortedatum en telefoonnummer op alle posities."""
    for woord in namen:
        for i in range(len(woord) + 1):
            lijst.append(woord[:i] + dag   + woord[i:])
            lijst.append(woord[:i] + maand + woord[i:])
            lijst.append(woord[:i] + jaar  + woord[i:])
            if len(jaar) == 4:
                lijst.append(woord[:i] + jaar[2:] + woord[i:])
            lijst.append(woord[:i] + telefoonnummer + woord[i:])
    if telefoonnummer:
        lijst.append(telefoonnummer)

def SchrijfNaarBestand(lijst):
    with open('passwordlist.txt', 'w') as f:
        for wachtwoord in lijst:
            f.write(f"{wachtwoord}\n")

# ── Hoofdprogramma ──────────────────────────────────────────
BelangrijkeWoorden()

for naam in namen:
    permuteer(naam)

namen = namen + tijdelijke_namen
MaakWachtwoordlijst(wachtwoordlijst)
SchrijfNaarBestand(wachtwoordlijst)

print(f"\nKlaar! {len(wachtwoordlijst)} wachtwoorden opgeslagen in passwordlist.txt")
