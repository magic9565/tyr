from typing import Counter
import emoji
import requests
import mysql.connector
from stringcolor import *
import telepot
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
import termcolor
import pyfiglet
import re
from pprint import pprint
from datetime import date,datetime
import convert_numbers
from reportlab.pdfgen import canvas
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
myconn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="magic9565"
)

mycursor = myconn.cursor()


today = date.today()
timeNow=datetime.now()
d1 = today.strftime("%Y/%m/%d")
dat=today.strftime("%A")
if dat == 'Friday':
    dat='الجمعة'
elif dat == 'Saturday':
    dat='السبت'
elif dat == 'Sunday':
    dat='الأحد'
elif dat == 'Monday':
    dat='الإثنين'
elif dat == 'Tuesday':
    dat='الثلاثاء'
elif dat == 'Wednesday':
    dat='الأربعاء'
elif dat == 'Thursday':
    dat='الخميس'

emoName = emoji.emojize(':sparkles:')
emoQuizT = emoji.emojize(':check_mark_button:')
emoQuizF = emoji.emojize(':cross_mark:')
emoExam = emoji.emojize(':collision:')
emopin = emoji.emojize(':pushpin:')
emoDoc = emoji.emojize(':blue_book:')
emoDoc1 = emoji.emojize(':closed_book:')
emoDoc2 = emoji.emojize(':green_book:')
emoAD = emoji.emojize(':collision:')
emoWeb = emoji.emojize(':clipboard:')
emoLogo = emoji.emojize(':large_orange_diamond:')


class BotHandler:
    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    #url = "https://api.telegram.org/bot<token>/"

    def get_updates(self, offset=0, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_photo(self, chat_id, text,):
        params = {'chat_id': chat_id, 'photo': text, 'parse_mode': 'HTML'}
        method = 'sendPhoto'
        resps = requests.post(self.api_url + method, params)
        return resps

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def send_document(self, chat_id, text, name):

        params = {'chat_id': chat_id, 'document': text,
                  'caption': name, 'parse_mode': 'HTML'}
        method = 'sendDocument'
        resps = requests.post(self.api_url + method, params)
        return resps

    def get_first_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            enter_update = get_result[0]
        else:
            enter_update = None

        return enter_update

 # وقت تشغيل التيلجرام


def startup(id,name):

    
   
    mycursor.execute("FLUSH TABLE `register_bot_id1`")
    mycursor.execute("select COUNT(DISTINCT(text)) from `register_bot_id1`WHERE text LIKE '4432%'")
    result55 = mycursor.fetchall()
    print(result55[0][0])
    keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=f"{emoAD}   عدد المستلمين جداولهم {result55[0][0]} {emoAD}")]])
    bot.sendMessage(id, f' اهلا {name}', reply_markup=keyboard)









#خاص بالمعلم تسجيل الطلاب بداية التحضير
def reg():
    print(dat)
    mycursor.execute(f"SELECT * FROM s where day='{dat}'")
    search = mycursor.fetchall()
    mycursor.execute(f"SELECT * FROM attendance where date='{d1}'")
    dateA = mycursor.fetchall()
    if search:
        if dateA:
            bot.sendMessage(181918397,'<b> يوجد متدربين لهم حضور في نفس التاريخ</b>')
        else:
            for i in search:
                mycursor.execute(f"insert into `attendance`(id,day,date,class1,class2) values({i[4]},'{dat}','{d1}',0,0)")
                myconn.commit()
            bot.sendMessage(181918397,'<b>تم تسجيل المتدربين لهذا اليوم</b>')
    else:
        bot.sendMessage(181918397,'<b>لايوجد متدربين للتسجيل</b>')
