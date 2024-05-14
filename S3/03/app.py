"""
Ejemplo Guiado
"""
"""
Desde un emprendimiento, se te ha solicitado comenzar el diseño de la estructura
de clases para sus productos. Por ahora, se considera solamente el caso de los
chocolates, donde existen, por el momento, solo los chocolates amargos (en el
futuro habrá más tipos específicos, pero considera que no pueden existir
chocolates “a secas”). Todos los chocolates deben tener un porcentaje de cacao
específico, de acuerdo a su tipo, siendo el de los chocolates amargos entre 75% y
85%.
A su vez, también existe una variedad de chocolate amargo sin gluten. Se debe
considerar que existirán en el futuro otros productos, además de los chocolates,
que también serán sin gluten.
"""

from chocolate import ChocolateAmargo
c = ChocolateAmargo(0.3)
print(c.porc_cacao)