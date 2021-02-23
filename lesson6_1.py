from time import sleep


class TrafficLight:
    __color = "Р§С‘СЂРЅС‹Р№"

    def running(self):
        while True:
            print("Trafficlight is red now!")
            sleep(7)
            print("Trafficlight is yellow now!")
            sleep(2)
            print("Trafficlight is green now!")
            sleep(7)
            print("Trafficlight is yellow now!")
            sleep(2)


trafficlight = TrafficLight()
trafficlight.running()