from ttkbootstrap import PhotoImage
from ttkbootstrap import Style
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from tooltip import CreateToolTip, HideToolTip
from treasure import ItemList
from random import randint, random
from time import sleep


class TopInter(object):

    def __init__(self, root):
        global rt
        rt = root
        self.root = root
        self.fc1 = self.fc2 = 6
        self.frs1 = self.frs2 = []
        self.r1 = self.r2 = 1
        self.top_frame = None
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

    def set_center(self):
        center_x = int(self.screen_width / 3.5)
        center_y = int(self.screen_height / 4)
        self.root.geometry("+{}+{}".format(center_x, center_y))
        sleep(0.1)

    def update(self, ind):
        frame = self.frs1[ind]
        ind += 1
        if ind == self.fc1:
            ind = 0
        gif_label1.configure(image=frame)
        gif_label1.image = frame
        gif_label1.after(100, self.update, ind)

    def update2(self, ind2):
        frame2 = self.frs2[ind2]
        ind2 += 1
        if ind2 == self.fc2:
            ind2 = 0
        gif_label2.configure(image=frame2)
        gif_label2.image = frame2
        gif_label2.after(100, self.update2, ind2)

    def top_inter(self, root):
        global gif_label1, gif_label2
        """------------------------------------------------------"""
        """顶部界面"""
        self.frs1 = [PhotoImage(file="interface/slime_prince.gif", format='gif -index %i' % i) for i in range(self.fc1)]
        self.frs2 = [PhotoImage(file="interface/fishron.gif", format='gif -index %i' % i) for i in range(self.fc2)]

        self.top_frame = ttk.Frame(master=root)
        self.top_frame.pack(side=TOP, fill=BOTH, ipady=30)
        self.top_frame.pack_propagate(0)
        gif_label1 = ttk.Label(master=self.top_frame, image=self.frs1[0])
        gif_label1.pack(side=LEFT, fill=BOTH, padx=10)
        gif_label1.pack_propagate(0)
        gif_label1.image = self.frs1[0]

        gif_label2 = ttk.Label(master=self.top_frame, image=self.frs2[0])
        gif_label2.pack(side=RIGHT, fill=BOTH, padx=10)
        gif_label2.pack_propagate(0)
        gif_label2.image = self.frs1[0]

        gif_label1.after(100, self.update, 0)
        gif_label2.after(100, self.update2, 0)
        var = ttk.StringVar()
        var.set("F")

        def dark_mode():
            if var.get() == "T":
                Style(theme="darkly")
            else:
                Style(theme="minty")

        cb1 = ttk.Checkbutton(master=self.top_frame, text="夜间模式",
                              variable=var, onvalue="T", offvalue="F",
                              command=dark_mode,
                              bootstyle=(SUCCESS, ROUND, TOGGLE))
        cb1.pack(fill=X, padx=10, pady=10, side=RIGHT)

    def exchangeGIF(self):
        left_gifs = {"betsy.gif": 6,
                     "slime_prince.gif": 6,
                     "golem.gif": 6,
                     "sus_eye.gif": 6,
                     "brain.gif": 6
                     }
        right_gifs = {"bee.gif": 6,
                      "fishron.gif": 6,
                      "emp_fairy.gif": 6,
                      "slime_princess.gif": 6,
                      "pumpkin.gif": 6
                      }
        self.r1 += randint(1, 4)
        self.r1 = self.r1 % 5
        self.r2 += randint(1, 4)
        self.r2 = self.r2 % 5
        gif1, self.fc1 = tuple(left_gifs.items())[self.r1]
        gif2, self.fc2 = tuple(right_gifs.items())[self.r2]
        self.frs1 = [PhotoImage(file="interface/" + gif1, format='gif -index %i' % i) for i in range(self.fc1)]
        self.frs2 = [PhotoImage(file="interface/" + gif2, format='gif -index %i' % i) for i in range(self.fc2)]
        gif_label1.after_cancel(gif_label1)
        gif_label2.after_cancel(gif_label2)
        gif_label1.configure(image=self.frs1[0])
        gif_label1.image = self.frs1[0]
        gif_label2.configure(image=self.frs2[0])
        gif_label2.image = self.frs2[0]
        gif_label1.after(100, self.update, 0)
        gif_label2.after(100, self.update2, 0)
        sleep(0.1)   # 用于刷新GIF图，防止GIF抽搐


