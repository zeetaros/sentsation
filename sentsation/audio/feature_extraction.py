import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from glob import glob
from librosa.feature import chroma_stft
from sklearn.preprocessing import scale

class FeatureIllustrator():
    def __init__(self, sampling_rate=None):
        self.sampling_rate = sampling_rate or 44100
    
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

    def plot(self, audiofile, feature):
        y, sr = librosa.load(audiofile, sr=self.sampling_rate)
        if feature == 'mfcc':
            mfcc = librosa.feature.mfcc(y=y, sr=sr, hop_length=256, n_mfcc=20)
            if scale:
                mfcc = scale(mfcc, axis=1)
            plt.figure(figsize=(25.6, 25.6), dpi=10)
            librosa.display.specshow(mfcc)
            plt.tight_layout()
        
        elif feature == 'power':
            S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128, fmax=8000)
            plt.figure(figsize=(51.2, 25.6), dpi=10)
            librosa.display.specshow(librosa.power_to_db(S, ref=np.max), fmax=8000)
            plt.tight_layout()

    def save(self, audiofile, feature, save_dir):
        self.plot(audiofile, feature)
        filename = str(audiofile.split('/')[-1])
        imagename = '.'.join(filename.split('.')[:-1] + ['jpg'])
        plt.savefig('/'.join([save_dir, imagename]))

    # def plot_mfcc(self, audiofilelist, save_dir, hop_length=None, n_mfcc=None, use_scale=False):
    #     hop_length = hop_length or 256
    #     n_mfcc = n_mfcc or 13

    #     for filename, y, sr in self._load(audiofilelist):
    #         imagename = '.'.join(filename.split('.')[:-1] + ['jpg'])
    #         mfccs = librosa.feature.mfcc(y=y, sr=sr, hop_length=hop_length, n_mfcc=n_mfcc)
    #         if scale:
    #             mfccs = scale(mfccs, axis=1)
    #         plt.figure(figsize=(25.6, 25.6), dpi=10)
    #         librosa.display.specshow(mfccs)
    #         plt.tight_layout()
    #         plt.savefig('/'.join([save_dir, imagename]))

    # def plot_power(self, audiofilelist, save_dir, n_mels=None, fmax=None):
    #     n_mels = n_mels or 128
    #     fmax = fmax or 8000

    #     for filename, y, sr in self._load(audiofilelist):
    #         imagename = '.'.join(filename.split('.')[:-1] + ['jpg'])
    #         S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=n_mels, fmax=fmax)
    #         plt.figure(figsize=(51.2, 25.6), dpi=10)
    #         librosa.display.specshow(librosa.power_to_db(S, ref=np.max), fmax=fmax)
    #         plt.tight_layout()
    #         plt.savefig('/'.join([save_dir, imagename]))


class MFCCsExtractor():
    def __init__(self, sampling_rate):
        self.sampling_rate = sampling_rate or 44100

    def from_audiofiles(self, audiofilelist, hop_length=None, n_mfcc=None, use_scale=False, max_len=None):
        hop_length = hop_length or 256
        n_mfcc = n_mfcc or 25

        mfcc_list = []
        for af in audiofilelist:
            y, sr = librosa.load(af, sr=self.sampling_rate)
            mfcc = self.extract_mfcc(wave=y, sr=sr, n_mfcc=n_mfcc,
                                      hop_length=hop_length, max_len=max_len)
            if use_scale:
                mfcc = scale(mfcc, axis=1)
            mfcc_list.append(mfcc)
        return mfcc_list

    def extract_mfcc(self, wave, sr, n_mfcc, hop_length, max_len=None):
        mfcc = librosa.feature.mfcc(wave, sr=sr, n_mfcc=n_mfcc, hop_length=hop_length)

        # If maximum length exceeds mfcc lengths then pad the remaining ones
        if max_len:
            if (max_len > mfcc.shape[1]):
                pad_width = max_len - mfcc.shape[1]
                mfcc = np.pad(mfcc, pad_width=((0, 0), (0, pad_width)), mode='constant')
            else:
                mfcc = mfcc[:, :max_len]
        return mfcc
