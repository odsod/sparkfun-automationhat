import automationhat
import time


def main():
    while True:
        print(automationhat.analog.one.read())
        time.sleep(0.1)


if __name__ == '__main__':
    main()
