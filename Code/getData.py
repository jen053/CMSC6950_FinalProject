import wget


def getData(location):
    url = 'https://raw.githubusercontent.com/jen053/windData/master/' + location + '.csv'

    wget.download(url, 'c:/Users/Jacob/CMSC6950_py/Open_Science_Project/CMSC6950_FinalProject/data.txt')

    return None


def main(args):
    if len(args) != 2:
        raise SystemExit('Stopped')

    getData(location=args[1])


if __name__ == '__main__':
    import sys

    main(sys.argv)
