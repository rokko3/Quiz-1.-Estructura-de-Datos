class nodo:
    def __init__(self):
        self.children = {}  # usamos un diccionario para almacenar 'clave' - valor 
        self.endOfWord = False  # nos permite indicar si el caracter es el final de una palabra

class arbol:
    def __init__(self):
        self.root = nodo()  

    def insert(self, word: str) -> None: # funcion void para insertar, pidiendo que la palabra sea de tipo string
        nodo_actual = self.root
        for c in word:
            if c not in nodo_actual.children:
                nodo_actual.children[c] = nodo()  
            nodo_actual = nodo_actual.children[c]  
        nodo_actual.endOfWord = True  

    def search(self, word: str) -> bool: #devuelve true o false
        nodo_actual = self.root
        for c in word:
            if c not in nodo_actual.children:
                return False  # el caracter no existe
            nodo_actual = nodo_actual.children[c]
        return nodo_actual.endOfWord  # final de la palabra

    def startsWith(self, prefijo: str) -> bool: # devuelve true o falso
        if self.search(prefijo):
            nodo_actual = self.root
            for c in prefijo:
                if c not in nodo_actual.children:
                    return False
                nodo_actual = nodo_actual.children[c]
            return True 


arbol = arbol()
    
palabras = ["manzana", "app", "application", "banana", "band"]
for word in palabras:
    arbol.insert(word)

# pruebas
print(arbol.search("apple"))     
print(arbol.search("app"))       
print(arbol.search("application")) 
print(arbol.search("ban"))     
               
# Pruebas de prefijo
print(arbol.startsWith("ban"))   # True
print(arbol.startsWith("app"))   # True
print(arbol.startsWith("orange")) # False