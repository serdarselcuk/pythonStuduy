from calendar import monthrange
from math import floor, ceil


YEAR = 2018
MONTH = 8

acildoktorlari = [input ('doktoracil1 : '),input ("doktoracil2 : ")]
AILEHEKIMI = [input("doktoraile1 : "), input("doktoraile2 : ")]

firstday, lmonth  = monthrange(YEAR, MONTH)

def isweekday(day):
    return (firstday + day) % 7 < 5
    
nweekday = 0

for day in range(lmonth):
    if isweekday(day):
        nweekday += 1

#doktorsayisi = int (input('doktor adedi giriniz :' ))
#for sayi in range(doktorsayisi):
 #   doktor.append (input('doktor adini giriniz :' ))


nnobet = int(floor((lmonth * 24 - nweekday * 8 * len(PRATISYEN)) / 24))

pnobet =int(ceil((nweekday * 8) / 24 + nnobet/doktorsayisi))



 #*(len(PRATISYEN) + len(AILEHEKIMI)))

print(nweekday, nnobet, pnobet)