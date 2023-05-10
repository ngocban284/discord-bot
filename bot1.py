from http.client import HTTPSConnection
import sys
from json import dumps
from time import sleep
import random

file = open("info1.txt")
text = file.read().splitlines()

if len(sys.argv) > 1 and sys.argv[1] == "--setall" and input("Configure bot? (y/n)") == "y":
    file.close()
    file = open("info1.txt", "w")
    text = []
    text.append(input("User agent: "))
    text.append(input("Discord token: "))
    text.append(input("Discord channel URL: "))
    text.append(input("Discord channel ID: "))

    for parameter in text:
        file.write(parameter + "\n")

    file.close()
    exit()
elif len(sys.argv) > 1 and sys.argv[1] == "--setchannel" and input("Set channel? (y/n)") == "y":
    user_agent = text[0]
    token = text[1]
    text = text[0:2]
    file.close()
    file = open("info1.txt", "w")
    text.append(input("Discord channel URL: "))
    text.append(input("Discord channel ID: "))
    for parameter in text:
        file.write(parameter + "\n")

    file.close()
    exit()
elif len(sys.argv) > 1 and sys.argv[1] == "--setauth" and input("Set authentication? (y/n)") == "y":
    channelurl = text[2]
    channelid = text[3]
    text = text[2:4]
    file.close()
    file = open("info1.txt", "w")
    text.insert(0, input("Discord token: "))
    text.insert(0, input("User agent: "))
    for parameter in text:
        file.write(parameter + "\n")

    file.close()
    exit()
elif len(sys.argv) > 1 and sys.argv[1] == "--help":
    print("Showing help for discord-auto-message")
    print("Usage:")
    print("  'python3 bot.py'               :  Runs the autotyper. Fill in the messages and wait times.")
    print("  'python3 bot.py --setall'      :  Configure all settings.")
    print("  'python3 bot.py --setchannel'  :  Set channel to send message to. Includes Channel ID and Channel URL")
    print("  'python3 bot.py --setauth'     :  Set authentication. Includes User Token and User Agent")
    print("  'python3 bot.py --help'        :  Show help")
    exit()

if len(text) != 4:
    print("An error was found inside the user info1rmation file. Run the script with the 'Set All' flag ('python3 bot.py --setall') to reconfigure.")
    exit()
    
if len(sys.argv) > 1:
    exit()
    
header_data = {
    "content-type": "application/json",
    "user-agent": text[0],
    "authorization": text[1],
    "host": "discordapp.com",
    "referrer": text[2]
}

print("Messages will be sent to " + header_data["referrer"] + ".")

def get_connection():
    return HTTPSConnection("discordapp.com", 443)


def send_message(conn, channel_id, message_data):
    try:
        conn.request("POST", f"/api/v6/channels/{channel_id}/messages", message_data, header_data)
        resp = conn.getresponse()

        if 199 < resp.status < 300:
            print("Message sent!")
            pass

        else:
            sys.stderr.write(f"Received HTTP {resp.status}: {resp.reason}\n")
            pass

    except:
        sys.stderr.write("Failed to send_message\n")
        for key in header_data:
            print(key + ": " + header_data[key])


def main(msg):
    message_data = {
        "content": msg,
        "tts": "false",
    }

    send_message(get_connection(), text[3], dumps(message_data))


randomMessage = [
    "第8个也不难呀。哪里会难。就是卡。第8个也不难呀。哪里会难",
    "现在水怎么变那么少了 没人卷  你们不是人均100号吧",
    "水还是不好领啊",
    "100个号到时候主网交互成本都不少",
    "没人卷  你们不是人均100号吧",
    "有什么可做的，做完了，一周搞一次就是了",
    "你们是真卷啊，现在还在做",
    "昨天领的多",
    "没有其他任务可以做吧",
    "0.1个，想做点啥要领好几天",
    "我都想进树林继续伐木了",
    "才换这么点 都不够加流动性",
    "大伙第八个任务 是不是SEI都不够用啦",
    "中文群一堆发乱七八糟的机器人，不闻不问，真是莫名其妙！",
    "这狗项目到底啥时候才主网啊",
    "这项目还能玩吗",
    "每个区的30秒都不同步的，好吧",
    "ご自身の国のチャンネルに投稿してください！",
    "有时候得刷好几次才成功",
    "机器人都没见踢，那得多水才被踢",
    "我等好多天,都卡著怪怪的",
    "任务6做不了现在。等几天吧",
    "多解答问题，太水了要遭踢",
    "加油加油冲冲冲冲冲",
    "水群等级吗？不难。就哔哔就行了"
    ]

if __name__ == '__main__':
    # print("Message to send- when finished, type an EOF character:")
    # message = sys.stdin.read()
    messages = int(input("Amount of messages: "))
    main_wait = int(input("Seconds between messages: "))
    human_margin = int(input("Human error margin: "))
    print()
    for i in range(0,messages):
        main(randomMessage[random.randrange(0, len(randomMessage))])
        print("Estimated time to complete: " + str((messages-i) * (human_margin // 2 + main_wait) // 60) + " minutes.")
        print("Iteration " + str(i) + " complete.\n")
        sleep(main_wait)
        sleep(random.random()*human_margin)

    print("Session complete! " + str(messages) + " messages sent.")
