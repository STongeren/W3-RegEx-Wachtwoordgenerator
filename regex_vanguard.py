import re

# Laad het gelekte Vanguard-rapport
with open('vanguard_lek.txt', 'r') as f:
    tekst = f.read()

print("=== VANGUARD LOGISTICS — RegEx Analyse ===\n")

# ── E-mailadressen ──────────────────────────────────────────
email_patroon = r'\b[\w.-]+@[\w.-]+\.\w{2,}\b'
emails = re.findall(email_patroon, tekst)
print(f"E-mailadressen gevonden ({len(emails)}):")
for e in emails:
    print(f"  {e}")

# ── IP-adressen ─────────────────────────────────────────────
ip_patroon = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
ips = re.findall(ip_patroon, tekst)
print(f"\nIP-adressen gevonden ({len(ips)}):")
for ip in ips:
    print(f"  {ip}")

# ── Telefoonnummers ─────────────────────────────────────────
telefoon_patroon = r'\+31\s?\d{2}\s?\d{3}\s?\d{4}'
nummers = re.findall(telefoon_patroon, tekst)
print(f"\nTelefoonnummers gevonden ({len(nummers)}):")
for nr in nummers:
    print(f"  {nr}")

# ── Verdachte domeinen ──────────────────────────────────────
domein_patroon = r'\b[\w-]+\.(?:ru|xyz|tk|ml|ga|cf)\b'
verdacht = re.findall(domein_patroon, tekst)
print(f"\nVerdachte domeinen gevonden ({len(verdacht)}):")
for d in verdacht:
    print(f"  {d}")

print("\n=== Analyse voltooid ===")
