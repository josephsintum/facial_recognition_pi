import cv2
from time import sleep

while True:

    student_name = input("Enter student's name: ")

    if student_name == 'exit':
        break

    std_name = student_name.strip()
    std_name = student_name.replace(" ", "_")
    std_name_img = std_name + ".jpg"

    cam = cv2.VideoCapture(0)

    cv2.namedWindow("Capture " + student_name)

    img_counter = 0

    while True:
        ret, frame = cam.read()
        cv2.imshow("Capture " + student_name, frame)
        if not ret:
            break
        k = cv2.waitKey(1)

        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = std_name_img.format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} saved!".format(img_name))
            img_counter += 1

    cam.release()

    cv2.destroyAllWindows()