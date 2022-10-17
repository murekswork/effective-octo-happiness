import time

from get_subtitle import subtitle_begin

from audio_part import get_audio, get_video, get_length_difference, change_audio_speed

from set_up_audio_in_video import put_audio_in_video, remove_files


def main():
    subtitle_text, language, file_name, url = subtitle_begin()
    get_audio(subtitle_text, file_name, language)

    get_video(url, file_name)

    speed = get_length_difference(file_name)

    change_audio_speed(file_name=file_name, speed=speed)

    put_audio_in_video(file_name)

    remove_files(file_name)
    return f'video_ready/{file_name}.mp4'


if __name__ == '__main__':
    main()