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
        """Simple comma seperated transmission, client will need to be aware of positions of various data items
        Add any new data items to the end so existing apps are not affected
        """
        try:
            data = []
            data.extend(ac.getCarState(0, acsys.CS.CurrentTyresCoreTemp)) #0-3 - Core tyre temperatures, Degrees celcius
            data.extend(info.physics.tyreWear) #4-7 #tyre wear
            data.extend(ac.getCarState(0, acsys.CS.DynamicPressure)) #8-11 pressure of each tyre in PSI
            data.extend(ac.getCarState(0, acsys.CS.TyreDirtyLevel)) #12-15 amount of dirt on each tyre
            data.append(ac.getCarState(0, acsys.CS.SpeedMS)) #16 speed in metres/sec
            data.append(ac.getCarState(0, acsys.CS.Gear)) #17 gear number
            data.append(ac.getCarState(0, acsys.CS.BestLap)) #18 best lap time in ms
            data.append(ac.getCarState(0, acsys.CS.RPM)) #19 rpm
            data.append(ac.getCarState(0, acsys.CS.LapCount)) #20 lap count
            data.append(ac.getCarState(0, acsys.CS.LapInvalidated)) #21 is lap invalid? 0-no, 1-yes
            data.append(ac.getCarState(0, acsys.CS.LapTime)) #22 current lap time in ms
            data.append(ac.getCarState(0, acsys.CS.LastLap)) #23 last lap in ms
            data.append(ac.getCarState(0, acsys.CS.PerformanceMeter)) #24 delta time in ms from best lap?? (haven't checked)
            data.append(ac.getCarState(0, acsys.CS.Steer)) #25 steering rotation in radians
            data.append(ac.getCarName(0)) #26 name of car being driven by player
            data.append(ac.getTrackName(0)) #27 track name
        except Exception as e:
            ac.console("{}".format(e))
        return ",".join(str(v) for v in data).encode()


class UDPServer(socketserver.BaseRequestHandler):
    """Manager to respond to UDP requests
    """

    def handle(self):
        car = Car.getInstance()
        data = self.request[0].decode().strip()
        if (data == "req"):
            socket = self.request[1]
            socket.sendto(car.marshall(), self.client_address)



