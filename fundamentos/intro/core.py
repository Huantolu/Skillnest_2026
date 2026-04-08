# Ranking de puntajes de un torneo de eSports
puntajes = [ [1000, 1500, 2000], [300, 700, 1400] ]
puntajes[1][0] = 600
print(puntajes)
# Lista de creadores de contenido en una plataforma de streaming
streamers = [
   {"nombre": "GameNinjaPro", "seguidores": 250000},
   {"nombre": "PixelWarrior", "seguidores": 180000}
]
streamers[0]["nombre"] = "EliteGamerX"
print(streamers)

# Eventos en distintas ciudades del mundo
eventos = {
   "Estados Unidos": ["Los Ángeles", "Nueva York", "Las Vegas"],
   "España": ["Madrid", "Barcelona", "Valencia"]
}
eventos["Estados Unidos"][2]= "San Francisco"
print(eventos)

# Coordenadas de la sede de un torneo internacional
ubicacion = [
   {"latitud": 34.052235, "longitud": -118.243683}
]
ubicacion[0]["latitud"]= "40.712776"
print(ubicacion)


#Diccionario
def iterar_diccionarios(streamers):
    for elemento in streamers:
       print(f"Nombre - {elemento["nombre"]}, Seguidores - {elemento["seguidores"]}")
iterar_diccionarios(streamers)
print()

#obtener valores
def obtener_valores(clave, lista):
    for diccionario in lista:
        print(diccionario[clave])

obtener_valores("nombre", streamers)
obtener_valores("seguidores", streamers)
print()


#Categorias de juegos
categorias = {
   "juegos_populares": [
      "Fortnite", 
      "Minecraft", 
      "Valorant", 
      "GTA V",
   ],
   "ciudades_eventos": [
      "Nueva York",
      "Madrid",
      "Tokio",
   ]
}


#muestra de informacion
def mostrar_informacion(diccionario):
    for clave, lista in diccionario.items():
        print(f"{len(lista)} {clave.upper()}")
        for elemento in lista:
            print(elemento)
        print()

mostrar_informacion(categorias)