from foto import Foto, FotoPerfil
from usuario import Usuario


u = Usuario("correo@correo.com", "123456")
u.agregar_fotos_al_album("foto1.png", 800, 600)
u.agregar_fotos_al_album("foto2.png", 800, 600)
u.agregar_fotos_al_album("foto3.png", 800, 600)
u.agregar_fotos_al_album("foto4.png", 800, 600)
u.agregar_fotos_al_album("foto5.png", 800, 600)
u.agregar_fotos_al_album("foto6.png", 800, 600)

u.actualizar_foto_perfil("foto_perfil.png", 400, 400)
u.reaccionar(u.foto_perfil)

for foto in u.album_fotos:
    u.reaccionar(foto)

for foto in u.album_fotos:
    print(f"Reacciones de la foto: {foto.reacciones}")

print(f"Reacciones de la foto de perfil: {u.foto_perfil.reacciones}")

# Output esperado:
# Reacciones de la foto: 1
# Reacciones de la foto: 0
# Reacciones de la foto: 0
# Reacciones de la foto: 0
# Reacciones de la foto: 0
# Reacciones de la foto: 0
