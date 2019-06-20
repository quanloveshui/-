#__author:  Administrator
#date:  2016/11/1
from src.repository.user_type import UserTypeRepository



'''
实现向user_type表中添加和删除角色
'''


def add_type():
    caption = input('请输入角色名：')
    # 执行SQL语句
    obj = UserTypeRepository()
    obj.add(caption)
    print('{:>8}角色添加成功'.format(''))


def del_type():
    caption = input('请输入需要删除角色名：')
    # 执行SQL语句
    obj = UserTypeRepository()
    obj.del_role(caption)
    print('{:>8}角色删除成功'.format(''))

