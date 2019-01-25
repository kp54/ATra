import os

import taglib


def main():
    with open('tracks.txt') as f:
        tmp = f.readlines()
    tracks = list()
    for t in tmp:
        tracks.append('.'.join(t.split('.')[1:])[:-1])

    files = os.listdir('./tmp/')
    for f in files:
        tmp = './tmp/' + f
        if os.path.isfile(tmp):
            tmq = int(f.split(' ')[0])
            print(f, tracks[tmq-1])
            g = taglib.File(tmp)
            g.tags['TITLE'] = [tracks[tmq-1]]
            g.save()
            g.close()
            os.rename(tmp, '{}{:02d} {}.{}'.format('./tmp/', tmq, tracks[tmq-1], 'mp3'))

    return 0


if __name__ == '__main__':
    import sys

    sys.exit(main())
