import urllib.request
import socket

def grab_http_banner(url):
    """Haal HTTP-headers op van een webserver (banner grabbing via HTTP)."""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        response = urllib.request.urlopen(req, timeout=5)
        print(f"\n=== Banner: {url} ===")
        for header, value in response.getheaders():
            print(f"  {header}: {value}")
    except Exception as e:
        print(f"Fout bij {url}: {e}")

def grab_tcp_banner(host, port):
    """Haal een ruwe TCP-banner op (bijv. voor SSH of FTP)."""
    try:
        s = socket.socket()
        s.settimeout(3)
        s.connect((host, port))
        banner = s.recv(1024).decode(errors="ignore").strip()
        s.close()
        print(f"\n=== TCP Banner {host}:{port} ===")
        print(f"  {banner}")
    except Exception as e:
        print(f"  Geen banner op {host}:{port} - {e}")

# ── Test met logistieke websites ────────────────────────────
urls = [
    "https://www.maersk.com",
    "https://www.fedex.com",
]

for url in urls:
    grab_http_banner(url)

# ── Optioneel: TCP banner op bekende poorten ────────────────
# Alleen gebruiken op systemen waarvoor je toestemming hebt!
# grab_tcp_banner("scanme.nmap.org", 22)   # SSH banner (legale testsomgeving)
