import base64


class Coder():
    def __init__(self,mode,text):
        text = bytes(text, 'utf-8')

        if mode=='encrypt':
            self.val=base64.b64encode(text)
        else:
            self.val=base64.b64decode(text)

    def getValue(self):
        return self.val.decode('utf-8')



