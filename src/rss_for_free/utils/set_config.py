import json
import os
from rss_for_free.settings import *

# 生成配置json文件
def config_init():
    with open(CONFIG_PATH,'w') as f:
        json.dump(CONFIG_INIT,f,indent = 4)

# 生成历史记录文件
def history_init():
    with open(HISTORY_PATH,'w') as f:
        pass

# 生成配置目录
def config_dir_init():
    os.mkdir(CONFIG_DIR)

# 配置初始化
def init():
    if not os.path.exists(CONFIG_DIR):
        config_dir_init()
    if not os.path.exists(CONFIG_PATH):
        config_init()
    else:
        choose = input("是否初始化配置文件{}？y/n\n".format(CONFIG_PATH))
        if choose == "y":
            config_init()
    if not os.path.exists(HISTORY_PATH):
        history_init()
    else:
        choose = input("是否初始化下载记录{}？y/n\n".format(HISTORY_PATH))
        if choose == "y":
            history_init()

#参数修改
def config_set(args:tuple):
    if not os.path.exists(CONFIG_PATH):
        init()
    check_res = args_check(args)
    if check_res != 'OK':
        print(check_res)
        print(CONF_HELP)
        return
    with open(CONFIG_PATH,'r') as f:
        config = json.load(f)
    config[args[0]][args[1]] = args[2]
    with open(CONFIG_PATH,'w') as f:
        json.dump(config,f,indent = 4)
    print('修改成功')
    config_show()

#参数检查
def args_check(args: tuple)-> str:
    with open(CONFIG_PATH,'r') as f:
        config = json.load(f)
    if len(args)<3:
        return "参数数目不够"
    if args[0] in config:
        config = config[args[0]]
    else:
        return "{}键值错误".format(args[0])
    if args[1] not in config:
        return "{}键值错误".format(args[1])
    return 'OK'
'''
#帮助信息
def config_help():
    dict_str = 
    print("配置文件结构为：\n")
    print(dict_str)
    print("修改配置：     {}\n".format(CONF_CHANGE_CMD))
    print("显示当前配置： {}\n".format(CONF_SHOW_CMD))
    print("初始化配置：   {}\n".format(CONF_INIT_CMD))
'''
#输出当前配置
def config_show():
    with open(CONFIG_PATH,'r') as f:
        config = json.load(f)
    config_str = json.dumps(config,indent = 4)
    print(config_str)

def config(args:tuple):
    if not args:
        print(CONF_HELP)
        return
    if args[0]=="show":
        config_show()
    elif args[0]== "init":
        init()
    else:
        config_set(args)
        