import time

import automationhat


def main():
    while True:
        time.sleep(1)
        automationhat.output.one.toggle()


if __name__ == '__main__':
    main()
