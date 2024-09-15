class Main:
    """
    Clase principal que gestiona una flota de vehículos.

    Attributes:
        flotaVehiculos (list): Lista que almacena los vehículos de la flota.
    """
    
    def __init__(self):
        self.flotaVehiculos = []

    def agregarVehiculo(self, vehiculo):
        self.flotaVehiculos.append(vehiculo)

    def buscarVehiculoPorAño(self, año):
        """
        Busca y devuelve una lista de vehículos que coincidan con un año específico.
        """
        return [vehiculo for vehiculo in self.flotaVehiculos if vehiculo.getAño() == año]

    def imprimirFlota(self):
        """Imprime en la consola los detalles de todos los vehículos en la flota, incluyendo color y potencia.""""
      
        if not self.flotaVehiculos:
            print("No hay vehículos registrados en la flota.")
        else:
            for vehiculo in self.flotaVehiculos:
                print(
                    f"Marca: {vehiculo.getMarca()}, Modelo: {vehiculo.getModelo()}, Año: {vehiculo.getAño()}, "
                    f"Kilometraje: {vehiculo.getKilometraje()}, Estado: {vehiculo.getEstadoActual()}, "
                    f"Combustible: {vehiculo.getTipoCombustible()}, Color: {vehiculo.getColor()}, "
                    f"Potencia: {vehiculo.getPotencia()} HP"
                )

"""
Muestra la marca, modelo, año, kilometraje, estado actual, tipo de combustible,
color y potencia de cada vehículo almacenado en la flota.

Ejemplo:
    main = Main()
        vehiculo1 = Vehiculo("Toyota", "Corolla", 2020, 15000, "Usado", "Gasolina", "Rojo", 130)
        vehiculo2 = Vehiculo("Tesla", "Model 3", 2022, 5000, "Nuevo", "Eléctrico", "Blanco", 250)
        main.agregarVehiculo(vehiculo1)
        main.agregarVehiculo(vehiculo2)
        main.imprimirFlota()

        Salida esperada:
            Marca: Toyota, Modelo: Corolla, Año: 2020, Kilometraje: 15000, 
            Estado: Usado, Combustible: Gasolina, Color: Rojo, Potencia: 130 HP
            Marca: Tesla, Modelo: Model 3, Año: 2022, Kilometraje: 5000, 
            Estado: Nuevo, Combustible: Eléctrico, Color: Blanco, Potencia: 250 HP
"""
