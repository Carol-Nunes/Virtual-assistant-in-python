import speech_recognition as sr
from playsound3 import playsound
from gtts import gTTS
import webbrowser
import pyttsx3
import os
import pyaudio


class virtual_assist():
  def __init__(self, assist_name, person):
    
    self.assist_name = assist_name
    self.person = person

    self.engine = pyttsx3.init()
    self.recognizer = sr.Recognizer()

    self.voice_data = ''

  def talk(self, text): # Fala da assistente virtual

      text = str(text)
      self.engine.say(text)
      self.engine.runAndWait()

  def record_audio(self, ask = ""):
      with sr.Microphone() as source:
           if ask:
              print("Gravando")
              self.talk(ask)

           audio = self.recognizer.listen(source, timeout=10, phrase_time_limit = 10)
           print("Gravação feita")

           try:
             self.voice_data = self.recognizer.recognize_google(audio)
           except sr.UnknownValueError:
             self.talk("Desculpe, mas eu não entendi o que você disse. Tente novamente")
           except sr.RequestError:
             self.talk("Desculpe, mas o serviço não está disponível no momento")
      return self.voice_data.lower()

    
  def speak(self, audio):

      tts = gTTS(audio, lang='en')
      audio_file = "voice.mp3"
      try:
          os.remove(audio_file)
      except OSError:
          pass

      tts.save(audio_file)
      playsound.playsound(audio_file)


  def respond(self, text):
    if "what's your name" in text:
      self.talk(f"Meu nome é {self.assist_name}")
    elif "hi, how are you doing" in text:
      self.talk("Eu estou ótima, obrigada por perguntar")
    elif "hi" in text or "hello" in text:
      self.talk(f"Olá, {self.person}. Como eu posso te ajudar hoje?")
    elif "search for" in text:
      search_term = text.split("for")[-1]
      url = f"https://google.com/search?q={search_term}"
      webbrowser.get().open(url)
      self.talk(f"Aqui está o que eu achei sobre {search_term} no google")
    elif "youtube" in text:
      self.talk("O que você quer que eu procure?")
      keyword = virtual_assist.record_audio(self)
      if keyword!= '':
          url = f"https://www.youtube.com/results?search_query={keyword}"
          webbrowser.get().open(url)
          self.talk(f"Aqui está o que eu encontrei sobre {keyword} no youtube")
    elif "what is the weather" in text:
      self.talk("Sobre qual lugar você quer saber?")
      information = virtual_assist.record_audio(self)
      url = f"https://www.google.com/search?q=weather+{information}"
      webbrowser.get().open(url)
      self.talk(f"Aqui está o clima do {information}")
    elif "tell me a joke" in text:
      self.talk("Aqui vai uma piada para você")
      self.talk("Por que não pode colocar calabresa no carro quando ele sobe um morro?")
      self.talk("Por que elinguiça")
    elif "play my comfort song" in text:
        url = f"https://www.youtube.com/watch?v=Ho32Oh6b4jc"
        webbrowser.get().open(url)
        self.talk(f"Tocando Perfect do One Direction")
    elif "exit" in text:
      self.talk(f"Até mais, {self.person}")
      exit()
    elif "you are so beautiful" in text:
      self.talk(f"Obrigada, {self.person}! Você também é muito bonita, além de muito inteligente!")
    elif "teenager" in text:
      self.talk("Mano, sério, essa semana foi um rolê muito doido. Primeiro que eu fui na casa do meu amigo, a gente ficou jogando aquele jogo de guerra por umas 5 horas, sem parar, sem fazer nada, só jogando. Depois, a gente saiu pra dar um rolê, ficou batendo papo e rindo de umas paradas nada a ver, tipo, memes e coisas do TikTok. Aí, quando a gente viu, já tava super tarde e nem tinha comido direito. O pior foi que ainda tivemos que correr porque o transporte público tava uma loucura. Enfim, foi um dia meio caótico, mas eu acho que foi o melhor rolê da semana, sem dúvida. Acho que vou dormir agora porque amanhã é mais um dia de correria, né?")
    elif "boy band" in text:
      self.talk("Mano, sério, não tem como negar: o One Direction é, sem dúvida, a melhor banda do mundo. Tipo, eles marcaram uma geração inteira, e não é à toa. Cada música que lançavam era tipo hino, sabe? Eles conseguiram juntar talento, estilo e uma vibe única que ninguém mais conseguiu igualar. As músicas deles têm aquela energia que te pega de jeito, e até hoje, quando ouço 'What Makes You Beautiful', é como se fosse a primeira vez. Além disso, o Liam, o Harry, o Louis, o Niall e o Zayn têm uma química única que você sente em cada apresentação e entrevista. Eles são muito mais do que só uma banda, são amigos, são uma família, e isso transparece nas músicas e nas entrevistas. E, tipo, os fãs? São completamente dedicados, porque o One Direction não é só sobre a música, é sobre as memórias, os sentimentos que cada letra transmite. E o mais legal é que, mesmo com o tempo passando, a gente ainda se conecta com as músicas deles, ainda sente aquela nostalgia boa. Eles são simplesmente atemporais, e isso é o que faz eles serem os melhores, na minha opinião. Mesmo com o tempo, ninguém vai superar o impacto que o One Direction causou no mundo da música e na nossa vida!")
    elif "diva":
      self.talk("Amiga, você me elogia assim e eu quase desmaio! Mas, sério, se eu sou diva, você é a musa inspiradora de todo esse brilho! Juntas, arrasamos sempre, né?")
    else:
      self.respond(virtual_assist.record_audio(self))
    


assistant = virtual_assist("Eva", "Carol")

while True:
    print("Eu estou ouvindo...")
    text = assistant.record_audio()
    print(text)
    assistant.respond(text)

