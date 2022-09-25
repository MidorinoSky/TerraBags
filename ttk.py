from ttkbootstrap import PhotoImage
from ttkbootstrap import Style
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from tooltip import CreateToolTip, HideToolTip
from ctypes import windll
from random import randint, random

moon_lord_list = {
    0: "彩虹猫之刃",
    1: "狂星之怒",
    2: "泰拉悠悠球",
    3: "月亮传送门法杖",
    4: "七彩水晶法杖",
    5: "太空海豚机枪",
    6: "庆典MK2",
    7: "最终棱镜",
    8: "月耀",
    9: "彩虹猫矿车",
    10: "夜明矿",
}

empress_list = {
    11: "星光",
    12: "夜光",
    13: "日暮",
    14: "万花筒",
    15: "女皇之翼",
    16: "星星吉他",
    17: "彩虹光标",
}

golem_list = {
    18: "毒刺发射器",
    19: "疯狂飞斧",
    20: "太阳石",
    21: "石巨人之眼",
    22: "大地法杖",
    23: "高温射线枪",
    24: "石巨人之拳",
    25: "锯刃镐",
}

plantera_list = {
    26: "榴弹发射器",
    27: "维纳斯万能枪",
    28: "爆裂藤蔓",
    29: "吹叶机",
    30: "花之力",
    31: "胡蜂枪",
    32: "种子弯刀",
    33: "矮人法杖",
    34: "吉他斧",
    35: "刺钩",
}

duke_list = {
    36: "泡泡枪",
    37: "利刃台风",
    38: "猪鲨链球",
    39: "海啸",
    40: "暴风雨法杖",
    41: "猪龙鱼之翼",
}

dev_list = {
    42: "Aaron的套装",
    43: "Arkhalis的套装",
    44: "Cenx的套装",
    45: "Red的套装",
    46: "Crowno的套装",
    47: "D-Town的套装",
    48: "Jim的套装",
    49: "Lazure的套装",
    50: "Leinfors的套装",
    51: "Loki的套装",
    52: "Red的套装",
    53: "Skiphs的套装",
    54: "Will的套装",
    55: "Yoraiz0r的套装",
    56: "Grox The Great的套装",
    57: "FoodBarbarian的套装",
    58: "Safeman的套装",
    59: "Ghostar的套装",
}

betsy_list = {
    60: "护卫奖章",  # 30-49
    61: "双足翼龙之翼",  # 25%
    62: "空中祸害",
    63: "天龙之怒",
    64: "双足翼龙怒气",
    65: "飞龙",
}

queen_slime_list = {
    66: "闪耀史莱姆气球",  # 25-74
    67: "水晶刺客兜帽",
    68: "水晶刺客上衣",
    69: "水晶刺客裤",  # 三个中掉两个
    70: "刃杖",  # 33%
    71: "明胶女式鞍",  # 50%
    72: "失谐钩爪",  # 50%
}

king_slime_list = {
    73: "皇家凝胶",
    74: "粘鞍",  # 50%
    75: "忍者兜帽",
    76: "忍者衣",
    77: "忍者裤",
    78: "史莱姆枪",  # 50%
    79: "史莱姆钩",  # 50%
}

eoc_list = {
    80: "克苏鲁之盾",
    81: "双筒望远镜",  # 1/30
    82: "魔矿",  # 30-90
    83: "邪箭",  # 20-50
    84: "腐化种子",  # 1-3
}

eater_list = {
    85: "蠕虫围巾",
    86: "暗影鳞片",
    87: "吞噬怪骨头",  # 0.05
}

brain_list = {
    88: "混乱之脑",
    89: "猩红矿",
    90: "组织样本",
    91: "骨头拨浪鼓",
}

bee_list = {
    92: "蜂巢背包",
    93: "蜜蜂枪",
    94: "养蜂人",
    95: "蜂膝弓",
    96: "蜂窝",
    97: "花蜜",
    98: "涂蜜护目镜",
    99: "蜂巢魔棒",
    100: "蜜蜂帽",
    101: "蜜蜂衣",
    102: "蜜蜂裤",
    103: "蜜蜂手榴弹",
    104: "蜂蜡",
}