def boss_setup(widget):
    global boss_var
    """------------------------------------------------------"""
    """左侧界面"""
    lframe = ttk.Frame(widget, padding=5)
    lframe.pack(side=LEFT, fill=BOTH, expand=YES)
    nb = ttk.Notebook(master=lframe)
    nb.pack(anchor=N, fill=BOTH, expand=YES, padx=0)
    pre_hm_frame = ttk.Frame(nb)
    pre_hm_frame.pack(expand=YES)
    hm_frame = ttk.Frame(nb)
    hm_frame.pack(expand=YES)
    all_boss_frame = ttk.Frame(nb)
    all_boss_frame.pack(expand=YES)
    nb.add(pre_hm_frame, text="困难模式前", sticky=W)
    nb.add(hm_frame, text="困难模式后", sticky=W)
    nb.add(all_boss_frame, text="全部", sticky=W)

    boss_var = ttk.IntVar(value=11)  # 单选按钮的变量
    values_hm = {
        "月亮领主": 1,
        "光之女皇": 2,
        "石巨人": 3,
        "世纪之花": 4,
        "猪龙鱼公爵": 5,
        "双足翼龙": 6,
        "双子魔眼": 7,
        "毁灭者": 8,
        "机械骷髅王": 9,
        "史莱姆皇后": 10,
    }
    values_phm = {
        "史莱姆王": 11,
        "克苏鲁之眼": 12,
        "世界吞噬者": 13,
        "克苏鲁之脑": 14,
        "蜂王": 15,
        "骷髅王": 16,
        "独眼巨鹿": 17,
        "血肉之墙": 18,
    }

    """------------------------------------------"""
    """所有、肉前、肉后"""
    grid_frame = ttk.Frame(master=all_boss_frame, padding=5)
    grid_frame.pack(fill=BOTH, anchor=NW, expand=YES)
    for i in range(18):
        img_file = "interface/" + str(i + 1) + ".png"
        img = PhotoImage(file=img_file)
        label = ttk.Label(master=grid_frame, image=img)
        if i < 9:
            label.grid(row=i, column=0, padx=10, pady=8)
            label.image = img
        if i >= 9:
            label.grid(row=i - 9, column=2, padx=10, pady=8)
            label.image = img
    k = 0
    all_values = dict(values_hm, **values_phm)
    for (text, value) in all_values.items():
        rb = ttk.Radiobutton(master=grid_frame, text=text, variable=boss_var, value=value)
        if k < 9:
            rb.grid(row=k, column=1, sticky=W, padx=5)
        if k >= 9:
            rb.grid(row=k - 9, column=3, sticky=W, padx=5)
        k += 1

    grid_pre_hm = ttk.Frame(master=pre_hm_frame, padding=5)
    grid_pre_hm.pack(fill=BOTH, anchor=NW, expand=YES)
    for i in range(10, 18):
        img_file = "interface/" + str(i + 1) + ".png"
        img = PhotoImage(file=img_file)
        label = ttk.Label(master=grid_pre_hm, image=img)
        label.grid(row=i - 10, column=0, padx=10, pady=8)
        label.image = img
    k = 0
    for (text, value) in values_phm.items():
        rb = ttk.Radiobutton(master=grid_pre_hm, text=text, variable=boss_var, value=value)
        rb.grid(row=k, column=1, sticky=W, padx=5)
        k += 1

    grid_hm = ttk.Frame(master=hm_frame, padding=5)
    grid_hm.pack(fill=BOTH, anchor=NW, expand=YES)
    for i in range(10):
        img_file = "interface/" + str(i + 1) + ".png"
        img = PhotoImage(file=img_file)
        label = ttk.Label(master=grid_hm, image=img)
        label.grid(row=i, column=0, padx=10, pady=8)
        label.image = img
    k = 0
    for (text, value) in values_hm.items():
        rb = ttk.Radiobutton(master=grid_hm, text=text, variable=boss_var, value=value)
        rb.grid(row=k, column=1, sticky=W, padx=5)
        k += 1

    """------------------------------------------"""

    button_frame = ttk.Frame(master=lframe, padding=3)
    button_frame.pack(side=TOP, expand=YES)
    ttk.Button(master=button_frame, text="打开宝藏袋",
               bootstyle=SUCCESS, command=open_bag, width=21).pack(anchor=N, padx=2, fill=X)
    ttk.Button(master=button_frame, text="重置",
               bootstyle=SUCCESS, command=clear_interface, width=9).pack(side=LEFT, padx=2, pady=4)
    ttk.Button(master=button_frame, text="更改宠物", width=10,
               bootstyle=SUCCESS, command=TopInter(rt).exchangeGIF).pack(side=LEFT, padx=2, pady=0)


