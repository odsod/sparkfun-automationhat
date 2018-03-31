import automationhat
import time


def main():
    while True:
        voltage = automationhat.analog.one.read()
        print('{}v'.format(voltage))
        time.sleep(1)


if __name__ == '__main__':
    main()
