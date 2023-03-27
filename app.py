import time
import youtubeVideoDownloader
from formatter_custom import mp4_2_wav
from nlp_azure import azure_speech_to_text
from vectorizeData import qNa, createVectorIndex

def main():
    
    # provide a youtube link to be dlownloaded as mp4
    youtube_link = "https://www.youtube.com/watch?v=Rwgux6vo9qs"
    # youtubeVideoDownloader.getAudioFrom(youtube_link, output_path='source_of_knowledge', file_name='youtubeAudio.mp4')

    # convert mp4 to mav
    time.sleep(5)
    mp4_2_wav("youtubeAudio.mp4")

    # converts audio to txt and writes the result to source_of_knowledge/output.txt
    azure_speech_to_text('source_of_knowledge/output.wav', 'output.txt') 

    #create vector index on source_of_knowledge/data directory
    vectorIndex = createVectorIndex('source_of_knowledge/data')

    # run the bot
    qNa('source_of_knowledge/vectorIndex.json')


if __name__ == "__main__":
    main()



