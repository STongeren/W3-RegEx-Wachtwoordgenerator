import re
import sys

# Probeer eerst Selenium (vangt ook JavaScript-gegenereerde content)
# Installeren: pip install selenium
# + download ChromeDriver: https://chromedriver.chromium.org/downloads

GEBRUIK_SELENIUM = True  # Zet op False als je geen Selenium hebt

def haal_html_op_selenium(url):
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    import time

    opties = Options()
    opties.add_argument("--headless")          # geen zichtbaar browservenster
    opties.add_argument("--disable-gpu")
    opties.add_argument("--no-sandbox")
    opties.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")

    driver = webdriver.Chrome(options=opties)
    driver.get(url)
    time.sleep(2)  # wacht tot JavaScript geladen is
    html = driver.page_source
    driver.quit()
    return html

def haal_html_op_urllib(url):
    import urllib.request
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    )
    ht = urllib.request.urlopen(req, timeout=10)
    return ht.read().decode('utf-8')

# ── Hoofdprogramma ──────────────────────────────────────────────
url = input("Voer de URL in: ")

print(f"\nPagina ophalen: {url}")
try:
    if GEBRUIK_SELENIUM:
        html = haal_html_op_selenium(url)
        print("(geladen via Selenium — JavaScript-content wordt meegenomen)")
    else:
        html = haal_html_op_urllib(url)
        print("(geladen via urllib — JavaScript-content wordt NIET meegenomen)")
except Exception as e:
    print(f"Fout: {e}")
    sys.exit(1)

# Verbeterd patroon: vangt ook domeinen met koppeltekens
email_patroon = re.compile(r'\b[\w.-]+@[\w.-]+\.\w{2,}\b')
gevonden = list(set(re.findall(email_patroon, html)))  # set() verwijdert duplicaten

if gevonden:
    print(f"\nGevonden e-mailadressen ({len(gevonden)}):")
    for email in sorted(gevonden):
        print(f"  {email}")
else:
    print("\nGeen e-mailadressen gevonden in de HTML.")
    print("Mogelijke oorzaken:")
    print("  - E-mailadressen worden door JavaScript geladen (gebruik Selenium)")
    print("  - E-mailadressen staan als afbeelding op de pagina")
    print("  - De site gebruikt mailto: links die anders worden gecodeerd")
