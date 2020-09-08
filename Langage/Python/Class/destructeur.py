class dest :
    def __init__(self):
        print("Je suis construis")


    # A la destruction de l'objet cette fonction est appelé
    def __del__(self):
        print("Je suis détruit")

if __name__ == "__main__" :
   a = dest()
