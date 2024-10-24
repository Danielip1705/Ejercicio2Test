
def formulaVel(cad1:str,cad2:str):
   #Declaracion de variables
    desplazamiento=0
    tiempo=0
    velocidad=0
    #Condicional para sacar la primera letra, 
    # y asignarla a la unidad correspondiente de la cadena 1
    if cad1[0].upper()=="D":
        desplazamiento=int(cad1[2:])
    elif cad1[0].upper()=="T":
        tiempo=int(cad1[2:])
    elif cad1[0].upper()=="V":
        velocidad=int(cad1[2:])
    #Condicional para sacar la primera letra, 
    # y asignarla a la unidad correspondiente de la cadena 2
    if cad2[0].upper()=="D":
        desplazamiento=int(cad2[2:])
    elif cad2[0].upper()=="T":
        tiempo=int(cad2[2:])
    elif cad2[0].upper()=="V":
        velocidad=int(cad2[2:])
    #Condicionales para sacar el resultado segun la formula para sacar la velocidad, tiempo
    # y desplazamiento.
    if desplazamiento!=0 and tiempo !=0:
        velocidad = int(desplazamiento/tiempo)
        result ="V="+str(velocidad)
    elif desplazamiento!=0 and velocidad!=0:
            if desplazamiento>velocidad:
                tiempo = int(desplazamiento/velocidad)
            elif velocidad>desplazamiento:
                tiempo = int(desplazamiento/velocidad)
            result ="T="+str(tiempo)
    elif tiempo!=0 and velocidad!=0:
        desplazamiento = int(tiempo*velocidad)
        result ="D="+str(desplazamiento)

    return result
    
def main():
   print(formulaVel("V=8", "D=32"))

if __name__ == "__main__":
    main()