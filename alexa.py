import math
from PyDictionary import PyDictionary
import pyjokes
import pyautogui
import pywhatkit
import random
import time
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyttsx3
from email.message import EmailMessage
import wolframalpha

facebook_list={'Muzammil':'muzammil.alam231@gmail.com'
               }
gmail_list={'Muzammil':'muzammil.alam231@gmail.com',
            'brother':'rayyanorangzeb007@gmail.com'
            }
name=['my name is alexa','my creator calls me alexa','i love to be called alexa']
made=['muzammil made me','i was made by muzammil']

age=['i dont want to answer this question, sorry','sorry, i dont want to answer']
built=['i was built in 2021 by muzammil','muzammil created or built me in 2021']
sport=['i love cricket','my favorite sport is cricket','i love to watch cricket']
how=['i am good','i am better than you','im fine']
color=['i love pink','my favorite color is pink']

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',180)
listener = sr.Recognizer()

def talk(text):
    engine.say(text)
    engine.runAndWait()



def get_info():
    try:
        with sr.Microphone() as source:
            print('Say some thing!')
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account

    server.login('muzammil.alam231@gmail.com', '125lasthop3')
    email = EmailMessage()
    email['From'] = 'muzammil.alam231gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'brother':'mudasir2002@yahoo.com',

}


def get_email_info():
    talk('To Whom you want to send email')
    name = Command()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject = Command()
    talk('Tell me the text in your email')
    message = Command()
    send_email(receiver, subject, message)
    talk('Hey sir. Your email has been sent')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak(", Good Morning!")

    elif hour>=12 and hour<16:
        speak(", Good Afternoon!")

    elif hour>16 and hour<18.5:
        speak(', good evening!')
    else:
        pass
def Command():
    #It takes microphone input from the user and returns string output

    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("say something SIR!")
        listener.pause_threshold = 1
        listener.adjust_for_ambient_noise(source)
        audio = listener.listen(source)

    try:
        print("Recognizing...")
        query =listener.recognize_google(audio,language='en-HI')
        print(f"User said: {query}")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query



