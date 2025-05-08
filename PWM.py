# Pulsweitenmodulation zum Dimmen einer LED
import RPi.GPIO as GPIO
import time

# Festlegen des initialen Tastgrads (duty cycle)
dc = 100

# Festlegen des GPIO-Pin 22 als LED-Pin
redLED = 22

# Festlegen des GPIO-Mode
GPIO.setmode(GPIO.BCM)

# Festlegen des GPIO-Pins der LED als Ausgang
GPIO.setup(redLED, GPIO.OUT)

# Erzeugen einer PWM-Instanz (PWM-Objekts) mit Pin und Frequenz
pwmLED = GPIO.PWM(redLED, 50)

# Starten der PWM-Instanz
pwmLED.start(dc)

# Schleife zur schrittweisen Erhöhung der LED-Leuchtstärke
for dcStep in range(dc, -1, -1):
    pwmLED.ChangeDutyCycle(dcStep)
    print("Der aktuelle Spannung am GPIO-Pin 22 beträgt:", 3.3*(dcStep/100))
    time.sleep(0.1)

# Stoppen der PWM
pwmLED.stop()
GPIO.cleanup()