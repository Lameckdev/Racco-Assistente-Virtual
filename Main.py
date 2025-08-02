import speech_recognition as sr

# Inicializa o reconhecedor
reconhecedor = sr.Recognizer()

print("Fale algo... (pressione Ctrl+C para parar o reconhecimento)")

try:
    while True:
        # Usa o microfone como fonte de áudio
        with sr.Microphone() as fonte:
            print("Ouvindo...")
            reconhecedor.adjust_for_ambient_noise(fonte)
            audio = reconhecedor.listen(fonte)

            try:
                # Reconhecimento online usando Google
                texto = reconhecedor.recognize_google(audio, language='pt-BR')
                print("Você disse:", texto)

            except sr.UnknownValueError:
                print("Não foi possível entender o áudio.")
            except sr.RequestError as e:
                print("Erro ao se conectar com o serviço de reconhecimento:", e)

except KeyboardInterrupt:
    print("\nEncerrando o programa. Até mais!")