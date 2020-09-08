class set_test():
    # initialisaition
    def __init__(self):
        self._value = 0
        pass


    @property  # Getter
    def value(self):
        print("getter call")
        return self._value


    @value.setter  # Setter
    def value(self, new_var):
        print("setter call")
        self._value = new_var


    @value.getter  # getter niveaux 2
    def value(self):
        print("getter call")
        return self._value


if __name__ == "__main__":
    a = set_test()
    z = a.value
    a.value = 2
    pass
