#Ejercicio Guiado
"""
Desde la empresa “Juegos por comida”, te han solicitado programar el prototipo de
una batalla entre un jugador y un monstruo. Para ello, debes considerar que tanto
los jugadores como los monstruos poseen puntos de vida (HP), puntos de ataque
(ATK) y puntos de defensa (DF), y opcionalmente un arma (solo especificar armas
al crear jugadores), que son asignados al momento de crearse. Además, tanto los
jugadores como los monstruos pueden generar ataques y defenderse.
Para esta demostración, se le solicita generar un script demo.py que genere un
jugador con 500 de HP, 10 de ATK, 5 de DF y una espada. El jugador debe
enfrentarse al monstruo “Bégimo”, el cual tiene 1.000 de HP, 1 de ATK y 8 de DF.
Ambos deben enfrentarse alternadamente en turnos de ataque-defensa, hasta que
alguno de los dos muera (tenga HP igual o menor a 0). 

Los ataques generan un puntaje de ataque (número entero).
● En el caso de los jugadores que tienen un arma, se debe retornar la cantidad de puntos de
ATK más un número al azar entre 1 y 5, en caso contrario solo se retorna los puntos de
ATK.
● En el caso de los monstruos, debe retornar los puntos de ATK más el 1% del HP actual
(retorna un número entero).
La acción de defensa recibe un ataque (número entero) y disminuye el HP.
● En el caso de los jugadores, al ataque recibido se le debe restar un número al azar entre 1
y los puntos de DF, y el resultado de ello (forzar a ser un número entero mayor a 0) se
debe restar al HP.
● En el caso de los monstruos, al ataque recibido se le debe restar los puntos de DF y el
0.1% del HP actual, y el resultado de ello (forzar a ser un número entero mayor a 0) se
debe restar al HP.

Independiente de quien inicie el ataque, el oponente debe defenderse del ataque
recibido, y luego atacar de vuelta al atacante (en caso de que aún tenga HP), quien
a su vez se defenderá de este ataque y luego volverá a atacar (en caso de que aún
tenga HP), y así sucesivamente hasta que alguno de los dos muera (su HP sea
menor o igual a 0).

Aspectos técnicos
Se solicita que tanto Jugador como Monstruo hereden de una clase común Personaje, con el fin de reutilizar el
constructor desde aquella clase. Debe considerar que no pueden existir instancias de Personaje, y que todas las
clases que hereden de ella deben implementar su propio método ataque y defensa. Por el momento, no se debe
aplicar encapsulamiento de los atributos.
"""
from jugador import Jugador
from monstruo import Monstruo

enfrentados = [Jugador(800, 10, 5, "espada"), Monstruo(1000, 1, 8)]
atk = 0

while any(e.hp <= 0 for e in enfrentados) == False:
    for e in enfrentados:
        if atk:
            e.defensa(atk)
        if e.hp > 0:
            atk = e.ataque()
        else:
            print(f"¡Oh no!, el {e.__class__.__name__} ha muerto :(")