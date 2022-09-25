from ttkbootstrap import Label, Toplevel
from ttkbootstrap.constants import SOLID


class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 57
        y = y + cy + self.widget.winfo_rooty() + 27
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(tw, text=" " + self.text,
                      background="#56cc9d", foreground="white", relief=SOLID, borderwidth=0,
                      font=("Microsoft YaHei", "9"))
        label.pack(ipadx=3, ipady=3)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()


def CreateToolTip(widget, text):
    toolTip = ToolTip(widget)

    def enter(event):
        toolTip.showtip(text)

    def leave(event):
        toolTip.hidetip()

    widget.bind('<Enter>', enter)  
    widget.bind('<Leave>', leave)


def HideToolTip(widget):
    toolTip = ToolTip(widget)

    def enter(event):
        toolTip.hidetip()

    widget.bind('<Enter>', enter)
