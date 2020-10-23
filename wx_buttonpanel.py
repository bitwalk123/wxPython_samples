import wx
import wx.lib.agw.buttonpanel as BP


class MyWindow(wx.Frame):

    def __init__(self):
        super().__init__(parent=None, id=wx.ID_ANY)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)

        bpnl = BP.ButtonPanel(self, -1, 'ButtonPanel')
        sizer.Add(bpnl, 0, wx.EXPAND)

        but1 = BP.ButtonInfo(bpnl, wx.ID_ANY, wx.Bitmap('png1.png', wx.BITMAP_TYPE_PNG))
        but1.SetText('icon 1')
        bpnl.AddButton(but1)
        self.Bind(wx.EVT_BUTTON, self.OnButton, but1)

        but2 = BP.ButtonInfo(bpnl, wx.ID_ANY, wx.Bitmap('png2.png', wx.BITMAP_TYPE_PNG))
        but2.SetText('icon 2')
        bpnl.AddButton(but2)
        self.Bind(wx.EVT_BUTTON, self.OnButton, but2)

        bpnl.DoLayout()
        sizer.Layout()


    def OnButton(self, event):
        obj = event.GetEventObject()
        print(obj.GetText())


if __name__ == '__main__':
    app = wx.App()
    win = MyWindow()
    win.Show()
    app.MainLoop()
