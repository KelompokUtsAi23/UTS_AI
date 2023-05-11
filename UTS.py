from speech_recognition import Microphone, Recognizer, UnknownValueError, RequestError



recog = Recognizer()
mic = Microphone()
hasil = ""

with mic:
        recog.adjust_for_ambient_noise(mic, duration=5)
        
        print("BICARA")
        audio = recog.record(mic, 10)
try:
        hasil = recog.recognize_google(audio, language='id-ID')
        print("KAMU MENGATAKAN :", hasil)

except RequestError as exc:
        print(exc)

except UnknownValueError:
        print("Tidak  bisa mendeteksi")


text_file = open("TeksSuara.txt", "w")
text_file.write(hasil)
text_file.close()    
        
