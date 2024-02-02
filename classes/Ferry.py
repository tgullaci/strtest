
class Ferry:
    def __init__(self):
        self.nom = ''
        self.places_voiture_max = 0
        self.places_voiture_restantes = 0
        self.voitures = []
        self.compagnie = ''
        self.trajet = ''
        self.capitaine = None
        self.nombre_cabines = 0
        self.cabines = {}

    def naming_ferry(self, nom):
        self.nom = nom
        return(self.nom)

    def set_place_voiture(self, places_voiture_max):
        self.places_voiture_max = places_voiture_max
        self.places_voiture_restantes = places_voiture_max
        return(places_voiture_max)

    def nommer_capitaine(self, capitaine):
        self.capitaine = capitaine
        return(self.capitaine)

    def definir_nombre_cabines(self, nombre_cabines):
        self.nombre_cabines = nombre_cabines
        return(self.nombre_cabines)

    def attribuer_passager_cabine(self, passager, numero_cabine):
        if numero_cabine <= self.nombre_cabines:
            if numero_cabine not in self.cabines:
                self.cabines[numero_cabine] = [passager]
                return(f"{passager} a été attribué(e) à la cabine {numero_cabine} du ferry {self.nom}.")
            else:
                return(f"La cabine {numero_cabine} du ferry {self.nom} est déjà prise.")
            
        else:
            return(f"La cabine {numero_cabine} n'existe pas sur le ferry {self.nom}.")

    def ajouter_voiture(self, nombre_voitures, nombre_camions):
        nombre_camions *= 3
        if (nombre_voitures + nombre_camions) <= self.places_voiture_restantes:
            self.places_voiture_restantes -= (nombre_voitures + nombre_camions)
            self.voitures.append(nombre_voitures + nombre_camions)
            return(f"{nombre_voitures} voiture(s) et {nombre_camions} camion(s) ont été ajoutée(s) au ferry {self.nom}.")
        else:
            return("Pas assez de places pour ajouter ces voitures.")

    def affecter_compagnie(self, compagnie):
        self.compagnie = compagnie
        return(f"Le ferry {self.nom} a été affecté à la compagnie {compagnie}.")

    def affecter_trajet(self, trajet):
        self.trajet = trajet
        return(f"Le ferry {self.nom} a été affecté au trajet de {trajet}.")

    def afficher_places_restantes(self):
        return self.places_voiture_restantes
        
    def afficher_nom_ferry(self):
        return self.nom

    def afficher_nom_ferry(self):
        return self.nom