def snake():
    print('Welcome to the snake water gun game :) ')
    speak('Welcome to the snake water gun game ')
    print('Lets start!')
    speak('Lets start!')
    alexa_score = 0
    chance = 1
    user_score = 0
    game_draw = 0
    total_chances = 5

    while total_chances >= 1:
        speak(f"you have {total_chances} chances")
        print(f"you have {total_chances} chances")

        Maryam_choice = random.choice(['snake', 'water', 'gun'])
        user_choice = Command()

        if user_choice == 'water' and Maryam_choice == 'snake':
            print(f"You chose {user_choice} and I chose {Maryam_choice}")
            speak(f"You chose {user_choice} and I chose {Maryam_choice}")
            print('I won this round')
            speak('I won this round')
            alexa_score += 1
            total_chances -= 1

        elif user_choice == Maryam_choice:
            print(f"You chose {user_choice} and I chose {Maryam_choice} too ")
            speak(f"You chose {user_choice} and I chose {Maryam_choice} too ")
            print('Round draw')
            speak('Round draw')
            game_draw += 1
            total_chances -= 1

        elif user_choice == 'water' and Maryam_choice == 'gun':
            print(f"you chose {user_choice} and I chose {Maryam_choice}")
            speak(f"you chose {user_choice} and I chose {Maryam_choice}")
            print('You won this round')
            speak('You won this round')
            user_score += 1
            total_chances -= 1

        elif user_choice == 'gun' and Maryam_choice == 'snake':
            print(f"You chose {user_choice} and I chose {Maryam_choice}")
            speak(f"You chose {user_choice} and I chose {Maryam_choice}")
            print('You won this round')
            speak('You won this round')
            user_score += 1
            total_chances -= 1

        elif user_choice == 'gun' and Maryam_choice == 'water':
            print(f"You chose {user_choice} and I chose {Maryam_choice} ")
            speak(f"You chose {user_choice} and I chose {Maryam_choice} ")
            print('I won this round')
            speak('I won this round')
            alexa_score += 1
            total_chances -= 1

        elif user_choice == 'snake' and Maryam_choice == 'gun':
            print(f"You chose {user_choice} and I chose {Maryam_choice}")
            speak(f"You chose {user_choice} and I chose {Maryam_choice}")
            print('I won this round')
            speak('I won this round')
            alexa_score += 1
            total_chances -= 1

        elif user_choice == 'snake' and Maryam_choice == 'water':
            print(f"You chose {user_choice} and I chose {Maryam_choice}")
            speak(f"You chose {user_choice} and I chose {Maryam_choice}")
            print('You won this round')
            speak('You won this round')
            user_score += 1
            total_chances -= 1
        else:
            print(f" Invalid Input You chose {user_choice} which is invalid, sorry")
            speak(f" Invalid Input You chose {user_choice} which is invalid, sorry")
            alexa_score += 1
            total_chances -= 1

    if user_score > alexa_score:
        print(f"Your final score is {user_score} and mine is {alexa_score}")
        speak(f"Your final score is {user_score} and mine is {alexa_score}")
        print(f'Round drew {game_draw} times')
        speak(f'Round drew {game_draw} times')
        print('You won!, Congratulations!')
        speak('You won! Congratulations!. do you want to play again?')
        a = Command()
        if 'yes' in a:
            snake()
        else:
            speak('ok sir!')

    elif user_score < alexa_score:
        print(f"Your final score is {user_score} and mine is {alexa_score}")
        speak(f"Your final score is {user_score} and mine is {alexa_score}")
        print(f'Round drew {game_draw} times')
        speak(f'Round drew {game_draw} times')
        print('I won!')
        speak('i won!. do you want to play again?')
        a=Command()
        if 'yes' in a:
            snake()
        else:
            speak('ok sir!')


    else:
        print(f"Your score is {user_score} and my score is {alexa_score} too :)")
        speak(f"Your score is {user_score} and my score is {alexa_score} too ")
        print(f"Round drew {game_draw} times")
        print(f"No one loses")
        speak(f"No one loses")
def uess():
    number_of_guesses=0
    guess=random.randint(3,19)
    speak('welcome to the guess game. you will have to guess the number. the number is between 3 and 19 . lets play!')
    while True:
        Guess=int(Command())
        if Guess>guess:
            number_of_guesses += 1
            speak(f'Try a lesser number!, you have {6-number_of_guesses} more guesses!')
        elif Guess=='Tu':
            a=str(Guess)
            a.replace('Tu','2')
            b=int(a)
            if b>guess:
                number_of_guesses+=1
                speak(f'Try a lesser number!, you have {6-number_of_guesses} more guesses')
            elif b<guess:
                number_of_guesses+=1
                speak(f'Try a greater number!, you have {6-number_of_guesses} more guesses')
            else:
                speak('you won, congratulations!')
                speak(
                    f'you took {number_of_guesses} guesses to guess my number!, the number was {guess}, do you want to play again?')
                again = Command()
                if 'yes' in again:
                    uess()
                else:
                    speak('ok sir!')
                    break
        elif Guess<guess:
            number_of_guesses += 1
            speak(f'Try a greater number!, you have {6-number_of_guesses} more guesses!')

        else:
            speak('you won, congratulations!')
            speak(f'you took {number_of_guesses} guesses to guess my number!, the number was {guess}, do you want to play again?')
            again=Command()
            if 'yes' in again:
                uess()
            else:
                speak('ok sir!')
                break

        if number_of_guesses>=6:
            speak(f'sorry, you lost sir!, better luck next time. by the way the number was {guess}. do you want to play again?')
            again = Command()
            if 'yes' in again:
                uess()
            else:
                speak('ok sir!')
                break

