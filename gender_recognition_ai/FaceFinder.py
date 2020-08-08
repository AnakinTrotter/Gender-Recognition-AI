import face_recognition as fr
import os
import PIL

pics_folder = os.path.join("..", "data", "wiki")
tolerance = 0.6
frame_thickness = 3
font_thickness = 2


# Navigates to the pictures folder then returns a list of all the face landmark data
# The number of faces returned is not more than max_photos in most conditions
# A value of -1, the default value, for max_photos gets faces from all the photos
def get_facial_features(max_photos=-1):
    faces = []
    # Iterates the folders 00 to 99 in the wiki directory
    for directory in os.listdir(pics_folder):
        numbered = os.path.join(pics_folder, directory)
        num_dirs = os.listdir(numbered)
        # Iterates through all the jpg files in each numbered directory
        for a in num_dirs:
            if -1 < max_photos <= len(faces):
                return faces
            image_path = os.path.join(numbered, a)
            # Tries to load an image from the image_path
            try:
                image = fr.load_image_file(image_path)
                facial_features = fr.face_landmarks(image)
                faces.append(facial_features)
            except PIL.UnidentifiedImageError as e:
                # If the image_path turns out to be invalid, closes the program
                # If the image_path points to a .mat or .md file, just skip over it
                if "mat" and "md" not in str(image_path).split("."):
                    print(e)
                    exit("Unidentified Image Format")
    return faces
