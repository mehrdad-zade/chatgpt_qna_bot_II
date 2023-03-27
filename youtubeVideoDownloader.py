from pytube import YouTube

def getAudioFrom(link, output_path, file_name):
    # Create YouTube object
    yt = YouTube(link)
    # Get the first stream that contains only audio
    audio_stream = yt.streams.filter(only_audio=True).first()
    # Download the audio stream as an MP4 file
    audio_file = audio_stream.download(output_path=output_path, filename=file_name)
    return audio_file


# Example usage
#link = "https://www.youtube.com/watch?v=cp9GXl9Qk_s" 
# link = "https://www.youtube.com/watch?v=Rwgux6vo9qs"
# getAudioFrom(link, output_path='source_of_knowledge', file_name='youtubeAudio.mp4')