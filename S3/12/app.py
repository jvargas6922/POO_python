from jugador import Jugador
from monstruo import Monstruo









# Se crea un objeto de la clase Jugador
m = Monstruo(hp=1000, atk=1, df=8, nombre="Bégimo")
# Se llama al método mostrar_dialogo
m.mostrar_dialogo("GRAAAWR")

# Se crea una lista con un objeto de la clase Jugador y un objeto de la clase Monstruo
enfrentados = [Jugador(500, 10, 5, "espada"), m]
atk = 0

# Se realiza un ciclo que termina cuando la vida de uno de los personajes llega a 0
while any(e.hp <= 0 for e in enfrentados) == False:
    # Se recorre la lista de personajes
    for e in enfrentados:
        # Se ataca al personaje
        if atk:
            # Se llama al método defensa
            e.defensa(atk)
        if e.hp > 0:
            # Se llama al método ataque
            atk = e.ataque()
        else:
            # Se muestra un mensaje dependiendo de si el personaje es un monstruo o un jugador
            #se evalua con la funcion isinstance si el objeto es una instancia de la clase Monstruo
            if isinstance(e, Monstruo):
                print("¡Felicidades!, ¡Haz ganado la batalla")
            #se evalua con la funcion isinstance si el objeto es una instancia de la clase Jugador
            elif isinstance(e, Jugador):
                print("¡Oh no!, haz perdido la batalla :(")