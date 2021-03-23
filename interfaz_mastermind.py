#Programando clases y obketos
#clase
class Lapiz:
    #atributos con init
    def __init__(self, color, borrador, grafito):
        color = color  
        contiene_borrador = norrador
        usa_grafito = grafito

    
    #Metodos
    def dibujar(self):
        print("Este lapiz esta dibujando.")

    def borrar(self):
        if self.es_valido_para_borrar(): #invocar un metodo
            print("El lapiz esta borrando.")
        else:
            print("No es posible borrar.")

    def es_valido_para_borrar(self):
        return self.contiene_borrador #invocar un atributo

#objeto
lapiz_generico = Lapiz("Verde", True, True)
lapiz_generico.dibujar()
lapiz_generico.borrar()
