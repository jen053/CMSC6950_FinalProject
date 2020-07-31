import wget
import sys

def getData(location):
    url = 'https://raw.githubusercontent.com/jen053/windData/master/' + location + '.csv'

    wget.download(url, 'data.txt')

    return None


def main(args):
    if len(args) != 2:
        raise SystemExit('Stopped')

    getData(location=args[1])


if __name__ == '__main__':
    main(sys.argv)
