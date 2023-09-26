# Import the required libraries
from spleeter.separator import Separator
from pydub import AudioSegment
import os

# Define a function to remove vocals from audio
def remove_vocals(audio_path):
    # Load the Spleeter separator model
    separator = Separator('spleeter:2stems')  # You can adjust the model as needed
    
    # Separate the vocals and accompaniment using Spleeter
    audio = separator.separate_to_file(audio_path, 'audio_segments')  # Save segments in 'audio_segments' folder
    
    # Retrieve the accompaniment audio paths
    accompaniment_audio_paths = audio['accompaniment']
    
    return accompaniment_audio_paths

# Define a function to combine segmented audio into one
def combine_audio_segments(audio_paths, output_path):
    combined_audio = AudioSegment.empty()
    for path in audio_paths:
        segment = AudioSegment.from_file(path)
        combined_audio += segment
    
    combined_audio.export(output_path, format=output_path.split('.')[-1])

# Get the input audio file path from the user
input_file = input("Ingresa la ruta del archivo de audio (mp3, mp4, wav): ")

# Remove vocals from the input audio and get the paths of the instrumental audio segments
instrumental_audio_paths = remove_vocals(input_file)

# Combine the instrumental audio segments into a single file
combined_output_file = "instrumental_combined." + input_file.split('.')[-1]
combine_audio_segments(instrumental_audio_paths, combined_output_file)

print("Voces removidas. Audio instrumental combinado guardado como:", combined_output_file)




