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

    print(f"- {p}")

    try:
        music = music_tag.load_file(p)

        music['title'] = p.split('/')[-1].split('.')[0]
        music['album'] = p.split('/')[-2]
        music['artist'] = p.split('/')[-3]
        # music['genre'] = p.split('/')[-4]

        music.save()

    except Exception as _:
        print(traceback.format_exc())
