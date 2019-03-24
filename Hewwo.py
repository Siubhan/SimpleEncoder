import wx


class Hewwo(wx.Dialog):
    def __init__(self, *args, **kwargs):
        super(Hewwo, self).__init__(*args, **kwargs)
        self.SetSize(500, 360)
        self.bgIm = wx.Image('1.jpg', wx.BITMAP_TYPE_ANY).ConvertToBitmap()

        self.InitUI()

    def InitUI(self):
        pnl = wx.Panel(self)
        bitmap1 = wx.StaticBitmap(pnl, -1, self.bgIm, (0, 0))

        pnl.SetSize(500, 360)
        self.Title='Привітання!'
        self.text = wx.StaticText(bitmap1, label="""
        Ласкаво просимо до программи
        Шифрування та дешифрування даних!
        Розробив студент 471 групи
        Алєксєйцева Н.Д.
        """,pos=(-15,10))
        font = wx.Font(20, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        self.text.SetFont(font)
        self.text.SetForegroundColour((117,35,64))
        self.btn=wx.Button(bitmap1,label='Почати роботу!',pos=(30,150))
        self.Bind(wx.EVT_BUTTON,self.ClDest,self.btn)

    def ClDest(self,e):
        self.Close()
        self.Destroy()

