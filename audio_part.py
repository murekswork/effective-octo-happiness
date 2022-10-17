import os

from gtts import gTTS
from mutagen.mp3 import MP3
from mutagen.mp4 import MP4
from pytube import YouTube

from pydub import AudioSegment


from logging_part import LOGGER


def get_audio(text, file_name, language):
    audio = gTTS(text=text, lang=language)
    audio.save(f'audio/{file_name}.mp3')

    LOGGER.warning(f'Voiced in {language} text file was saved in audio/{file_name}.mp3')
    return file_name, language


def get_video(url, file_name):

    try:
        yt = YouTube(url)
        video = yt.streams.get_lowest_resolution()
        video.download(output_path='video', filename=f'{file_name}.mp4')
        LOGGER.warning(f'Video file was successfully downloaded as video/{file_name}.mp4')
    except:
        LOGGER.warning('Could not download video from YouTube. Check connection.')
        return file_name


def get_length_difference(file_name):
    audio = MP3(f'audio/{file_name}.mp3')
    audio_length = audio.info.length

    video = MP4(f'video/{file_name}.mp4')
    video_length = video.info.length
    print(video_length, audio_length)
    diff = audio_length / video_length
    # if video_length > audio_length:
    #     diff = (video_length - audio_length) / audio_length
    # else:
    #     diff = (audio_length - video_length) / video_length
    return diff


def change_audio_speed(file_name, speed):
    LOGGER.warning('Started to change audio speed')

    file_path = f'audio/{file_name}.mp3'
    audio = AudioSegment.from_mp3(file_path)

    LOGGER.warning('Starting to change audio file frame rate...')

    LOGGER.warning(f'FRAME RATE: {audio.frame_rate} - {audio.frame_rate * speed * 1.45}')
    audio_with_changed_frame_rate = audio._spawn(audio.raw_data, overrides={
        "frame_rate": int(audio.frame_rate * speed)
            # int(audio.frame_rate - ((audio.frame_rate * speed) * 1.45))
    })
    audio_with_changed_frame_rate.set_frame_rate(audio.frame_rate)
    # os.remove(f'audio/{file_name}.mp3')
    audio_with_changed_frame_rate.export(f'audio/{file_name}.mp3', format='mp3')
    LOGGER.warning('Deleted parent audio and paste edited')