from glob import glob
from time import sleep
import tkinter as tk
import tkinter.messagebox as tkmsg
#from tkinter.font import nametofont
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk,Radiobutton,IntVar,Scrollbar,StringVar

from kiwisolver import Variable
#from colorama import Style
#from matplotlib import style


def notice(s="正文",type="info",title="来自Python课设的提示",time=0):
    ntc=tk.Tk()
    ntc.withdraw()
    if time>0: tms=int(time*1000)
    else: tms=int(10*1000) #10秒后必须销毁
    ntc.after(tms, ntc.destroy)
    if type=="err":
        tkmsg.showerror(title,s,master=ntc)
    elif type=="warn":
        tkmsg.showwarning(title,s,master=ntc)
    else: tkmsg.showinfo(title,s,master=ntc)
    return ntc

def asktf(s,title="PY程序设计"):
    window = Tk()
    window.withdraw()  # 退出默认 tk 窗口
    result = tkmsg.askquestion(title,s)
    return result

def tk_table():
    pass
def rk2score(rk):
    try:
        rk=int(rk)
    except (ValueError, ArithmeticError):
        notice("该生名次不是数字！请检查数据文件","err","名次错误")
    except: notice("未知异常","err","名次错误")
    if rk==1: return 10
    elif rk==2: return 8
    elif 3<=rk<=8: return 9-rk
    else: return 0

def initial():
    global sports, faculties, stus
    sports, faculties, stus=[],[],[]
    
def file_append(filename,content):#文件末尾追加内容
    import re
    f=open(filename,"r+",encoding='gbk')
    s=f.read()
    if s[-1]!="\n": s+="\n"
    f=open(filename,"w+",encoding='gbk')
    f.write("\n".join(re.split(r"\n+", s)))#去除原有多余的、末尾的换行
    f.write(content+"\n")
    f.close()

def sex_change(n):
    if n==1: return "男"
    else: return "女"