def text_box_setup(widget):
    global item_labels, txt, tv
    """------------------------------------------------------"""
    """右侧界面"""
    rframe = ttk.Frame(widget, padding=5)
    rframe.pack(side=RIGHT, fill=BOTH, expand=YES)

    res_group = ttk.Labelframe(
        rframe, text="获取的物品", padding=10
    )
    res_group.pack(fill=BOTH, ipady=10, side=BOTTOM, expand=YES)

    txt = ttk.ScrolledText(master=res_group, height=8, width=55)
    txt.pack(side=TOP, anchor=W, pady=5, fill=BOTH, expand=YES)

    tv = ttk.Treeview(master=res_group, columns=[0, 1], show=HEADINGS, height=8)
    for i in range(5):
        tv.insert("", END, values=(" ", " "))

    tv.heading(0, text="物品")
    tv.heading(1, text="数量")
    tv.column(0, width=150)
    tv.column(1, width=150, anchor=CENTER)
    tv.pack(side=TOP, anchor=W, fill=BOTH, pady=5, expand=YES)

    icons_frame = ttk.Labelframe(master=res_group, text="最后获取的物品", padding=5)
    icons_frame.pack(fill=BOTH, expand=YES, pady=0, side=BOTTOM, anchor=W, ipady=65)
    icons_frame.pack_propagate(0)
    fr = ttk.Frame(master=icons_frame)
    fr.pack(side=LEFT, anchor=W)
    fr.pack_propagate(0)

    item_labels = [ttk.Label(master=fr, image="", width=2) for j in range(11)]
    for i, l in enumerate(item_labels):
        l.grid(row=0, column=i, padx=10, pady=4, sticky=W)


