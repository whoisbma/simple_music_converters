import os
filepath = os.path.dirname(os.path.abspath(__file__))
onlyfiles = [f for f in os.listdir(filepath) if os.path.isfile(os.path.join(filepath, f))]

flacs = [file for file in onlyfiles if file != 'convertflac.py' and ".flac" in file]
print flacs

from subprocess import call
for file in flacs:
	call(["ffmpeg", "-i", file, "-ab", "192k", "-map_metadata", "0", "-id3v2_version", "3", file + ".mp3"])