# التحضير والموقع
def loc(lat, lon,id):
    mycursor.execute(f"SELECT * FROM `register_bot_id` WHERE `id-telegram`={id}")
    search = mycursor.fetchall()
    mycursor.execute(f"SELECT `on/off` FROM `on/off` WHERE name='class1'")
    class1 = mycursor.fetchall()
    mycursor.execute(f"SELECT `on/off` FROM `on/off` WHERE name='class2'")
    class2 = mycursor.fetchall()
    
    mycursor.execute("FLUSH TABLE `on/off`")
    if search:
        mycursor.execute(f"SELECT * from s where day='{dat}' and id='{search[0][3]}'")
        ddat = mycursor.fetchall()
        if ddat:
            if class1[0][0]== 1 and class2[0][0]== 0:
                mycursor.execute(f"insert into `location`(id,latitude,longitude) values({search[0][3]},'{lat}','{lon}')")
                myconn.commit()
                mycursor.execute(f"UPDATE `attendance` SET class1=1 WHERE id={search[0][3]}")
                myconn.commit()
                bot.sendMessage(id,'<b>تم تحضيرك المحاضرة الاولى</b>')
                bot.sendMessage(181918397,f'<b> {id}تم تحضيرك المحاضرة الاولى</b>')
            elif class2[0][0]== 1 and class1[0][0]== 0:
                mycursor.execute(f"insert into `location`(id,latitude,longitude) values({search[0][3]},'{lat}','{lon}')")
                myconn.commit()
                mycursor.execute(f"UPDATE `attendance` SET class2=1 WHERE id={search[0][3]}")
                myconn.commit()
                bot.sendMessage(id,'<b>تم تحضيرك المحاضرة الثانية</b>')
                bot.sendMessage(id,f'<b> {id}تم تحضيرك المحاضرة الثانية</b>')
            elif class2[0][0]== 1 and class1[0][0]== 1:
                bot.sendMessage(id,'<b>التحضير مغلق</b>')
                bot.sendMessage(181918397,'<b>المحاضرتين كلها شغاله طفي وحده منها</b>')
            else:
                bot.sendMessage(id,'<b>التحضير مغلق</b>')
                bot.sendMessage(181918397,f'<b> {id} التحضير مغلق</b>')
        else:
            bot.sendMessage(id,'<b>لاتوجد محاضره لديك في الوقت الحالي</b>')
            bot.sendMessage(181918397,'<b>لايوجد محاضره لديك في الوقت الحالي</b>')
    else:
        bot.sendMessage(id,'<b>مااحتاج موقعك ليه ترسله</b>')
        bot.sendMessage(181918397,f' <b>واحد ارسل موقعه وهو مو متدرب عندك رقمه {id}</b>')

# المقررات المتبقية



token = '5621849796:AAGIxtHkThb7Bm-1CrHCELt72XEYEk99GqY'    # test
magnito_bot = BotHandler(token)  # Your bot's name
bot = telepot.Bot(token)


