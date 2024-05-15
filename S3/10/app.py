"""
funcion isintance:
La función isinstance recibe como argumentos un objeto y una clase y devuelve True si el objeto es una instancia de dicha clase o de una subclase de ella.

"""


from pelota import PelotaDeFutbol, PelotaDeTenis

pdf = PelotaDeFutbol("Blanco y Negro", 15)
pdt = PelotaDeTenis()
pelotas = [pdf, pdf, pdt, pdt, pdf]
for p in pelotas:
    if isinstance(p, PelotaDeTenis) == False:
        p.color = "Roja"
    if isinstance(p, PelotaDeFutbol):
        p.hacer_pase("jugador 2", 3)
    elif isinstance(p, PelotaDeTenis):
        p.hacer_saque(2, 3)

"""
lo que se evalua en el desarrollo es la definicion de la funcion
si la clase que recibe es una instancia de dicha clase("es hacer validaciones de la clase que se recibe como argumento en la funcion")
"""