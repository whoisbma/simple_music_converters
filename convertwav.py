import os
filepath = os.path.dirname(os.path.abspath(__file__))
onlyfiles = [f for f in os.listdir(filepath) if os.path.isfile(os.path.join(filepath, f))]

wavs = [file for file in onlyfiles if file != "convertwav.py" and ".wav" in file]
print wavs

from subprocess import call
for file in wavs:
	call(["ffmpeg", "-i", file, "-ab", "192k", "-map_metadata", "0", "-id3v2_version", "3", file + ".mp3"])
