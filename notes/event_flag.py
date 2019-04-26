import threading
import time


event = threading.Event()


def lighter():
    count = 0
    event.set()
    while True:
        if 5 < count <= 10:
            event.clear()
            print("\33[41;1mred light is on...\033[0m")
        elif count > 10:
            event.set()
            count = 0
        else:
            print("\33[42;1mgreen light is on...\033[0m")

        time.sleep(1)
        count += 1


def car(name):
    while True:
        if event.is_set():
            print("[%s] running..." % name)
            time.sleep(1)
        else:
            print("[%s] sees red light,waiting..." % name)
            event.wait()
            print("[%s] green light is on,start going..." % name)


light = threading.Thread(target=lighter,)
light.start()

car = threading.Thread(target=car, args=("MINI",))
car.start()
