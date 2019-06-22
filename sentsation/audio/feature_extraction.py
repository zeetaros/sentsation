import librosa
import librosa.display
import matplotlib.pyplot as plt
from tqdm import tqdm
from glob import glob
from librosa.feature import chroma_stft
from sklearn.preprocessing import scale

class AudioFeature():
    def __init__(self):
        pass
    
    def _load(self, audiofilelist):
        y_list=[]
        sr_list=[]
        filenames=[]
        for af in audiofilelist:
            y, sr = librosa.load(af)
            y_list.append(y)
            sr_list.append(sr)
            filenames.append(str(af.split('/')[-1]))
        return zip(filenames, y_list, sr_list)

    def save_mfcc(self, audiofilelist, save_dir, hop_length=None, n_mfcc=None, use_scale=False):
        hop_length = hop_length or 256
        n_mfcc = n_mfcc or 13

        for filename, y, sr in tqdm(self._load(audiofilelist)):
            imagename = '.'.join(filename.split('.')[:-1] + ['jpg'])
            mfccs = librosa.feature.mfcc(y=y, sr=sr, hop_length=hop_length, n_mfcc=n_mfcc)
            if scale:
                mfccs = scale(mfccs, axis=1)
            plt.figure(figsize=(25.6, 25.6), dpi=10)
            librosa.display.specshow(mfccs)
            plt.tight_layout()
            plt.savefig('/'.join([save_dir, imagename]))