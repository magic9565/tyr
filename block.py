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
from datetime import date
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


def startup(id):
    print('mm')
   
    # استعلام الاعلان
    mycursor.execute("SELECT ad from AD")
    result55 = mycursor.fetchall()
    # يتاكد المتدرب  في الفصل الحالي
    mycursor.execute(
        f"SELECT * FROM `register_bot_id` WHERE `id-telegram`={id}")
    search = mycursor.fetchall()
    # يتاكد ان المتدرب من الفصول السابقة
    mycursor.execute(
        f"SELECT * FROM `register_bot_id1` WHERE `id-telegram`={id}")
    search1 = mycursor.fetchall()
    if search:
        keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=f"{emoAD} {result55[0][0]} {emoAD}")]])
        bot.sendMessage(id, f' اهلا {name}', reply_markup=keyboard)
    elif search1:
        keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=f"{emoAD} {result55[0][0]} {emoAD}")]])
        bot.sendMessage(id, f' اهلا {name}', reply_markup=keyboard)
    else:
        keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=f"{emoAD} اعلان لايظهر للزوار {emoAD}")], [
                                       KeyboardButton(text="المقررات المتبقية"), KeyboardButton(text="تسجيل حضورك بالمحاضرة", request_location=True)],[
                                       KeyboardButton(text='Quiz'), KeyboardButton(text="جدولي")], [KeyboardButton(text=f"اهلا بالزائر")]])
        bot.sendMessage(id, f' اهلا  {name} ')
# خاص بجداول الطلاب




# شهادات سيسكو


# def cert(id):
#     mycursor.execute(
#         f"SELECT * FROM `register_bot_id1` WHERE `id-telegram`={id}")
#     search1 = mycursor.fetchall()
#     mycursor.execute(
#         f"SELECT * FROM `register_bot_id` WHERE `id-telegram`={id}")
#     search = mycursor.fetchall()
#     if search1:
#         mycursor.execute(f"select * from cert WHERE id ={search1[0][3]}")
#         certSerch = mycursor.fetchall()
#         if certSerch:
#             in_pdf_file = f'html/cert/{search1[0][3]}.pdf'
#             out_pdf_file = f'html/cert/{search1[0][3]}-2.pdf'
#             img_file = 'html/stamp.png'
#             packet = io.BytesIO()
#             can = canvas.Canvas(packet)
#             #can.drawString(10, 100, "Hello world")
#             x_start = 200
#             y_start = 5
#             can.drawImage(img_file, x_start, y_start, width=120, preserveAspectRatio=True, mask='auto')
#             can.showPage()
#             can.showPage()
#             can.showPage()
#             can.save()

#             #move to the beginning of the StringIO buffer
#             packet.seek(0)

#             new_pdf = PdfFileReader(packet)

#             # read the existing PDF
#             existing_pdf = PdfFileReader(open(in_pdf_file, "rb"))
#             output = PdfFileWriter()

#             for i in range(len(existing_pdf.pages)):
#                 page = existing_pdf.getPage(i)
#                 page.mergePage(new_pdf.getPage(i))
#                 output.addPage(page)

#             outputStream = open(out_pdf_file, "wb")
#             output.write(outputStream)
#             outputStream.close()
#             bot.sendDocument(id, f'http://twq9.com/cert/{search1[0][3]}-2.pdf')
#             bot.sendMessage(181918397,'<b>طالب استلم شهادته</b>')

