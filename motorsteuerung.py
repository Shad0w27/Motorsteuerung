import RPi.GPIO as GPIO
from time import sleep

enable = 16
mlfwd = 20
mlbwd = 21
mrfwd = 1
mrbwd = 12

speed = 100
frequency = 50

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(enable, GPIO.OUT)
    GPIO.setup(mlfwd, GPIO.OUT)
    GPIO.setup(mlbwd, GPIO.OUT)
    GPIO.setup(mrfwd, GPIO.OUT)
    GPIO.setup(mrbwd, GPIO.OUT)


def main():
    setup()
    
    mlfwd_pwm = GPIO.PWM(mlfwd, frequency)
    mlbawd_pwm = GPIO.PWM(mlbwd, frequency)
    mrfwd_pwm = GPIO.PWM(mrfwd, frequency)
    mrbwd_pwm = GPIO.PWM(mrbwd, frequency)
    
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
            fwd(mlbawd_pwm)
        elif user_input == "bwd":
            bwd()
        elif user_input == "left":
            left()
        elif user_input == "right":
            right()
        elif user_input == "changeSpeed":
            speed = int(input("Enter new speed: "))
            print(f"Speed changed to {speed}")
        else:
            print("Unknown command. Type 'help' or '?' to show availeble commands.")
    exiting()

def fwd(pwm: GPIO.PWM):
    tmpSpeed = 0
    pwm.start(tmpSpeed)
    
    for i in range(tmpSpeed, speed + 1):
        currentSpeed = i
        pwm.ChangeDutyCycle(currentSpeed)
        print("Der aktuelle Spannung am GPIO-Pin 20 beträgt:", 3.3*(tmpSpeed/100))
        sleep(0.1)
        
    sleep(0.5)
    
    for i in range(currentSpeed, 0, -1):
        currentSpeed = i
        pwm.ChangeDutyCycle(currentSpeed)
        print("Der aktuelle Spannung am GPIO-Pin 20 beträgt:", 3.3*(tmpSpeed/100))
        sleep(0.1)
        
    pwm.stop()

def bwd(pwm):
    pass

def left(pwm):
    pass

def right(pwm):
    pass

def exiting():
    GPIO.output(enable, GPIO.LOW)
    GPIO.output(mlfwd, GPIO.LOW)
    GPIO.output(mlbwd, GPIO.LOW)
    GPIO.output(mrfwd, GPIO.LOW)
    GPIO.output(mrbwd, GPIO.LOW)
    print("\nexiting...")

try:
    if __name__ == "__main__":
        main()
except KeyboardInterrupt:
    exiting()