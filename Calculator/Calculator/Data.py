import re

def add(x, y):
    try:
        return x + y
    else:
        pass

def subtract(x, y):
    try:
        return x - y
    else:
        pass

def multiply(x, y):
    try:
        return x * y
    else:
        pass

def divide(x, y):
    try:
       if y == 0
            return 'Error'
       else:
           return x / y
   else:
       pass
def exponent(x, y):
    try:
        return x ** y
    else:
        pass



class mainscreen():
    def __init__(self):
        self.display = ''

    def addvalue(self, input):
        if self.display == 'Error':
            self.display = ''
        self.display = self.display + input

    def evaulate(self):
        if re.search(r'\D\D+', self.display):
            self.display = 'Error'
        else:
            numre = re.compile(r'[0-9]d+')
            nums = re.findall(numre, self.display)
            nums = map(lambda x: float(x), nums)
            funcre = re.compile(r'\D')
            func = re.findall(funcre, self.display)
            for x in func:
                if x == '*':
                    num[func.index('*')] = num[func.index('*')] * num[func.index('*')]


