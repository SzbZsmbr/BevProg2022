class Team:
    def __init__(self, nev, projekt, szerepkor):
        self._nev = nev
        self._projekt = projekt
        self._szerepkor = szerepkor
        print("--Developer létrehozva--")
    def __str__(self):
        return (self._nev + " a " + self._projekt + "-en dolgozik" + self._szerepkor + "szerepkörben.")
    def __eq__(self, masik):
            return str(self._projekt).lower == (masik._projekt).lower
if __name__ == "__main__":
    dev1 = Team("Ricsi", "SolArch", "Frontend")
    print(dev1)
    dev2 = Team("Angéla", "ZerTeng", "Tesztelő")
    print(dev2)
    dev3 = Team("Peti", "KefERP", "Backend")
    print(dev3)
    dev4 = Team("Éva", "KefERP", "Frontend")
    print(dev4)
    if (dev3 == dev4):
        print(dev3._nev + " és " + dev4._nev + " egy projekten dolgoznak.")