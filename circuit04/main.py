import automationhat
import time


def main():
    leds = [
        automationhat.output[0],
        automationhat.relay[0],
        automationhat.output[1],
        automationhat.relay[1],
        automationhat.output[2],
        automationhat.relay[2],
    ]
    while True:
        for led_to_light in leds:
            for led in leds:
                if led == led_to_light:
                    led.on()
                else:
                    led.off()
            time.sleep(1)


if __name__ == '__main__':
    main()
