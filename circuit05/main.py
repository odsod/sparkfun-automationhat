import automationhat
import time


def main():
    while True:
        print('{} {}'.format(
            automationhat.input.one.read(),
            automationhat.input.two.read()))
        time.sleep(0.1)


if __name__ == '__main__':
    main()
