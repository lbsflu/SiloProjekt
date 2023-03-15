def check_menge(menge):
    return bool(type(menge) is float and menge > 0.0)


def error_print(menge):
    print(f"Die Menge: {menge} is falsch.")


class Silo:
    def __init__(self, silonummer: int, kapazitat: float):
        self._kapazitat = 0.0
        self._silonummer = 0
        self._bestand = 0.0
        self._set_kapazitat(kapazitat)
        self._set_silonummer(silonummer)

    def auslagern(self, menge: float):
        if check_menge(menge):
            if self.get_bestand() - menge > 0:
                self._set_bestand(self.get_bestand() - menge)
                print(f"auslagern New amount stock: %s " % (self.get_bestand()))
            else:
                error_print(menge)
        else:
            error_print(menge)

    def einlagern(self, menge: float):
        if check_menge(menge):
            if self.get_kapazitat() - self.get_bestand() > 0.0:
                neue_bestand = self.get_bestand() + menge
                self._set_bestand(neue_bestand)
                print(f"Neu Bestand: %s " % (self.get_bestand()))
            else:
                print(f" Silo voll. Die menge:  {error_print(menge)}.")
        else:
            error_print(menge)

    def _set_silonummer(self, silonummer):
        self._silonummer = silonummer

    def get_silonummer(self):
        return self._silonummer

    def _set_kapazitat(self, kapazitat):
        self._kapazitat = kapazitat

    def get_kapazitat(self):
        return self._kapazitat

    def _set_bestand(self, menge):
        self._bestand += menge

    def get_bestand(self):
        return self._bestand
