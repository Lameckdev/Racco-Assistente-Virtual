# our main file
import speech_recognition as sr

# Inicializa o reconhecedor
recognizer = sr.Recognizer()

# Captura o áudio pelo microfone
with sr.Microphone() as source:
    print("Fale algo 🎤")
    audio = recognizer.listen(source)  # define o microfone como fonte de áudio

    try:
        # Reconhecimento online com Google (é necessário estar conectado à internet)
        texto = recognizer.recognize_google(audio, language='pt-')
        print("Você disse:", texto)
    except sr.UnknownValueError:
        print("Não entendi o que você disse 😅")
    except sr.RequestError as e:
        print("Erro ao se conectar com a API do Google:", e)
