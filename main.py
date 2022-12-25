import pyperclip
import pytube

url = pyperclip.paste()
if 'youtu' not in url:
    raise Exception("Wrong URL copied")

video = pytube.YouTube('https://www.youtube.com/watch?v=N8TY13ELB-g')
video. \
    streams. \
    filter(progressive=True, file_extension="mp4"). \
    first(). \
    download(output_path=r"C:\Users\ksurowka\Downloads")
