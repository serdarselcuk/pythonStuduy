


import calendar

yil = int(input('yili giriniz : '))
ay = int(input('ayi giriniz : '))


ilk_gun, uzunluk = calendar.monthrange(yil, ay)

ailehekimleri = [input('doktor adi giriniz : ') for i in range(int(input("aile hekimi sayisi : ")))]
acilhekimleri = [input('doktoradi giriniz : ') for i in range(int(input("acil doktoru sayisi : ")))]
tumhekimler = ailehekimleri + acilhekimleri

HSONU = acilhekimleri * 10
HICI = tumhekimler * 25

nobet_listesi = []


for day_of_month in range(uzunluk):

    day_of_week = (ilk_gun + day_of_month) % 7

    if day_of_week > 4:
        if len(nobet_listesi) > 1 and HSONU[0] == nobet_listesi[-1]:
            nobet_listesi.append(HSONU.pop(1))
        else:
            nobet_listesi.append(HSONU.pop(0))
 
    else:
        if len(nobet_listesi) > 1 and HICI[0] == nobet_listesi[-1]:
            nobet_listesi.append(HICI.pop(1))
        else:
            nobet_listesi.append(HICI.pop(0))
      
from collections import Counter
print(Counter(nobet_listesi))

print(nobet_listesi)
