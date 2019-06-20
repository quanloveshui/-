#!/usr/bin/env python
# -*- coding:utf-8 -*-
from src.utils.db_connection import DbConnection


class UserTypeRepository:
    def __init__(self):
        self.db_conn = DbConnection()


    def add(self, caption):
        """
        在user_type表中添加角色
        :param caption:
        :return:
        """
        cursor = self.db_conn.connect()
        sql = """
          insert into user_type(caption) values(%s)
        """
        cursor.execute(sql, [caption,])
        self.db_conn.close()


    def del_role(self,role):
        """
        在user_type表中删除角色
        :param role:
        :return:
        """
        cursor = self.db_conn.connect()
        sql = "delete from user_type WHERE caption=%s"
        cursor.execute(sql, role)
        self.db_conn.close()

    def get_info(self):
        """
        获取user_type表中所有用户角色类型
        :return:
        """
        cursor = self.db_conn.connect()
        sql='select * from user_type'
        cursor.execute(sql)
        result = cursor.fetchall()
        self.db_conn.close()
        return result
