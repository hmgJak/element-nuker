import pyaudio
import wave

# Set up audio player
player = pyaudio.PyAudio()
sound_file = wave.open("creepy-clown-laugh--By-tuna.voicemod.net.mp3", 'rb')
stream = player.open(format=player.get_format_from_width(sound_file.getsampwidth()),
                     channels=sound_file.getnchannels(),
                     rate=sound_file.getframerate(),
                     output=True)

# Monitor microphone state
previous_state = True  # Assume microphone is initially unmuted
while True:
    current_state = # Code to check current microphone state (e.g. using system APIs)
    if current_state and not previous_state:
        # Microphone was just unmuted, play sound
        data = sound_file.readframes(1024)
        while data:
            stream.write(data)
            data = sound_file.readframes(1024)
    previous_state = current_state
