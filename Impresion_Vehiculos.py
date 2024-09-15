class Main:
    """
    Clase principal que gestiona una flota de vehículos.

    Attributes:
        flota_vehiculos (list): Lista que almacena los vehículos de la flota.
    """
    
    def __init__(self):
        self.flota_vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        self.flota_vehiculos.append(vehiculo)

    def buscar_vehiculo_por_año(self, año):
        return [vehiculo for vehiculo in self.flota_vehiculos if vehiculo.get_año() == año]

    def imprimir_flota(self):
    
        for vehiculo in self.flota_vehiculos:
            print(f"Marca: {vehiculo.get_marca()}, Modelo: {vehiculo.get_modelo()}, "
                  f"Año: {vehiculo.get_año()}, Kilometraje: {vehiculo.get_kilometraje()}, "
                  f"Estado: {vehiculo.get_estado_actual()}, Combustible: {vehiculo.get_tipo_combustible()}")

"""
  Imprime en la consola los detalles de todos los vehículos en la flota.

    Muestra la marca, modelo, año, kilometraje, estado actual y tipo de combustible
    de cada vehículo almacenado en la flota.

        Ejemplo:
            main = Main()
            vehiculo1 = Vehiculo("Toyota", "Corolla", 2020, 15000, "Usado", "Gasolina")
            vehiculo2 = Vehiculo("Tesla", "Model 3", 2022, 5000, "Nuevo", "Eléctrico")
            main.agregar_vehiculo(vehiculo1)
            main.agregar_vehiculo(vehiculo2)
            main.imprimir_flota()

main.imprimir_flota()

# Salida esperada:
# Marca: Toyota, Modelo: Corolla, Año: 2020, Kilometraje: 15000, Estado: Usado, Combustible: Gasolina
# Marca: Tesla, Modelo: Model 3, Año: 2022, Kilometraje: 5000, Estado: Nuevo, Combustible: Eléctrico
"""

