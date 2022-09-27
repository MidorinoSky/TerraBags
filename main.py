from ttkbootstrap import Style
from ttkbootstrap.constants import *
from ttkbootstrap import Notebook, Frame, LabelFrame
from ctypes import windll
from boss import boss_setup, mini_boss_setup, text_box_setup, TopInter


def window_setup():
    windll.shcore.SetProcessDpiAwareness(1)  # 适应高dpi
    root = Style(theme="minty").master
    ti = TopInter(root)
    ti.top_inter(root)
    labelframe = LabelFrame(master=root, text="选择")
    labelframe.pack(side=LEFT, fill=BOTH, expand=YES, pady=5, padx=5, ipadx=5)
    main_tab = Notebook(master=labelframe)
    main_tab.pack(anchor=NW, side=LEFT, fill=BOTH, expand=YES)
    text_box_setup(root)
    boss_tab_frame = Frame(main_tab)
    boss_tab_frame.pack(fill=BOTH, expand=YES)
    main_tab.add(boss_tab_frame, text="Boss")
    mini_boss_tab_frame = Frame(main_tab)
    mini_boss_tab_frame.pack(fill=BOTH, expand=YES)
    main_tab.add(mini_boss_tab_frame, text="事件Boss")
    boss_setup(boss_tab_frame)
    mini_boss_setup(mini_boss_tab_frame)
    ti.set_center()
    return root


if __name__ == "__main__":
    window = window_setup()
    window.iconbitmap("bag_queen.ico")
    window.title("泰拉瑞亚：宝藏袋")
    window.mainloop()
