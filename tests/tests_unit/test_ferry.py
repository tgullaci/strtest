import os, sys
import unittest
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from classes.Ferry import Ferry

class test_ferry(unittest.TestCase):


    def test_afficher_places_restantes(self):
        ferry = Ferry()
        ferry.set_place_voiture(50)
        rslt=ferry.afficher_places_restantes()
        attendu=50
        self.assertEqual(rslt,attendu)

    def test_afficher_places_restantes_apres_ajout_voiture(self):
        ferry = Ferry()
        ferry.set_place_voiture(50)
        ferry.naming_ferry('Ferry1')
        ferry.ajouter_voiture(1, 0)
        rslt=ferry.afficher_places_restantes()
        attendu=49
        self.assertEqual(rslt,attendu)

    def test_ajouter_voiture_camions(self):
        ferry = Ferry()
        ferry.set_place_voiture(50)
        ferry.naming_ferry('Ferry1')
        rslt1=ferry.ajouter_voiture(5, 0)
        attendu="5 voiture(s) et 0 camion(s) ont été ajoutée(s) au ferry Ferry1."
        self.assertEqual(rslt1,attendu)
        rslt2=ferry.ajouter_voiture(10, 2)
        attendu="10 voiture(s) et 6 camion(s) ont été ajoutée(s) au ferry Ferry1."
        self.assertEqual(rslt2,attendu)

    def test_ajouter_voiture_error_place_limite(self):
        ferry = Ferry()
        ferry.set_place_voiture(50)
        ferry.naming_ferry('Ferry1')
        rslt=ferry.ajouter_voiture(21, 23)
        attendu="Pas assez de places pour ajouter ces voitures."
        self.assertEqual(rslt,attendu)

    def test_afficher_nom_ferry(self):
        ferry = Ferry()
        ferry.set_place_voiture(50)
        ferry.naming_ferry('Ferry1')
        rslt=ferry.afficher_nom_ferry()
        attendu="Ferry1"
        self.assertEqual(rslt,attendu)

    def test_afficher_nom_ferry_error(self):
        ferry = Ferry()
        ferry.set_place_voiture(50)
        ferry.naming_ferry('Ferry1')
        rslt=ferry.afficher_nom_ferry()
        attendu="Ferry2"
        self.assertNotEqual(rslt,attendu)

    def test_affecter_compagnie(self):
        ferry = Ferry()
        ferry.naming_ferry('Ferry1')
        rslt=ferry.affecter_compagnie('BrestFerry')
        attendu="Le ferry Ferry1 a été affecté à la compagnie BrestFerry."
        self.assertEqual(rslt,attendu)

    def test_affecter_trajet(self):
        ferry = Ferry()
        ferry.naming_ferry('Ferry1')
        rslt=ferry.affecter_trajet('Brest Lisbonne')
        attendu="Le ferry Ferry1 a été affecté au trajet de Brest Lisbonne."
        self.assertEqual(rslt,attendu)

    def test_affecter_compagnie_error(self):
        ferry = Ferry()
        ferry.naming_ferry('Ferry1')
        rslt=ferry.affecter_compagnie('BrestFerry')
        attendu="Brest"
        self.assertNotEqual(rslt,attendu)

    def test_affecter_trajet_error(self):
        ferry = Ferry()
        ferry.naming_ferry('Ferry1')
        rslt=ferry.affecter_trajet('Brest Lisbonne')
        attendu="Brest"
        self.assertNotEqual(rslt,attendu)

    def test_nommer_capitaine(self):
        ferry = Ferry()
        ferry.naming_ferry('Ferry1')
        rslt=ferry.nommer_capitaine('Alexy le pirate')
        attendu="Alexy le pirate"
        self.assertEqual(rslt,attendu)

    def test_nommer_capitaine_error(self):
        ferry = Ferry()
        ferry.naming_ferry('Ferry1')
        rslt=ferry.nommer_capitaine('Alexy le pirate')
        attendu="Alexy"
        self.assertNotEqual(rslt,attendu)

    def test_definir_nombre_cabines(self):
        ferry = Ferry()
        ferry.naming_ferry('Ferry1')
        rslt=ferry.definir_nombre_cabines(200)
        attendu=200
        self.assertEqual(rslt,attendu)

    def test_definir_nombre_cabines_error(self):
        ferry = Ferry()
        ferry.naming_ferry('Ferry1')
        rslt=ferry.definir_nombre_cabines('')
        attendu=200
        self.assertNotEqual(rslt,attendu)

    def test_attribuer_passager_cabine(self):
        ferry = Ferry()
        ferry.naming_ferry('Ferry1')
        ferry.definir_nombre_cabines(200)
        rslt=ferry.attribuer_passager_cabine('Morgane', 3)
        attendu='Morgane a été attribué(e) à la cabine 3 du ferry Ferry1.'
        self.assertEqual(rslt,attendu)
        rslt=ferry.attribuer_passager_cabine('Morgane', 3)
        attendu='La cabine 3 du ferry Ferry1 est déjà prise.'
        self.assertEqual(rslt,attendu)

if __name__ == "__main__":
    print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    unittest.main()

