import sys
import os
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

def convert(dctin, filein):
    f = filein + '.huff'
    if os.path.exists(f):
        output = open(f, 'r+')
    else:
        output = open(f,'w')
    output.write(str(dctin) + '\n')
    fin = open(filein)
    for lines in fin:
        for characters in lines:
            output.write(dctin[characters])




def main():
    args = sys.argv[1:]
    for files in args:
        lst = count(files)
        dct = ht.lsttostring(lst[0], lst[1])
        convert(dct, files)






if __name__ == '__main__':
    main()