import cv2

movie = cv2.VideoCapture('../vid/02-10-17/001_M_02102017150000.dav')

while movie.isOpened():
    _, frame = movie.read()

    cv2.imshow('movie', frame)

    print frame.shape

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

movie.release()
cv2.destroyAllWindows()
