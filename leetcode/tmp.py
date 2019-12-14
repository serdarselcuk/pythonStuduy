

class Hasta:

    def __init__(self, isim, soyisim, yas, durum):
        self.isim = isim.title()
        self.soyisim = soyisim
        self.yas = yas
        self.dogum
        self.email


serdar = Hasta("serdar", "Selcuk", 38, "Saglikli")
sencer = Hasta("Sencer", "Selcuk", 32, "Saglikli")

def email_at(hasta):
    print(f"Sayin {hasta.isim} {hasta.soyisim},\n")
    print(f"{2019 - hasta.dogum_yili}")
"Sayin Serdar Selcuk,

39. dogum gununuz kutlu olsun"