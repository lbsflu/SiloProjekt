import random
from silo import Silo
from siloVerwaltung import SiloVerwaltung

if __name__ == '__main__':
    silo_verwaltung = SiloVerwaltung

    silo_list = []
    number = 1
    while number < 10:
        globals()['silo_%s' % number] = Silo(number, round(random.uniform(80.00, 100.00)))

        print(globals()['silo_%s' % number].__str__())
        globals()['silo_%s' % number].einlagern(round(random.uniform(10.00, 80.00)))
        globals()['silo_%s' % number].einlagern(round(random.uniform(10.00, 80.00)))

        silo_list.append(globals()['silo_%s' % number])

        number += 1

    siloVerwaltung = SiloVerwaltung(silo_list)

    print(f" Gesamt kapazitat:{siloVerwaltung.get_silo_gesamt_kapazitat()}")

    print(f" Gesamt bestand:{siloVerwaltung.get_silo_gesamt_bestand()}")

    print(f" Gesamt Silos:{siloVerwaltung.get_silo_total()}")

    print(f" Gültige Kapazitat:{siloVerwaltung.get_gultig_kapazitat()}")


