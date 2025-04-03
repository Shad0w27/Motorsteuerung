import RPi.GPIO as GPIO
from time import sleep

enable = 16
mlfwd = 20
mlbwd = 21
mrfwd = 1
mrbwd = 12

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(enable, GPIO.OUt)
    GPIO.setup(mlfwd, GPIO.OUT)
    GPIO.setup(mlbwd, GPIO.OUT)
    GPIO.setup(mrfwd, GPIO.OUT)
    GPIO.setup(mrbwd, GPIO.OUT)


def main():
    setup()
    user_input = ""
    print("\033c")
    while True:
        user_input = str(input("Enter you command: ")).strip().lower()

        if user_input == "exit":
            break
        elif user_input == "":
            pass
        elif user_input == "help" or user_input == "?":
            print("Help\nPossible commands:\nhelp: Shows this\nclear: Clears console window\nfwd: Foreward\nbwd: Backward\nleft: Turn left\nright: Turn right\nexit: Terminates program")
        elif user_input == "clear":
            print("\033c")
        elif user_input == "fwd":
            fwd()
        elif user_input == "bwd":
            bwd()
        elif user_input == "left":
            left()
        elif user_input == "right":
            right()
        else:
            print("Unknown command. Type 'help' or '?' to show availeble commands.")
    exiting()

def fwd():
    print("mlfwd on")
    print("mlbwd off")
    print("mrfwd on")
    print("mrbwd off")
    GPIO.output(enable, GPIO.HIGH)
    GPIO.output(mlfwd, GPIO.HIGH)
    GPIO.output(mlbwd, GPIO.LOW)
    GPIO.output(mrfwd, GPIO.HIGH)
    GPIO.output(mrbwd, GPIO.LOW)
    sleep(0.5)
    print()
    print("mlfwd off")
    print("mlbwd off")
    print("mrfwd off")
    print("mrbwd off")
    GPIO.output(enable, GPIO.LOW)
    GPIO.output(mlfwd, GPIO.LOW)
    GPIO.output(mlbwd, GPIO.LOW)
    GPIO.output(mrfwd, GPIO.LOW)
    GPIO.output(mrbwd, GPIO.LOW)

def bwd():
    print("mlfwd off")
    print("mlbwd on")
    print("mrfwd off")
    print("mrbwd on")
    GPIO.output(enable, GPIO.HIGH)
    GPIO.output(mlfwd, GPIO.LOW)
    GPIO.output(mlbwd, GPIO.HIGH)
    GPIO.output(mrfwd, GPIO.LOW)
    GPIO.output(mrbwd, GPIO.HIGH)
    sleep(0.5)
    print()
    print("mlfwd off")
    print("mlbwd off")
    print("mrfwd off")
    print("mrbwd off")
    GPIO.output(enable, GPIO.LOW)
    GPIO.output(mlfwd, GPIO.LOW)
    GPIO.output(mlbwd, GPIO.LOW)
    GPIO.output(mrfwd, GPIO.LOW)
    GPIO.output(mrbwd, GPIO.LOW)

def left():
    print("mlfwd off")
    print("mlbwd on")
    print("mrfwd on")
    print("mrbwd off")
    GPIO.output(enable, GPIO.HIGH)
    GPIO.output(mlfwd, GPIO.LOW)
    GPIO.output(mlbwd, GPIO.HIGH)
    GPIO.output(mrfwd, GPIO.HIGH)
    GPIO.output(mrbwd, GPIO.LOW)
    sleep(0.5)
    print()
    print("mlfwd off")
    print("mlbwd off")
    print("mrfwd off")
    print("mrbwd off")
    GPIO.output(enable, GPIO.LOW)
    GPIO.output(mlfwd, GPIO.LOW)
    GPIO.output(mlbwd, GPIO.LOW)
    GPIO.output(mrfwd, GPIO.LOW)
    GPIO.output(mrbwd, GPIO.LOW)

def right():
    print("mlfwd on")
    print("mlbwd off")
    print("mrfwd off")
    print("mrbwd on")
    GPIO.output(enable, GPIO.HIGH)
    GPIO.output(mlfwd, GPIO.HIGH)
    GPIO.output(mlbwd, GPIO.LOW)
    GPIO.output(mrfwd, GPIO.LOW)
    GPIO.output(mrbwd, GPIO.HOGH)
    sleep(0.5)
    print()
    print("mlfwd off")
    print("mlbwd off")
    print("mrfwd off")
    print("mrbwd off")
    GPIO.output(enable, GPIO.LOW)
    GPIO.output(mlfwd, GPIO.LOW)
    GPIO.output(mlbwd, GPIO.LOW)
    GPIO.output(mrfwd, GPIO.LOW)
    GPIO.output(mrbwd, GPIO.LOW)

def exiting():
    GPIO.output(enable, GPIO.LOW)
    GPIO.output(mlfwd, GPIO.LOW)
    GPIO.output(mlbwd, GPIO.LOW)
    GPIO.output(mrfwd, GPIO.LOW)
    GPIO.output(mrbwd, GPIO.LOW)
    print()
    print("exiting...")

try:
    if __name__ == "__main__":
        main()
except KeyboardInterrupt:
    exiting()
