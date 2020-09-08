class TType :
    pass

class TType2 :
    def __str__(self):
        return "moi"
    def __type__(self):
        return "ici "
    pass



if __name__ == "__main__" :
    a = TType()
    b = TType2()
    print("a : ",type(a),"\nb : ",  type(b))
