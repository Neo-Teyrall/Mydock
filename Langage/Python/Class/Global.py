class Global():
    count = 0 # global 
    def __init__(self):
        Global.count += 1 # OUI #
        self.count += 1 # NON #
        print(Global.count, " attention ", self.count)
        pass


if __name__ == "__main__" :
   a = Global()
   b = Global()
   c = Global()