def main():
    new_offset = 0
    print('hi, now launching...')
    

    while True:
        all_updates = magnito_bot.get_updates(new_offset)

        if len(all_updates) > 0:

            for current_update in all_updates:

                first_update_id = current_update['update_id']
                print(current_update)
                if 'channel_post' in current_update:

                    new_offset = first_update_id + 1
                    break
                if 'my_chat_member' in current_update:
                    first_chat_id = current_update['my_chat_member']['chat']['id']
                    status=current_update['my_chat_member']['old_chat_member']['status'];
                    bot.sendMessage(181918397,f'فيه واحد اقفل البوت {status}');
                    new_offset = first_update_id + 1
                    break
                elif 'location' in current_update['message']:
                        first_chat_id = current_update['message']['chat']['id']
                        lat= current_update['message']['location']['latitude']
                        long= current_update['message']['location']['longitude']
                        loc(lat,long,first_chat_id)
                        new_offset = first_update_id + 1
                        break
                elif 'reply_to_message' in current_update['message']:
                    first_chat_id = current_update['message']['chat']['id']
                    # لما يرسل احد الموقع بدون الزر
                    if 'location' in current_update['message']:
                        lat= current_update['message']['location']['latitude']
                        long= current_update['message']['location']['longitude']
                        bot.sendMessage(first_chat_id,'<b>مااحتاج موقعك ليه ترسله</b>') 
                        new_offset = first_update_id + 1
                        break
                   
                    else:
                        new_offset = first_update_id + 1
                        break
                        replay = current_update['message']['reply_to_message']['text']
                        formReplay = re.findall(r'\d+', replay)
                        first_chat_text = current_update['message']['text']
                        if formReplay:
                            bot.sendMessage(formReplay[0], f"<b>{first_chat_text}</b>")
                            bot.sendMessage(181918397, 'تم الارسال')
                        else: # في حالة احد سوى رد بدون رقم
                            bot.sendMessage(181918397,replay)
                        new_offset = first_update_id + 1
                        break

                    
                elif 'text' in current_update['message']:
                    first_chat_text = current_update['message']['text']
                    first_chat_id = current_update['message']['chat']['id']
                    bot.sendMessage(
                        181918397, f'{first_chat_text}  {first_chat_id}')
                    

                elif 'photo' in current_update['message']:
                    first_chat_id = current_update['message']['chat']['id']
                    photoID = current_update['message']['photo'][0]['file_id']
                    bot.sendMessage(
                        first_chat_id, '<b> TVTC </b>'.center(23, emoLogo))
                    magnito_bot.send_photo(
                        first_chat_id, 'http://twq9.com/back.jpg')
                    bot.sendMessage(first_chat_id, '<b> تم استلام الصورة </b>')
                    bot.sendPhoto(181918397, photoID, first_chat_id)
                    new_offset = first_update_id + 1
                    break

                elif 'animation' in current_update['message']:
                    first_chat_id = current_update['message']['chat']['id']
                    bot.sendMessage(
                        first_chat_id, '<b> TVTC </b>'.center(23, emoLogo))
                    magnito_bot.send_photo(
                        first_chat_id, 'https://twq9.com/back.jpg')
                    bot.sendMessage(
                        first_chat_id, '<b>نوع الملفات غير مسموح به</b>')
                    new_offset = first_update_id + 1
                    break

                elif 'document' in current_update['message']:
                    first_chat_id = current_update['message']['chat']['id']
                    documentID = current_update['message']['document']['file_id']
                    bot.sendMessage(
                        first_chat_id, '<b> TVTC </b>'.center(23, emoLogo))
                    bot.sendDocument(181918397, documentID,
                                     caption=first_chat_id)
                    bot.sendMessage(first_chat_id, '<b>تم استلام الملف</b>')
                    new_offset = first_update_id + 1
                    break

                elif 'poll' in current_update['message']:
                    first_chat_id = current_update['message']['chat']['id']
                    bot.sendMessage(
                        first_chat_id, '<b> ممنوع ارسال التصويتات</b>')
                    bot.sendMessage(
                        181918397, f'<b> واحد ارسل تصويت </b> {first_chat_id}')
                    new_offset = first_update_id + 1
                    break

                elif 'audio' in current_update['message']:
                    first_chat_id = current_update['message']['chat']['id']
                    audioID = current_update['message']['audio']['file_id']
                    bot.sendMessage(
                        first_chat_id, '<b> TVTC </b>'.center(23, emoLogo))
                    magnito_bot.send_photo(
                        first_chat_id, 'https://twq9.com/back.jpg')
                    bot.sendMessage(
                        first_chat_id, '<b> تم ارسال مقطعك الصوتي</b>')
                    bot.sendAudio(181918397, audioID)
                    new_offset = first_update_id + 1
                    break

                elif 'contact' in current_update['message']:
                    first_chat_id = current_update['message']['chat']['id']
                    contactID = current_update['message']['contact']['phone_number']
                    contactName = current_update['message']['contact']['first_name']
                    bot.sendMessage(
                        first_chat_id, '<b> TVTC </b>'.center(23, emoLogo))
                    magnito_bot.send_photo(
                        first_chat_id, 'https://twq9.com/back.jpg')
                    bot.sendContact(181918397, contactID, contactName)
                    new_offset = first_update_id + 1
                    break

                if 'first_name' in current_update['message']:
                    first_chat_name = current_update['message']['chat']['first_name']
                elif 'new_chat_member' in current_update['message']:
                    first_chat_name = current_update['message']['new_chat_member']['username']
                elif 'from' in current_update['message']:
                    first_chat_name = current_update['message']['from']['first_name']
                else:
                    first_chat_name = "unknown"
                    
                today = date.today()

                d1 = today.strftime("%Y/%m/%d")
                dat=today.strftime("%A")
                if dat == 'Friday':
                    dat='الجمعة'
                elif dat == 'Saturday':
                    dat='السبت'
                elif dat == 'Sunday':
                    dat='الأحد'
                elif dat == 'Monday':
                    dat='الإثنين'
                elif dat == 'Tuesday':
                    dat='الثلاثاء'
                elif dat == 'Wednesday':
                    dat='الأربعاء'
                elif dat == 'Thursday':
                    dat='الخميس'    

                # يقوم تحديث الجدول
                # mycursor.execute("FLUSH TABLE Q")
                
                #     new_offset = first_update_id + 1
                #     break
                
                
                # جمالية في بداية الاستعلام
                
                mycursor.execute(f"SELECT id FROM block WHERE id={first_chat_id}")
                blook= mycursor.fetchall()
                if blook:
                    new_offset = first_update_id + 1
                    break
                elif first_chat_id ==181918397 or first_chat_id ==1904465616 or first_chat_id ==799862958:
                    startup(first_chat_id,first_chat_name)
                bot.sendMessage(first_chat_id, '<b> TVTC </b>'.center(23, emoLogo))
                magnito_bot.send_photo(first_chat_id, '')
                if first_chat_text.isdigit() == False:
                    
                    if first_chat_text == 'regdel':
                        mycursor.execute(f"DELETE FROM `attendance` WHERE date='{d1}'")
                        myconn.commit()
                        bot.sendMessage(181918397, '<b> تم حذف غيابات المتدربين لهذا اليوم </b>')
                        new_offset = first_update_id + 1
                        break
                    elif first_chat_text == 'regclear1':
                        mycursor.execute(f"UPDATE `attendance` SET class1=0  where date='{d1}'")
                        myconn.commit()
                        bot.sendMessage(181918397, '<b> تم تصفير الغيابات لهذا اليوم للمحاضرة الاولى</b>')
                        new_offset = first_update_id + 1
                        break
                    elif first_chat_text == 'regclear2':
                        mycursor.execute(f"UPDATE `attendance` SET class2=0  where date='{d1}'")
                        myconn.commit()
                        bot.sendMessage(181918397, '<b> تم تصفير الغيابات لهذا اليوم للمحاضرة الثانية</b>')
                        new_offset = first_update_id + 1
                        break

                   
                    elif first_chat_text == 'del admin':
                        mycursor.execute(f"DELETE FROM `register_bot_id` WHERE `id-telegram`={first_chat_id}")
                        myconn.commit()
                        mycursor.execute(f"DELETE FROM `register_bot_id1` WHERE `id-telegram`={first_chat_id}")
                        myconn.commit()
                        bot.sendMessage(first_chat_id, '<b> تم الحذف </b>')
                       
                        new_offset = first_update_id + 1
                        break
       
                
                    elif first_chat_text == 'regclass':
                        reg()
                        new_offset = first_update_id + 1
                        break
                    
                    else:
                        bot.sendMessage(first_chat_id,f'<b>اكتب رقمك التدريبي يا {first_chat_name}</b>')
                        bot.sendMessage(first_chat_id, '<b> TVTC </b>'.center(23, emoLogo))
                        new_offset = first_update_id + 1
                        break
                else:
                    first_chat_text=convert_numbers.hindi_to_english(first_chat_text)
                    new_offset = first_update_id + 1
           

                    

                       
                        
                    print(termcolor.colored("""
                                                    `:oDFo:`
                                                ./ymM0dayMmy/.
                                                -+dHJ5aGFyZGVyIQ==+-
                                            `:sm⏣~~Destroy.No.Data~~s:`
                                        -+h2~~Maintain.No.Persistence~~h+-
                                    `:odNo2~~Above.All.Else.Do.No.Harm~~Ndo:`
                                ./etc/shadow.0days-Data'%20OR%201=1--.No.0MN8'/.
                            -++SecKCoin++e.AMd`       `.-://///+hbove.913.ElsMNh+-
                            -~/.ssh/id_rsa.Des-                  `htN01UserWroteMe!-
                            :dopeAW.No<nano>o                     :is:TЯiKC.sudo-.A:
                            :we're.all.alike'`                     The.PFYroy.No.D7:
                            :PLACEDRINKHERE!:                      yxp_cmdshell.Ab0:
                            :msf>exploit -j.                       :Ns.BOB&ALICEes7:
                            :---srwxrwx:-.`                        `MS146.52.No.Per:
                            :<script>.Ac816/                        sENbove3101.404:
                            :NT_AUTHORITY.Do                        `T:/shSYSTEM-.N:
                            :09.14.2011.raid                       /STFU|wall.No.Pr:
                            :hevnsntSurb025N.                      dNVRGOING2GIVUUP:
                            :#OUTHOUSE-  -s:                       /corykennedyData:
                            :$nmap -oS                              SSo.6178306Ence:
                            :Awsm.da:                            /shMTl#beats3o.No.:
                            :Ring0:                             `dDestRoyREXKC3ta/M:
                            :23d:                               sSETEC.ASTRONOMYist:
                            /-                        /yo-    .ence.N:(){ :|: & };:
                                                        `:Shall.We.Play.A.Game?tron/
                                                        ```-ooy.if1ghtf0r+ehUser5`
                                                    ..th3.H1V3.U2VjRFNN.jMh+.`
                                                    `MjM~~WE.ARE.se~~MMjMs
                                                    +~KANSAS.CITY's~-`
                                                        J~HAKCERS~./.`
                                                        .esc:wq!:`
                                                        +++ATH`
                                                        `             """,color="blue"))
                    
                        


if __name__ == '__main__':

    main()
