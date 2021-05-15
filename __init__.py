from src import connect
from src import data


def menu_2():
    i = 1
    if i == 0:
        exit(0)
    elif i == 1:
        temp = 1
        if temp == 1:
            print("开始爬取日榜数据")
            num = temp
            database = data.get_rank( num)
            a = 2
            if a == 1:
                num = 1
            elif a == 2:
                num = 0
            else:
                print("选项错误！\n")
                menu_2()
            data.get_rank_picture_source(database, num)#proxy
        else:
            print("输入的值超出范围！\n")
            menu_2()
    elif i == 2:
        temp = input("请输入要下载的图片：(图片ID)\n")
        artworks_id = str(temp)
        data.get_picture_source(artworks_id, proxy)


def menu():
    # 登录菜单
    temp = input('请选择登录方式（0～1）\n1.账号登录\n2.cookie登录\n3.游客登录\n0.退出\n')
    i = int(temp)
    if i == 0:
        exit(0)
    elif i == 1:
        connect.account_login()
    elif i == 2:
        connect.cookies_login()
        data.get_rank()
        exit(0)
    elif i == 3:
        print("功能尚未实现")
        exit(0)
    else:
        print("错误输入！")
        exit(1)


if __name__ == '__main__':
    print("正在初始化")
    connect.cookies_login()
    menu_2()
    print("done!")
