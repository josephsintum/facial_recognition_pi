import face_recognition
import cv2

print("\n Running Training mode \n")

# Get a reference to your webcam 
video_capture = cv2.VideoCapture(0)

# training mode

print("Encoding FOO")

# Load a sample picture of yourself and learn how to recognize it.
foo_image = face_recognition.load_image_file("foo.jpg")
foo_face_encoding = face_recognition.face_encodings(foo_image)[0]


print("Encoding ARYAN")

# Load a sample picture of yourself and learn how to recognize it.
aryan_image = face_recognition.load_image_file("aryan.jpeg")
aryan_face_encoding = face_recognition.face_encodings(aryan_image)[0]

print("Encoding BAR")

# Load a second sample picture and learn how to recognize it.
bar_image = face_recognition.load_image_file("bar.jpg")
bar_face_encoding = face_recognition.face_encodings(bar_image)[0]

print("Encoding GANESH")

# Load a second sample picture and learn how to recognize it.
ganesh_image = face_recognition.load_image_file("ganesh.jpeg")
ganesh_face_encoding = face_recognition.face_encodings(ganesh_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    foo_face_encoding,
    aryan_face_encoding,
    bar_face_encoding,
    ganesh_face_encoding
]
known_face_names = [
    "Bill Gates",
    "Aryan",
    "Elon Musk",
    "Ganesh"
]

# detection mode
print("\n Running Detection mode \n")

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # Grab a frame of the video
    ret, frame = video_capture.read()

    # Resize frame of video to smaller size for faster  processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # If a match was found in known_face_encodings, just use the first one.
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
