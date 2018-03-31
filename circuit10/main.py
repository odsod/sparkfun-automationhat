import automationhat
import os
import sys
import time


def main():
    max_voltage = 5.17
    strip_len = 80
    while True:
        os.system('clear')
        voltage = automationhat.analog.one.read()
        percent = voltage / max_voltage
        current_location = round(strip_len * percent)
        for i in range(0, 5):
            for coord in range(0, strip_len + 1):
                if coord == current_location:
                    sys.stdout.write('|####|')
                else:
                    sys.stdout.write('-')
            sys.stdout.write('\n')
        sys.stdout.flush()
        time.sleep(0.25)


if __name__ == '__main__':
    main()
