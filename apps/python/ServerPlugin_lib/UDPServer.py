import socketserver
import ac
import acsys
from sim_info import info

class Car:
    inst = None

    @staticmethod
    def getInstance():
        """Should use this static method to get a Car object, no need for multiple instances"""
        if Car.inst is None: Car.inst = Car()
        return Car.inst

    def __init__(self):
        pass

    def marshall(self):
        """Simple comma seperated transmission, client will need to be aware of positions of various data items"""
        data = []
        data.extend(ac.getCarState(0, acsys.CS.CurrentTyresCoreTemp)) #0-3 - Core tyre temperatures, Degrees celcius
        data.extend(info.physics.tyreWear) #4-7 #tyre wear
        return ",".join(data).encode()


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



