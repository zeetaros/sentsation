import os
import csv
import click
import subprocess
from tqdm import tqdm

def list_files(directory, extension=None):
    if extension:
        return [f for f in os.listdir(directory) if f.endswith('.' + extension)]
    else:
        return [f for f in os.listdir(directory)]

def video2audio(input_dir, output_dir, extension=None):
    ext = extension or "mp4"
    files = list_files(input_dir, ext)
    failed_log = []
    for f in tqdm(files):
        new_filename = '.'.join(f.split('.')[:-1] + ['wav'])
        try:
            command = "ffmpeg -i {0} -ab 160k -ac 2 -ar 44100 -vn {1}".format(os.path.join(input_dir,f),
                                                                        os.path.join(output_dir,new_filename))
            subprocess.call(command, shell=True)
        except:
            failed_log.append(f)
    if failed_log:
        with open(os.path.join(output_dir, "files_failed.csv"),'wb') as log:
            wr = csv.writer(log, dialect='excel')
            wr.writerow(failed_log)