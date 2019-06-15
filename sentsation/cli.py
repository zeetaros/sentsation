import click
from .preprocess.audio import video2audio

@click.command()
@click.argument('--input_dir', '-i', help='directory for input files')
@click.argument('--output_dir', '-o', help='directory to store outputs')
@click.option('--extension', '-e', help='only convert files with extension')
def convert(input_dir, output_dir, extension=None):
    video2audio(input_dir, output_dir, extension)


# if __name__ == '__main__':
#     convert()