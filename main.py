class Telescope:
    def __init__(self, diametre, focale, oculaires, barlows):
        self.diametre = diametre
        self.focale = focale
        self.oculaires = oculaires
        self.barlows = barlows
        self.zoomMaxTheorique = 2*diametre
        self.zoomMiniTheorique = diametre / 6
        
def initialisation():
    diametre = int(input("Veuillez entrer le diamètre de votre instrument (en mm) : "))
    focale = int(input("Veuillez entrer la longueur focale de votre instrument (en mm) : "))
    print("Le rapport F/D de votre instrument est donc de : " + str(focale/diametre))
    print()
    oculaires = []
    focaleOculaire = -1
    while focaleOculaire != 0:
        focaleOculaire = float(input("Veuillez entrer la focale de votre oculaire (en mm)(0 pour quitter) : "))
        if focaleOculaire != 0:
            champOculaire = int(input("Veuillez entrer le champ de vision apparent de votre oculaire (en degrés) : "))
            oculaires.append((focaleOculaire, champOculaire))
            print("Oculaire n°"+str(len(oculaires))+" ajouté !")
            print()
    barlows = [1]
    zoomBarlow = 1
    while zoomBarlow != 0:
        zoomBarlow = float(input("Veuillez entrer la valeur du zoom de la Barlow (0 pour quitter) : "))
        if zoomBarlow != 0:
            barlows.append(zoomBarlow)
            print("Barlow n°"+str(len(barlows)-1)+" ajouté !")
    telescope = Telescope(diametre, focale, oculaires, barlows)
    seeing = float(input("Veuillez entrer la valeur du seeing lors de l'observation (en seconde d'arc) : "))
    print("La valeur du seeing est de " + str(seeing) + '"')


