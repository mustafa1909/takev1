import requests, uuid, secrets
from colored import fg

co1 = fg(1)  # احمر
co2 = fg(28)  # اخضر
co3 = fg(3)  # اصفر
co4 = fg(88)

num = 0
u = uuid.uuid4()
r = requests.session()
cook = secrets.token_hex(8) * 2
p = co2 + '''


  __  __ _    _  _____ _______       ______      
 |  \/  | |  | |/ ____|__   __|/\   |  ____/\    
 | \  / | |  | | (___    | |  /  \  | |__ /  \   
 | |\/| | |  | |\___ \   | | / /\ \ |  __/ /\ \  
 | |  | | |__| |____) |  | |/ ____ \| | / ____ \ 
 |_|  |_|\____/|_____/   |_/_/    \_\_|/_/    \_\

'''

print(p)
print(co4 + '''>>>>>>>>>>>>>> Codded By inst:z9_wz <<<<<<<<<<<<<<''')
us = input('us:')
ps = input('pss:')
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60',
    'x-csrftoken': 'missing', 'mid': cook

}
keyword = open("keywords.txt", "r").read().splitlines()
user_list = open("usernames.txt", "w")


def login():
    url = 'https://www.instagram.com/accounts/login/ajax/'
    dat = {

        'username': us,
        'enc_password': '#PWD_INSTAGRAM_BROWSER:0:&:' + ps
    }
    req = r.post(url=url, headers=headers, data=dat)
    if '"userId"' in req.text:
        print(f'log >> {us}')
    else:
        print('error')
    m = r.headers.update({'x-csrftoken': req.cookies [ 'csrftoken' ]})

    # print(m)


def l():
    login()
    global num
    try:

        for word in keyword:

            url = 'https://www.instagram.com/web/search/topsearch/?context=blended&query='
            req = requests.get(url + word + "&count=1800", headers=headers).json()
            for index in req['users']:
                username = index['user']['username']
                num += 1
                print(username)
                user_list.write(f"{username}\n")

        user_list.close()
        input(f'[!] Total Usernames :{num}')

    except Exception: \
            print('[-] Error ==> ')


l()
