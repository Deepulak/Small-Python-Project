##############

# TypeError: argument of type 'function' is not iterable

##################



import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia 
import pyjokes
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
	engine.say(text)
	engine.runAndWait()

	#wiki = wikipedia.summary(person, 1)		
	#print(info)
	#talk(info)

def take_commands():
	try:
		with sr.Microphone as source:
			print('listening..............')
			voice = listener.listen(source)
			command = listener.recognize_google(voice)
			command = command.lower()
			if 'alexa' in command:
				command = command.replace('alexa', '')
				print(command)

	except:
		pass
	return command

def run_alexa():
	command = take_commands
	print(command)
	if 'what is your name' in command:
		talk('My name is Elli')
	elif 'fuck you in Elli' in command:
		talk("what is your name")
	elif 'my name is d' in command:
		talk("Fuck you D")
	elif 'play' in command:
		song = command.replace('play', '')
		talk('playing ' + song)
		pywhatkit.playonyt(song)
	elif 'time' in command:
		time = datetime.datetime.now().strftime('%I:%M %p')
		talk('Current time is ' + time)
	#elif 'who the heck is' in command:
		#person = command.replace('who the hack is', '')
		#info #
	elif 'date' in command:
		talk('sorry, i have headache')
	elif 'are you single' in command:
		talk('I am in a relationship with wifi')
	elif 'joke' in command:
		talk(pyjokes.get_joke())
	else:
		talk('please say the command again.')

while True:
	run_alexa()
