#README!!!!!!!!!!!!!!!!!!!!!!!!!!
README="""
       PhoneGetV1.0
      By  Flysmallfish
      软件协议   GPLv3
      请不要将本软件用于
      商业目的！！！！！
 作者的话：PhoneGet使用了别人的API
 若PhoneGet不能用了，请即使联系作者
    18623304101@163.ccom      
                             """



lg=r"""
    //  |————| ——————                     |   |————|      //
   //   |    | |                \      /  |   |    |     //
  //    |————| |   ——|           \    /   |   |    |    //
 //     |      |     |            \  /    |   |    |   //
//      |      |_____|             \/     | . |____|  //             

"""



#=============================================Loading
"              ";print('PhoneGet  Loading 加载中(导库) :\n [%\033[5;31m'+'—'*60+'\033[0m%]    0%\n')
import os
os.system("CLS");print(lg);print('PhoneGet  Loading 加载中(导库) :\n [%\033[5;36m'+'—'*15+'\033[0m\033[5;31m'+'—'*45+'\033[0m%]  25%')
from tkinter import *
os.system("CLS");print(lg);print('PhoneGet  Loading 加载中(导库) :\n [%\033[5;36m'+'—'*30+'\033[0m\033[5;31m'+'—'*30+'\033[0m%]  50%')
import requests
os.system("CLS");print(lg);print('PhoneGet  Loading 加载中(导库) :\n [%\033[5;36m'+'—'*45+'\033[0m\033[5;31m'+'—'*15+'\033[0m%]  75%')
import json  
os.system("CLS");print(lg);print('PhoneGet  Loading 加载中(导库) :\n [%\033[5;36m'+'—'*60+'\033[0m%]  100%\n [ ! ] 导库完毕')
print('\n\033[5;36mPhoneGet 作者Flysmallfish Blog:fishblog.sikomc.xyz\033[0m\n \033[5;31m[ ! ] 注意使用本工具后发生的一切后果本人不负责\n       软件测试中可能有bug!\n\n       由于接口问题，破解时间可能变长。\033[0m')
#=====================================================

global myHeader
myHeader = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
}

def gsm(url):
    global myHeader
    try:
        StrHtml=requests.get(url, headers=myHeader);get = json.loads(StrHtml.text)
    except:
        print("\n\n\033[5;31m[T_T] 您的网络连接/输入格式 出一些问题，请检查。\033[0m\n")
    return get

def getcustomdata():
    print("\n\n \033[5;36m[ ! ] URL请求头大全\n    手机查QQ:https://zy.xywlapi.cc/qqphone?phone=\n    QQ号查询LOL信息:https://zy.xywlapi.cc/qqlol?qq=\n    LOL查询QQ信息:https://zy.xywlapi.cc/lolname?name=\n    通过QQ查询其老密码(有可能是假的):https://zy.xywlapi.cc/qqlm?qq=\n    微博通过ID查手机号:https://zy.xywlapi.cc/wbapi?id=    \n    通过手机号查微博ID:https://zy.xywlapi.cc/wbphone?phone=\033[0m\n\n")
    urlhead=input("\n\n[输入] 输入需要的请求头:\n >> ")
    xx=input("\n\n[输入] 输入后面的信息:\n >> ")

    try:
        print("\n[获取] 正在破解ing")
        StrHtml=requests.get(urlhead+xx, headers=myHeader);
        print(" [ ! ] 自定义查询暂时只能直接输出JSON，请您见谅。")
        print("\n******************************************\n\033[5;32m"+StrHtml.text+"\n\033[0m******************************************\n")
    except:
        print("\n\n\033[5;31m[T_T] 您的网络连接/输入格式 出一些问题，请检查。\033[0m\n")


def getdata():
    global myHeader
    QQ=input("\n\n[输入] 输入要破解的QQ号(若输入C，我们将跳转到自定义获取信息！):\n >> ")

    if QQ=="C" or QQ=="c":
        getcustomdata()


    else:
        Url="https://zy.xywlapi.cc/qqapi?qq="+QQ
        print("\n\n[获取] 正在破解ing")

        phone_data=gsm(Url)

        if phone_data["message"] != "输入参数类型错误" and phone_data["message"] != "没有找到":
            print("\n******************************************\n\033[5;32m"+phone_data["message"]+"！\n"+"QQ号  : "+QQ+"\n手机号: "+phone_data["phone"]+"\n地区  : "+phone_data["phonediqu"]+"\n\033[0m******************************************")
        else:
            print("\n\n\033[5;31m没有找到/输入格式错误！\n    ①该QQ号可能没有绑定密保手机\n    ②或您输错了QQ号\033[0m\n")

    if input("\n再来一次?(直接回车)\n") == "":
        getdata()
    else:
        exit()

getdata()