skeletron_list = {
    105: "骨头手套",  # 100%
    106: "骷髅王之手",
    107: "骷髅头法书",
}

deerclop_list = {
    108: "骸骨头盔",  # 100%
    109: "眼骨",  # 1/3
    110: "眼球伞",  # 1/3
    111: "收音机",  # 1/3
    112: "气喇叭",
    113: "天候棒",
    114: "眼球激光塔",
    115: "露西斧",
}

wof_list = {
    116: "神锤",
    117: "战士徽章",
    118: "游侠徽章",
    119: "巫士徽章",
    120: "召唤师徽章",
    121: "毁灭刃",  # 四选一
    122: "发条式突击步枪",
    123: "激光步枪",
    124: "鞭炮",
    125: "恶魔之心"
}

addition = {
    126: "骷髅王面具",
    127: "天界星盘",
    128: "传送枪",
    129: "重力球",
    130: "可疑触手",
    131: "翱翔证章",
    132: "闪亮石",
    133: "甲虫外壳",
    134: "孢子囊",
    135: "神庙钥匙",
    136: "幼苗",
    137: "虾松露",
    138: "挥发明胶",
}

all_names = list(moon_lord_list.values()) + list(
    empress_list.values()) + list(
    golem_list.values()) + list(
    plantera_list.values()) + list(
    duke_list.values()) + list(
    dev_list.values()) + list(
    betsy_list.values()) + list(
    queen_slime_list.values()) + list(
    king_slime_list.values()) + list(
    eoc_list.values()) + list(
    eater_list.values()) + list(
    brain_list.values()) + list(
    bee_list.values()) + list(
    skeletron_list.values()) + list(
    deerclop_list.values()) + list(
    wof_list.values()) + list(
    addition.values())

counts = [0] * len(all_names)

"""========================================================"""


