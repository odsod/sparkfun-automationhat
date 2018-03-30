import automationhat
import time


def main():
    max_voltage = 5.17
    while True:
        voltage = automationhat.analog.one.read()
        sleep_duration = 0.05 + voltage / max_voltage
        automationhat.output.one.on()
        time.sleep(sleep_duration)
        automationhat.output.one.off()
        time.sleep(sleep_duration)


if __name__ == '__main__':
    main()
