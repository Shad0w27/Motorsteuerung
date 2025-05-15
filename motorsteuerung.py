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
    mlbwd_pwm = GPIO.PWM(mlbwd, frequency)
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
            drive(mlfwd_pwm, mrfwd_pwm)
        elif user_input == "bwd":
            drive(mlbwd_pwm, mrbwd_pwm)
        elif user_input == "left":
            pass
        elif user_input == "right":
            pass
        elif user_input == "changeSpeed":
            speed = int(input("Enter new speed: "))
            print(f"Speed changed to {speed}")
        else:
            print("Unknown command. Type 'help' or '?' to show availeble commands.")
    exiting()

def drive(pwmL: GPIO.PWM, pwmR: GPIO.PWM):
    GPIO.output(enable, GPIO.HIGH)
    tmpSpeed = 0
    pwmL.start(tmpSpeed)
    pwmR.start(tmpSpeed)
    
    for i in range(tmpSpeed, speed + 1):
        currentSpeed = i
        pwmL.ChangeDutyCycle(currentSpeed)
        pwmR.ChangeDutyCycle(currentSpeed)
        print("Der aktuelle Spannung am GPIO-Pin 20 beträgt:", 3.3*(currentSpeed/100))
        sleep(0.1)
        
    sleep(2)
    
    for i in range(speed, 0, -1):
        currentSpeed = i
        pwmL.ChangeDutyCycle(currentSpeed)
        pwmR.ChangeDutyCycle(currentSpeed)
        print("Der aktuelle Spannung am GPIO-Pin 20 beträgt:", 3.3*(currentSpeed/100))
        sleep(0.1)
        
    pwmL.stop()
    pwmR.stop()

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