def window_setup():
    global boss_var, txt, tv, fr, item_labels
    windll.shcore.SetProcessDpiAwareness(1)  # 适应高dpi
    root = Style(theme="minty").master

    """------------------------------------------------------"""
    """顶部界面"""
    frameCnt = 6
    frames = [PhotoImage(file="interface/slime_prince.gif", format='gif -index %i' % i) for i in range(frameCnt)]
    frames2 = [PhotoImage(file="interface/fishron.gif", format='gif -index %i' % i) for i in range(frameCnt)]

    bg_frame = ttk.Frame(master=root)
    bg_frame.pack(side=TOP, fill=BOTH)
    bg_label = ttk.Label(master=bg_frame, image=frames[0])
    bg_label.pack(side=LEFT, fill=BOTH, padx=10)
    bg_label.image = frames[0]
    bg_label2 = ttk.Label(master=bg_frame, image=frames2[0])
    bg_label2.pack(side=RIGHT, fill=BOTH, padx=10)
    bg_label2.image = frames[0]

    def update(ind):
        frame = frames[ind]
        frame2 = frames2[ind]
        ind += 1
        if ind == frameCnt:
            ind = 0
        bg_label.configure(image=frame)
        bg_label2.configure(image=frame2)
        root.after(100, update, ind)

    var = ttk.StringVar()
    var.set("F")

    def dark_mode():
        if var.get() == "T":
            Style(theme="darkly")
        else:
            Style(theme="minty")

    cb1 = ttk.Checkbutton(master=bg_frame, text="夜间模式",
                          variable=var, onvalue="T", offvalue="F",
                          command=dark_mode,
                          bootstyle=(SUCCESS, ROUND, TOGGLE))
    cb1.pack(fill=X, padx=10, pady=10, side=RIGHT)

    """------------------------------------------------------"""
    """左侧界面"""
    lframe = ttk.Frame(root, padding=5)
    lframe.pack(side=LEFT, fill=BOTH, expand=YES)

    rb_group = ttk.Labelframe(
        lframe, text="Boss", padding=5
    )
    rb_group.pack(fill=BOTH, side=TOP, expand=YES)

    nb = ttk.Notebook(master=rb_group)
    nb.pack(anchor=N, fill=X, expand=YES, pady=3)
    pre_hm_frame = ttk.Frame(nb)
    pre_hm_frame.pack(expand=YES)
    hm_frame = ttk.Frame(nb)
    hm_frame.pack(expand=YES)
    all_boss_frame = ttk.Frame(nb)
    all_boss_frame.pack(expand=YES)
    nb.add(pre_hm_frame, text="困难模式前", sticky=W)
    nb.add(hm_frame, text="困难模式后", sticky=W)
    nb.add(all_boss_frame, text="全部", sticky=W)

    boss_var = ttk.IntVar(root, 1)  # 单选按钮的变量
    values_hm = {
        "月亮领主": 1,
        "光之女皇": 2,
        "石巨人": 3,
        "世纪之花": 4,
        "猪龙鱼公爵": 5,
        "双足翼龙": 6,
        "史莱姆皇后": 7,
    }
    values_phm = {
        "史莱姆王": 8,
        "克苏鲁之眼": 9,
        "世界吞噬者": 10,
        "克苏鲁之脑": 11,
        "蜂王": 12,
        "骷髅王": 13,
        "独眼巨鹿": 14,
        "血肉之墙": 15,
    }

    """------------------------------------------"""
    """所有、肉前、肉后"""
    grid_frame = ttk.Frame(master=all_boss_frame, padding=5)
    grid_frame.pack(fill=BOTH, anchor=CENTER, expand=YES)
    for i in range(15):
        img_file = "interface/" + str(i + 1) + ".png"
        img = PhotoImage(file=img_file)
        label = ttk.Label(master=grid_frame, image=img)
        if i < 7:
            label.grid(row=i, column=0, padx=10, pady=8)
            label.image = img
        if i >= 7:
            label.grid(row=i - 7, column=2, padx=10, pady=8)
            label.image = img
    k = 0
    all_values = dict(values_hm, **values_phm)
    for (text, value) in all_values.items():
        rb = ttk.Radiobutton(master=grid_frame, text=text, variable=boss_var, value=value)
        if k < 7:
            rb.grid(row=k, column=1, sticky=W, padx=5)
        if k >= 7:
            rb.grid(row=k - 7, column=3, sticky=W, padx=5)
        k += 1

    grid_pre_hm = ttk.Frame(master=pre_hm_frame, padding=5)
    grid_pre_hm.pack(fill=BOTH, anchor=CENTER, expand=YES)
    for i in range(7, 15):
        img_file = "interface/"+str(i+1)+".png"
        img = PhotoImage(file=img_file)
        label = ttk.Label(master=grid_pre_hm, image=img)
        label.grid(row=i-7, column=0, padx=10, pady=8)
        label.image = img
    k = 0
    for (text, value) in values_phm.items():
        rb = ttk.Radiobutton(master=grid_pre_hm, text=text, variable=boss_var, value=value)
        rb.grid(row=k, column=1, sticky=W, padx=5)
        k += 1

    grid_hm = ttk.Frame(master=hm_frame, padding=5)
    grid_hm.pack(fill=BOTH, anchor=CENTER, expand=YES)
    for i in range(7):
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

    button_frame = ttk.Frame(master=lframe, padding=5)
    button_frame.pack(anchor=CENTER, expand=YES)
    ttk.Button(master=button_frame, text="打开宝藏袋",
               bootstyle=SUCCESS, command=open_bag, width=15).pack(pady=5)
    ttk.Button(master=button_frame, text="重置",
               bootstyle=SUCCESS, command=clear_interface, width=15).pack(pady=5)

    """------------------------------------------------------"""
    """右侧界面"""
    rframe = ttk.Frame(root, padding=5)
    rframe.pack(side=RIGHT, fill=BOTH, expand=YES)

    res_group = ttk.Labelframe(
        rframe, text="获取的物品", padding=10
    )
    res_group.pack(fill=BOTH, ipady=10, side=TOP, expand=YES)

    txt = ttk.ScrolledText(master=res_group, height=7, width=50)
    txt.pack(side=TOP, anchor=W, pady=5, fill=BOTH, expand=YES)

    tv = ttk.Treeview(master=res_group, columns=[0, 1], show=HEADINGS, height=6)
    for i in range(5):
        tv.insert("", END, values=(" ", " "))

    tv.heading(0, text="物品")
    tv.heading(1, text="数量")
    tv.column(0, width=150)
    tv.column(1, width=150, anchor=CENTER)
    tv.pack(side=TOP, anchor=W, fill=BOTH, pady=5, expand=YES)

    icons_frame = ttk.Labelframe(master=res_group, text="最后获取的物品", padding=5)
    icons_frame.pack(fill=X, expand=YES, pady=0, side=BOTTOM, anchor=W, ipady=55)
    icons_frame.pack_propagate(0)
    fr = ttk.Frame(master=icons_frame)
    fr.pack(side=LEFT, anchor=W)
    fr.pack_propagate(0)

    item_labels = [ttk.Label(master=fr, image="", width=2) for j in range(11)]
    for i, l in enumerate(item_labels):
        l.grid(row=0, column=i, padx=10, pady=4, sticky=W)

    root.after(0, update, 0)

    return root


