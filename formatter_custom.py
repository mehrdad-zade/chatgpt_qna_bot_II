'''
downlaod and setup path for ffmpeg: https://ffmpeg.org/download.html
'''

import subprocess


def mp4_2_wav(mp4_file):
    command2mp3 = "ffmpeg -i source_of_knowledge/" + mp4_file + " source_of_knowledge/output.mp3"
    command2wav = "ffmpeg -i source_of_knowledge/output.mp3 source_of_knowledge/output.wav"
    
    # execute above scripts and generatet the wav file
    subprocess.check_output(command2mp3)
    subprocess.check_output(command2wav)

# mp4_2_wav('youtubeAudio.mp4')