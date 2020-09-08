class hidd:
    def __init__(self):
        self._hidden()
        self.__hidden()
    def _hidden(self):
        print("public")
    def __hidden(self):
        print("privé")

if __name__ == "__main__" :
   a = hidd()
   a._hidden()
   a._hidd__hidden()
   a.__hidden()