def display_rank():
    item_dict = dict(zip(all_names, counts))
    item_rank = sorted(item_dict.items(), key=lambda x: x[1], reverse=True)
    for item in tv.get_children():
        tv.delete(item)

    for item in item_rank:
        if item[1] != 0:
            tv.insert("", END, values=item)
        else:
            continue


def get_multiple_items(amount, item_id, show_list):
    counts[item_id] += amount
    show_list.append(item_id)
    text = "".join(("，", all_names[item_id], "*", str(amount)))
    return text


def item_prob(x, p, item_id, show_list):
    item_name = ""
    if 0 <= x < p:
        item_name = "，" + all_names[item_id]
        counts[item_id] += 1
        show_list.append(item_id)
    return item_name


def choose_items(a, b, show_list, num=1):
    if num == 1:
        item_id = randint(a, b)
        item_name = all_names[item_id]
        counts[item_id] += 1
        show_list.append(item_id)
        return item_name
    if num == 2:
        item_id = randint(a, b)
        item2_id = item_id
        while item2_id == item_id:
            item2_id = randint(a, b)
        counts[item_id] += 1
        counts[item2_id] += 1
        show_list.extend([item_id, item2_id])
        name1 = all_names[item_id]
        name2 = "，" + all_names[item2_id]
        return name1 + name2


def get_dev_item(show_list):
    r = randint(42, 59)
    r2 = random()
    dev_item = ""
    if 0 <= r2 < 0.05:
        counts[r] += 1
        dev_item = "，" + dev_list[r]
    if dev_item != "":
        show_list.append(r)
    return dev_item


def show_last_items(id_list):
    for k, item_id in enumerate(id_list):
        icon = PhotoImage(file="item/"+str(item_id)+".png")
        item_labels[k].configure(image=icon)
        item_labels[k].image = icon
        CreateToolTip(item_labels[k], all_names[item_id])

    for j in range(len(id_list), 11):
        item_labels[j].configure(image="")
        item_labels[j].children.clear()
        HideToolTip(item_labels[j])


