from http.client import HTTPSConnection
import sys
from json import dumps
from time import sleep
import random

file = open("info.txt")
text = file.read().splitlines()

if len(sys.argv) > 1 and sys.argv[1] == "--setall" and input("Configure bot? (y/n)") == "y":
    file.close()
    file = open("info.txt", "w")
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
    file = open("info.txt", "w")
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
    file = open("info.txt", "w")
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
    print("An error was found inside the user information file. Run the script with the 'Set All' flag ('python3 bot.py --setall') to reconfigure.")
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
    "ae cày kéo đến đâu rồi, có mỏi tay không =))",
    "mai lên lv7 hết thôiii, cố lên ae", 
    "chúng ta sắp thành công rồi anh em ơi",
    "Chúng ta sắp giàu rồi anh em ơi",
    "aaaaa, phải cố lên thôi",
    "hehehe, cố lên mn, sắp đc rồi",
    "chuẩn bị ngủ thôii",
    "nhiều bác kêu nhiệm vụ 6 khó nhỉ mình làm trước ngay khi sei đăng bài đến khi nhiệm vụ ra bấm vèo cái xong rùi",
    "mấy hôm không vào, hình như tăng thành viên hic bị chặn chat lên đến 2 phút lận :(((",
    "Sao Rồi ae ai cho xin cái form với nào,mình sắp lv7 rồi còn 6lv nữa thôi",
    "bác nòa có cho e xin ít 0.2 thôi", 
    "cày lên lv 20 chắc cũng căng à nha ngồi 6-7 ngày  liên tục",
    "cứ chat thôi bác… nó lên đc nhiêu thì lên!!! Nếu giỏi English bác qua General chat nhanh hơn, 1/1p",
    "Sắp đc rồi, mọi người đừng nản",
    "cố lên minaaa",
    "nếu mọi người không biết, thì tôi chạy bốt hehe",
    "bye bye, hẹn gặp lại mọi người",
    "cày được lv10 đỉnh quá",
    "chào các pro! chúc mọi người 1 ngày mới tốt lành nhé",
    "Nhiều ông cứ cày trước rồi huy động họ hàng vào kyc là cái chắc",
    "thần kinh với cái Liquid quá. giờ kiếm đâu sei mà swap rồi add??",
    "Mà kèo aidrop toàn tính trước mấy tháng",
    "ae chats mạnh quá đọc tin hoa cả mắt @@",
    "thôi cố thêm 1h mn nữa ạ",
    "Gần được các brooo ơi",
    "Cho mình xin cái form với nào, mình sắp lv7 rồi còn vài lv nữa thôi",
    "Ngủ chưa ae",
    "Lên 7 còn đi ngủ nào",
    "vn mình cày air chiến thật",
    "Cho tôi lên level 6 đi các ông ơi. Chat cả tiếng sao mãi chưa lên được huhu",
    "Có ai đang cày không",
    "Tôi cũng đang cày đây",
    "Baby đừng có khóc nữa, anh sẽ cày cho em",
    "Baby đừng làm a suy",
    "i told you long ago, on the road",
    "you are not alone, i am here with you",
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