def mini_boss_setup(widget):
    """------------------------------------------------------"""
    """左侧界面"""
    lframe = ttk.Frame(widget, padding=5)
    lframe.pack(side=LEFT, fill=BOTH, expand=YES)

    ev_frame = ttk.Frame(
        lframe, padding=5
    )
    ev_frame.pack(fill=BOTH, side=TOP, expand=YES)
    global ev_var
    ev_var = ttk.IntVar(value=19)
    ev_dict = {
        "黑暗法师": 19,
        "食人魔": 20,
        "荷兰飞盗船": 21,
        "哀木": 22,
        "南瓜王": 23,
        "常绿尖叫怪": 24,
        "圣诞坦克": 25,
        "冰雪女王": 26,
        "火星飞碟": 27
    }
    for i in range(19, 28):
        img_file = "interface/" + str(i) + ".png"
        img = PhotoImage(file=img_file)
        label = ttk.Label(master=ev_frame, image=img)
        label.grid(row=i - 19, column=0, padx=10, pady=8)
        label.image = img
    k = 0
    for (text, value) in ev_dict.items():
        rb = ttk.Radiobutton(master=ev_frame, text=text, variable=ev_var, value=value)
        rb.grid(row=k, column=1, sticky=W, padx=5)
        k += 1

    """------------------------------------------------------"""
    """右侧界面"""
    """
    rframe = ttk.Frame(widget, padding=5)
    rframe.pack(side=RIGHT, fill=BOTH, expand=YES)

    res_group = ttk.Labelframe(
        rframe, text="获取的物品", padding=10
    )
    res_group.pack(fill=BOTH, ipady=10, side=TOP, expand=YES)

    txt2 = ttk.ScrolledText(master=res_group, height=8, width=55)
    txt2.pack(side=TOP, anchor=W, pady=5, fill=BOTH, expand=YES)

    tv2 = ttk.Treeview(master=res_group, columns=[0, 1], show=HEADINGS, height=8)
    for i in range(5):
        tv2.insert("", END, values=(" ", " "))

    tv2.heading(0, text="物品")
    tv2.heading(1, text="数量")
    tv2.column(0, width=150)
    tv2.column(1, width=150, anchor=CENTER)
    tv2.pack(side=TOP, anchor=W, fill=BOTH, pady=5, expand=YES)

    icons_frame = ttk.Labelframe(master=res_group, text="最后获取的物品", padding=5)
    icons_frame.pack(fill=BOTH, expand=YES, pady=0, side=BOTTOM, anchor=W, ipady=65)
    icons_frame.pack_propagate(0)
    fr = ttk.Frame(master=icons_frame)
    fr.pack(side=LEFT, anchor=W)
    fr.pack_propagate(0)
    global item_labels2
    item_labels2 = [ttk.Label(master=fr, image="", width=2) for j in range(11)]
    for i, l in enumerate(item_labels2):
        l.grid(row=0, column=i, padx=10, pady=4, sticky=W)
    
    """

    button_frame = ttk.Frame(master=lframe, padding=3)
    button_frame.pack(side=TOP, expand=YES)

    ttk.Button(master=button_frame, text="获取宝藏",
               bootstyle=SUCCESS, command=obtain_treasures, width=21).pack(anchor=N, padx=2, fill=X)
    ttk.Button(master=button_frame, text="重置",
               bootstyle=SUCCESS, command=clear_interface, width=9).pack(side=LEFT, padx=2, pady=4)
    ttk.Button(master=button_frame, text="更改宠物", width=10,
               bootstyle=SUCCESS, command=TopInter(rt).exchangeGIF).pack(side=LEFT, padx=2, pady=0)


def get_multiple_items(amount, item_id, show_list):
    ItemList.counts[item_id] += amount
    show_list.append(item_id)
    text = "".join(("，", ItemList.all_names[item_id], "*", str(amount)))
    return text


def item_prob(x, p, item_id, show_list):
    item_name = ""
    if 0 <= x < p:
        item_name = "，" + ItemList.all_names[item_id]
        ItemList.counts[item_id] += 1
        show_list.append(item_id)
    return item_name


def choose_items(choose_list, show_list, num=1):
    if num == 1:
        item_id = choose_list[randint(0, len(choose_list) - 1)]
        item_name = ItemList.all_names[item_id]
        ItemList.counts[item_id] += 1
        show_list.append(item_id)
        return item_name
    if num == 2:
        item_id = choose_list[randint(0, len(choose_list) - 1)]
        item2_id = item_id
        while item2_id == item_id:
            item2_id = choose_list[randint(0, len(choose_list) - 1)]
        ItemList.counts[item_id] += 1
        ItemList.counts[item2_id] += 1
        show_list.extend([item_id, item2_id])
        name1 = ItemList.all_names[item_id]
        name2 = "，" + ItemList.all_names[item2_id]
        return name1 + name2


