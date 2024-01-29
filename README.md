# run403
pua ai写的一个绕过访问路径时403的工具
有些页面的权限校验不严格，直接访问该目录时，会提示权限不足，返回403；但是如果在目录中加一些字符，说不定可以绕过。
比如如直接访问http://test.com/main/home，会返回403；但是访问http://test.com/main/%2e/home, 成功获取页面内容

用法：
python  ./run403.py       url        路径
python  ./run403.py http://test.com  home
python  ./run403.py http://test.com/main  home
运行脚本后，同时按下 Ctrl+C 键暂停


举个例子：
python .\run403.py http://192.168.137.1 phpinfo.php
![image](https://github.com/52yao/run403/assets/67967304/697b23f6-7089-43bf-aeaf-ddacd34f955e)

同时按下 Ctrl+C 键后暂停，暂停状态下，输入c继续，输入q退出
![image](https://github.com/52yao/run403/assets/67967304/21f58580-ed34-4608-8f5b-62152e4d285c)
