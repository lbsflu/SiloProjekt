def check_value_type(value, name):
    if not (isinstance(value, (int, float)) and value > 0):
        raise ValueError(f"{name} :{value}  type: {type(value)} ist nicht gültig")


class Silo:
    def __init__(self, silonummer: int, kapazitat: float):
        check_value_type(silonummer, "Silonummer")
        check_value_type(kapazitat, "Kapazitat")
        self._bestand = 0.0
        self._set_kapazitat(kapazitat)
        self._set_silonummer(silonummer)

    def auslagern(self, menge: float):
        check_value_type(menge, "Menge")
        if self.get_bestand() - menge >= 0:
            self._set_bestand(self.get_bestand() - menge)
            print(f"Auslagern Silo: {self.get_silonummer()} neu Bestand: %s " % (self.get_bestand()))
        else:
            print(f" Menge zu auslagern {menge} ist groß als bestand: {self.get_bestand()}")

    def einlagern(self, menge: float):
        check_value_type(menge, "Menge")
        aktuell_kapazitat = self.get_kapazitat() - self.get_bestand()

        if 0.0 < aktuell_kapazitat >= menge:
            self._set_bestand(self.get_bestand() + menge)
            print(f"Einlagern Silo: {self.get_silonummer()} neu Bestand: %s " % (self.get_bestand()))
        else:
            print(f" Silo voll. Aktuell kapazitat {aktuell_kapazitat} , menge zu einlagern: {menge}")

    def _set_silonummer(self, silonummer: int):
        self._silonummer = silonummer

    def get_silonummer(self):
        return self._silonummer

    def _set_kapazitat(self, kapazitat):
        self._kapazitat = kapazitat

    def get_kapazitat(self):
        return self._kapazitat

    def _set_bestand(self, menge):
        self._bestand = menge

    def get_bestand(self):
        return self._bestand
