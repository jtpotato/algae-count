import calculate_algae
import os
import time

print("WARNING: Reflections (particularly plant reflections) will count as algae. Prevent reflections from appearing in source image.")

def get_file_paths(directory):
    file_paths = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == ".DS_Store":
                continue
            file_paths.append(os.path.join(root, file))

    return file_paths

file_paths = get_file_paths("images")

with open("algae_index.csv", "w") as f:
    print("image,algae_index", file=f)

    for path in file_paths:
        calculate_algae.get_algae(path, f)
        time.sleep(1)