from geopy.geocoders import Nominatim
from geopy import distance

def calcular_distancia(coord1, coord2):
    return round(distance.distance(coord1, coord2).kilometers, 1)

def calcular_duracion(tiempo):
    horas = int(tiempo)
    minutos = int((tiempo - horas) * 60)
    return horas, minutos

def calcular_combustible(distancia):
    return round(distancia / 10, 1)

def obtener_coordenadas(ciudad):
    geolocator = Nominatim(user_agent="my-app")
    location = geolocator.geocode(ciudad)
    return location.latitude, location.longitude

ciudad_origen = input("Ciudad de Origen: ")
ciudad_destino = input("Ciudad de Destino: ")

coord_origen = obtener_coordenadas(ciudad_origen)
coord_destino = obtener_coordenadas(ciudad_destino)

distancia = calcular_distancia(coord_origen, coord_destino)

duracion_horas = distancia / 80
duracion_minutos, duracion_segundos = calcular_duracion(duracion_horas)

combustible = calcular_combustible(distancia)

print("Duración del viaje: {} horas, {} minutos, {} segundos".format(duracion_horas, duracion_minutos, duracion_segundos))
print("Combustible requerido: {} litros".format(combustible))
print("S")

print("Viaje desde {} hasta {}".format(ciudad_origen, ciudad_destino))
print("Distancia: {} km".format(distancia))
print("Duración estimada: {} horas, {} minutos, {} segundos".format(duracion_horas, duracion_minutos, duracion_segundos))
print("Combustible requerido: {} litros".format(combustible))
print("¡Que tenga un buen viaje!")
