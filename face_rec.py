import face_recognition
import cv2

known_face_encodings = []
known_face_names = []

# capture function


def training_mode():

    # training mode

    print("\n Running Training mode \n")

    student_name = input("Enter student's name: ")
    std_name_img = student_name
    std_name_img.strip()
    std_name_img.replace(" ", "_")
    std_name_img = std_name_img + ".jpg"

    cam = cv2.VideoCapture(0)

    cv2.namedWindow("Capture " + student_name)

    while True:
        ret, frame = cam.read()
        cv2.imshow("Capture " + student_name, frame)
        if not ret:
            break
        k = cv2.waitKey(1)

        if k % 256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k % 256 == 32:
            # SPACE pressed
            cv2.imwrite(std_name_img, frame)
            print("{} saved!".format(std_name_img))

            # encode student info

            # Load a sample picture of yourself and learn how to recognize it.
            known_face_encodings.append(face_recognition.face_encodings(
                face_recognition.load_image_file(std_name_img))[0])
            known_face_names.append(student_name)

    cam.release()

    cv2.destroyAllWindows()


# detection mode

def detection_mode():

    print("\n Running Detection mode \n")

    # Get a reference to your webcam
    video_capture = cv2.VideoCapture(2)
    video_capture.set(3, 768)
    video_capture.set(4, 1024)

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
            face_encodings = face_recognition.face_encodings(
                rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(
                    known_face_encodings, face_encoding)
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
            cv2.rectangle(frame, (left, bottom - 35),
                          (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6),
                        font, 1.0, (255, 255, 255), 1)

        cv2.namedWindow("main", cv2.WINDOW_NORMAL)

        # Display the resulting image
        cv2.imshow('Video', frame)

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()


while True:

    choice = input(
        "\nPress \n\t1 to enter student for training mode \n\t2 run detection mode\n")

    if choice == '1':
        print("\ncapturing student data\n")

        # capturing student information
        training_mode()

    else:
        detection_mode()
