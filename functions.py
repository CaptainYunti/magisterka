import librosa
import numpy as np

def extract_features(y_segment, sr, n_mfcc=13):
    n_fft = min(2048, len(y_segment)//4)
    mfcc = librosa.feature.mfcc(y=y_segment, sr=sr, n_mfcc=13, n_fft=n_fft, hop_length = n_fft // 4)
    delta = librosa.feature.delta(mfcc) #pochodna
    delta2 = librosa.feature.delta(mfcc, order=2) # 2 pochodna

    chroma = librosa.feature.chroma_stft(y=y_segment, sr=sr, n_fft=n_fft, hop_length = n_fft // 4) # harmonia
    contrast = librosa.feature.spectral_contrast(y=y_segment, sr=sr, n_fft=n_fft, hop_length = n_fft // 4) # różnica między pasmami
    tonnetz = librosa.feature.tonnetz(y=y_segment, sr=sr, hop_length = n_fft // 4) # tonalność
    rms = librosa.feature.rms(y=y_segment, hop_length = n_fft // 4).mean() # głośność
    tempo = librosa.beat.tempo(y=y_segment, sr=sr, hop_length = n_fft // 4)[0] #tempo

    stats = lambda x: np.concatenate([x.mean(axis=1), x.std(axis=1), x.min(axis=1), x.max(axis=1)])

    features = np.concatenate([
        stats(mfcc),       # 13 x 4
        stats(delta),      # 13 x 4
        stats(delta2),     # 13 x 4
        stats(chroma),     # 12 x 2
        stats(contrast),   # 7 x 2
        tonnetz.mean(axis=1),  # 6
        [rms],
        [tempo],
    ])
    return features
