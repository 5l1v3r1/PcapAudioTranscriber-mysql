import speech_recognition as sr
from pydub import AudioSegment
import pyshark
import mysql.connector
import sys
import os

# pip install speech_recognition
# pip install pyshark
# pip install pydub
# pip install mysql


# simply shitty mysql connector to connect to the DB
mydb = mysql.connector.connect(
  host="MYSQL IP",
  port="PORT",
  database="DATABASE NAME",
  user="USERNAME",
  passwd="DB PASSWORD"
)

# thanks to wbwarnerb for help the base of the code that was modified for this
def scraper():
    pcap_file = input("Enter the name of your pcap file in this folder: ")
    filter_type = input("What layer do you want to filter on? (rtp):  ")
    out_file = input("Provide your desired output filename: ")
    rtp_list =[]
    print("Scraping: " + pcap_file)
    cap = pyshark.FileCapture(pcap_file,display_filter=filter_type)
    raw_audio = open(out_file,'wb')

    for i in cap:
        try:
            rtp = i[3]
            if rtp.payload:
                print(rtp.payload)
                rtp_list.append(rtp.payload.split(":"))
        except:
            pass
    for rtp_packet in rtp_list:
        packet = " ".join(rtp_packet)
        print(packet)
        audio = bytearray.fromhex(packet)
        raw_audio.write(audio)

        src = self.outfile
        dst = "output.wav"
        sound = AudioSegment.from_mp3(src)
        sound.export(dst, format="wav")
        AUDIO_FILE = dst
        r = sr.Recognizer()
        with sr.AudioFile(AUDIO_FILE) as source:
            audio = r.record(source)  # read the entire audio file
            transcription = r.recognize_google(audio)
        mycursor = mydb.cursor()
        sql = "INSERT INTO transcribedaudio (transcribed) VALUES (%s)"
        val = (transcription)
        mycursor.execute(sql, val)
        mydb.commit()

# terrible basic menu system bellow
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def menu():
    clear()
    ans = True
    while ans:
        print("")
        print("#######################################################")
        print("#    Pcap Audio Transcriber By @TheCyberViking        #")
        print("#######################################################")
        print("This will Generator a Full Cover Story for you")
        print("This tool will crate a Raw Audio File and Also transcribe")
        print("that audio file to a provided mysql Database")
        print("")
        print("""
        1.  Pcap to Audio
        99. Exit/Quit
        """)
        print("")
        ans = input("Choose and Option from the List: ")
        if ans == "1":
            scraper()
        elif ans == "99":
            print("\n Closing Program Now")
            clear()
            sys.exit()
        else:
            print("!!! please choose a vaild menu option, now exiting !!!")
            menu()

# This will run the code
menu()
