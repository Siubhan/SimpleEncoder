import wx


class UpprP(wx.Dialog):
    def __init__(self, *args, **kwargs):
        super(UpprP, self).__init__(*args, **kwargs)
        self.SetSize(360, 130)
        if self.Parent != None:
            self.set_mode()
        self.InitUI()

    def InitUI(self):
        pnl = wx.Panel(self)
        pnl.SetSize(320, 100)
        self.tE = wx.TextCtrl(pnl, pos=(10, 40), size=(340, 20))
        if self.Parent is None:
            label = wx.StaticText(pnl, label='Вкажіть шлях до файлу(з розширенням):', pos=(10, 10))
        elif self.mode ==99:
            label = wx.StaticText(pnl, label='Вкажіть шлях до публічного ключа:', pos=(10, 10))
        elif self.mode == 4 or self.mode == 3:
            label = wx.StaticText(pnl, label='Вкажіть шлях до файлу(з розширенням):', pos=(10, 10))
        elif self.mode == 2:
            label = wx.StaticText(pnl, label='Вкажіть шлях для збереження шифрованих даних(з розширенням):',
                                  pos=(10, 10))
        else:
            label = wx.StaticText(pnl, label='Вкажіть шлях для збереження даних(з розширенням):', pos=(10, 10))

        btnOK = wx.Button(pnl, label='Підтвердити', pos=(253, 70))
        self.Bind(wx.EVT_BUTTON, lambda event: self.bOK(), btnOK)
        btnCN = wx.Button(pnl, label='Відмінити', pos=(10, 70))

        self.Bind(wx.EVT_BUTTON, lambda event: self.ClMe(), btnCN)

    def set_mode(self):
        self.mode = self.Parent.m

    def ClMe(self):
        self.Close()
        self.Destroy()

    def bOK(self):
        atr = r'' + str(self.tE.GetValue())
        if self.GetTitle() == 'Зчитування шифру RSA':
            if atr != '':
                wx.MessageBox('Файл зчитано!', 'Статус', wx.OK | wx.ICON_INFORMATION)
                self.a = atr

            else:
                wx.MessageBox('Введено порожню строку|зчитуваного файлу не iснує!', 'Статус', wx.OK | wx.ICON_ERROR)

        elif self.Parent is None:
            if atr != '':
                wx.MessageBox('Файл записано!', 'Статус', wx.OK | wx.ICON_INFORMATION)
                self.a = atr

            else:
                wx.MessageBox('Введено порожню строку!', 'Статус', wx.OK | wx.ICON_ERROR)
        elif self.mode == 99:
            self.a = atr
        elif self.mode == 4:
            try:
                with open(atr, 'r') as file:
                    self.Parent.origMes.Clear()
                    self.Parent.origMes.AppendText(file.read())
                    wx.MessageBox('Файл прочитано!', 'Статус', wx.OK | wx.ICON_INFORMATION)
            except FileNotFoundError:
                    wx.MessageBox('Зчитуваного файлу не існує!', 'Помилка!', wx.OK | wx.ICON_ERROR)
        elif self.mode == 1:
            if atr != '':
                with open(atr, 'w') as file:
                    file.write(self.Parent.rsltEncr.GetValue())
                    wx.MessageBox('Файл записано!', 'Статус', wx.OK | wx.ICON_INFORMATION)
            else:
                wx.MessageBox('Введено порожню строку!', 'Статус', wx.OK | wx.ICON_ERROR)
        elif self.mode == 2:
            if atr != '':
                with open(atr, 'w') as file:
                    file.write(self.Parent.rsltDecr.GetValue())
                    wx.MessageBox('Файл записано!', 'Статус', wx.OK | wx.ICON_INFORMATION)
            else:
                wx.MessageBox('Введено порожню строку!', 'Статус', wx.OK | wx.ICON_ERROR)

        else:
            try:
                with open(atr, 'r') as file:
                    self.Parent.rawData.Clear()
                    self.Parent.rawData.AppendText(file.read())
                    wx.MessageBox('Файл прочитано!', 'Статус', wx.OK | wx.ICON_INFORMATION)
            except FileNotFoundError:
                wx.MessageBox('Зчитуваного файлу не існує!', 'Помилка!', wx.OK | wx.ICON_ERROR)
        self.ClMe()