if __name__ == "__main__":
    speak('hi sir')
    wishMe()
    speak('i am alexa, tell me, how may i help you?')
    while True:
    # if 1:
        query = Command().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open google' in query:
            speak('ok sir, opening google')
            webbrowser.open('https://www.google.com')
        elif 'open facebook' in query:
            speak('ok sir, opening facebook')
            webbrowser.open('https://www.facebook.com')

        elif 'open youtube' in query:
            speak('opening youtube, but sir do you want to search anything on youtube?')
            a=Command()
            if 'yes' in a:
                speak('ok, then tell me what do you want to search?')
                b=Command()
                webbrowser.open("https://www.youtube.com")
                pyautogui.moveTo(881,129)
                pyautogui.moveTo(881,131)
                time.sleep(5)
                pyautogui.leftClick()
                pyautogui.write(b)
                speak('here you go')
                pyautogui.press('enter')
            else:
                speak('ok sir, here you go!')
                webbrowser.open('https://www.youtube.com')

        elif 'daraz' in query:
            speak('opening daraz, but sir do you want to search anything on daraz?')
            a = Command()
            if 'yes' in a:
                speak('ok, then tell me what do you want to search?')
                b = Command()
                webbrowser.open("https://www.daraz.pk")
                pyautogui.moveTo(890,162)
                pyautogui.moveTo(890, 160)
                time.sleep(5)
                pyautogui.leftClick()
                pyautogui.write(b)
                speak('here you go')
                pyautogui.press('enter')
            else:
                speak('ok sir, here you go sir')
                webbrowser.open('https://www.daraz.pk')

        elif 'play music' in query:
            music_dir = 'D:\\images and stuff\\songs\\s'
            songs = os.listdir(music_dir)
            a=random.randint(0,29)
            speak('ok sir, playing music for you')
            os.startfile(os.path.join(music_dir, songs[a]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"Sir, the current time is {strTime}")

        elif 'visual' in query:
            codePath = "C:\\Users\\Mudasir\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email' in query:
            get_email_info()
            speak('do you want to send more emails?')
            while True:
                c=Command()
                if 'yes' in c:
                    get_email_info()
                else:
                    speak('ok sir!')

        elif 'search for' in query:
            speak('Searching...')
            query = query.replace("search for", "")
            results = pywhatkit.search(query)
            speak('here you go sir!')

        elif 'search about' in query:
            speak('searching...')
            query=query.replace('search about','')
            results=pywhatkit.search(query)
            speak('here you go!')
        elif 'search' in query:
            speak('Searching.')
            query = query.replace("search", "")
            results = pywhatkit.search(query)
            speak('here you go sir!')

        elif 'whatsapp' in query:
            speak('to whom you want to send the whatsapp message?')
            to=Command()
            name=phone_list[to]
            speak('what is the message?')
            msg=Command()
            speak('inorder to send the whatsapp message a specific time in 24 hours format is required. please tell me the hours')
            hours=Command()
            speak('can you please tell me the minutes?')
            minutes=Command()
            speak('ok sir. i will be sending your message soon.')
            pywhatkit.sendwhatmsg(name,msg,int(hours),int(minutes),20)

        elif 'name' in query:
            speak(random.choice(name))
        elif 'age' in query:
            speak(random.choice(age))
        elif 'made'in query:
            speak(random.choice(made))
        elif 'made' and 'when' in query:
            speak(random.choice(built))
        elif 'built' in query:
            speak(random.choice(built))
        elif 'goodbye' in query:
            speak('ok sir, you can call me whenever you want. take care, see you again')
            exit()

        elif 'shutdown' in query:
            speak('are you sure')
            a=Command()
            if 'yes' in a:
                shutdown='C:\\Users\\Mudasir\\Desktop\\shutdown\\New Text Document (2).bat'
                speak(' ok sir, shutting down your computer')
                os.startfile(shutdown)
            else:
                speak('ok sir')

        elif 'restart' in query:
            speak('are you sure??')
            sure=Command()
            if 'yes' in sure:
                restart='C:\\Users\\Mudasir\\Desktop\\shutdown\\(2).bat'
                speak('ok sir, restarting your computer.')
                os.startfile(restart)
            else:
                speak('ok sir')

        elif 'sleep' in query:
            speak(' ok sir!, i am going to sleep')
            time.sleep(300)
            speak('hi sir, i am back, tell me how may i help you')

        elif 'joke' in query:
            speak('what type of joke ,  say c for chuck or n for neutral?')
            a=Command()
            if 'c' in a:
                speak('ok sir, let me thing about chuck norris joke')
                time.sleep(2)
                joke=pyjokes.get_joke(language='en',category='chuck')
                print(joke)
                speak(joke)
            elif 'n' in a:
                speak('ok sir, let me think about programming joke')
                time.sleep(2)
                joke=pyjokes.get_joke(language='en',category='neutral')
                print(joke)
                speak(joke)
            else:
                speak(' sorry sir, i do not have those types of jokes')

        elif 'math' in query:
            speak('ok sir, but i dont know maths well, i can only add, subtract. i can tell square root of number, i can determine whether a number is prime or not, i can tell the factorial of any number and i can tell the table of any number. now ask me a question')
            while True:
                a=Command()

                if 'square root' in a:
                    speak('ok sir, tell me the number')
                    square = Command()
                    try:
                        final = math.sqrt(int(square))
                        print(final)
                        speak(f'The square root of {square} is {final}')
                    except Exception as ArithmeticError:
                        print('sorry')
                        speak('sorry')

                elif 'factorial' in a:
                    speak('ok, then tell me the number')
                    factorial=Command()
                    if 'sex' in factorial:
                        b=factorial.replace('sex','6')
                        a=b
                        c=int(a)
                        factorial=c
                        f = 1
                        for i in range(1, factorial + 1):
                            f = f * i
                        print(f)
                        speak(f'the factorial of {factorial} is {f}')
                    else:
                        f=1
                        for i in range(1,int(factorial)+1):
                            f=f*i
                        print(f)
                        speak(f'the factorial of {factorial} is {f}')
                elif 'Prime' in a:
                    speak('ok sir, then tell me the number')
                    p=Command()
                    if 'sex' in p:
                        g=p.replace('sex','6')
                        z=g
                        d=int(z)
                        p=d
                        for i in range(2, p):
                            if p % i == 0:
                                speak(f'{p} is a composite number')
                                break
                                break
                            else:
                                speak(f'{p} is a prime number')
                                break
                    else:
                        v=int(p)
                        for i in range(2,v):
                            if v>1:
                                if v%i==0:
                                    speak(f'{v} is a composite number')
                                    break
                                else:
                                    speak(f'{v} is a prime number')
                                    break
                            else:
                                speak(f'sorry sir, i couldnt find out that either {v} is prime or composite')
                                break

                elif 'table' in a:
                    speak('ok, then tell me the number')
                    num = int(Command())
                    speak('till which number do you want to get the table')
                    x = int(Command())
                    engine.setProperty('rate',200)
                    for i in range(1, x + 1):
                        print(f'{num} x {i} = {num*i}')
                        speak(f'{num} multiplied by {i} is equal to {num*i}')

                elif 'come out' in a:
                    speak('ok sir, no more maths now')
                    break

                elif 'x' in a:
                    b=a.replace('x','*')
                    h=b
                    o=eval(h)
                    speak(o)
                    print(o)
                # elif 'divide' in a:
                #     y=a.replace('divide','/')
                #     _=y
                #     k=eval(_)
                #     speak(k)
                #     print(k)
                else:
                    c=eval(a)
                    speak(c)

        elif 'snake water gun' in query:
            snake()

        elif 'guess game' in query:

            uess()
        elif 'date' in query:
            date_time_now = datetime.datetime.now()
            a = datetime.datetime.date(date_time_now)
            speak(f'sir. today is {a} and ')
        elif 'close google' in query:
            os.system("taskkill /f /im chrome.exe")
            speak('done!')
        elif 'close pycharm' in query:
            os.system("taskkill /f /im pycharm64.exe")
            speak('done!')
        elif 'stop music' in query:
            os.system("taskkill /f /im VLC.exe")
            speak('done!')

        elif 'login facebook' in query:
            speak('ok sir, tell me the user name')
            user_name=Command()
            facebook_user=facebook_list[user_name]
            final_user=facebook_user
            speak('now tell me the password secretly by typing in the console')
            facebook_pass=input('Enter your password here: ')
            speak('ok sir!, opening facebook and logging you in.')
            webbrowser.open('https://www.facebook.com')
            time.sleep(8)
            pyautogui.moveTo(1236,277)
            pyautogui.moveTo(1236,275)
            pyautogui.leftClick()
            pyautogui.typewrite(final_user)
            time.sleep(0.5)
            pyautogui.moveTo(1350,337)
            pyautogui.moveTo(1356,335)
            pyautogui.leftClick()
            time.sleep(0.5)
            pyautogui.moveTo(1290,335)
            pyautogui.leftClick()
            pyautogui.typewrite(facebook_pass)
            time.sleep(0.5)
            pyautogui.press('enter')
            speak('successfully logged you in.')

        elif 'logout facebook' in query:
            speak('ok sir, logging you out.')
            webbrowser.open('https://www.facebook.com')
            time.sleep(8)
            pyautogui.moveTo(1993,125)
            pyautogui.leftClick()
            time.sleep(0.5)
            pyautogui.moveTo(1771,559)
            time.sleep(0.5)
            pyautogui.leftClick()
            speak('successfully logged you out.')

        elif 'login google' in query:
            speak('ok sir, tell me the user name.')
            user = Command()
            gmail_user = gmail_list[user]
            gmail_final = gmail_user
            speak('ok sir, now tell me the password secretly by typing in the console')
            password = input('Enter your password here: ')
            speak('ok sir, logging you in.')
            webbrowser.open("https://www.gmail.com")
            time.sleep(5)
            pyautogui.moveTo(964, 892)
            time.sleep(0.5)
            pyautogui.leftClick()
            time.sleep(0.5)
            pyautogui.moveTo(933, 567)
            time.sleep(0.5)
            pyautogui.leftClick()
            time.sleep(0.5)
            pyautogui.typewrite(gmail_final)
            time.sleep(0.5)
            pyautogui.moveTo(1171, 754)
            time.sleep(0.5)
            pyautogui.leftClick()
            time.sleep(0.5)
            pyautogui.moveTo(949, 585)
            time.sleep(0.5)
            pyautogui.leftClick()
            time.sleep(0.5)
            pyautogui.typewrite(password)
            time.sleep(0.5)
            pyautogui.moveTo(1165, 710)
            time.sleep(0.5)
            pyautogui.leftClick()
            speak('successfully logged you in.')


        elif 'logout google' in query:
            speak('ok sir, logging you out.')
            webbrowser.open('https://google.com')
            time.sleep(1)
            pyautogui.moveTo(1991,50)
            pyautogui.leftClick()
            time.sleep(0.5)
            pyautogui.moveTo(1798,405)
            pyautogui.leftClick()
            speak('successfully logged you out.')

        elif 'what can you do' in query:
            speak('I am alexa. I can do simple tasks for muzammil. I can send email to anyone, i can send a whatsapp message to anyone, i can login to gmail account, i can login to facebook account. I can play guess game and snake water gun too. i can easily open youtube and daraz and search anything on these websites. i can shutdown and restart this computer. i can solve mathematical questions, but i am only capable to add, subtract. I can determine whether a number is prime or composite, i can tell the factorial of any number and i can tell the table of a number too. I can tell jokes, I can play music, i can tell the date and time, i can search anything on wikipedia and i can read the wikipedia articles too. lastly i can search anything on google. i hope you will like me.')
        elif 'thank you'in query:
            speak('Welcome sir!')
        elif 'sport' in query:
            speak(random.choice(sport))
        elif 'colour' in query:
            speak(random.choice(color))
        elif 'how are you' in query:
            speak(random.choice(how))
        elif 'what is love' in query:
            speak('Love is complex. A mix of emotions, behaviors, and beliefs associated with strong feelings of affection, protectiveness, warmth, and respect for another person.For example, a person might say he or she loves his or her dog, loves freedom, or loves God')

        elif 'my favourite playlist' in query:
            speak('sir which playlist? The bollywood one or the programming one?')
            song=Command()
            if 'Bollywood' in song:
                speak('ok sir, playing your bollywood playlist.')
                webbrowser.open('https://www.youtube.com')
                time.sleep(6)
                pyautogui.moveTo(92,300)
                time.sleep(0.8)
                pyautogui.leftClick()
                time.sleep(2)
                pyautogui.moveTo(718,916)
                time.sleep(0.8)
                pyautogui.leftClick()
                time.sleep(1)
                pyautogui.leftClick()
                time.sleep(0.5)
                pyautogui.moveTo(2040,915)
                time.sleep(0.5)
                pyautogui.leftClick()
                pyautogui.moveTo(577,768)
                time.sleep(0.8)
                pyautogui.leftClick()
                time.sleep(1)
                pyautogui.moveTo(1194,810)
                time.sleep(0.5)
                pyautogui.leftClick()
                speak('here you go sir')

            elif 'programming' in song:
                speak('ok sir, playing your programming playlist.')
                webbrowser.open('https://www.youtube.com')
                time.sleep(6)
                pyautogui.moveTo(92, 300)
                time.sleep(0.8)
                pyautogui.leftClick()
                time.sleep(2)
                pyautogui.moveTo(718, 916)
                time.sleep(0.8)
                pyautogui.leftClick()
                time.sleep(1)
                pyautogui.leftClick()
                time.sleep(0.5)
                pyautogui.moveTo(2040, 915)
                time.sleep(0.5)
                pyautogui.leftClick()
                pyautogui.moveTo(577, 768)
                time.sleep(0.8)
                pyautogui.leftClick()
                time.sleep(1)
                pyautogui.moveTo(826, 807)
                time.sleep(0.5)
                pyautogui.leftClick()
                speak('here you go sir')
            else:
                speak('sorry sir, i cant play that playlist.')

        elif 'minimise window' in query:
            pyautogui.moveTo(1933,12)
            pyautogui.leftClick()
            pyautogui.moveTo(500,200)
            speak('done')
            
        elif 'close window' in query:
            pyautogui.moveTo(2025,14)
            pyautogui.leftClick()
            speak('done')

        elif 'what is the meaning of' in query:
            f=PyDictionary()
            a=query.replace('what is the meaning of','')
            b=f.meaning(a).values()
            c=f.antonym(a)
            d=f.synonym(a)
            try:
                print(b,c,d)
                speak(f'meaning of {a} is {str(b).replace("dict_values"," ")}. The antonyms of {a} is {c}. The synonyms of {a} is {d}')
            except Exception as AttributeError:
                print('srry sir')
                speak('sorry sir i couldnt understand.')

       
        elif 'alexa what is' in query:
            question = query.replace('alexa what is','')
            app_id = "9JQRR7-QVL5KRAAY8"
            client = wolframalpha.Client(app_id)
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif 'alexa who is' in query:
            question = query.replace('alexa who is', '')
            app_id = "9JQRR7-QVL5KRAAY8"
            client = wolframalpha.Client(app_id)
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
        elif 'ip address' in query:
            ip=get('https://api.ipify.org').text
            print(ip)
            speak(f'Your ip address is {ip}')

        else:
            print('cant recognize')





