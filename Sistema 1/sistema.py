class Sistema1:
    def __init__(self):
        self.pila_delantera = [] 
        self.pila_trasera = []   
        self.pagina_actual = None

    def visitar_pagina(self, url):
        if self.pagina_actual:
            self.pila_trasera.append(self.pagina_actual)
        self.pagina_actual = url
        self.pila_delantera.clear() 
        print("Visitando:"+ self.pagina_actual)

    def retroceder(self):
        if not self.pila_trasera:
            print("Error, no existe pagina para retroceder")
            return
        self.pila_delantera.append(self.pagina_actual)
        self.pagina_actual = self.pila_trasera.pop()
        print("Retrocediendo a:"+ self.pagina_actual)

    def avanzar(self):
        if not self.pila_delantera:
            print("Error, no existe pagina para avanzar")
            return
        self.pila_trasera.append(self.pagina_actual)
        self.pagina_actual = self.pila_delantera.pop()
        print("Avanzando a:" + self.pagina_actual)


nav = Sistema1()
nav.visitar_pagina("pagina1.com")
nav.visitar_pagina("pagina2.com")
nav.visitar_pagina("pagina3.com")

nav.retroceder()
nav.retroceder()
nav.avanzar()
nav.avanzar()
nav.avanzar() 
