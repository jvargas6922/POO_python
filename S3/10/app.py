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