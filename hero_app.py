"""
__author__ = 'duomi'
__desc__ = 'python练习作业'

实现需求：
创建英雄：当前游戏中，创建英雄角色，定义好对应英雄的血量及其攻击力。
查看英雄信息：查看当前游戏中所有的英雄信息。
修改英雄信息：修改英雄的血量。
删除英雄：英雄太弱，不需要，删除掉。
退出系统：结束程序

"""


def print_menu():
    print("""
        1. **创建英雄**
        2. **查看英雄信息**
        3. **修改英雄信息**
        4. **删除英雄**
        5. **退出系统**
    """)


def print_all_heroes(hero_list):
    print("当前英雄列表如下：")
    for hero in hero_list:
        print(f"{hero_list.index(hero) + 1}. {hero.get('name')}")


def add_hero(hero_list):
    hero_name = input("请输入英雄的名称：")
    hero_volume = input("请输入英雄的血量：")
    hero_power = input("请输入英雄的攻击力：")
    hero_info = {"name": hero_name, "volume": hero_volume, "power": hero_power}
    print(f"创建成功！英雄名称为{hero_name} ，英雄的血量为{hero_volume} ，英雄的攻击力为{hero_power}")
    hero_list.append(hero_info)


def view_hero(hero_list):
    if hero_list:
        print_all_heroes(hero_list)
        res = int(input("请输入需要查看的英雄编号：")) - 1
        print(f"英雄名称为{hero_list[res]['name']} ，英雄的血量为{hero_list[res]['volume']} ，英雄的攻击力为{hero_list[res]['power']}")
    else:
        print("当前没有任何英雄，请先添加！")


def update_hero(hero_list):
    if hero_list:
        print_all_heroes(hero_list)
        res = int(input("请输入需要修改的英雄编号：")) - 1
        print(
            f"当前英雄名称为{hero_list[res]['name']} ，英雄的血量为{hero_list[res]['volume']} ，英雄的攻击力为{hero_list[res]['power']}")
        hero_name = input("请输入英雄的新名称：")
        hero_volume = input("请输入英雄的新血量：")
        hero_power = input("请输入英雄的新攻击力：")
        hero_info = {"name": hero_name, "volume": hero_volume, "power": hero_power}
        hero_list[res] = hero_info
        print(f"修改成功！修改后的英雄名称为{hero_name} ，英雄的血量为{hero_volume} ，英雄的攻击力为{hero_power}")
    else:
        print("当前没有任何英雄，请先添加！")


def delete_hero(hero_list):
    if hero_list:
        print_all_heroes(hero_list)
        res = int(input("请输入需要删除的英雄编号：")) - 1
        hero_list.pop(res)
        print("删除成功！")
    else:
        print("当前没有任何英雄，请先添加！")


def main():
    hero_list = []
    while True:
        print_menu()
        res = input("请输入对应的选项，即可执行对应的操作：")
        if res == "1":
            add_hero(hero_list)
        elif res == "2":
            view_hero(hero_list)
        elif res == "3":
            update_hero(hero_list)
        elif res == "4":
            delete_hero(hero_list)
        else:
            break


if __name__ == '__main__':
    main()