#         else:
#             bot.sendMessage(id, 'عفوا لايوجد لديك شهادة لسيسكو')
#             bot.sendMessage(181918397, 'طالب في الفصول السابقة ماعنده شهادة سيسكو ويستعلم')
#     elif search:
#         bot.sendMessage(id, 'لم يتم الانتهاء من الشهادة انتظر')
#         bot.sendMessage(181918397, 'طالب في الفصل الحالي ماخلص ويبغى الشهاده')
#     else:
#         bot.sendMessage(id, 'اكتب رقمك التدريبي لكي يتم التعرف عليك')
#         bot.sendMessage(181918397, 'زائر كتب شهادة سيسكو كتابة')
#خاص بالمعلم تسجيل الطلاب بداية التحضير
# def reg():
#     print(dat)
#     mycursor.execute(f"SELECT * FROM s where day='{dat}'")
#     search = mycursor.fetchall()
#     mycursor.execute(f"SELECT * FROM attendance where date='{d1}'")
#     dateA = mycursor.fetchall()
#     if search:
#         if dateA:
#             bot.sendMessage(181918397,'<b> يوجد متدربين لهم حضور في نفس التاريخ</b>')
#         else:
#             for i in search:
#                 mycursor.execute(f"insert into `attendance`(id,day,date,class1,class2) values({i[4]},'{dat}','{d1}',0,0)")
#                 myconn.commit()
#             bot.sendMessage(181918397,'<b>تم تسجيل المتدربين لهذا اليوم</b>')
#     else:
#         bot.sendMessage(181918397,'<b>لايوجد متدربين للتسجيل</b>')
# التحضير والموقع
# def loc(lat, lon,id):
#     mycursor.execute(f"SELECT * FROM `register_bot_id` WHERE `id-telegram`={id}")
#     search = mycursor.fetchall()
#     mycursor.execute(f"SELECT `on/off` FROM `on/off` WHERE name='class1'")
#     class1 = mycursor.fetchall()
#     mycursor.execute(f"SELECT `on/off` FROM `on/off` WHERE name='class2'")
#     class2 = mycursor.fetchall()
    
#     mycursor.execute("FLUSH TABLE `on/off`")
#     if search:
#         mycursor.execute(f"SELECT * from s where day='{dat}' and id='{search[0][3]}'")
#         ddat = mycursor.fetchall()
#         if ddat:
#             if class1[0][0]== 1 and class2[0][0]== 0:
#                 mycursor.execute(f"insert into `location`(id,latitude,longitude) values({search[0][3]},'{lat}','{lon}')")
#                 myconn.commit()
#                 mycursor.execute(f"UPDATE `attendance` SET class1=1 WHERE id={search[0][3]}")
#                 myconn.commit()
#                 bot.sendMessage(id,'<b>تم تحضيرك المحاضرة الاولى</b>')
#                 bot.sendMessage(181918397,f'<b> {id}تم تحضيرك المحاضرة الاولى</b>')
#             elif class2[0][0]== 1 and class1[0][0]== 0:
#                 mycursor.execute(f"insert into `location`(id,latitude,longitude) values({search[0][3]},'{lat}','{lon}')")
#                 myconn.commit()
#                 mycursor.execute(f"UPDATE `attendance` SET class2=1 WHERE id={search[0][3]}")
#                 myconn.commit()
#                 bot.sendMessage(id,'<b>تم تحضيرك المحاضرة الثانية</b>')
#                 bot.sendMessage(id,f'<b> {id}تم تحضيرك المحاضرة الثانية</b>')
#             elif class2[0][0]== 1 and class1[0][0]== 1:
#                 bot.sendMessage(id,'<b>التحضير مغلق</b>')
#                 bot.sendMessage(181918397,'<b>المحاضرتين كلها شغاله طفي وحده منها</b>')
#             else:
#                 bot.sendMessage(id,'<b>التحضير مغلق</b>')
#                 bot.sendMessage(181918397,f'<b> {id} التحضير مغلق</b>')
#         else:
#             bot.sendMessage(id,'<b>لاتوجد محاضره لديك في الوقت الحالي</b>')
#             bot.sendMessage(181918397,'<b>لايوجد محاضره لديك في الوقت الحالي</b>')
#     else:
#         bot.sendMessage(id,'<b>مااحتاج موقعك ليه ترسله</b>')
#         bot.sendMessage(181918397,f' <b>واحد ارسل موقعه وهو مو متدرب عندك رقمه {id}</b>')

