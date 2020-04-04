import sys
from rss_for_free.settings import _HELP
from rss_for_free.utils.rss_for_free import rss_for_free
from rss_for_free.utils.set_config import config

def main():
    cur_CMD = sys.argv
    if len(cur_CMD)==1:
        print(_HELP)
        return
    if cur_CMD[1]=='conf':
        config(cur_CMD[2:])
    else:
        job = rss_for_free()
        job.run(cur_CMD[1:])
if __name__ == "__main__":
    main()
