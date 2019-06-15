import os
import click
import subprocess

def list_files(directory, extension=None):
    if extension:
        return [f for f in os.listdir(directory) if f.endswith('.' + extension)]
    else:
        return [f for f in os.listdir(directory)]

@click.command()
@click.argument('--input_dir', '-i', help='directory for input files')
@click.argument('--output_dir', '-o', help='directory to store outputs')
@click.option('--extension', '-e', help='only convert files with extension')
def video2audio(input_dir, output_dir, extension=None):
    ext = extension or "mp4"
    files = list_files(input_dir, ext)
    for f in files:
        command = "ffmpeg -i {0} -ab 160k -ac 2 -ar 44100 -vn {1}".format(input_dir + "/" + f,
                                                                          output_dir + "/" + f)
        subprocess.call(command, shell=True)

# if __name__ == '__main__':
#     video2audio()