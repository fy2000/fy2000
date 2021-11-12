# -*- coding: utf-8 -*-
import sqlite3


class SqliteOpt:
    def __init__(self, dbname: str):
        self._connect = sqlite3.connect(dbname)
        self._tb_sequence = 'sqlite_sequence'

    def save_table_to_db(self, tbname: str, datatb: dict):
        # 清空表内容
        sql = f'delete from {tbname}'
        self.execute(sql)

        # 清楚自动增长的列的序号
        if self.is_table_exist(self._tb_sequence):
            sql = f"SELECT name FROM {self._tb_sequence} where name='{tbname}'"
            if self.search(sql):
                sql = f"UPDATE {self._tb_sequence} SET seq = 0 where name='{tbname}'"
                self.execute(sql)

        # 获取表字典信息
        tbcolinfo = self.get_table_columns_info(tbname)
        strcol = ','.join([str(i[1]) for i in tbcolinfo])
        valuestr = ('?,' * len(tbcolinfo)).strip(",")
        sql = f'INSERT INTO {tbname}({strcol}) VALUES({valuestr.strip(",")})'
        # 入库处理
        self.executemany(sql, [tuple(datatb[key]) for key in datatb.keys()])

    def search(self, sql: str):
        try:
            cur = self._connect.cursor()
            cur.execute(sql)
            return cur.fetchall()
        except Exception as e:
            print(e.args)
            return ()
        finally:
            cur.close()

    def execute(self, sql: str):
        try:
            cur = self._connect.cursor()
            cur.execute(sql)
            self._connect.commit()
        except Exception as e:
            print(e.args)
        finally:
            cur.close()

    def executemany(self, sql: str, datalist: list):
        try:
            cur = self._connect.cursor()
            cur.executemany(sql, datalist)
            self._connect.commit()
        except Exception as e:
            print(e.args)
        finally:
            cur.close()

    def get_table_columns_info(self, tbname: str):
        sql = f"PRAGMA table_info('{tbname}')"  # 获取表字段信息
        tbcolinfo = self.search(sql)
        return tbcolinfo

    def get_table_create_sql(self, tbname: str):
        sql = f"SELECT sql FROM sqlite_master WHERE type='table' AND name = '{tbname}'"
        result = self.search(sql)
        if result:
            return result[0][0]
        else:
            return ''

    def create_table_by_tbmodel(self, modeltb: str, newtb: str):
        sql = self.get_table_create_sql(modeltb)
        sql = sql.replace(modeltb, newtb)
        if not self.is_table_exist(newtb):
            self.execute(sql)

    def is_table_exist(self, tbname: str):
        sql = f"SELECT * FROM sqlite_master WHERE type='table' AND name = '{tbname}'"
        result = self.search(sql)
        if not result:
            return False
        else:
            return True

    def close(self):
        self._connect.close()
