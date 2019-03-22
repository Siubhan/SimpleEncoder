class SSC():
    def __init__(self, mode, text):
        if mode == 'encrypt':
            self.val = self.encrypt(text)
        else:
            self.val = self.decrypt(text)

    def encrypt(self, txt):
        l = ''
        for i in txt:
            ch = ord(i)
            if ch % 2 == 0:
                ch += 2
            else:
                if ch - 4 >= 0:
                    ch -= 4
            l += chr(ch)
        return l

    def decrypt(self, txt):
        l = ''
        for i in txt:
            c = ord(i)
            if c % 2 == 0:
                c -= 2
            else:
                if c - 4 >= 0:
                    c += 4
            l += chr(c)
        return l

    def getVal(self):
        return self.val
