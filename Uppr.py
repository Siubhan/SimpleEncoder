import wx

class UpprP(wx.Dialog):
    def __init__(self,*args,**kwargs):
        super(UpprP,self).__init__(*args,**kwargs)
        self.SetSize(360,130)
        self.mode=''
        self.InitUI()

    def InitUI(self):
        pnl = wx.Panel(self)
        pnl.SetSize(320,100)
        self.tE=wx.TextCtrl(pnl,pos=(10,40),size=(340,20))
        if self.mode=='Зчитування даних з файлу':
            label=wx.StaticText(pnl,label='Вкажіть шлях до файлу(з розширенням):',pos=(10,10))

        elif self.mode=='Збереження шифрованих даних':
            label=wx.StaticText(pnl,label='Вкажіть шлях для збереження шифрованих даних(з розширенням):', pos=(10,10))
        elif self.mode=='Зчитування шифру з файлу':
            label=wx.StaticText(pnl,label='Вкажіть шлях до файлу(з розширенням):',pos=(10,10))

        else:
            label=wx.StaticText(pnl,label='Вкажіть шлях для збереження даних(з розширенням):',pos=(10,10))

        btnOK=wx.Button(pnl,label='Підтвердити',pos=(253,70))
        self.Bind(wx.EVT_BUTTON,self.bOK,btnOK)
        btnCN=wx.Button(pnl,label='Відмінити',pos=(10,70))
    def set_mode(self,m):
        self.mode=m

    def bOK(self,e):
        atr=r''+str(self.tE.GetValue())
        if self.mode=='Зчитування даних з файлу':
            print('Збереження шифрованих 1')

        elif self.mode == 'Збереження шифрованих даних':

            print('Збереження шифрованих 2')
        elif self.mode =='Збереження дешифрованих даних':
            print('Збереження шифрованих 3')
        else:
            print('Збереження шифрованих 4')




