import re

text = 'Dit is een tekst met een e-mailadres: hendrikeetperen@gmail.com.'
match = re.search(r'\w+@\w+\.\w+', text)
if match:
    print('E-mailadres gevonden:', match.group(0))
else:
    print('Geen e-mailadres gevonden')
