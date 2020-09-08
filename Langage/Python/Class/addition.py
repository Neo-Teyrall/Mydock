import sys
import traceback 
class addition():
    def __init__(self, new_x, new_y):
        self.x = new_x
        self.y = new_y 
        pass

    def __add__(self,add):
        if not isinstance(add, addition) :
            traceback.print_stack()
            sys.exit("Error: is not addditon class. Addition Impossible ")
        return addition(self.x + add.x,
                        self.y + add.y )
    #def __mul__(self):
    #def __sub__(self):
    #def __mul__(self):
    #def __floodiv__(self):
    #def __truediv__(self):

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

if __name__ == "__main__" :
   a = addition(2,2)
   b = addition(4,4)
   print(a)
   print(b)
   a += b
   print(a)
   a += 1 # Erreur
