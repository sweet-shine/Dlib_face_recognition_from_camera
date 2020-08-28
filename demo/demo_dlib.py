# coding=utf-8
# auther:wangc
# 2020-08-27
import dlib, cv2

detector = dlib.get_frontal_face_detector()

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, img = cap.read()

    faces = detector(img, 1)
    print(faces, len(faces))
    if len(faces)>1:
        print(faces[0],faces[1])
    for k, d in enumerate(faces):
        pos_start = tuple([d.left(), d.top()])
        pos_end = tuple([d.right(), d.bottom()])
        height = d.bottom() - d.top()
        width = d.right() - d.left()
        cv2.rectangle(img, pos_start, pos_end, (0, 255, 0), 2)
        # print(k, d)
        # print(d.left())
    # cv2.namedWindow('camera',0)
    cv2.imshow("camera", img)
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
