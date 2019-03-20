
import webbrowser

import pyperclip as pyperclip
import wx
import wx.html

from TransparentText import TransparentText
from Uppr import UpprP
from PlusTwoCh import PTC
from MinusTenCh import MTC
from ShotoSlozhnoeCh import SSC


class GUI(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(GUI, self).__init__(*args, **kwargs)
        self.mainPanel = wx.Panel(self)
        self.cryptoPanel = wx.Panel(self)
        self.decryptoPanel = wx.Panel(self)

        self.cryptoPanel.Hide()
        self.decryptoPanel.Hide()

        self.mainPanel.SetSize(0, 0, 600, 450)
        self.cryptoPanel.SetSize(0, 0, 600, 450)
        self.decryptoPanel.SetSize(0, 0, 600, 450)

        self.bgIm = wx.Image('fon.jpg', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.font1 = wx.Font(24, wx.FONTFAMILY_ROMAN, wx.NORMAL, wx.BOLD)
        self.font2 = wx.Font(10, wx.FONTFAMILY_TELETYPE, wx.NORMAL, wx.FONTWEIGHT_LIGHT)

        self.initGui()

    def crypto(self, txt):
        par = self.comboCrypt.GetStringSelection()
        self.rsltEncr.Clear()
        if par == 'PTC':
            self.rsltEncr.AppendText(PTC('encrypt', txt).getVal())
        elif par == 'MTC':
            self.rsltEncr.AppendText(MTC('encrypt', txt).getVal())
        else:
            self.rsltEncr.AppendText(SSC('encrypt', txt).getVal())

    def decrypt(self, txt):
        par = self.comboDecrypt.GetStringSelection()
        self.rsltDecr.Clear()
        if par == 'PTC':
            self.rsltDecr.AppendText(PTC('decrypt', txt).getVal())
        elif par == 'MTC':
            self.rsltDecr.AppendText(MTC('decrypt', txt).getVal())
        else:
            self.rsltDecr.AppendText(SSC('decrypt', txt).getVal())

    def setMainPanel(self):
        self.cryptoPanel.Hide()
        self.decryptoPanel.Hide()
        self.mainPanel.Show()

        bitmap1 = wx.StaticBitmap(self.mainPanel, -1, self.bgIm, (0, 0))
        text = TransparentText(self.mainPanel, label="JUMBLE UP", pos=(75, 70))
        text.SetFont(self.font1)
        text.SetForegroundColour("#8F5A3F")
        self.b1 = wx.Button(bitmap1, label="Зашифрувати дані", pos=(75, 120), size=(150, 50))
        self.b2 = wx.Button(bitmap1, label="Дешифрувати дані", pos=(75, 170), size=(150, 50))
        self.b3 = wx.Button(bitmap1, label="Довідка", pos=(75, 220), size=(150, 50))
        self.b1.Bind(wx.EVT_BUTTON, self.setCryptoPanel)
        self.b2.Bind(wx.EVT_BUTTON, self.setDecrPanel)
        self.b3.Bind(wx.EVT_BUTTON, self.showHelp)
        self.b1.SetFont(self.font2)
        self.b2.SetFont(self.font2)
        self.b3.SetFont(self.font2)
        self.ReadFF.Enable(False)
        self.WriteTF.Enable(False)
        self.mainPanel.Layout()
        self.Layout()

    def showHelp(self, event):
        url = r'file:///Users/shiva/PycharmProjects/kp/dtp/index.html'
        b = webbrowser.get('Safari')

        b.open_new(url)

    def setCryptoPanel(self, event):
        self.mainPanel.Hide()
        self.ReadFF.Enable(True)
        self.WriteTF.Enable(True)
        bitmap2 = wx.StaticBitmap(self.cryptoPanel, -1, self.bgIm, (0, 0))
        txt1 = TransparentText(bitmap2, label="JUMBLE UP", pos=(230, 10))
        txt2 = TransparentText(bitmap2, label="Зашифровані дані", pos=(380, 45))
        txt3 = TransparentText(bitmap2, label="Оригінальні дані", pos=(90, 45))
        txt4 = TransparentText(bitmap2, label="Вибір алгоритму:", pos=(35, 307))

        self.rsltEncr = wx.TextCtrl(bitmap2, style=wx.TE_MULTILINE | wx.TE_READONLY, size=(260, 220), pos=(305, 70))
        self.origMes = wx.TextCtrl(bitmap2, style=wx.TE_MULTILINE, size=(260, 220), pos=(20, 70))

        btnEx = wx.Button(bitmap2, label="До меню", pos=(20, 350), size=(100, 30))
        btnEnc = wx.Button(bitmap2, label="Зашифрувати", pos=(465, 350), size=(100, 30))
        btnEx.Bind(wx.EVT_BUTTON, lambda evt: self.setMainPanel())
        btnEnc.Bind(wx.EVT_BUTTON, lambda evt: self.crypto(self.origMes.GetValue()))

        txt1.SetForegroundColour("#E65D17")
        txt2.SetForegroundColour("#032447")
        txt4.SetForegroundColour("#032447")
        txt3.SetForegroundColour("#032447")

        txt1.SetFont(self.font1)
        btnEx.SetFont(self.font2)
        btnEnc.SetFont(self.font2)
        self.rsltEncr.SetFont(self.font2)
        self.origMes.SetFont(self.font2)
        txt2.SetFont(self.font2)
        txt3.SetFont(self.font2)
        txt4.SetFont(self.font2)
        self.origMes.AppendText("Введіть дані, для шифрування")

        cryptMet = ['PTC', 'MTC', 'SSC']

        self.comboCrypt = wx.ComboBox(bitmap2, value=cryptMet[0], choices=cryptMet, pos=(150, 300),
                                      style=wx.CB_READONLY)
        self.comboCrypt.SetFont(self.font2)
        self.cryptoPanel.Show()
        self.cryptoPanel.Layout()
        self.Layout()

    def setDecrPanel(self, event):
        self.mainPanel.Hide()
        self.ReadFF.Enable(True)
        self.WriteTF.Enable(True)
        bitmap2 = wx.StaticBitmap(self.decryptoPanel, -1, self.bgIm, (0, 0))
        txt1 = TransparentText(bitmap2, label="JUMBLE UP", pos=(230, 10))
        txt2 = TransparentText(bitmap2, label="Зашифровані дані", pos=(400, 40))
        txt3 = TransparentText(bitmap2, label="Дешифровані дані", pos=(100, 40))
        txt4 = TransparentText(bitmap2, label="Вибір алгоритму:", pos=(35, 307))

        self.rsltDecr = wx.TextCtrl(bitmap2, style=wx.TE_MULTILINE | wx.TE_READONLY, size=(260, 220), pos=(305, 70))
        self.rawData = wx.TextCtrl(bitmap2, style=wx.TE_MULTILINE, size=(260, 220), pos=(20, 70))

        btnEx = wx.Button(bitmap2, label="До меню", pos=(20, 350), size=(100, 30))
        btnEnc = wx.Button(bitmap2, label="Дешифрувати", pos=(465, 350), size=(100, 30))
        btnEx.Bind(wx.EVT_BUTTON, lambda evt: self.setMainPanel())

        txt1.SetForegroundColour("#E65D17")
        txt2.SetForegroundColour("#032447")
        txt3.SetForegroundColour("#032447")
        txt4.SetForegroundColour("#032447")

        txt1.SetFont(self.font1)
        btnEx.SetFont(self.font2)
        btnEnc.SetFont(self.font2)
        self.rsltDecr.SetFont(self.font2)
        self.rawData.SetFont(self.font2)
        txt2.SetFont(self.font2)
        txt3.SetFont(self.font2)
        txt4.SetFont(self.font2)

        self.rawData.AppendText("Введіть дані, для дешифрування")
        cryptMet = ['PTC', 'MTC', 'SSC']

        self.comboDecrypt = wx.ComboBox(bitmap2, value=cryptMet[0], choices=cryptMet, pos=(150, 300),
                                        style=wx.CB_READONLY)

        self.comboDecrypt.SetFont(self.font2)
        btnEnc.Bind(wx.EVT_BUTTON, lambda e: self.decrypt(self.rawData.GetValue()))
        self.decryptoPanel.Show()
        self.decryptoPanel.Layout()
        self.Layout()

    @property
    def setUpprPanel(self):
        menuBar = wx.MenuBar()

        FileB = wx.Menu()
        InfoB = wx.Menu()

        editMenu = wx.Menu()
        copyItem = wx.MenuItem(editMenu, 100, text="Копіювати\tCtrl+C")
        editMenu.Append(copyItem)
        cutItem = wx.MenuItem(editMenu, 101, text="Вирізати\tCtrl+X")
        editMenu.Append(cutItem)
        pasteItem = wx.MenuItem(editMenu, 102, text="Вставити\tCtrl+V")
        editMenu.Append(pasteItem)

        ExitItem = wx.MenuItem(FileB, wx.ID_EXIT, "Вихід\tCtrl+Q", "Завершити роботу програми")
        Info = wx.Menu()
        InfoItemAbout = wx.MenuItem(Info, wx.ID_FILE8, "Створив студент 471 групи Алєксєйцева Н.Д.",
                                    "Інформація про розробника")
        Info.Append(InfoItemAbout)
        HelpItem = wx.MenuItem(InfoB, wx.ID_HELP_CONTEXT, "Довідка\tCtrl+I",
                               "Довідка програми")
        InfoB.AppendSubMenu(Info, "&Про розробника")
        InfoB.Append(HelpItem)
        self.Bind(wx.EVT_MENU, self.Quit, ExitItem)
        self.Bind(wx.EVT_MENU, self.showHelp, HelpItem)
        NavEdit = wx.Menu()
        self.ReadFF = wx.MenuItem(NavEdit, wx.ID_FILE, "Зчитати з файлу", "Зчитати дані з файлу")
        self.WriteTF = wx.MenuItem(NavEdit, wx.ID_FILE1, "Записати до файлу", "Записати дані до файлу")
        self.ReadFF.Enable(False)
        self.WriteTF.Enable(False)
        NavEdit.Append(self.ReadFF)
        NavEdit.Append(self.WriteTF)
        FileB.AppendSubMenu(editMenu, "&Редагування")
        FileB.Append(ExitItem)
        menuBar.Append(FileB, '&Файл')
        FileB.AppendSeparator()
        FileB.AppendSubMenu(NavEdit, '&Робота з файлом')
        FileB.AppendSeparator()
        menuBar.Append(InfoB, '&Інформація')

        self.Bind(wx.EVT_MENU, self.on_cut, cutItem)
        self.Bind(wx.EVT_MENU, self.on_paste, pasteItem)
        self.Bind(wx.EVT_MENU,self.on_copy, copyItem)
        self.Bind(wx.EVT_MENU, self.wF, self.WriteTF)
        self.Bind(wx.EVT_MENU, self.rF, self.ReadFF)

        return menuBar

    def initGui(self):
        self.SetMenuBar(self.setUpprPanel)
        self.setMainPanel()
        self.SetTitle('Шифрування даних - JUMBLE UP')
        self.Show(True)

    def Quit(self, e):
        self.Close()

    def on_copy(self, event):
        widget = self.FindFocus()
        pyperclip.copy(widget.GetValue())

    def on_cut(self, event):
        widget = self.FindFocus()
        pyperclip.copy(widget.GetValue())
        widget.Clear()

    def on_paste(self, event):
        widget = self.FindFocus()
        widget.WriteText(pyperclip.paste())

    def wF(self, e):
        u = UpprP(self, title='Запис до файлу', style=wx.MINIMIZE_BOX | wx.CLOSE_BOX | wx.CAPTION)
        u.ShowModal()
        u.Destroy()

    def rF(self, e):
        u = UpprP(self, title='Зчитування з файлу', style=wx.MINIMIZE_BOX | wx.CLOSE_BOX | wx.CAPTION)
        u.ShowModal()
        u.Destroy()



if __name__ == '__main__':
    app = wx.App()
    gui = GUI(None, size=(600, 420), style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CLOSE_BOX | wx.CAPTION)

    app.MainLoop()
