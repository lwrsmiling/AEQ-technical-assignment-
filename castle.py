#!/usr/bin/python
# build castles

def build_castles(land):
    count = 1
    i = 1
    while i < len(land) - 1:
        if land[i] > land[i-1]:
            while i < len(land) - 1 and land[i] == land[i+1]:
                i = i + 1
            if land[i] > land[i+1]:
                count = count + 1
        elif land[i] < land[i-1]:
            while i < len(land) - 1 and land[i] == land[i+1]:
                i = i + 1
            if land[i] < land[i+1]:
                count = count + 1
        i = i + 1
    return count


def main():
    print build_castles([1])
    print build_castles([1, 2])
    print build_castles([6, 1, 4])
    print build_castles([2, 6, 3, 4])
    print build_castles([1, 3, 3, 3, 3, 2])


if __name__ == '__main__':
    main()
