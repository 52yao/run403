# run403
pua ai写的一个绕过访问路径时403的工具
有些页面的权限校验不严格，直接访问该目录时，会提示权限不足，返回403；但是如果在目录中加一些字符，说不定可以绕过。
比如如直接访问http://test.com/main/home，会返回403；但是访问http://test.com/main/%2e/home, 成功获取页面内容

1、用法：
python  ./run403.py       url        路径
python  ./run403.py http://test.com  home
python  ./run403.py http://test.com/main  home


运行脚本后，同时按下 Ctrl+C 键暂停

1开头的是直接在url上做修改
2开头的是在请求头上做修改
3开头的是post请求
4开头的是其它请求

2、举个例子：
python .\run403.py http://192.168.137.1 phpinfo.php
![image](https://github.com/52yao/run403/assets/67967304/697b23f6-7089-43bf-aeaf-ddacd34f955e)

同时按下 Ctrl+C 键后暂停，暂停状态下，输入c继续，输入q退出
![image](https://github.com/52yao/run403/assets/67967304/5754547c-e629-4df0-87ce-7cc79ee7a44c)

3、日志信息是保存在run403.py文件同目录下的orrer.txt中，
'''
logging.basicConfig(filename='error.txt', level=logging.DEBUG)
'''
默认是debug模式，可根据实际需要修改在代码中进行修改

DEBUG: 详细信息，通常用于开发过程中排查问题。
INFO: 重要信息，描述程序的一般运行状态。
WARNING: 潜在的问题或不太正常的状态，但程序仍可以继续运行。
ERROR: 发生了异常或错误，可能需要干预才能使程序继续运行。
CRITICAL: 严重的问题，通常使程序无法继续运行。

如：设置level=logging.WARNING时，只有WARNING, ERROR, 和 CRITICAL级别的日志会被记录。而DEBUG和INFO级别的日志则不会被记录。
