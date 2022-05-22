#※输入0以退出/返回
#※创建用于测试的对象（临时）

#定义由名次得到积分的函数
def RankToScore(a):
    if a==1:score=10
    if a==2:score=8
    if a==3:score=6
    if a==4:score=5
    if a==5:score=4
    if a==6:score=3
    if a==7:score=2
    if a==8:score=1
    return score

#添加信息
def addpro():#添加运动会项目信息
    form1=open('运动会项目基本信息.txt','a')
    _=input('请输入项目编号,项目名称,项目组别;输入0以结束')
    while _!='0':
        form1.writelines(['\n',_.replace('，',',')])#防止用户输入时使用中文逗号
        #添加至字典
        lst1=(_.replace('，',',')).split(',',1)
        project[lst1[0]]=lst1[1]
        _=input('请输入项目编号,项目名称,项目组别;输入0以结束')
    form1.close()
    #add()#询问是否向其他表格添加信息

def addacd():#添加学院信息
    form2=open('学校院系.txt','a')
    _=input('请输入院系编号,院系名称;输入0以结束')
    while _!='0':
        form2.writelines(['\n',_.replace('，',',')])#防止用户输入时使用中文逗号
        #添加至字典
        lst2=(_.replace('，',',')).split(',',1)
        academy[lst2[0]]=lst2[1]
        _=input('请输入院系编号,院系名称;输入0以结束')
    form2.close()
    add()#询问是否向其他表格添加信息

def addstu():#添加学生信息
    form3=open('学生参与项目及成绩.txt','a')
    _=input('请输入学号,姓名,性别,院系编号,项目编号,名次;输入0以结束')
    while _!='0':
        _.replace('，',',')#防止用户输入时使用中文逗号
        lst3=_.split(',')#将输入内容拆分为对象属性列表
        lst3.append(str(RankToScore(int(lst3[5]))))#利用自定义函数得到积分并写入对象属性列表
        count.append(item(lst3[0],lst3[1],lst3[2],lst3[3],lst3[4],lst3[5],lst3[6]))#创建对象
        form3.writelines(['\n'])
        for i in range((len(lst3))-1):
            form3.writelines(lst3[i])
            form3.writelines([','])
        form3.writelines([lst3[len(lst3)-1]])
        _=input('请输入学号,姓名,性别,院系编号,项目编号,名次;输入0以结束')
    form3.close()
    #add()#询问是否向其他表格添加信息

def add():#添加信息索引
    flagadd=eval(input('输入1以添加运动会项目信息,输入2以添加院系信息,输入3以添加学生信息;输入0结束'))
    while flagadd!=0:
        if flagadd==1:addpro()
        if flagadd==3:addstu()
        flagadd=eval(input('输入1以添加运动会项目信息,输入2以添加院系信息,输入3以添加学生信息;输入0结束'))


#查询所有信息
def surfingall():
    for _ in ['运动会项目基本信息.txt','学校院系.txt','学生参与项目及成绩.txt']:
        print(_[:(len(_)-4)])#打印文件名
        fo=open(_,'r+')
        lst=fo.readlines()#按行拆分文件
        for i in range(len(lst)):
            sublst=lst[i].split(',')#按元素拆分行
            for k in range(len(sublst)):
                print(sublst[k],end='\t')
            print()
        print()
        fo.close()
    main()


#修改信息
def modify():
    nameflag=input('请输入要修改名次的学生姓名')
    projectflag=input('请输入要修改名次的项目编号')#避免一学生参加多项目时，只按名字索引导致的混乱
    fo=open('学生参与项目及成绩.txt','r+')#循环外打开文件准备循环内修改
    lst=fo.readlines()
    for _ in count:
        if _.name==nameflag and _.project==projectflag:#修改对象的名次属性
            rank0=int(_.rank)
            print('{}当前在项目{}中的名次是{}'.format(_.name,project[_.project],_.rank))
            _.rank=eval(input('请输入{}在项目{}的正确名次'.format(_.name,project[_.project])))
            if rank0>int(_.rank):#名次降低时处理其他选手名次
                for i in count:
                    if i.project==projectflag and i.name!=nameflag and int(_.rank)>=int(i.rank)>rank0:
                        i.rank=int(i.rank)-1
            if rank0<int(_.rank):#名次升高时处理其他选手名次
                for i in count:
                    if i.project==projectflag and i.name!=nameflag and int(_.rank)<=int(i.rank)<rank0:
                        i.rank=int(i.rank)+1
        for i in range(len(lst)):#修改lst内容
            if lst[i][4]==projectflag:
                lst[i][4]=_.rank
    
    fo.close()
    fo=open('学生参与项目及成绩.txt','w+')#清空文件，此时文件内容暂存于lst中
    for i in range(len(lst)):#将lst内容写入文件
        fo.writelines(lst[i])
        fo.writelines(['\n'])
    fo.close()
    main()
                
            
