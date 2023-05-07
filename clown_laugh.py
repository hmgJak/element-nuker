import pyaudio
import wave
import sounddevice as sd

# Set up audio player
player = pyaudio.PyAudio()
sound_file = wave.open("creepy-clown-laugh--By-tuna.voicemod.mp3", 'rb')
stream = player.open(format=player.get_format_from_width(sound_file.getsampwidth()),
                     channels=sound_file.getnchannels(),
                     rate=sound_file.getframerate(),
                     output=True)

# Monitor microphone state
previous_state = True  # Assume microphone is initially unmuted
while True:
    current_state = not sd.query_devices('default')['default_mic_mute']  # Check current microphone state
    if current_state and not previous_state:
        # Microphone was just unmuted, play sound
        data = sound_file.readframes(1024)
        while data:
            stream.write(data)
            data = sound_file.readframes(1024)
    previous_state = current_state
