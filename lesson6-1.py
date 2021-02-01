from time import sleep

class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self):
        print(f'The light turned: {TrafficLight.__color[0]}')
        sleep(7)
        print(f'The light turned: {TrafficLight.__color[1]}')
        sleep(2)
        print(f'The light turned: {TrafficLight.__color[2]}')
        sleep(5)
        return my_traffic_light.running()


my_traffic_light = TrafficLight()
my_traffic_light.running()