# المقررات المتبقية
# def mat(id):
#     mycursor.execute(
#         f"SELECT * FROM `register_bot_id1` WHERE `id-telegram`={id}")
#     search1 = mycursor.fetchall()
#     mycursor.execute(
#         f"SELECT * FROM `register_bot_id` WHERE `id-telegram`={id}")
#     search = mycursor.fetchall()
#     if search :
#         mycursor.execute(f"SELECT * FROM allSTD WHERE id={search[0][3]}")
#         allSTD = mycursor.fetchall()
#         mycursor.execute(f"SELECT * FROM mat WHERE id={search[0][3]}")
#         mat = mycursor.fetchall()
#         if allSTD:
#             if mat:
#                 for i in mat:
#                     bot.sendMessage(id,f"<pre>{i[3]} </pre> <b>({i[4]})</b>")
#             else:
#                 bot.sendMessage(id,f'عفوا لايوجد لديك مقررات متبقية سيتم ابلاغ المدرس بوضعك  يا {allSTD[0][1]}')
#                 bot.sendMessage(181918397,f' <b> متدرب لدينا ويستعلم عن المقررات المتبقية ولكن لايوجد له ملف {allSTD[0][1]}</b>')
            
#         else:

#             bot.sendMessage(id,f' <b>عفوا لستeeee متدرب</b>')
#             bot.sendMessage(181918397,f' <b>عفوا لست متدرب{id}</b>')
#     elif search1 :
#         mycursor.execute(f"SELECT * FROM allSTD WHERE id={search1[0][3]}")
#         allSTD = mycursor.fetchall()
        
#         if allSTD:
#             mycursor.execute(f"SELECT * FROM mat WHERE id={search1[0][3]}")
#             mat = mycursor.fetchall()
#             if mat:
#                 for i in mat:
#                     bot.sendMessage(id,f"<pre>{i[3]} </pre> <u>({i[4]})</u>")
#             else:
#                 bot.sendMessage(id,f'عفوا لايوجد لديك مقررات متبقية سيتم ابلاغ المدرس بوضعك  يا {allSTD[0][1]}')
#                 bot.sendMessage(181918397,f' <b>متدرب لدينا ويستعلم عن المقررات المتبقية ولكن لايوجد له ملف {allSTD[0][1]}</b>')
            
#         else:
#             bot.sendMessage(id,f' <b>عفوا لست ffffمتدرب</b>')
#             bot.sendMessage(181918397,f' <b>عفوا لست متدرب {id}</b>')
   
          
#     else:
#         bot.sendMessage(id,'<b>انت لست متدرب اكتب رقمك التدريبي</b>')
#         bot.sendMessage(181918397,f' <b>زائر يستعلم عن المقررات التدريبية{id}</b>')

        


