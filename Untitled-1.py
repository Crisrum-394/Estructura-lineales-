class ArrayList:
    def __init__(self, size=100, initial_elements=[]):
        pass
    def __str__(self):
        pass
    def _len_(self):
        pass
    def isEmpty(self):
        pass
    def _getitem_(self, index):
        pass
    def _iter_(self):
        pass
    def _contains_(self, element):
        pass
    def append(self, element):
        pass
    def insert(self,index, element):
        pass
    def remove(self, element):
        pass
    def pop(self, element):
        pass
    def clear(self):
        pass

    lista = ArrayList = (10, [1, 2, 3])

    print(lista)        
    lista.append(4)
    print(lista)        

    lista.insert(1, 10)
    print(lista)        

    lista.remove(2)
    print(lista)        

    print(lista.pop(0)) 
    print(lista)        

    print(3 in lista)   