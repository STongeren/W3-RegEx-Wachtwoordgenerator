# RegEx, OSINT and targeted wordlists

Python exercises from my Cyber Security programme at the Hogeschool van Amsterdam (week 3: regular expressions). The case is a fictional company, Vanguard Logistics, whose internal incident report has leaked.

| Script | What it does |
|---|---|
| `regex_vanguard.py` | Pulls e-mail addresses, IP addresses, phone numbers and suspicious domains out of the leaked report (`vanguard_lek.txt`) with regular expressions (suspicious domains are matched on risky TLDs such as .ru and .xyz) |
| `email_finder.py` | Scrapes a web page (Selenium for JavaScript pages, plain HTTP as fallback) and lists every e-mail address it finds |
| `banner_grabber.py` | Grabs HTTP and raw TCP banners (SSH, FTP) to see which software a server announces |
| `PasswordListGenerator_vanguard.py` | Builds a targeted wordlist from personal details such as names, birth date and phone number, to show why passwords based on personal facts are weak. Adapted from [utpalbalse/PasswordListGenerator](https://github.com/utpalbalse/PasswordListGenerator) |
| `expressie.py` | The smallest possible RegEx example |

## Lessons

- An attacker needs only one leaked document to get names, internal IPs and an org chart for a phishing campaign.
- Passwords built from a birth date or a pet's name fall to a wordlist of a few thousand guesses.

All names, addresses and numbers in `vanguard_lek.txt` are made up. Only use these tools on systems you own or are allowed to test. Comments and output are in Dutch.

## Run

```
pip install selenium
python regex_vanguard.py
python PasswordListGenerator_vanguard.py   # writes passwordlist.txt
```
