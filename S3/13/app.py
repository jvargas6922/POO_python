#EJERCICIO GUIADO
"""
Requerimientos
1. En un archivo membresia.py, crear la clase que permita definir los atributos de
instancia y comportamiento de todas las membresías. Considere:
(2 Puntos)
    a. Utilice abstracción para definir el o los comportamientos requeridos (puede
    definir también métodos no abstractos).
    b. Utilice encapsulamiento para los atributos de instancia. Declare las
    propiedades que estime necesarias según lo solicitado.
2. En el mismo archivo, crear la clase que permita crear instancias de membresías de
tipo Gratis. Considere:
(2 Puntos)
    a. Heredar la o las clases necesarias para evitar repetir implementaciones.
    b. Definir los atributos de clase necesarios.
    c. Definir los métodos necesarios (en caso de que se justifique).
    d. Sobrescribir los métodos necesarios (en caso de que se justifique).
3. En el mismo archivo, crear la clase que permita crear instancias de membresías de
tipo Básica. Considere:
(2 Puntos)
    a. Heredar la o las clases necesarias para evitar repetir implementaciones.
    b. Definir los atributos de clase necesarios.
    c. Definir los métodos necesarios (en caso de que se justifique).
    d. Sobrescribir los métodos necesarios (en caso de que se justifique).

    Tip: Puede ser útil el uso de isinstance en para establecer los días de regalo.
4. En el mismo archivo, crear la clase que permita crear instancias de membresías de
tipo Familiar. Considere:
(2 Puntos)
    a. Heredar la o las clases necesarias para evitar repetir implementaciones.
    b. Definir los atributos de clase necesarios.
    c. Definir los métodos necesarios (en caso de que se justifique).
    d. Sobrescribir los métodos necesarios (en caso de que se justifique).

5. En el mismo archivo, crear la clase que permita crear instancias de membresías de
tipo Sin Conexión. Considere:
(1 Punto)
    a. Heredar la o las clases necesarias para evitar repetir implementaciones.
    b. Definir los atributos de clase necesarios.
    c. Definir los métodos necesarios (en caso de que se justifique).
    d. Sobrescribir los métodos necesarios (en caso de que se justifique).
6. En el mismo archivo, crear la clase que permita crear instancias de membresías de
tipo Pro. Considere:
(1 Punto)
    a. Heredar la o las clases necesarias para evitar repetir implementaciones.
    b. Definir los atributos de clase necesarios.
    c. Definir los métodos necesarios (en caso de que se justifique).
    d. Sobrescribir los métodos necesarios (en caso de que se justifique).
"""
from membresia import Membresia, Gratis



g = Gratis("correo@prueba.cl", "123 456 789")
print(type(g))
b = g.cambiar_suscripcion(1)
print(type(b))
f = b.cambiar_suscripcion(2)
print(type(f))
sc = f.cambiar_suscripcion(3)
print(type(sc))
pro = sc.cambiar_suscripcion(4)
print(type(pro))
g2 = pro.cancelar_suscripcion()
print(type(g2))