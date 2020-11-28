import datetime
import locale

isOK = False #0か3ケタだとisOKがTrueになるようにする。最初はFalseにする。

while isOK == False: #falseの間whileが回り続ける。
    input_trackNum = input('追跡番号を入力してください。\n（無い場合は0を入力）：')
    trackNum = str(input_trackNum)
    trackNumLength = len(trackNum)
    print(trackNumLength)
    #3ケタか0が入ったらisOKをTrueにしてループを抜ける。
    if trackNumLength == 3 or trackNum == str(0):
        isOK = True

else: 
    print("good job! 3ケタか0を入れました")