#VideoJuego
class Personaje():
    def __init__(self,nombre,clase,vida,fuerza,poder,habilidad_especial):
        self.nombre = nombre
        self.clase = clase
        self.vida = vida
        self.fuerza = fuerza
        self.poder = poder
        self.habilidad_especial = habilidad_especial
        
    def estado(self):
        print(f"{self.nombre} es de clase {self.clase}, tiene {self.vida} HP, {self.fuerza} de fuerza, {self.poder} de poder.")    
    
    def atacar(self):
        print(f"{self.nombre} está atacando...")
        
    def defender(self):
        print(f"{self.nombre} se está defendiendo...")    
        
    def tomar_pocion(self):
        print(f"{self.nombre} se está tomando una poción de vida y recupera su salud...")   
        
    def muerte(self):
        print(f"{self.nombre} ha muerto.") 
        
    def usar_habilidad(self):
        print(f"{self.nombre}, está usando {self.habilidad_especial}...")            



        
mago = Personaje("Wizzard","Mago",300, 70, 500,"Bola de fuego")   
guerrero = Personaje("Cronos","Guerrero",500, 90, 300,"Danza de espadas") 



print("========================Presentado los personajes============================")
mago.estado()
guerrero.estado()  
print("========================Que comience la lucha================================")
mago.atacar()
mago.usar_habilidad()
guerrero.defender()
guerrero.tomar_pocion()
guerrero.atacar()
guerrero.usar_habilidad()
mago.muerte()
print(f"El victorioso fué el {guerrero.nombre}, felicidades!!!")
