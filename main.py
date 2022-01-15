import speech_recognition as sr
import pyttsx3
from PIL import Image
from pytesseract import image_to_string



engine = pyttsx3.init()

def sayToMe(talk):
    engine.say(talk)
    engine.runAndWait()
    
sayToMe('Hello, dude')
sayToMe('Please, say something')

record = sr.Recognizer()
try:
    with sr.Microphone(device_index=6) as source:
        print('Говорите..')
        audio = record.listen(source)
        result = record.recognize_google(audio, language='ru-RU')
        result = result.lower()
        print(result)
        while result != 'выход':
            print('Говорите..')
            audio = record.listen(source)
            result = record.recognize_google(audio, language='ru-RU')
            result = result.lower()
            print(result)
            if result == 'запиши файл':
                text = image_to_string(Image.open('images/photo.png'))
                file = r'image_text.txt'
                with open(file, 'a+') as f:
                    f.write(text)
            elif result == 'запиши секретный файл':
                text = image_to_string(Image.open('images/watchit.png'))
                file = r'image_text.txt'
                with open(file, 'a+') as f:
                    f.write(text)
            elif result == 'запиши другой файл':
                text = image_to_string(Image.open('images/code.png'))
                file = r'image_text.txt'
                with open(file, 'a+') as f:
                    f.write(text)
            elif result == 'прочитай файл':
                with open('image_text.txt', 'r') as n_f:
                    content = n_f.read()
                    print(content)
            elif result == 'очистить файл':
                with open('image_text.txt', 'r+') as f:
                    f.truncate(0)            
except sr.UnknownValueError:
    print('Голос был не распознан')
except sr.RequestError:
    print('Что-то пошло не так')
    
    

    
    
    
    
    
    
