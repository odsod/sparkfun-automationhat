import automationhat
import time


red = 0
green = 1
blue = 2


def show_colors(colors):
    for color in [red, green, blue]:
        if color in colors:
            automationhat.relay[color].on()
        else:
            automationhat.relay[color].off()


def main():
    while True:
        for color_combination in [
            [],
            [red],
            [green],
            [blue],
            [red, green], # yellow
            [green, blue], # cyan
            [red, blue], # purple
            [red, green, blue], # white
        ]:
            show_colors(color_combination)
            time.sleep(1)


if __name__ == '__main__':
    main()
