# encoding:utf-8
import sys,os
import subprocess

class ServerException(Exception):
    '''服务器内部错误 500'''
    pass

class base_case(object):

    def handle_file(self,handler,full_path):
        try:
            with open(full_path,'rb') as reader:
                content = reader.read()
            handler.send_content(content)
        except IOError as msg:
            msg = "'{0}' connot be read:{1}".format(full_path,msg)
            handler.handle_error(msg)

    def index_path(self,handler):
        return os.path.join(handler.full_path,'index.html')
        

    def test(self,handler):
        assert False,'Not implemented'

    def act(self,handler):
        assert False ,'Not implemented'
   

class case_no_file(base_case):
    # 该路径不存在
    def test(self,handler):
        print('case_no_file test:'+ handler.path)
        return not os.path.exists(handler.full_path)

    def act(self,handler):
        print('case_no_file act:'+ handler.path)
        return ServerException("'{0}' not found".format(handler.path))

class case_cgi_file(object):

    def run_cgi(self,handler):
        data = subprocess.check_output(["Python3",handler.full_path],shell=False)
        handler.send_content(data)
    # 脚本文件处理
    def test(self,handler):
        return os.path.isfile(handler.full_path) and handler.full_path.endswith('.py')
    def act(self,handler):
        # 运行脚本文件
        self.run_cgi(handler)

class case_existing_file(base_case):
    # 该路径是文件
    def test(self,handler):
        # print('case_existing_file test:'+ handler.path)
        return os.path.isfile(handler.full_path)

    def act(self,handler):
        # print('case_existing_file act:'+ handler.path)
        self.handle_file(handler,handler.full_path)



class case_index_file(object):

    def test(self,handler):
        return  os.path.isdir(handler.full_path) and os.path.isfile(self.index_path(handler))

    def act(self,handler):
        # print("首页index 路径sad act:" + self.index_path(handler))
        self.handle_file(handler,self.index_path(handler))



class case_always_fail(object):
    # 所有情况都不符合的时候默认处理类
    def test(self,handler):
        # print('case_always_fail test:'+ handler.path)
        return True

    def act(self,handler):
        # print('case_existing_file act:'+ handler.path)
        return ServerException("Unknow object {0}".format(handler.path))