#查询信息
def proget():#按项目查询
    projectflag=input('请输入项目编号')
    for _ in count:
        if _.project==projectflag:
            print('{}在{}中的排名是{}，积分为{}'.format(_.name,project[_.project],int(_.rank),int(_.score)))
    get()#询问是否继续查询

def stuget():#按学生查询
    nameflag=input('请输入学生姓名')
    for _ in count:
        if _.name==nameflag:
            print('{}在{}中的排名是{}，积分为{}'.format(_.name,project[_.project],int(_.rank),int(_.score)))
    get()#询问是否继续查询
    
def acdget():#按学院查询
    academyflag=input('请输入学院名')
    for _ in count:
        if _.academy==academyflag:
            print('{}在{}中的排名是{}，积分为{}'.format(_.name,project[_.project],int(_.rank),int(_.score)))
    get()#询问是否继续查询

def get():#查询方式索引
    flag=eval(input('输入1以按项目查询，输入2以按学生查询，输入3以按学院查询；输入0以结束'))
    if flag==1:proget()
    if flag==2:stuget()
    if flag==3:acdget()
    else:main()


#查看学院排名
def getrankA(subcount):#学院分数计算与输出
    rankA={}
    for _ in academy.keys():
        S=0
        for i in subcount:
            if i.academy==_:
                S+=int(i.score)
        rankA[academy[_]]=S
    for mark in sorted(rankA.values()):
        r=0
        for i in rankA.keys():
            r+=1
            if int(mark)==int(rankA[i]):
                print('{}的积分为{}，排名为{}'.format(rankA[i],int(mark),r))
    getrank()#询问是否继续查看排名
       
def getrankG():#分性别查看
    gender=set()#生成性别集合
    print(gender)
    genderflag=input('请输入需要查看排名的性别；或输入all以列出所有性别的排名')
    if genderflag==all:
        subcount=count
    else:
        subcount=set()
        for i in count:
            if i.gender==genderflag:
                subcount.add(i)
        print(genderflag,':',sep='',end='\n')
    getrankA(subcount)
    getrank()#询问是否继续查看排名

def getrank():#索引是否按性别查看
    flag=eval(input('输入1以查看学院总分排名,输入2以分性别查看学院排名；输入0以结束'))
    if flag==1:getrankA(count)
    if flag==2:getrankG()
    else:main()

#主程序
def main():
    flag=eval(input('输入1添加信息，输入2以查看所有信息，输入3以修改学生名次，输入4以查询信息，输入5以查看学院排名;输入0以退出'))
    while flag!=0:
        if flag==1:add()
        if flag==2:surfingall()
        if flag==3:modify()
        if flag==4:get()
        if flag==5:getrank()
        flag=eval(input('输入1添加信息，输入2以查看所有信息，输入3以修改学生名次，输入4以查询信息，输入5以查看学院排名;输入0以退出'))
    
    

#初始化
project={}#创建运动会项目字典
academy={}#创建学院字典
count=[]#创建参赛人次类及列表,每人每项目为一个对象
class item:

    def __init__(self,number,name,gender,academe,project,rank=0,score=0):
        self.number=number
        self.name=name
        self.gender=gender
        self.academy=academy
        self.project=project
        self.rank=rank
        self.score=score
#创建三个表格
form1=open('运动会项目基本信息.txt','a+')
form1.writelines(['项目编号,项目名称,项目组别'])
form1.close()

form2=open('学校院系.txt','a+')
form2.writelines(['院系编号,院系名称'])
form2.close()

form3=open('学生参与项目及成绩.txt','a+')
form3.writelines(['学号,姓名,性别,院系编号,项目编号,名次,积分'])
form3.close()

main()
print('感谢使用')
