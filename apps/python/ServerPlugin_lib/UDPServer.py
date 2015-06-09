import socketserver
import ac
import acsys

class Car:
    inst = None

    @staticmethod
    def getInstance():
        """Should use this static method to get a Car object, no need for multiple instances"""
        if Car.inst is None: Car.inst = Car(1)
        return Car.inst

    def __init__(self, a):
        pass

    def getCoreTyreTemps(self):
        return ac.getCarState(0, acsys.CS.CurrentTyresCoreTemp)

    def update(self):
        coreTemps = ac.getCarState(0, acsys.CS.CurrentTyresCoreTemp)

    def marshall(self):
        return "--car-details--".encode()


class UDPServer(socketserver.BaseRequestHandler):
    """...
    """

    def handle(self):
        car = Car.getInstance()
        data = self.request[0].decode().strip()
        if (data == "req_data"):
            socket = self.request[1]
            car.update()
            socket.sendto(car.marshall(), self.client_address)



