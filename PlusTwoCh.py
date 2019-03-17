class PTC():
    def __init__(self, mode, text):
        if mode == 'encrypt':
            self.val = self.encrypt(text)
        else:
            self.val = self.decrypt(text)

    def encrypt(self, txt):
        l = ''
        for i in txt:
            l += chr(ord(i) + 2)
        return l

    def decrypt(self, txt):
        l = ''
        for i in txt:
            c = ord(i) - 2
            if c >= 0:
                l += chr(c)
            else:
                l += chr(c + 2)
        return l

    def getVal(self):
        return self.val
