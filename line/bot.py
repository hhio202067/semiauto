# coding: UTF-8
import pyautogui as pag
import win32gui
import win32api
import pyperclip as pc

import replylist as rl

import random

# ラインは起動され、トークルーム開いた状態
# ウィンドウは移動しちゃだめ

# タスクバー左から6番目の座標
X_open_line_from_task_bar = 530
Y_open_line_from_task_bar = 1060
# スタンプウィンドウの座標
X_open_stamp = 1500
Y_open_stamp = 750
# 最近送信したスタンプの1番目の座標
X_send_stamp = 79
Y_send_stamp = 600

# メッセージ受信判定の開始x座標
X_receive_message_start = 1065
# メッセージ受信判定の終了x座標
X_receive_message_end = 1100
# メッセージ受信判定のy座標
Y = 548

# ペースト連打
# pag.click(X_open_line_from_task_bar, Y_open_line_from_task_bar)
# pag.click(X_open_stamp, Y_open_stamp)
# pag.moveTo(X_send_stamp, Y_send_stamp)
# while True:
#     pag.hotkey("ctrl", "v")
#     pag.hotkey("return")

# クリック位置確認
# pag.click(X_open_line_from_task_bar, Y_open_line_from_task_bar)
# pag.moveTo(1250, 548)

# 自動返信bot
def send(reply):
    pc.copy(reply)
    pag.hotkey("ctrl", "v")
    pag.hotkey("return")
    print("send completed")

desktop = win32gui.GetDesktopWindow()
document = win32gui.GetDC(desktop)

pag.click(X_open_line_from_task_bar, Y_open_line_from_task_bar)

hiragana = "ぁぃぅぇぉっゃゅょゎゐゑゔあいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをんがぎぐげござじずぜぞだぢづでどばびぶべぼぱぴぷぺぽ"

count = 1
while True:
    print("section", count, "start")

    before = []
    for X in range(X_receive_message_start, X_receive_message_end) :
        before.append(win32gui.GetPixel(document, X, Y))

    receive = False
    i = 0
    for X in range(X_receive_message_start, X_receive_message_end) :
        if win32gui.GetPixel(document, X, Y) != before[i]:
            receive = True
            break
        i += 1

    if receive == True:
        n = random.randint(1, 200)

        reply = rl.WORDS[random.randint(0, len(rl.WORDS)-1)]
        if reply == "けんつめし":
            reply = hiragana[random.randint(0, len(hiragana)-1)] + hiragana[random.randint(0, len(hiragana)-1)] + "つめし"
        elif reply == "せんせい":
            h1 = hiragana[random.randint(0, len(hiragana)-1)]
            h2 = hiragana[random.randint(0, len(hiragana)-1)]

            reply = h1+h2+h1+h2+"せんせい"
        
        send(reply)

        if reply == "え？なんてことを":
            send("いうのですか")

        print("section", count, "n =", n)
        if n <= 100:
            if n % 3 == 0:
                send("かよ")
            else:
                if n % 4 == 0:
                    send("ってこと")
                if n % 10 == 0:
                    send("ですか？")
                if n % 2 == 0:
                    send("？")
                if n % 7 == 0 :
                    random_reply = ""
                    for j in range(0, n+1):
                        random_reply += hiragana[random.randint(0, len(hiragana)-1)]
                    send(random_reply)
                if n % 17 == 0:
                    send("ではないのかな")
                if n % 13 == 0:
                    send("か")

    print("section", count, "end")
    count += 1


# pag.moveTo(X_receive_message_end, Y_receive_message_end)