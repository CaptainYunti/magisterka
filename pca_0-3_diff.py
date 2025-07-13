import librosa
import numpy as np
import matplotlib.pyplot as plt
import capymoa.drift.detectors as detectors
import paths_drifts
import os
from sklearn.decomposition import PCA
import functions
from sklearn.preprocessing import StandardScaler

# filename = librosa.example("nutcracker")
#changes = [7,49,69,90,110,150,171,191,221]
#audio_path = "./music/BackInBlack.mp3"

album = paths_drifts.album


n_mfcc = 13

for song in album:

    y, sr = librosa.load(song["path"], sr=None)

    duration = librosa.get_duration(y=y, sr=sr)

    print(f"Track length: {duration:.2f} s = {int(duration//60)}.{int(duration%60)} min")

    all_frames_lengths = [4, 3, 2.5, 2, 1.5, 1, 0.5]

    for frame_length in all_frames_lengths:

        frame_samples = int(frame_length * sr)
        num_frames = len(y) // frame_samples

        print(f"Number of frames: {num_frames}")

        mfcc_features = []

        for i in range(num_frames):
            start = i * frame_samples
            end = start + frame_samples
            frame = y[start:end]

            mfcc = functions.extract_features(y_segment=frame, sr=sr, n_mfcc=n_mfcc)
            mfcc_features.append(mfcc)
            

        mfcc_features = np.array(mfcc_features)

        pca = PCA(n_components=4)
        scaler = StandardScaler()
        diff = np.diff(pca.fit_transform(scaler.fit_transform(mfcc_features)), axis=0)
        pca_mfcc_signal = np.linalg.norm(diff, axis=1)

        # all_detectors = [detectors.ADWIN, detectors.STEPD, detectors.HDDMAverage]
        all_detectors = [detectors.DDM]


        for detector in all_detectors:

            detector_name = detector.__name__

            detector = detector()

            change_points = []

            for i, x in enumerate(pca_mfcc_signal):
                detector.add_element(x)

                if detector.detected_change():
                    change_points.append(i)


            time_axis = np.arange(len(pca_mfcc_signal)) * frame_length
            # feature_vals = [vec.mean() for vec in mfcc_features]

            plt.figure(figsize=(12,5))
            plt.plot(time_axis, pca_mfcc_signal, label=f"Różnicowanie, PCA 0-3")

            for cp in change_points:
                # plt.axvline(cp * frame_length, color="red", linestyle="--", label="Dryf" if cp==change_points[0] else "")
                plt.axvline(cp * frame_length, color="red", linestyle="--", label="Wykryty dryf" if cp == change_points[0] else "")
            for indx, t in enumerate(song["drift"][0]):
                    plt.axvline(t, color = "green", linestyle="--", label="Zmiana" if indx == 0 else "")
                    ymin, ymax = plt.ylim()
                    plt.text(t + .1, ymin + 10, song["drift"][1][indx],rotation=90, color="green")
            plt.xlabel("Czas [s]")
            plt.ylabel("Diff, PCA 0-3")
            plt.title(f"Wykrywanie segmentów utworu {song["title"]}, okno: {frame_length} s, {detector_name}")
            plt.legend()
            plt.grid()
            directory = f"./plots/mfcc_pca_normalized_0-3_diff/{detector_name}/{frame_length}/"
            if not os.path.isdir(directory):
                 os.makedirs(directory)
            plt.savefig(f"{directory}/{song["title"]}_mfcc_pca_0-3_diff_{detector_name}_{frame_length}.png")





