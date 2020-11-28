import datetime
import locale
# shopname = ['minne shop', 'BASE shop', 'creema shop']
# gyosya = ['日本郵便', '佐川急便', 'ヤマト運輸', '日本郵便定形外']
# mailtext = '【メール】 info@wires-products.com\n'
# telltext = ['【電話】 08091093387\n',''] 
# input_num = input('サービスを選んでください。\n' +\
#     '0 : ' + shopname[0] + ' / 1 :' + shopname[1] + ' / 2 :' + shopname[2] + '：')
# input_pname = input('宛名を入力してください。：')
# input_haisou = input('配送業者を選んでください。\n' +\
#     '0 : ' + gyosya[0] + ' / 1 :' + gyosya[1] + ' / 2 :' + gyosya[2] + ' / 3 :' + gyosya[3] + '：')
input_track = input('追跡番号を入力してください。\n（無い場合は0を入力）：')
track_numBsub = str(input_track)
track_numB = list(track_numBsub)
track_numC = len(track_numB)
while int(input_track) != 0 and int(track_numC) != 12:
    input_track = input('追跡番号を入力してください。\n（無い場合は0を入力）：')
    track_numBsub = str(input_track)
    track_numB = list(track_numBsub)
    track_numC = len(track_numB)
track_numA = int(input_track)
if track_numA == 0:
    track_numB = 'なし'
else:
    track_numB = track_numB[0] + track_numB[1] + track_numB[2] + track_numB[3] + '-' +  track_numB[4] + track_numB[5] + track_numB[6] + track_numB[7] + '-' + track_numB[8] + track_numB[9] + track_numB[10] + track_numB[11]
input_day = input('何日後の到着予定か入力してください。:' )
input_sub = input('署名に電話番号を記載するか選択してください。\n' +\
    '0 : はい / 1 : いいえ：')
sub_select = int(input_sub)
exportname = int(input_num)
exportgyosya = int(input_haisou)
pname = str(input_pname)
daydate = int(input_day)
youbi = ["月","火","水","木","金","土","日"]
d_today = datetime.date.today()
dt_now = datetime.datetime.now()
td_count = datetime.timedelta(days=daydate)
dt_result = dt_now + td_count
textA = pname + 'さま\n\n\nいつもお世話になっております。\nヘソラボ ' + shopname[exportname] + ' shopの西村です。' +\
    '\n大変お待たせいたしました。\n' +\
    '下記内容で商品の発送が完了いたしました。\n' +\
    str(input_day) + '日後の' + dt_result.strftime('%m月%d日') +  '(' + youbi[dt_result.weekday()] + '曜日）の到着予定となります。\n' +\
    'お受け取りのほどよろしくお願いいたします。\n\n' +\
        '--------------------------------------\n' +\
        '【発送業者】' + gyosya[exportgyosya] + '\n' +\
        '【追跡番号】' + track_numB + '\n' +\
        '【到着予定日】' + dt_result.strftime('%m月%d日') + '(' + youbi[dt_result.weekday()] + '曜日）（配送業者の状況により、前後する可能性がございます。予めご了承ください。）\n' +\
        '--------------------------------------\n\n' +\
    '到着後、ご不明な点や問題がございましたらお申し付け下さいませ。\n' +\
    'この度は当店をご利用いただき誠にありがとうございました。\n' +\
    '今後ともどうぞよろしくお願いいたします。\n\n\n' +\
    'ヘソラボ ' + shopname[exportname] + ' 西村\n\n\n' +\
    '--\nヘソラボ\nwires-products.com\n' +\
    '〒878-0003\n大分県竹田市片ヶ瀬1841\n' +\
        mailtext +\
        telltext[sub_select] +\
    '代表者：西村 和宏\n' 
print(textA)