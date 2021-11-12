# -*- coding:utf-8 -*-

import csv


class CsvOpt:
    def __init__(self, file_name, rw_type='r'):
        self.__filename = file_name
        self.__lines_data = []
        self.__rw_model = rw_type

    def read_csv_lines(self):
        if self.__rw_model.find('r') < 0:
            print('please set file option type! ...')
            return []

        with open(self.__filename, self.__rw_model) as r:
            reader = csv.reader(r)
            for line in reader:
                self.__lines_data.append(line)

        return self.__lines_data

    def write_csv_lines(self, data_lines, head_list=[]):
        if self.__rw_model.find('w') < 0:
            print('please set file option type! ...')
            return False

        with open(self.__filename, self.__rw_model, newline='') as w:
            writer = csv.writer(w)
            if len(head_list) > 0:
                writer.writerow(head_list)

            for line in data_lines:
                writer.writerow(line)

        return True


if __name__ == '__main__':
    mycsv = CsvOpt(r"C:\Users\mt\Desktop\统计汇总\all_file.csv")
    myline = mycsv.read_csv_lines()
    print(type(myline))

    for item in myline:
        print(item)
    print("please call function name ...")
