import wx

class UpprP(wx.Dialog):
    def __init__(self,*args,**kwargs):
        super(UpprP,self).__init__(*args,**kwargs)
        self.SetSize(360,120)
        self.InitUI()

    def InitUI(self):
        pnl = wx.Panel(self)
        pnl.SetSize(320,100)
        self.tE=wx.TextCtrl(pnl,pos=(10,40),size=(340,20))
        if self.Title=='Зчитування даних з файлу':
            label=wx.StaticText(pnl,label='Вкажіть шлях до файлу(з розширенням):',pos=(10,10))
        elif self.Title=='Збереження шифрованих даних':
            label=wx.StaticText(pnl,label='Вкажіть шлях для збереження шифрованих даних(з розширенням):', pos=(10,10))
        elif self.Title=='Зчитування шифру з файлу':
            label=wx.StaticText(pnl,label='Вкажіть шлях до файлу(з розширенням):',pos=(10,10))
        else:
            label=wx.StaticText(pnl,label='Вкажіть шлях для збереження даних(з розширенням):',pos=(10,10))
        btnOK=wx.Button(pnl,label='Підтвердити',pos=(253,70))
        btnCN=wx.Button(pnl,label='Відмінити',pos=(10,70))

    def bOK(self,e):
        atr=r''+str(self.tE.GetValue())
        if self.Title=='Зчитування даних з файлу':
            self.Parent.txtCrypt.Clear()
            with open(atr) as file:
                data=file.read()

            self.Parent.txtCrypt.Append()
        else:
            pass




