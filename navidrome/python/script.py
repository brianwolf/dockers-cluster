import sys
from pathlib import Path
import traceback

import music_tag


MUSIC_EXTENSIONS = ['mp3', 'flac', 'ogg', 'wav']

workindir = sys.argv[1]

print(f"Running script for path -> {workindir}")

paths = [
    str(p)
    for p in Path(workindir).rglob('*')
    if str(p).split('.')[-1].lower() in MUSIC_EXTENSIONS
]

for p in paths:

    try:
        music = music_tag.load_file(p)

        folders = p.split('/')[1:]

        music['title'] = folders[-1].split('.')[0]
        music['genre'] = folders[2]

        if len(folders) >= 2:
            music['album'] = folders[-2]

        if len(folders) >= 3:
            music['artist'] = folders[-3]

        music.save()

        print(f"- {p} - OK")

    except Exception as _:
        print(f"- {p} - ERROR")
        print(traceback.format_exc())
