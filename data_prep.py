import librosa
import torch
import numpy as np
import paths_drifts
from torch.utils.data import Dataset, DataLoader
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import os
import capymoa.drift.detectors as detectors

drift_dict = {
    0: "other",
    1: "verse",
    2: "chorus",
    3: "vocal - other"
}

album = paths_drifts.album_short

frame_length = 1 #seconds
percent_to_drift = 0.9

songs_mfcc = []

for song in album:

    y, sr = librosa.load(song["path"], sr=None)
    print(f"sr= {sr}")

    duration = librosa.get_duration(y=y, sr=sr)

    # print(f"Track length: {duration:.2f} s = {int(duration//60)}.{int(duration%60)} min")

    frame_samples = int(frame_length * sr)
    num_frames = len(y) // frame_samples

    # print(f"Number of frames: {num_frames}")

    mfcc = []

    j = 1

    for i in range(num_frames):
        start = i * frame_samples
        end = start + frame_samples
        frame = y[start:end]

        if(j < len(song["drift"][1])):
            if (i+1) * frame_length >= song["drift"][0][j]:
                j = j+1
        
        part_class = song["drift"][1][j-1]

        x_mat = librosa.feature.mfcc(y=frame, sr=sr, n_mfcc=13)
        
        for k in range(x_mat.shape[1]):
            mfcc.append((tuple(x_mat[:,k]), part_class))

    songs_mfcc.append(mfcc)


class FrameDataset(Dataset):
    def __init__(self, X, y):
        self.X = torch.tensor(X, dtype=torch.float32)
        self.y = torch.tensor(y, dtype=torch.long)

    def __len__(self):
        return len(self.X)
    
    def __getitem__(self, index):
        return self.X[index], self.y[index]


def get_data(test_song_id, normalize = False):

    scaler = StandardScaler()

    train_data = [song for indx, song in enumerate(songs_mfcc) if indx != test_song_id]
    test_data = songs_mfcc[test_song_id]

    train_flat = [pair for song in train_data for pair in song]
    X_train = np.array([x for x, _ in train_flat])
    Y_train = np.array([y for _, y in train_flat])

    X_test = np.array([x for x, _ in test_data])
    Y_test = np.array([y for _, y in test_data])

    train_ds = FrameDataset(X_train, Y_train)
    test_ds = FrameDataset(X_test, Y_test)

    if normalize:
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.fit_transform(X_test)

    return train_ds, test_ds


def data_visualization(song_number: int, predictions: list, detector: str):
    y, sr = librosa.load(album[song_number]["path"], sr=None)
    duration = librosa.get_duration(y=y, sr=sr)
    drift_detector = detectors.ADWIN()
    drift_detector_name = detectors.ADWIN.__name__

    frame_samples = int(frame_length * sr)
    num_frames = len(y) // frame_samples

    mfcc_features = []

    for i in range(num_frames):
        start = i * frame_samples
        end = start + frame_samples
        frame = y[start:end]

        mfcc = librosa.feature.mfcc(y=frame, sr=sr, n_mfcc=13)
        mfcc_features.append(mfcc.mean(axis=1))
            

    mfcc_features = np.array(mfcc_features)

    time_axis = np.arange(len(mfcc_features)) * frame_length
    feature_vals = [x.mean() for x in mfcc_features]

    change_points = []

    window = []
    max_window_length = 10
    window_length = 0
    for indx, frame in enumerate(np.array_split(predictions, num_frames)):
        frame = frame.tolist()
        window += frame
        window_length = window_length + 1
        if (max(window.count(0), window.count(1), window.count(2), window.count(3)) / len(window)) < percent_to_drift:
            change_points.append(indx)
            window = []
            window_length = 0
        else:
            if window_length == max_window_length:
                window = window[len(window)//max_window_length:]
                window_length = max_window_length-1



    # for indx, frame in enumerate(np.array_split(predictions, num_frames)):
    #     frame = frame.tolist()
    #     for element in frame:
    #         drift_detector.add_element(element)

    #     if drift_detector.detected_change():
    #         change_points.append(i)


    plt.figure(figsize=(12,5))
    plt.plot(time_axis, feature_vals, label=f"Śrenia MFCC")


    for cp in change_points:
        plt.axvline(cp * frame_length, color="red", linestyle="--", label="Wykryty dryf" if cp == change_points[0] else "")
    for indx, t in enumerate(song["drift"][0]):
        plt.axvline(t, color = "green", linestyle="--", label="Zmiana" if indx == 0 else "")
        ymin, ymax = plt.ylim()
        plt.text(t + .1, ymin + 10, drift_dict[song["drift"][1][indx]],rotation=90, color="green")
    plt.xlabel("Czas [s]")
    plt.ylabel("Średnia MFCC")
    # plt.title(f"Wykrywanie segmentów utworu {song["title"]}, okno: {frame_length} s, MLP: {detector}, detector: {drift_detector_name}")
    plt.title(f"Wykrywanie segmentów utworu {song["title"]}, okno: {frame_length} s, MLP: {detector}")
    plt.legend()
    plt.grid()
    directory = f"./plots/MLP/{detector}/"
    if not os.path.isdir(directory):
        os.makedirs(directory)
    plt.savefig(f"{directory}/{album[song_number]["title"]}_MLP_{detector}.png")