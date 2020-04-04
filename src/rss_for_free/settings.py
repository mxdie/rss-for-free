import os
import json
# 初始配置
CONFIG_INIT = {
    "common": {
        "sleep": "300"
    },
    "mt": {
        "rsslink": "",
        "sizemax": "1000",
        "sizemin": "-1",
        "cookie" : "",
        "dlurl"  : "",
        "dlpath" : ""
    },
    "nanyang":{
        "rsslink": "",
        "sizemax": "1000",
        "sizemin": "-1",
        "cookie" : "",
        "dlurl"  : "",
        "dlpath" : ""
    }
}

# 用户目录
CONFIG_DIR = os.path.expanduser('~') + "\\rss-for-free\\"
# 用户配置文件
CONFIG_PATH = CONFIG_DIR + "config.json"
# 用户下载历史
HISTORY_PATH = CONFIG_DIR + "history.dat"
# 用户日志目录
LOG_PATH =CONFIG_DIR +"\\log\\"


# 配置命令
CONF_CHANGE_CMD = 'rff conf key1 key2 "value"'
CONF_SHOW_CMD = 'rff conf show'
CONF_INIT_CMD = 'rff conf init'


# 帮助文件
CONF_HELP = '''配置文件结构为：
{}
初始化配置             {}
显示当前配置           {}
修改配置               {}
例如
修改rss间隔为一分钟     rff conf common sleep "600"
修改mt种子大小下限为1G  rff conf mt sizemin "1"
'''.format(json.dumps({"key1":{"key2":"value"}},indent = 4),
            CONF_INIT_CMD,
            CONF_SHOW_CMD,
            CONF_CHANGE_CMD
            )
RUN_HELP = '''开始使用   rff site1 site2 ...
例如
只运行mt的rss         rff mt
同时运行mt和nanyang   rff mt nanyang
'''
_HELP = CONF_HELP + '\n' + RUN_HELP