def get_dev_item(show_list):
    r = randint(42, 59)
    r2 = random()
    dev_item = ""
    if 0 <= r2 < 0.05:
        ItemList.counts[r] += 1
        dev_item = "，" + ItemList.dev_list[r]
    if dev_item != "":
        show_list.append(r)
    return dev_item


def show_text_and_icons(text, id_list):
    txt.insert(END, text)
    txt.yview_moveto(1)
    item_dict = dict(zip(ItemList.all_names, ItemList.counts))
    item_rank = sorted(item_dict.items(), key=lambda x: x[1], reverse=True)
    for item in tv.get_children():
        tv.delete(item)
    for item in item_rank:
        if item[1] != 0:
            tv.insert("", END, values=item)
        else:
            continue
    if id_list:
        for k, item_id in enumerate(id_list):
            icon = PhotoImage(file="item/" + str(item_id) + ".png")
            item_labels[k].configure(image=icon)
            item_labels[k].image = icon
            CreateToolTip(item_labels[k], ItemList.all_names[item_id])

        for j in range(len(id_list), 11):
            item_labels[j].config(image="")
            item_labels[j].children.clear()
            HideToolTip(item_labels[j])


def open_bag():
    if boss_var.get() == 1:
        show_list = []
        weapon = choose_items([i for i in range(0, 9)], show_list)
        luminites = get_multiple_items(randint(70, 90), 10, show_list)
        cart = item_prob(random(), 0.1, 9, show_list)
        starboard = item_prob(0, 1, 127, show_list)
        portal_gun = item_prob(0, 1, 128, show_list)
        gravity_globe = item_prob(0, 1, 129, show_list)
        tentacle = item_prob(0, 1, 130, show_list)
        dev_item = get_dev_item(show_list)

        res_text = "".join((weapon, luminites,
                            cart, starboard, portal_gun, gravity_globe, tentacle,
                            dev_item, "\n"))
        show_text_and_icons(res_text, show_list)

    if boss_var.get() == 2:
        show_list = []
        weapon = choose_items([i for i in range(11, 15)], show_list)
        wing = item_prob(random(), 0.1, 15, show_list)
        guitar = item_prob(random(), 0.05, 16, show_list)
        rainbow_cursor = item_prob(random(), 0.05, 17, show_list)
        insignia = item_prob(0, 1, 131, show_list)
        dev_item = get_dev_item(show_list)
        res_text = "".join((weapon, wing, guitar, rainbow_cursor, insignia, dev_item, "\n"))
        show_text_and_icons(res_text, show_list)

    if boss_var.get() == 3:
        show_list = []
        weapon = choose_items([i for i in range(18, 25)], show_list)
        picksaw = item_prob(random(), 1 / 3, 25, show_list)
        shiny = item_prob(0, 1, 132, show_list)
        husks = get_multiple_items(randint(18, 23), 133, show_list)
        dev_item = get_dev_item(show_list)
        res_text = "".join((weapon, picksaw, shiny, husks,
                            dev_item, "\n"))
        show_text_and_icons(res_text, show_list)

    if boss_var.get() == 4:
        show_list = []
        weapon = choose_items([i for i in range(26, 33)], show_list)
        pygmy = item_prob(random(), 0.5, 33, show_list)
        axe = item_prob(random(), 0.05, 34, show_list)
        seedling = item_prob(random(), 1 / 15, 136, show_list)
        hook = item_prob(random(), 0.1, 35, show_list)
        sac = item_prob(0, 1, 134, show_list)
        key = item_prob(0, 1, 135, show_list)
        dev_item = get_dev_item(show_list)
        res_text = "".join((weapon, pygmy, axe, seedling, hook, sac, key, dev_item, "\n"))
        show_text_and_icons(res_text, show_list)

    if boss_var.get() == 5:
        show_list = []
        weapon = choose_items([i for i in range(36, 41)], show_list)
        wing = item_prob(random(), 1 / 15, 41, show_list)
        truffle = item_prob(0, 1, 137, show_list)
        dev_item = get_dev_item(show_list)
        res_text = "".join((weapon, wing, truffle, dev_item, "\n"))
        show_text_and_icons(res_text, show_list)

    if boss_var.get() == 6:
        show_list = []
        weapon = choose_items([i for i in range(62, 66)], show_list)
        medals = get_multiple_items(randint(30, 49), 60, show_list)
        wing = item_prob(random(), 0.25, 61, show_list)
        dev_item = get_dev_item(show_list)
        res_text = "".join((weapon, medals, wing, dev_item, "\n"))
        show_text_and_icons(res_text, show_list)

    if boss_var.get() == 7:  # 双子
        show_list = []
        sight = get_multiple_items(randint(25, 40), 143, show_list).replace("，", "")
        piece = item_prob(0, 1, 142, show_list)
        bars = get_multiple_items(randint(15, 30), 139, show_list)
        dev_item = get_dev_item(show_list)
        res_text = "".join((sight, piece, bars, dev_item, "\n"))
        show_text_and_icons(res_text, show_list)

    if boss_var.get() == 8:
        show_list = []
        might = get_multiple_items(randint(25, 40), 141, show_list).replace("，", "")
        piece = item_prob(0, 1, 140, show_list)
        bars = get_multiple_items(randint(15, 30), 139, show_list)
        dev_item = get_dev_item(show_list)
        res_text = "".join((might, piece, bars, dev_item, "\n"))
        show_text_and_icons(res_text, show_list)

    if boss_var.get() == 9:
        show_list = []
        fright = get_multiple_items(randint(25, 40), 145, show_list).replace("，", "")
        piece = item_prob(0, 1, 144, show_list)
        bars = get_multiple_items(randint(15, 30), 139, show_list)
        dev_item = get_dev_item(show_list)
        res_text = "".join((fright, piece, bars, dev_item, "\n"))
        show_text_and_icons(res_text, show_list)

    if boss_var.get() == 10:
        show_list = []
        armor = choose_items([67, 68, 69], show_list, num=2)
        staff = item_prob(random(), 1 / 3, 70, show_list)
        pillion = item_prob(random(), 0.5, 71, show_list)
        hook = item_prob(random(), 0.5, 72, show_list)
        balloons = get_multiple_items(randint(25, 74), 66, show_list)
        gelatin = item_prob(0, 1, 138, show_list)
        dev_item = get_dev_item(show_list)
        res_text = "".join((armor, staff, pillion, hook,
                            balloons, gelatin, dev_item, "\n"))
        show_text_and_icons(res_text, show_list)

    if boss_var.get() == 11:
        show_list = []
        armor = choose_items([75, 76, 77], show_list, num=2)
        saddle = item_prob(random(), 0.5, 74, show_list)
        gun = item_prob(random(), 0.5, 78, show_list)
        hook = item_prob(random(), 0.5, 79, show_list)
        gel = item_prob(0, 1, 73, show_list)
        res_text = "".join((armor, saddle, gun, hook, gel, "\n"))
        show_text_and_icons(res_text, show_list)

    if boss_var.get() == 12:
        show_list = [80]
        ItemList.counts[80] += 1
        scope = item_prob(random(), 1 / 30, 81, show_list)
        demonites = get_multiple_items(randint(30, 90), 82, show_list)
        arrows = get_multiple_items(randint(20, 50), 83, show_list)
        seeds = get_multiple_items(randint(1, 3), 84, show_list)
        res_text = "".join(("克苏鲁之盾", scope, demonites, arrows, seeds, "\n"))
        show_text_and_icons(res_text, show_list)

    if boss_var.get() == 13:
        show_list = [85]
        ItemList.counts[85] += 1
        bone = item_prob(random(), 0.05, 87, show_list)
        demonites = get_multiple_items(randint(30, 59), 82, show_list)
        scales = get_multiple_items(randint(10, 19), 86, show_list)
        res_text = "".join(("蠕虫围巾", bone, demonites, scales, "\n"))
        show_text_and_icons(res_text, show_list)

    if boss_var.get() == 14:
        show_list = [88]
        ItemList.counts[88] += 1
        bone = item_prob(random(), 0.05, 91, show_list)
        ores = get_multiple_items(randint(40, 90), 89, show_list)
        samples = get_multiple_items(randint(10, 19), 90, show_list)
        res_text = "".join(("混乱之脑", bone, ores, samples, "\n"))
        show_text_and_icons(res_text, show_list)

    if boss_var.get() == 15:
        show_list = []
        weapon = choose_items([93, 94, 95], show_list)
        vanity = choose_items([100, 101, 102], show_list, num=2)
        comb = item_prob(random(), 1 / 3, 96, show_list)
        nectar = item_prob(random(), 1 / 9, 97, show_list)
        goggles = item_prob(random(), 1 / 9, 98, show_list)
        hivepack = item_prob(0, 1, 92, show_list)
        wand = item_prob(0, 1, 99, show_list)
        beenades = get_multiple_items(randint(10, 29), 103, show_list)
        wax = get_multiple_items(randint(17, 29), 104, show_list)
        res_text = "".join((weapon, "，", vanity, comb, nectar, goggles,
                            hivepack, wand, beenades, wax,
                            "\n"))
        show_text_and_icons(res_text, show_list)

    if boss_var.get() == 16:
        show_list = []
        item_prob(0, 1, 105, show_list)
        ids = [106, 107, 126]
        r = randint(0, 2)
        item_get = "，" + ItemList.all_names[ids[r]]
        ItemList.counts[ids[r]] += 1
        show_list.append(ids[r])
        res_text = "".join(("骨头手套", item_get, "\n"))
        show_text_and_icons(res_text, show_list)

    if boss_var.get() == 17:
        show_list = []
        weapon = choose_items([i for i in range(112, 116)], show_list)
        helmet = item_prob(0, 1, 108, show_list)
        eye_bone = item_prob(random(), 1 / 3, 109, show_list)
        umbrella = item_prob(random(), 1 / 3, 110, show_list)
        radio = item_prob(random(), 1 / 3, 111, show_list)
        res_text = "".join((weapon, helmet, eye_bone, umbrella, radio, "\n"))
        show_text_and_icons(res_text, show_list)

    if boss_var.get() == 18:
        show_list = []
        weapon = choose_items([i for i in range(121, 125)], show_list)
        emblem = choose_items([i for i in range(117, 121)], show_list)
        show_list.extend([116, 125])
        ItemList.counts[116] += 1
        ItemList.counts[125] += 1
        res_text = "".join((weapon, "，", emblem, "，神锤，恶魔之心\n"))
        show_text_and_icons(res_text, show_list)


