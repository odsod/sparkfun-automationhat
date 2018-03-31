import automationhat
import time


def main():
    while True:
        voltage = automationhat.analog.one.read()
        degreesC = (voltage - 0.5) * 100
        print('{}v: {}C'.format(voltage, degreesC))
        time.sleep(1)


if __name__ == '__main__':
    main()
