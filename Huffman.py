import sys
import HuffmanTree as ht

def count(file):
    f = open(file)
    items = []
    count = []
    for line in f:
        for x in line:
            if x in items:
                count[items.index(x)] += 1
            else:
                items.append(x)
                count.append(1)
    return [items, count]



def main():
    args = sys.argv[1:]
    for files in args:
        lst = count(files)
        dct = ht.lsttostring(lst[0], lst[1])

if __name__ == '__main__':
    main()