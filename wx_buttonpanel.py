import wx
import wx.lib.agw.buttonpanel as BP

# reference
# https://wxpython.org/Phoenix/docs/html/wx.lib.agw.buttonpanel.ButtonPanel.html
# https://wxpython.org/Phoenix/docs/html/wx.lib.agw.buttonpanel.ButtonInfo.html
class MyWindow(wx.Frame):

    def __init__(self):
        super().__init__(parent=None, id=wx.ID_ANY)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)

        bpanel = BP.ButtonPanel(self, text='ButtonPanel')
        sizer.Add(bpanel, 0, wx.EXPAND)

        but1 = BP.ButtonInfo(bpanel, wx.ID_ANY, wx.Bitmap('png1.png', wx.BITMAP_TYPE_PNG))
        but1.SetText('icon 1')
        bpanel.AddButton(but1)
        self.Bind(wx.EVT_BUTTON, self.OnButton, but1)

        but2 = BP.ButtonInfo(bpanel, wx.ID_ANY, wx.Bitmap('png2.png', wx.BITMAP_TYPE_PNG))
        but2.SetText('icon 2')
        bpanel.AddButton(but2)
        self.Bind(wx.EVT_BUTTON, self.OnButton, but2)

        bpanel.DoLayout()
        sizer.Layout()


    def OnButton(self, event):
        obj = event.GetEventObject()
        print(obj.GetText())


if __name__ == '__main__':
    app = wx.App()
    win = MyWindow()
    win.Show()
    app.MainLoop()
