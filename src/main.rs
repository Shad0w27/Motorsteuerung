use rust_gpiozero::LED;

fn main() {
    let mut led = LED::new(17); // GPIO pin 17

    led.blink(0.5, 0.5); // Blink with 0.5 seconds on and off
}
