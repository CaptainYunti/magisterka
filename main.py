import librosa
import numpy as np
import matplotlib.pyplot as plt
import capymoa.drift.detectors as detectors


# filename = librosa.example("nutcracker")

changes = [7,49,69,90,110,150,171,191,221]

audio_path = "./music/BackInBlack.mp3"
frame_length = .05

y, sr = librosa.load(audio_path, sr=None)

duration = librosa.get_duration(y=y, sr=sr)

print(f"Track length: {duration:.2f} s = {int(duration//60)}.{int(duration%60)} min")

frame_samples = int(frame_length * sr)
num_frames = len(y) // frame_samples

print(f"Number of frames: {num_frames}")

mfcc_features = []

for i in range(num_frames):
    start = i * frame_samples
    end = start + frame_samples
    frame = y[start:end]

    mfcc = librosa.feature.mfcc(y=frame, sr=sr, n_mfcc=13)
    mfcc_mean = mfcc.mean(axis=1)
    mfcc_var = mfcc.var(axis=1)
    mfcc_features.append(mfcc_mean)
    # mfcc_features.append(mfcc_var)

mfcc_features = np.array(mfcc_features)

detector = detectors.ADWIN()

change_points = []

for i, vec in enumerate(mfcc_features):
    val = vec.mean()
    detector.add_element(val)

    if detector.detected_change():
        change_points.append(i)


time_axis = np.arange(len(mfcc_features)) * frame_length
feature_vals = [vec.mean() for vec in mfcc_features]

plt.figure(figsize=(12,5))
plt.plot(time_axis, feature_vals, label="Średnie MFCC")

for cp in change_points:
    # plt.axvline(cp * frame_length, color="red", linestyle="--", label="Dryf" if cp==change_points[0] else "")
    plt.axvline(cp * frame_length, color="red", linestyle="--", label="Wykryty dryf" if cp == change_points[0] else "")
for c in changes:
        plt.axvline(c, color = "green", linestyle="--", label="Zmiana" if c == changes[0] else "")
plt.xlabel("Czas [s]")
plt.ylabel("Średnia MFCC")
plt.title(f"Wykrywanie segmentów utworu - okno: {frame_length} s")
plt.legend()
plt.grid()
plt.show()





