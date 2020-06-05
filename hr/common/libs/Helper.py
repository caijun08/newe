import os
from application import app
import json, datetime
import os
import psutil
import hashlib
from collections import Counter
from decimal import *
import os

class Helper(object):
    @staticmethod
    def errlog():
        f = open('log.txt','w+')
        f.write('a')
        f.close()

    @staticmethod
    def filespath(filename=''):
        # path = app.root_path
        path = os.getcwd()
        path = os.path.join(path, 'files')
        if not os.path.exists(path) or not os.path.isdir(path):
            os.mkdir(path)
        if filename:
            filename = '%s' % filename
            path = os.path.join(path, filename)
            if not os.path.exists(path) or not os.path.isdir(path):
                os.mkdir(path)
        return path

    @staticmethod
    def get_current_time():
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def cov_int(num):
        try:
            return int(num)
        except:
            return 0

    @staticmethod
    def cov_float(num):
        try:
            num = str(num).replace(',', '')
            return float(num)
        except:
            return 0

    @staticmethod
    def writetxt(txt, name='log.txt'):
        filename = os.path.join(Helper.filespath(), name)
        filename = filename.replace('\\', '/')
        f = open(filename,'a+')
        f.writelines(txt)
        f.close()

    @staticmethod
    def islogintime():
        hour = datetime.datetime.now().hour
        minute = datetime.datetime.now().minute
        countmin = hour*60 + minute
        if countmin >= 4*60 + 10 and countmin <= 7*60 + 15:
            return False
        else:
            return True

    @staticmethod
    def create_id(_id):
        _year = _id[1:3]
        if _year != datetime.datetime.now().strftime('%Y')[2:]:
            _id = 0
        else:
            _id = Helper.cov_int(_id[3:])
        _id = '%04d' % (_id + 1)
        return '%s%s' % (datetime.datetime.now().strftime('%Y')[2:], _id)

    @staticmethod
    def processinfo(processName):
        pids = psutil.pids()
        for pid in pids:
            # print(pid)
            p = psutil.Process(pid)
            if p.name() == processName:
                command = 'taskkill -f -pid %s' % p.pid
                os.popen(command)
                return True  # 如果找到该进程则打印它的PID，返回true
        return False  # 没有找到该进程，返回false

    @staticmethod
    def merge(dict1, dict2):
        return {**dict1, **dict2}

    @staticmethod
    def mergeplus(dict1, dict2):
        return dict(Counter(dict1) + Counter(dict2))

    @staticmethod
    def gene_pwd(salt, pwd):
        m = hashlib.md5()
        string = '%s%s' % (salt, pwd)
        m.update(string.encode('utf-8'))
        return m.hexdigest()

    @staticmethod
    def decimal_cov(num):
        return "%s%s" % (str((num * 100).quantize(Decimal('0.0'))), '%')

class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        else:
            return json.JSONEncoder.default(self, obj)

if __name__ == '__main__':
    pass