def open_bag():
    if boss_var.get() == 1:
        show_list = []
        weapon = choose_items(0, 8, show_list)
        luminites = get_multiple_items(randint(70, 90), 10, show_list)
        cart = item_prob(random(), 0.1, 9, show_list)
        starboard = item_prob(0, 1, 127, show_list)
        portal_gun = item_prob(0, 1, 128, show_list)
        gravity_globe = item_prob(0, 1, 129, show_list)
        tentacle = item_prob(0, 1, 130, show_list)
        dev_item = get_dev_item(show_list)

        res_text = "".join(("获得：", weapon, luminites,
                            cart, starboard, portal_gun, gravity_globe, tentacle,
                            dev_item, "\n"))
        txt.insert(END, res_text)
        txt.yview_moveto(1)
        display_rank()
        show_last_items(show_list)

    if boss_var.get() == 2:
        show_list = []
        weapon = choose_items(11, 14, show_list)
        wing = item_prob(random(), 0.1, 15, show_list)
        guitar = item_prob(random(), 0.05, 16, show_list)
        rainbow_cursor = item_prob(random(), 0.05, 17, show_list)
        insignia = item_prob(0, 1, 131, show_list)
        dev_item = get_dev_item(show_list)
        res_text = "".join(("获得：", weapon, wing, guitar, rainbow_cursor, insignia, dev_item, "\n"))
        txt.insert(END, res_text)
        txt.yview_moveto(1)
        display_rank()
        show_last_items(show_list)

    if boss_var.get() == 3:
        show_list = []
        weapon = choose_items(18, 24, show_list)
        picksaw = item_prob(random(), 1 / 3, 25, show_list)
        shiny = item_prob(0, 1, 132, show_list)
        husks = get_multiple_items(randint(18, 23), 133, show_list)
        dev_item = get_dev_item(show_list)
        res_text = "".join(("获得：", weapon, picksaw, shiny, husks,
                            dev_item, "\n"))
        txt.insert(END, res_text)
        txt.yview_moveto(1)
        display_rank()
        show_last_items(show_list)

    if boss_var.get() == 4:
        show_list = []
        weapon = choose_items(26, 32, show_list)
        pygmy = item_prob(random(), 0.5, 33, show_list)
        axe = item_prob(random(), 0.05, 34, show_list)
        seedling = item_prob(random(), 1 / 15, 136, show_list)
        hook = item_prob(random(), 0.1, 35, show_list)
        sac = item_prob(0, 1, 134, show_list)
        key = item_prob(0, 1, 135, show_list)
        dev_item = get_dev_item(show_list)
        res_text = "".join(("获得：", weapon, pygmy, axe, seedling, hook, sac, key, dev_item, "\n"))
        txt.insert(END, res_text)
        txt.yview_moveto(1)
        display_rank()
        show_last_items(show_list)

    if boss_var.get() == 5:
        show_list = []
        weapon = choose_items(36, 40, show_list)
        wing = item_prob(random(), 1 / 15, 41, show_list)
        truffle = item_prob(0, 1, 137, show_list)
        dev_item = get_dev_item(show_list)
        res_text = "".join(("获得：", weapon, wing, truffle, dev_item, "\n"))
        txt.insert(END, res_text)
        txt.yview_moveto(1)
        display_rank()
        show_last_items(show_list)

    if boss_var.get() == 6:
        show_list = []
        weapon = choose_items(62, 65, show_list)
        medals = get_multiple_items(randint(30, 49), 60, show_list)
        wing = item_prob(random(), 0.25, 61, show_list)
        dev_item = get_dev_item(show_list)
        res_text = "".join(("获得：", weapon, medals, wing, dev_item, "\n"))
        txt.insert(END, res_text)
        txt.yview_moveto(1)
        display_rank()
        show_last_items(show_list)

    if boss_var.get() == 7:
        show_list = []
        armor = choose_items(67, 69, show_list, num=2)
        staff = item_prob(random(), 1 / 3, 70, show_list)
        pillion = item_prob(random(), 0.5, 71, show_list)
        hook = item_prob(random(), 0.5, 72, show_list)
        balloons = get_multiple_items(randint(25, 74), 66, show_list)
        gelatin = item_prob(0, 1, 138, show_list)
        dev_item = get_dev_item(show_list)
        res_text = "".join(("获得：", armor, staff, pillion, hook,
                            balloons, gelatin, dev_item, "\n"))
        txt.insert(END, res_text)
        txt.yview_moveto(1)
        display_rank()
        show_last_items(show_list)

    if boss_var.get() == 8:
        show_list = []
        armor = choose_items(75, 77, show_list, num=2)
        saddle = item_prob(random(), 0.5, 74, show_list)
        gun = item_prob(random(), 0.5, 78, show_list)
        hook = item_prob(random(), 0.5, 79, show_list)
        gel = item_prob(0, 1, 73, show_list)
        res_text = "".join(("获得：", armor, saddle, gun, hook, gel, "\n"))
        txt.insert(END, res_text)
        txt.yview_moveto(1)
        display_rank()
        show_last_items(show_list)

    if boss_var.get() == 9:
        show_list = [80]
        counts[80] += 1
        scope = item_prob(random(), 1 / 30, 81, show_list)
        demonites = get_multiple_items(randint(30, 90), 82, show_list)
        arrows = get_multiple_items(randint(20, 50), 83, show_list)
        seeds = get_multiple_items(randint(1, 3), 84, show_list)
        res_text = "".join(("获得：", "克苏鲁之盾", scope, demonites, arrows, seeds, "\n"))
        txt.insert(END, res_text)
        txt.yview_moveto(1)
        display_rank()
        show_last_items(show_list)

    if boss_var.get() == 10:
        show_list = [85]
        counts[85] += 1
        bone = item_prob(random(), 0.05, 87, show_list)
        demonites = get_multiple_items(randint(30, 59), 82, show_list)
        scales = get_multiple_items(randint(10, 19), 86, show_list)
        res_text = "".join(("获得：蠕虫围巾", bone, demonites, scales, "\n"))
        txt.insert(END, res_text)
        txt.yview_moveto(1)
        display_rank()
        show_last_items(show_list)

    if boss_var.get() == 11:
        show_list = [88]
        counts[88] += 1
        bone = item_prob(random(), 0.05, 91, show_list)
        ores = get_multiple_items(randint(40, 90), 89, show_list)
        samples = get_multiple_items(randint(10, 19), 90, show_list)
        res_text = "".join(("获得：混乱之脑", bone, ores, samples, "\n"))
        txt.insert(END, res_text)
        txt.yview_moveto(1)
        display_rank()
        show_last_items(show_list)

    if boss_var.get() == 12:
        show_list = []
        weapon = choose_items(93, 95, show_list)
        vanity = choose_items(100, 102, show_list, num=2)
        comb = item_prob(random(), 1 / 3, 96, show_list)
        nectar = item_prob(random(), 1 / 9, 97, show_list)
        goggles = item_prob(random(), 1 / 9, 98, show_list)
        hivepack = item_prob(0, 1, 92, show_list)
        wand = item_prob(0, 1, 99, show_list)
        beenades = get_multiple_items(randint(10, 29), 103, show_list)
        wax = get_multiple_items(randint(17, 29), 104, show_list)
        res_text = "".join(("获得：", weapon, "，", vanity, comb, nectar, goggles,
                            hivepack, wand, beenades, wax,
                            "\n"))
        txt.insert(END, res_text)
        txt.yview_moveto(1)
        display_rank()
        show_last_items(show_list)

    if boss_var.get() == 13:
        show_list = []
        item_prob(0, 1, 105, show_list)
        ids = [106, 107, 126]
        r = randint(0, 2)
        item_get = "，" + all_names[ids[r]]
        counts[ids[r]] += 1
        show_list.append(ids[r])
        res_text = "".join(("获得：骨头手套", item_get, "\n"))
        txt.insert(END, res_text)
        txt.yview_moveto(1)
        display_rank()
        show_last_items(show_list)

    if boss_var.get() == 14:
        show_list = []
        weapon = choose_items(112, 115, show_list)
        helmet = item_prob(0, 1, 108, show_list)
        eye_bone = item_prob(random(), 1 / 3, 109, show_list)
        umbrella = item_prob(random(), 1 / 3, 110, show_list)
        radio = item_prob(random(), 1 / 3, 111, show_list)
        res_text = "".join(("获得：", weapon, helmet, eye_bone, umbrella, radio, "\n"))
        txt.insert(END, res_text)
        txt.yview_moveto(1)
        display_rank()
        show_last_items(show_list)

    if boss_var.get() == 15:
        show_list = []
        weapon = choose_items(121, 124, show_list)
        emblem = choose_items(117, 120, show_list)
        show_list.extend([116, 125])
        counts[116] += 1
        counts[125] += 1
        res_text = "".join(("获得：", weapon, "，", emblem, "，神锤，恶魔之心\n"))
        txt.insert(END, res_text)
        txt.yview_moveto(1)
        display_rank()
        show_last_items(show_list)


def clear_interface():
    for i in range(len(counts)):
        counts[i] = 0
    for item in tv.get_children():
        tv.delete(item)
    txt.delete(1.0, END)


if __name__ == "__main__":
    window = window_setup()
    window.iconbitmap("bag.ico")
    window.title("泰拉瑞亚：宝藏袋")
    window.mainloop()
