import playsound
import sounddevice as sd

# Set up audio file path
sound_file = "creepy-clown-laugh--By-tuna.voicemod.mp3"

# Monitor microphone state
previous_state = True  # Assume microphone is initially unmuted
while True:
    current_state = not sd.query_devices('default')['default_mic_mute']  # Check current microphone state
    if current_state and not previous_state:
        # Microphone was just unmuted, play sound
        playsound.playsound(sound_file)
    previous_state = current_state