def add1():#录入运动会项目
    def add1_gui():
        def form():
            file_append("1.csv",entry_1.get()+","+entry_2.get()+","+sex_change(sex.get()))
            notice(entry_1.get()+entry_2.get()+sex_change(sex.get())+"添加成功","info","添加成功",1.9)
            return
        window = Tk()
        window.title("项目增添-运动会项目")
        window.geometry("464x400")
        window.configure(bg = "#FFFFFF")
        canvas = Canvas(
            window,
            bg = "#FFFFFF",
            height = 400,
            width = 464,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        canvas.place(x = 0, y = 0)
        
        op=IntVar(master=window)
        op.set(1)
        entry_0 = Radiobutton(window,text="追加",value=1,variable=op)
        entry_0.place(
            x=125.0,
            y=70.0,
            width=308.0,
            height=25.0
        )
        
        entry_1 = Entry(
            window,
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0
        )
        entry_1.place(
            x=125.0,
            y=114.0,
            width=308.0,
            height=45.0
        )

        entry_2 = Entry(
            window,
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0
        )
        entry_2.place(
            x=125.0,
            y=194.0,
            width=308.0,
            height=45.0
        )

        sex=IntVar(master=window)
        
        entry_31 = Radiobutton(window,text="男",value=1,variable=sex)
        entry_31.place(
            x=125,
            y=274,
            width=154.0,
            height=45.0
        )

        entry_32 = Radiobutton(window,text="女",value=0,variable=sex)
        entry_32.place(
            x=279,
            y=274,
            width=154.0,
            height=45.0
        )

        canvas.create_text(
            110.0,
            134.0,
            anchor="e",
            text="项目编号",
            fill="#000000",
            font=("Microsoft YaHei", 16 * -1)
        )

        canvas.create_text(
            110.0,
            214.0,
            anchor="e",
            text="项目名称",
            fill="#000000",
            font=("Microsoft YaHei", 16 * -1)
        )

        canvas.create_text(
            110.0,
            294.0,
            anchor="e",
            text="项目组别",
            fill="#000000",
            font=("Microsoft YaHei", 16 * -1)
        )

        canvas.create_text(
            232,
            24.0,
            anchor="n",
            text="项目信息",
            fill="#000000",
            font=("Microsoft YaHei", 18 * -1)
        )

        button_1 = Button(
            window,
            borderwidth=0,
            highlightthickness=0,
            command=form,
            relief="flat",
            #bg=mdcolor[2],
            text="提交",
            #font=btn_sty,
            fg="#000"
        )
        button_1.place(
            x=232,
            y=380,
            width=140.0,
            height=30.0,
            anchor="s"
        )
        window.resizable(False, False)
        window.mainloop()
        
    global sports
    #maintain=asktf("要保留原数据吗？\n【是】保留已有数据\n【否】清除已有数据")
    maintain=True#调试
    
    #if maintain:
    #    f1=open("1.csv","a+",encoding='gbk')
    #else: f1=open("1.csv","w+",encoding='gbk')5\
    add1_gui()
    #f1.close()
    print("运动会项目输入完毕！\n----------")

def add2(): #录入院系信息
    global faculties
    
    def add2_gui():
        def form():
            file_append("2.csv",entry_1.get()+","+entry_2.get())
            notice(entry_1.get()+entry_2.get()+"添加成功","info","添加成功",2.1)
            return
        window = Tk()
        window.title("项目增添-学院信息")
        window.geometry("464x320")
        window.configure(bg = "#FFFFFF")
        canvas = Canvas(
            window,
            bg = "#FFFFFF",
            height = 320,
            width = 464,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        canvas.place(x = 0, y = 0)
        
        op=IntVar(master=window)
        op.set(1)
        entry_0 = Radiobutton(window,text="追加",value=1,variable=op)
        entry_0.place(
            x=125.0,
            y=70.0,
            width=308.0,
            height=25.0
        )
        
        entry_1 = Entry(
            window,
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0
        )
        entry_1.place(
            x=125.0,
            y=114.0,
            width=308.0,
            height=45.0
        )

        entry_2 = Entry(
            window,
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0
        )
        entry_2.place(
            x=125.0,
            y=194.0,
            width=308.0,
            height=45.0
        )

        canvas.create_text(
            110.0,
            134.0,
            anchor="e",
            text="学院编号",
            fill="#000000",
            font=("Microsoft YaHei", 16 * -1)
        )

        canvas.create_text(
            110.0,
            214.0,
            anchor="e",
            text="学院名称",
            fill="#000000",
            font=("Microsoft YaHei", 16 * -1)
        )

        canvas.create_text(
            232,
            24.0,
            anchor="n",
            text="学院信息",
            fill="#000000",
            font=("Microsoft YaHei", 18 * -1)
        )

        button_1 = Button(
            window,
            borderwidth=0,
            highlightthickness=0,
            command=form,
            relief="flat",
            #bg=mdcolor[2],
            text="提交",
            #font=btn_sty,
            fg="#000"
        )
        button_1.place(
            x=232,
            y=300,
            width=140.0,
            height=30.0,
            anchor="s"
        )
        window.resizable(False, False)
        window.mainloop()
    add2_gui()
    print("运动会项目输入完毕！\n----------")

def array_falcuties(n):
    readf2()
    global faculties
    a1,a2,a3=[],[],[]
    for i in range(len(faculties)):
        a1.append(faculties[i]["fid"])
        a2.append(faculties[i]["fname"])
        a3.append(faculties[i]["fid"]+" "+faculties[i]["fname"])
    if n==1: print(a1);return a1
    elif n==2: return a2
    elif n==3: return a3

def array_sports(n):
    readf1()
    global sports
    a=[]
    for i in range(len(sports)):
        a.append([sports[i]["name"],sports[i]["group"]])
    return a

def add3():#录入成绩信息
    #global stus
    def add3_gui():
        def form():
            a=[entry_1.get(),entry_2.get(),sex_change(entry_3.get()),get_falcuty_fid(entry_4.get()),get_sportid(entry_5.get()),entry_6.get()]
            print(a)
            file_append("3.csv",a[0]+","+a[1]+","+a[2]+","+a[3]+","+a[4]+","+a[5])
            
            return
        window = Tk()
        window.geometry("762x313")
        window.configure(bg = "#FFFFFF")
        canvas = Canvas(
            window,
            bg = "#FFFFFF",
            height = 313,
            width = 762,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_text(
            381,
            10,
            anchor="n",
            text="学生信息",
            fill="#000000",
            font=("Microsoft YaHei", 18 * -1)
        )

        canvas.create_text(
            80.0,
            103.0,
            anchor="e",
            text="学号",
            fill="#000000",
            font=("Microsoft YaHei", 18 * -1)
        )

        canvas.create_text(
            335,
            103,
            anchor="e",
            text="姓名",
            fill="#000000",
            font=("Microsoft YaHei", 18 * -1)
        )

        canvas.create_text(
            565.0,
            103,
            anchor="e",
            text="性别",
            fill="#000000",
            font=("Microsoft YaHei", 18 * -1)
        )

        canvas.create_text(
            80.0,
            173.0,
            anchor="e",
            text="院系编号",
            fill="#000000",
            font=("Microsoft YaHei", 18 * -1)
        )

        canvas.create_text(
            335.0,
            173.0,
            anchor="e",
            text="项目编号",
            fill="#000000",
            font=("Microsoft YaHei", 18 * -1)
        )

        canvas.create_text(
            565.0,
            173.0,
            anchor="e",
            text="名次",
            fill="#000000",
            font=("Microsoft YaHei", 18 * -1)
        )

        button_1 = Button(
            window,
            borderwidth=0,
            highlightthickness=0,
            command=form,
            relief="flat",
            text="追加",
        )
        button_1.place(
            x=331.0,
            y=241.0,
            width=100.0,
            height=37.0
        )

        entry_1 = Entry(
            window,
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0
        )
        entry_1.place(
            x=81.0,
            y=84.0,
            width=145.0,
            height=38.0
        )

        entry_2 = Entry(
            window,
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0
        )
        entry_2.place(
            x=345.0,
            y=84.0,
            width=145.0,
            height=38.0
        )

        entry_3 = IntVar(window)
        entry_31 = Radiobutton(window,text="男",value=1,variable=entry_3)
        entry_31.place(
            x=588.0,
            y=84.0,
            width=72.5,
            height=38.0
        )
        entry_32 = Radiobutton(window,text="女",value=0,variable=entry_3)
        entry_32.place(
            x=660.5,
            y=84.0,
            width=72.5,
            height=38.0
        )

        entry_4=StringVar(window)
        entry_40 = tk.OptionMenu(
            window,entry_4,
            *array_falcuties(2)
        )
        entry_40.place(
            x=81.0,
            y=155.0,
            width=145.0,
            height=38.0
        )
        
        entry_5=StringVar(window)
        entry_50 = tk.OptionMenu(
            window,entry_5,
            *array_sports(1)
        )
        entry_50.place(
            x=344.0,
            y=155.0,
            width=145.0,
            height=38.0
        )

        entry_6 = Entry(
            window,
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0
        )
        entry_6.place(
            x=588.0,
            y=155.0,
            width=145.0,
            height=38.0
        )
        window.resizable(False, False)
        window.mainloop()
        
    add3_gui()
    
    print("运动会项目输入完毕！\n----------")
    
def fileop1():
    btn_sty=('Microsoft Yahei', '18')
    
    window = Tk()
    window.geometry("303x362")
    window.configure(bg = "#FFFFFF")
    window.title("信息增添")
    window.protocol("WM_DELETE_WINDOW", lambda: on_destroy(window) )#关闭窗口，显示主菜单
    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 362,
        width = 303,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_text(
        151.5,
        26.0,
        anchor="center",
        text="1.信息增添",
        fill="#000000",
        font=("Microsoft YaHei", 20 * -1)
    )

    canvas.create_text(
        151.5,
        56.0,
        anchor="center",
        text="第1题：信息录入",
        fill="#000000",
        font=("Microsoft YaHei", 15 * -1)
    )

    button_1 = Button(
        window,
        borderwidth=0,
        highlightthickness=0,
        command=add1,
        relief="flat",
        bg=mdcolor[1],
        text="运动会项目",
        font=btn_sty,
        fg="#fff"
    )
    button_1.place(
        x=81.0,
        y=87.0,
        width=140.0,
        height=56.0
    )

    button_2 = Button(
        window,
        borderwidth=0,
        highlightthickness=0,
        command=add2,
        relief="flat",
        bg=mdcolor[1],
        text="学校院系",
        font=btn_sty,
        fg="#fff"
    )
    button_2.place(
        x=81.0,
        y=178.0,
        width=140.0,
        height=56.0
    )

    button_3 = Button(
        window,
        borderwidth=0,
        highlightthickness=0,
        command=add3,
        relief="flat",
        bg=mdcolor[1],
        text="学生成绩",
        font=btn_sty,
        fg="#fff"
    )
    button_3.place(
        x=81.0,
        y=269.0,
        width=140.0,
        height=56.0
    )
    window.resizable(False, False)
    #window.mainloop()

def new_table(columns,values,title="表格",win=False):
    if not win: #如无win，新建窗口
        win = Tk()
        win.title(title)    # #窗口标题
    #win.geometry("600x500+200+20")   # #窗口位置500后面是字母x
    scrollBar = Scrollbar(win)
    scrollBar.pack(side="right", fill="y")
    tree = ttk.Treeview(
        win,
        show='headings',
        style="table_style.Treeview",
        yscrollcommand=scrollBar.set
    )      # #创建表格对象
    tree["columns"] = columns
    for i in tree["columns"]:
        tree.column(i, anchor="center",width=100)          # #设置列
        tree.heading(i, text=i,anchor="center")        # #设置显示的表头名
    tree.pack()
    
    for i in range(len(values)):
        tree.insert("", 'end', values=values[i])#表格追加数据
    
    
def readf1(print_to_console=False):#从文件1读入数据到sports变量
    global sports
    sports=[]
    f1=open("1.csv","r",encoding='gbk')
    
    if print_to_console:#初始化表格，创建表头
        values=[] 
    s=f1.readline().strip()
    while s!="":
        a=s.split(",")
        sports.append({"sportid":a[0],"name":a[1],"group":a[2]})
        if print_to_console:
            values.append(a)
        s=f1.readline().strip()
    if print_to_console:
        new_table(("编号","名称","组别"),values,"2.1 项目基本信息")
    f1.close()
    
    
def readf2(print_to_console=False):#从文件2读入数据到falcuties变量
    global faculties
    faculties=[]
    if print_to_console:#初始化表格，创建表头
        values=[]
    
    f2=open("2.csv","r",encoding='gbk')
    s=f2.readline().strip()
    while s!="":
        a=s.split(",")
        faculties.append({"fid":a[0],"fname":a[1]})
        if print_to_console:
            values.append(a)
        s=f2.readline().strip()
    f2.close()
    
    if print_to_console:
        new_table(("院系编号","院系名称"),values,"2.2 院系信息")

def readf3(print_to_console=False):#从文件3读入数据到stus变量
    global stus
    stus=[]
    if print_to_console:#初始化表格，创建表头
        values=[]
    
    f3=open("3.csv","r",encoding='gbk')
            
    s=f3.readline().strip()
    while s!="" and s!="\n":
        a=s.split(",")
        stus.append({"stu_id":a[0],"stu_name":a[1],"stu_sex":a[2],"stu_faculty":a[3],"stu_sportid":a[4],"stu_rk":a[5]})
        if print_to_console:
            values.append(a)
        s=f3.readline().strip()
    if print_to_console:
        new_table(("学号","姓名","性别","所属院系","项目编号","排名"),values,"2.3 学生参赛信息")
    f3.close()
    
def fileop2():
    readf1(True)
    readf2(True)
    readf3(True)
    
def fileop3():
    global sports, faculties, stus
    readf3()#写入数据文件
    
    a=input("输入要修改的【学生学号】【项目编号】【名次】：").split()
    found=False
    for i in range(len(stus)):
        if stus[i]["stu_id"]==a[0] and stus[i]["stu_sportid"]==a[1]:
            stus[i]["stu_rk"]=a[2]
            found=stus[i]["stu_name"]
    if found:notice(found+"的名次"+"修改成功！","info","T3",1.9)
    else: notice("查无此项","warn","T3")
    
    #重写file3
    f3=open("3.csv","r+",encoding='gbk')
    for i in range(len(stus)):
        f3.writelines(stus[i]["stu_id"]+","+stus[i]["stu_name"]+","+stus[i]["stu_sex"]+","+stus[i]["stu_faculty"]+","+stus[i]["stu_sportid"]+","+stus[i]["stu_rk"]+"\n")
    f3.close()
    
def find_sport_id(name,group):#根据项目名称和组别找项目编号
    global sports
    readf1()
    for i in range(len(sports)):
        if sports[i]["name"]==name and sports[i]["group"]==group:
            return sports[i]["sportid"]
    return False

def get_item_all_stu(sportid):#查询参与该项目的学生姓名及成绩信息
    out=""
    for i in range(len(stus)):
        if stus[i]["stu_sportid"]==sportid:
            out+=stus[i]["stu_name"]+"\t"+str(rk2score(stus[i]["stu_rk"]))+"\n"
    print(out)

def fileop4():
    readf1()
    readf3()
    a=input("输入【项目名称】【组别】：").split()
    sport_id=find_sport_id(a[0],a[1])
    if sport_id:
        get_item_all_stu(sport_id)
    else:
        notice("未找到该项目","err")

def find_stu_item(name):
    global stus
    stu_all_score=0
    out=""
    for i in range(len(stus)):
        if stus[i]["stu_name"]==name:
            stu_score=rk2score(stus[i]["stu_rk"])
            stu_all_score+=rk2score(stus[i]["stu_rk"])
            out+=stus[i]["stu_sportid"]+"\t"+str(stu_score)+"\n"
    out+="总成绩"+"\t"+str(stu_all_score)
    print(out)

def fileop5():
    readf3()
    s=input("输入学生姓名：")
    find_stu_item(s)



def get_falcuty_fid(s):#根据院系名找院系fid
    readf2()
    
    for i in range(len(faculties)):
        if faculties[i]["fname"]==s:
            return faculties[i]["fid"]
    return False


    

def fileop6():
    readf3()
    out=""
    s=input("输入学院名称：")
    score_tree=dict()
    fid=get_falcuty_fid(s)
    for i in range(len(stus)):
        if stus[i]["stu_faculty"]==fid:#该条是这个学院的
            stuname=stus[i]["stu_name"]
            if stuname in score_tree.keys():
                score_tree[stuname]+=rk2score(stus[i]["stu_rk"])
            else: score_tree[stuname]=rk2score(stus[i]["stu_rk"])
    print(score_tree)
    

def get_falcuty_fname(s):#根据院系fid找院系fname
    readf2()
    
    for i in range(len(faculties)):
        if faculties[i]["fid"]==s:
            return faculties[i]["fname"]
    return False

def get_sportid(a):
    readf1()
    global sports
    a=eval(a)
    print(a,type(a))
    print(a[0])
    for i in range(len(sports)):
        if sports[i]["name"]==a[0] and sports[i]["group"]==a[1]:
            print(sports[i]["sportid"])
            return sports[i]["sportid"]
    return False

def fileop7(print_to_console=True):

    def update_dic(sex,fid,score):#在对应列表的键值对增加分数
        if fid in sex.keys():
            sex[fid]+=score
        else:
            sex[fid]=score

    readf3()
    male,fe,whole={},{},{}
    for i in range(len(stus)):
        fid=stus[i]["stu_faculty"]
        score=rk2score(stus[i]["stu_rk"])
        if stus[i]["stu_sex"]=="男":
            update_dic(male,fid,score)
        if stus[i]["stu_sex"]=="女":
            update_dic(fe,fid,score)
        update_dic(whole,fid,score)
    
    male_array=sorted(male.items(),key=lambda x:x[1], reverse=True)
    fe_array=sorted(fe.items(),key=lambda x:x[1], reverse=True)
    whole_array=sorted(whole.items(),key=lambda x:x[1], reverse=True)

    if print_to_console:
        out_male,out_fe,out_whole="【男生】\n学院\t成绩\n","【女生】\n学院\t成绩\n","【总分】\n学院\t成绩\n"
        for i in range(len(male_array)):
            out_male+=get_falcuty_fname(male_array[i][0])+"\t"+str(male_array[i][1])+"\n"
        for i in range(len(fe_array)):
            out_fe+=get_falcuty_fname(fe_array[i][0])+"\t"+str(fe_array[i][1])+"\n"
        for i in range(len(whole_array)):
            out_whole+=get_falcuty_fname(whole_array[i][0])+"\t"+str(whole_array[i][1])+"\n"
        
        print(out_male)
        print(out_fe)
        print(out_whole)
    
    return whole_array

def plt_draw(x,y,title="图表",color="#6D4C41"):
    def on_close(event):
        main_gui_window.deiconify()#显示主窗口
    
    import matplotlib.pyplot as plt
    plt.rcParams['font.sans-serif'] = ['SimHei']
    fig = plt.figure(figsize=(6, 3))
    fig.canvas.mpl_connect('close_event', on_close)
    fig.canvas.manager.set_window_title(title)
    plt.title(title)
    plt.barh(x,y,color=color)
    plt.show()
    
def fileop8():
    print("第三方库加载较慢，请稍后")
    whole_array=fileop7(False)
    x_axis,y_axis=[],[]
    for i in range(len(whole_array)):
        fname=get_falcuty_fname(whole_array[i][0])
        x_axis.append(fname)
        y_axis.append(whole_array[i][1])
    plt_draw(x_axis,y_axis,"学院积分一览表")
    #ntcbox.destroy()


#--------------
#图形界面
def main_gui():

    global main_gui_window,mdcolor
    
    main_gui_window = Tk()
    main_gui_window.title('主菜单 - 0')

    main_gui_window.geometry("895x526")
    main_gui_window.configure(bg = "#FFFFFF")


    canvas = Canvas(
        main_gui_window,
        bg = "#FFFFFF",
        height = 526,
        width = 895,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_text(
        447.5,
        48.0,
        anchor="center",
        text="学生信息管理系统",
        fill="#000000",
        font=("黑体", 50 * -1)
    )

    canvas.create_text(
        447.5,
        104.0,
        anchor="center",
        text="Python课程设计",
        fill="#000000",
        font=("Microsoft YaHei", 25 * -1)
    )

    canvas.create_text(
        890.0,
        520.0,
        anchor="se",
        text="化生环2107\n林卓城",
        fill="#000000",
        font=("Microsoft YaHei", 20 * -1)
    )
    
    canvas.create_text(
        10.0,
        520.0,
        anchor="sw",
        text="部分功能，需在cmd内运行！",
        fill="#000000",
        font=("Microsoft YaHei", 20 * -1)
    )


    btn_sty=('Microsoft Yahei', '18')
    button_1 = Button(
        bg=mdcolor[1],
        fg="#fff",
        text="增加信息",
        font=btn_sty,
        borderwidth=0,
        highlightthickness=0,
        command=lambda :gui_handle(1),
        relief="flat"
    )
    button_1.place(
        x=81.0,
        y=180.0,
        width=166.0,
        height=83.0
    )

    button_2 = Button(
        bg=mdcolor[2],
        fg="#fff",
        text="读取信息",
        font=btn_sty,
        borderwidth=0,
        highlightthickness=0,
        command=lambda :gui_handle(2),
        relief="flat"
    )
    button_2.place(
        x=277.0,
        y=180.0,
        width=166.0,
        height=83.0
    )

    button_3 = Button(
        bg=mdcolor[3],
        fg="#fff",
        text="修改学生名次",
        font=btn_sty,
        borderwidth=0,
        highlightthickness=0,
        command=lambda :gui_handle(3),
        relief="flat"
    )
    button_3.place(
        x=473.0,
        y=180.0,
        width=166.0,
        height=83.0
    )

    button_4 = Button(
        bg=mdcolor[4],
        fg="#fff",
        text="项目信息查询",
        font=btn_sty,
        borderwidth=0,
        highlightthickness=0,
        command=lambda :gui_handle(4),
        relief="flat"
    )
    button_4.place(
        x=669.0,
        y=180.0,
        width=166.0,
        height=83.0
    )

    button_5 = Button(
        bg=mdcolor[5],
        fg="#fff",
        text="学生成绩查询",
        font=btn_sty,
        borderwidth=0,
        highlightthickness=0,
        command=lambda :gui_handle(5),
        relief="flat"
    )
    button_5.place(
        x=81.0,
        y=314.0,
        width=166.0,
        height=83.0
    )

    button_6 = Button(
        bg=mdcolor[6],
        fg="#fff",
        text="学院参赛学生",
        font=btn_sty,
        borderwidth=0,
        highlightthickness=0,
        command=lambda :gui_handle(6),
        relief="flat"
    )
    button_6.place(
        x=277.0,
        y=314.0,
        width=166.0,
        height=83.0
    )

    button_7 = Button(
        bg=mdcolor[7],
        fg="#fff",
        text="学院积分排行",
        font=btn_sty,
        borderwidth=0,
        highlightthickness=0,
        command=lambda :gui_handle(7),
        relief="flat"
    )
    button_7.place(
        x=473.0,
        y=314.0,
        width=166.0,
        height=83.0
    )

    button_8 = Button(
        bg=mdcolor[8],
        fg="#fff",
        text="学院积分图表",
        font=btn_sty,
        borderwidth=0,
        highlightthickness=0,
        command=lambda :gui_handle(8),
        relief="flat"
    )
    button_8.place(
        x=669.0,
        y=314.0,
        width=166.0,
        height=83.0
    )

    main_gui_window.resizable(False, False)
    main_gui_window.mainloop()


def on_destroy(close_window):
    #销毁传入的窗口
    try:
        close_window.destroy()
    except:
        print("This window cannot be destroyed, maybe because it has already been.")
    
    main_gui_window.deiconify()#显示主窗口

def gui_handle(n):
    main_gui_window.withdraw()#隐藏主窗口
    btn_sty=('Microsoft Yahei', '16')
    
    if n==1: 
        fileop1()
    if n==2:
        window = Tk()
        window.geometry("303x362")
        window.configure(bg = "#FFFFFF")
        window.title("信息查询")
        window.protocol( "WM_DELETE_WINDOW", lambda: on_destroy(window) )#关闭窗口，显示主菜单
        canvas = Canvas(
            window,
            bg = "#FFFFFF",
            height = 362,
            width = 303,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_text(
            151.5,
            26.0,
            anchor="center",
            text="2.信息查询",
            fill="#000000",
            font=("Microsoft YaHei", 20 * -1)
        )

        canvas.create_text(
            151.5,
            56.0,
            anchor="center",
            text="从表文件中读出数据并显示",
            fill="#000000",
            font=("Microsoft YaHei", 15 * -1)
        )

        button_1 = Button(
            window,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: readf1(True),
            relief="flat",
            bg=mdcolor[2],
            text="运动会项目",
            font=btn_sty,
            fg="#fff"
        )
        button_1.place(
            x=81.0,
            y=87.0,
            width=140.0,
            height=56.0
        )

        button_2 = Button(
            window,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: readf2(True),
            relief="flat",
            bg=mdcolor[2],
            text="学校院系",
            font=btn_sty,
            fg="#fff"
        )
        button_2.place(
            x=81.0,
            y=178.0,
            width=140.0,
            height=56.0
        )

        button_3 = Button(
            window,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: readf3(True),
            relief="flat",
            bg=mdcolor[2],
            text="学生成绩",
            font=btn_sty,
            fg="#fff"
        )
        button_3.place(
            x=81.0,
            y=269.0,
            width=140.0,
            height=56.0
        )
        window.resizable(False, False)
        #window.mainloop()
    elif n==8:
        fileop8()

#-----------
#入口
sports, faculties, stus=[],[],[]
mdcolor=["fff","#C2185B","#7B1FA2","#5E35B1","#3949AB","#00695C","#388E3C","#827717","#6D4C41"]
main_gui()
#initial()

#fileop1()