def obtain_treasures():
    def del_1st_comma(text1):
        text1 = text1.split("，")[1:]
        return "，".join(text1) + "\n"

    if ev_var.get() == 19:
        show_list = []
        text = ""
        if random() < 0.1:
            text += "，" + choose_items([146, 147], show_list)
        if random() < 0.25:
            text += "，" + choose_items([148, 149], show_list)
        text += item_prob(random(), 0.1, 150, show_list)
        text += item_prob(random(), 0.25, 151, show_list)
        if text:
            show_text_and_icons(del_1st_comma(text), show_list)
        else:
            show_text_and_icons("无掉落\n", show_list)

    if ev_var.get() == 20:
        show_list = []
        text = ""
        if random() < 0.125:
            text += "，" + choose_items([i for i in range(152, 156)], show_list)
        if random() < 0.25:
            text += "，" + choose_items([i for i in range(156, 161)], show_list)
        text += item_prob(random(), 0.1, 162, show_list)
        text += item_prob(random(), 0.25, 161, show_list)
        text += item_prob(random(), 0.25, 219, show_list)
        if text:
            show_text_and_icons(del_1st_comma(text), show_list)
        else:
            show_text_and_icons("无掉落\n", show_list)

    if ev_var.get() == 21:
        show_list = []
        text = ""
        text += item_prob(random(), 0.0025, 163, show_list)
        text += item_prob(random(), 0.005, 164, show_list)
        text += item_prob(random(), 0.01, 165, show_list)
        text += item_prob(random(), 0.01, 166, show_list)
        text += item_prob(random(), 0.02, 167, show_list)
        text += item_prob(random(), 0.05, 168, show_list)
        text += item_prob(random(), 0.1, 169, show_list)
        text += item_prob(random(), 0.25, 170, show_list)
        text += item_prob(random(), 0.1, 171, show_list)
        if text:
            show_text_and_icons(del_1st_comma(text), show_list)
        else:
            show_text_and_icons("无掉落\n", show_list)

    if ev_var.get() == 22:
        show_list = []
        text = ""
        text += get_multiple_items(randint(30, 50), 172, show_list)
        text += "，" + choose_items([173, 174, 175, 177, 178], show_list)
        if "尖桩发射器" in text.split("，"):
            text += get_multiple_items(randint(30, 60), 176, show_list)
        text += item_prob(random(), 0.25, 180, show_list)
        text += item_prob(random(), 0.25, 181, show_list)
        text += item_prob(random(), 0.1, 179, show_list)
        show_text_and_icons(del_1st_comma(text), show_list)

    if ev_var.get() == 23:
        show_list = []
        text = ""
        text += "，" + choose_items([182, 183, 184, 185, 186, 187, 189, 191], show_list)
        if ItemList.all_names[187] in text.split("，"):
            text += get_multiple_items(randint(50, 100), 188, show_list)
        if ItemList.all_names[189] in text.split("，"):
            text += get_multiple_items(randint(25, 50), 190, show_list)
        text += item_prob(random(), 0.25, 193, show_list)
        text += item_prob(0, 1, 192, show_list)
        show_text_and_icons(del_1st_comma(text), show_list)

    if ev_var.get() == 24:
        show_list = []
        text = ""
        if random() < 3 * (1 / 9 + 0.2):
            text += "，" + choose_items([194, 195, 196], show_list)
        else:
            text += item_prob(0, 1, 197, show_list)
        text += item_prob(random(), 0.25, 199, show_list)
        text += item_prob(random(), 0.1, 198, show_list)
        show_text_and_icons(del_1st_comma(text), show_list)

    if ev_var.get() == 25:
        show_list = []
        text = ""
        text += "，" + choose_items([200, 201], show_list)
        text += item_prob(random(), 0.25, 203, show_list)
        text += item_prob(random(), 0.6, 202, show_list)
        show_text_and_icons(del_1st_comma(text), show_list)

    if ev_var.get() == 26:
        show_list = []
        text = ""
        if random() < 3 * (1 / 9 + 0.2):
            text += "，" + choose_items([204, 205, 206], show_list)
        else:
            text += item_prob(0, 1, 207, show_list)
        text += item_prob(random(), 1 / 30, 208, show_list)
        text += item_prob(random(), 0.25, 210, show_list)
        text += item_prob(random(), 0.6, 209, show_list)
        show_text_and_icons(del_1st_comma(text), show_list)

    if ev_var.get() == 27:
        show_list = []
        text = ""
        text += "，" + choose_items([i for i in range(211, 217)], show_list)
        text += item_prob(random(), 0.25, 218, show_list)
        text += item_prob(random(), 0.1, 217, show_list)
        show_text_and_icons(del_1st_comma(text), show_list)


def clear_interface():
    for i in range(len(ItemList.counts)):
        ItemList.counts[i] = 0
    for item in tv.get_children():
        tv.delete(item)
    txt.delete(1.0, END)
