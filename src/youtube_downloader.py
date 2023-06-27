from deep_translator import GoogleTranslator
from loguru import logger
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi

from src.utils import YouTubeErorr


class YouTubeDownoader:

    def __init__(self, url):
        self.url = url

    def download_audio(self, path):
        audio = YouTube(self.url)
        audio = audio.streams.filter(only_audio=True).first()

        try:
          audio.download(path)
        except:
          logger.info("Failed to download audio")

        logger.info("audio was downloaded successfully")

    def download_video(self, path):

        video = YouTube(self.url)
        video = video.streams.filter(file_extension='mp4').get_highest_resolution()

        try:
            video.download(path)

        except:
            logger.info("Failed to download video")

        logger.info("video was downloaded successfully")

    def get_transcript(self, return_lang='en'):

        video_id = YouTube(self.url).video_id
        transcript_lst = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])

        if return_lang not in ['en', 'fa']:
            raise YouTubeErorr('Availebe Languages ["en", "fa"]')

        elif return_lang == 'en':
            logger.info("Start Download English Transcript...")
            text = ' '.join([i['text'] for i in transcript_lst])
            return text

        elif return_lang == 'fa':
            dt_obj = GoogleTranslator(source='auto', target='fa')
            return [dt_obj.translate(text['text'])  for text in transcript_lst]

if __name__ == "__main__":
    yt_obj = YouTubeDownoader("https://www.youtube.com/watch?v=TR1GUDj9FFE")
    data = yt.get_transcript()
    print(data[:5])
