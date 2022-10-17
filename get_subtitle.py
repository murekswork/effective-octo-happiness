import random
from logging_part import LOGGER
from youtube_transcript_api import YouTubeTranscriptApi
from gtts import gTTS

from audio_part import get_audio


def check_url(url) -> dict:
    if 'https://www.youtube.' in url:
        return {'success': True}
    else:
        return {'success': False, 'text': 'Invalid url address'}


def check_generated_languages(url) -> str:
    language = ['ru', 'en', 'by', 'ua', 'de', 'fr']
    av_language = []
    for i in language:
        try:
            YouTubeTranscriptApi.get_transcript(url, languages=[i])
            av_language.append(i)
        except:
            pass
    LOGGER.warning(f'Parent language is {av_language}')
    return av_language[0]


def extract_subtitle_text(url):
    text = ''
    video_id = url.split('=')[1].split('&')[0]
    yt = YouTubeTranscriptApi.list_transcripts(video_id)

    parent_language = check_generated_languages(video_id)
    yt_s = yt.find_generated_transcript(language_codes=[f'{parent_language}'])
    translate_language = input('What language you want translate to: ')
    subtitle_dict = yt_s.translate(translate_language).fetch()

    for _ in subtitle_dict:
        text += _['text']

    return text, translate_language


def subtitle_begin():
    video_url = input('Enter video URL address: ')
    url_validation = check_url(video_url)

    if url_validation['success'] is False:
        LOGGER.warning('URL address is invalid!')
        return False

    file_name = f'{random.randint(1, 1000)}'
    LOGGER.warning(f'URL address is valid, file name: {file_name}')

    subtitle_text, language = extract_subtitle_text(video_url)
    LOGGER.warning('Extract subtitle part is done, starting work with audio part!')

    return subtitle_text, language, file_name, video_url
