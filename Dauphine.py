def main(): 
    print("Veuillez entrer une chaîne de caractères")
    chaineDeCar = str(input())
    nombreDeMin = combienDeLettreMinuscules(chaineDeCar)
    print(str(nombreDeMin))

def combienDeLettreMinuscules(chaineDeCar): 
    ''' Méthode permettant le renvoie du nombre de lettres minuscules dans une chaîne de caractères passée en paramètre. '''
    incrementationCar = 0
    if(len(chaineDeCar) > 0):
        for c in chaineDeCar:
            if c.islower():
                incrementationCar += 1           
    return incrementationCar

if __name__ == "__main__":
    main()