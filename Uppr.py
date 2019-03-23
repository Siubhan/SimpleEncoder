import wx


class UpprP(wx.Dialog):
    def __init__(self, *args, **kwargs):
        super(UpprP, self).__init__(*args, **kwargs)
        self.SetSize(360, 130)
        self.set_mode()
        print(self.mode)
        self.InitUI()

    def InitUI(self):
        pnl = wx.Panel(self)
        pnl.SetSize(320, 100)
        self.tE = wx.TextCtrl(pnl, pos=(10, 40), size=(340, 20))
        if self.mode == 4:
            label = wx.StaticText(pnl, label='Вкажіть шлях до файлу(з розширенням):', pos=(10, 10))
        elif self.mode==3:
            label = wx.StaticText(pnl, label='Вкажіть шлях до файлу(з розширенням):', pos=(10, 10))
        elif self.mode == 2:
            label = wx.StaticText(pnl, label='Вкажіть шлях для збереження шифрованих даних(з розширенням):',
                                  pos=(10, 10))
        else:
            label = wx.StaticText(pnl, label='Вкажіть шлях для збереження даних(з розширенням):', pos=(10, 10))

        btnOK = wx.Button(pnl, label='Підтвердити', pos=(253, 70))
        self.Bind(wx.EVT_BUTTON, lambda event: self.bOK(), btnOK)
        btnCN = wx.Button(pnl, label='Відмінити', pos=(10, 70))

        self.Bind(wx.EVT_BUTTON,lambda event: self.ClMe(), btnCN)

    def set_mode(self):
        self.mode = self.Parent.m

    def ClMe(self):
        self.Close()
        self.Destroy()

    def bOK(self):
        atr = r'' + str(self.tE.GetValue())

        if self.mode == 'Зчитування даних з файлу':
            try:
                with open(atr,'r') as file:
                    self.Parent.origMes.Clear()
                    self.Parent.origMes.AppendText(file.read())
            except FileNotFoundError:
                print('file not found!')
        elif self.mode == 'Збереження шифрованих даних':
            with open(atr, 'w') as file:
                file.write(self.Parent.rsltEncr.GetValue())
        elif self.mode == 'Збереження дешифрованих даних':
            with open(atr, 'w') as file:
                file.write(self.Parent.rsltDecr.GetValue())
        else:
            try:
                with open(atr,'r') as file:
                    self.Parent.rawData.Clear()
                    self.Parent.rawData.AppendText(file.read())
            except FileNotFoundError:
                print('file not found!')
        self.ClMe()
