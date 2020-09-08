class glob:
    def __init__(self, new_var):
        self.var  = new_var
        pass
    def print_info(self): 
        print(self.var)
    def info():
        print(" Cette class est une class d'info ")

if __name__ == "__main__" :
   a = glob(2)
   glob.print_info(a)
   glob.info()
