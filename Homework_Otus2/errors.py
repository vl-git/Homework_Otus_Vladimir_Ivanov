class StartError(Exception):
    def __str__(self):
        return 'You need to start engine first'


class BoatStartError(StartError):
    def __str__(self):
        return 'You need to set the sail first'


class VehicleTypeError(TypeError):
    def __str__(self):
        return 'Invalid method for vehicle without fuel engine'
