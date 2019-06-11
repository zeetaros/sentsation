import click
import subprocess

# TODO:write a function to accept a directory, loop through files in that directory

def video2audio():

    command = "ffmpeg -i C:/test.mp4 -ab 160k -ac 2 -ar 44100 -vn audio.wav"

    subprocess.call(command, shell=True)