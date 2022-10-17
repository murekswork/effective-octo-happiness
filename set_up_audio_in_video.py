import os

import moviepy.editor as mpe
from moviepy.editor import *
from logging_part import LOGGER

def put_audio_in_video(file_name):
    video = mpe.VideoFileClip(f'video/{file_name}.mp4')
    audio = mpe.AudioFileClip(f'audio/{file_name}.mp3')
    LOGGER.warning('Set up files in moviepy class')
    # final_audio = mpe.CompositeAudioClip([video.audio, audio])
    final_video = video.without_audio()
    conc = final_video.set_audio(audio)

    text_clip = TextClip('prod. by mureks lab.', fontsize=35, color='red')
    text_clip = text_clip.set_position('top').set_duration(20)

    final_text_video = CompositeVideoClip([conc, text_clip])
    # conc.write_videofile(f'video_ready/{file_name}.mp4')
    final_text_video.write_videofile(f'video_ready/{file_name}.mp4')
    video.close()

    LOGGER.warning('D O N E')

def remove_files(file_name):
    os.remove(f'audio/{file_name}.mp3')
    os.remove(f'video/{file_name}.mp4')
    LOGGER.warning('Parent files were successfully removed')