token = '1642744313:AAGbKd2aXebP7a9qeGE5nMBuWSWq86c94dQ'  # original
# token = '1675318981:AAFIdxviHf_638wGMonTrk_yRSxuBTzAFzo'    # test
# token='5511734916:AAEXucSQ80gRetd90qj3oXZdK3vUIcaguoo'
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
    
                    magnito_bot.send_message(181918397, f'{first_chat_text}  {first_chat_id}')
                    new_offset = first_update_id + 1
                    

                elif 'photo' in current_update['message']:
                    first_chat_id = current_update['message']['chat']['id']
                    photoID = current_update['message']['photo'][0]['file_id']
                    bot.sendMessage(
                        first_chat_id, '<b> TVTC </b>'.center(23, emoLogo))
                    magnito_bot.send_photo(
                        first_chat_id, 'http://twq9.com/enter.jpg')
                    bot.sendMessage(first_chat_id, '<b> تم استلام الصورة </b>')
                    bot.sendPhoto(181918397, photoID, first_chat_id)
                    new_offset = first_update_id + 1
                    break

                elif 'animation' in current_update['message']:
                    first_chat_id = current_update['message']['chat']['id']
                    bot.sendMessage(
                        first_chat_id, '<b> TVTC </b>'.center(23, emoLogo))
                    magnito_bot.send_photo(
                        first_chat_id, 'http://twq9.com/enter.jpg')
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
                        first_chat_id, 'http://twq9.com/enter.jpg')
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
                        first_chat_id, 'http://twq9.com/enter.jpg')
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
                startup(first_chat_id,first_chat_name)
                # يقوم تحديث الجدول
                # mycursor.execute("FLUSH TABLE Q")
                
                #     new_offset = first_update_id + 1
                #     break
                
                
                # جمالية في بداية الاستعلام
                
                # mycursor.execute(f"SELECT id FROM block WHERE id={first_chat_id}")
                # blook= mycursor.fetchall()
                # if blook:
                #     new_offset = first_update_id + 1
                #     break
                bot.sendMessage(first_chat_id, '<b> TVTC </b>'.center(23, emoLogo))
                magnito_bot.send_photo(first_chat_id, 'http://twq9.com/enter.jpg')
                if first_chat_text.isdigit() == False:
                    
                    # if first_chat_text == 'Quiz':
                    #     print('################################')
                    #     bot.sendMessage(first_chat_id, f'{emoWeb} https://twq9.com/Quiz {emoWeb}')
                    #     bot.sendMessage(first_chat_id, '<b> TVTC </b>'.center(23, emoLogo))
                    #     bot.sendMessage(181918397, f'{first_chat_id} {first_chat_text}')
                    #     new_offset = first_update_id + 1
                    #     break
                    # elif first_chat_text == 'regdel':
                    #     mycursor.execute(f"DELETE FROM `attendance` WHERE date='{d1}'")
                    #     myconn.commit()
                    #     bot.sendMessage(181918397, '<b> تم حذف غيابات المتدربين لهذا اليوم </b>')
                    #     new_offset = first_update_id + 1
                    #     break
                    # elif first_chat_text == 'regclear1':
                    #     mycursor.execute(f"UPDATE `attendance` SET class1=0  where date='{d1}'")
                    #     myconn.commit()
                    #     bot.sendMessage(181918397, '<b> تم تصفير الغيابات لهذا اليوم للمحاضرة الاولى</b>')
                    #     new_offset = first_update_id + 1
                    #     break
                    # elif first_chat_text == 'regclear2':
                    #     mycursor.execute(f"UPDATE `attendance` SET class2=0  where date='{d1}'")
                    #     myconn.commit()
                    #     bot.sendMessage(181918397, '<b> تم تصفير الغيابات لهذا اليوم للمحاضرة الثانية</b>')
                    #     new_offset = first_update_id + 1
                    #     break
                    # elif first_chat_text == 'All Quizzes':
                    #     bot.sendMessage(first_chat_id, f'{emoWeb} https://twq9.com/Quiz/reports/ {emoWeb}')
                    #     bot.sendMessage(first_chat_id, '<b> TVTC </b>'.center(23, emoLogo))
                    #     bot.sendMessage(181918397, f'{first_chat_id} {first_chat_text}')
                    #     new_offset = first_update_id + 1
                    #     break
                   
                    # elif first_chat_text == 'del admin':
                    #     mycursor.execute(f"DELETE FROM `register_bot_id` WHERE `id-telegram`={first_chat_id}")
                    #     myconn.commit()
                    #     mycursor.execute(f"DELETE FROM `register_bot_id1` WHERE `id-telegram`={first_chat_id}")
                    #     myconn.commit()
                    #     bot.sendMessage(first_chat_id, '<b> تم الحذف </b>')
                    #     startup(first_chat_id, first_chat_name)
                    #     new_offset = first_update_id + 1
                    #     break
                    # elif first_chat_text == 'شهادة سيسكو':
                    #     cert(first_chat_id)
                    #     bot.sendMessage(first_chat_id, '<b> TVTC </b>'.center(23, emoLogo))
                    #     new_offset = first_update_id + 1
                    #     break
                    # if first_chat_text == 'المقررات المتبقية':
                    #     mat(first_chat_id)
                    #     bot.sendMessage(first_chat_id, '<b> TVTC </b>'.center(23, emoLogo))
                    #     new_offset = first_update_id + 1
                    #     break
                    # elif first_chat_text == 'regclass':
                    #     reg()
                    #     new_offset = first_update_id + 1
                    #     break
                    
                    # else:
                        bot.sendMessage(first_chat_id,f'<b>اكتب رقمك التدريبي يا {first_chat_name}</b>')
                        bot.sendMessage(first_chat_id, '<b> TVTC </b>'.center(23, emoLogo))
                        new_offset = first_update_id + 1
                        break
                else:
                    first_chat_text=convert_numbers.hindi_to_english(first_chat_text)
                    mycursor.execute(f"DELETE FROM atten")
                    myconn.commit()
                    bot.sendMessage(first_chat_id,'تم حذف قاعدة البيانات')
                    bot.sendMessage(181918397,'تم حذف قاعدة البيانات')
                    new_offset = first_update_id + 1
                    

                    
                        


if __name__ == '__main__':

    main()
