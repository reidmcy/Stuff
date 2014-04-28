"""Binary tree creation for the character to binary mapping"""
class node:
    """Non terminating tree component"""
    def __init__(self, v):
        self.value = v
        self.one = None
        self.zero = None
    def isnode(self):
        return True

class leaf:
    """Terminating tree component"""
    def __init__(self, l, n):
        self.letter = l
        self.value = n
    def isnode(self):
        return False

def maketree(llst, nlst):
    """Takes in two lists of equal length, one with charcters the other with
    their number of occurnces and creates a binary tree"""
    ndlst = []
    for x in range(0, len(llst)):
        ndlst.append(leaf(llst[x], nlst[x]))
    while len(ndlst) > 1:
        nd1 = ndlst.pop(ndlst.index(min(ndlst, key = lambda x : x.value)))
        nd2 = ndlst.pop(ndlst.index(min(ndlst, key = lambda x : x.value)))
        brc = node(nd1.value + nd2.value)
        brc.one = nd1
        brc.zero = nd2
        ndlst.append(brc)
    return ndlst[0]

def makestrings(nd, sdct, s = ''):
    """Adds the values from the tree to the dict, the s term is for
     the recursion"""
    if nd.isnode():
        s0 = s + str(0)
        s1 = s + str(1)
        makestrings(nd.one, sdct, s0)
        makestrings(nd.zero, sdct, s1)
    else:
        sdct[nd.letter] = s

def lsttostring(llst, nlst):
    """takes in two lists one of characters and the other of their occurnces
    and produces a dict of their Huffman code"""
    dct = {}
    makestrings(maketree(llst, nlst), dct)
    return dct