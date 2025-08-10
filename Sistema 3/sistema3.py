class Nodo:
    def __init__(self):
        self.hijos = {} 
        self.fin_palabra = False  

class ArbolPrefijos:
    def __init__(self):
        self.raiz = Nodo()
    
    def insertar(self, palabra: str):
        nodo_actual = self.raiz # selecciona el nodo raiz
        for letra in palabra: # recorre cada letra en la palabra ingresada
            if letra not in nodo_actual.hijos: # si la letra no se encuentra en un nodo hijo
                nodo_actual.hijos[letra] = Nodo() # agrega la letra como nodo hijo
            nodo_actual = nodo_actual.hijos[letra]
        nodo_actual.fin_palabra = True # la ultima letra se considera como fin de la palabra
    
    def buscar_por_prefijo(self, prefijo: str) -> list: # devuelve una lista, parametro un prefijo str
        nodo_actual = self.raiz
        
        # Navegar hasta el final del prefijo
        for letra in prefijo:
            if letra not in nodo_actual.hijos:
                return []
            nodo_actual = nodo_actual.hijos[letra]
        
        # Recoger todas las palabras desde este nodo
        palabras = []
        self._recoger_palabras(nodo_actual, prefijo, palabras)
        return palabras
    
    def _recoger_palabras(self, nodo, prefijo_actual, palabras):
        if nodo.fin_palabra:
            palabras.append(prefijo_actual)
        
        for letra, nodo_hijo in nodo.hijos.items():
            self._recoger_palabras(nodo_hijo, prefijo_actual + letra, palabras)



arbol = ArbolPrefijos()

# Insertar palabras
palabras = ["manzana", "manano", "manuel", "banana", "band", "apple"]
for palabra in palabras:
    arbol.insertar(palabra)

print(arbol.buscar_por_prefijo("man"))
