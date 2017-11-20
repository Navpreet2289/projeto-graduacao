import cv2
import os

try:
    PLATE_WIDTH = 44
    PLATE_HEIGHT = 20
    PERCENTAGE = 20  # 20%
    HIGHER_PERCENTAGE = 1 + 0.01 * PERCENTAGE
    LOWER_PERCENTAGE = 1 - 0.01 * PERCENTAGE

    MAX_WIDTH_ACCEPTED = int(PLATE_WIDTH * HIGHER_PERCENTAGE)
    MIN_WIDTH_ACCEPTED = int(PLATE_WIDTH * LOWER_PERCENTAGE)
    MAX_HEIGHT_ACCEPTED = int(PLATE_HEIGHT * HIGHER_PERCENTAGE)
    MIN_HEIGHT_ACCEPTED = int(PLATE_HEIGHT * LOWER_PERCENTAGE)

    img_detected_num = 1

    path = '../vid/02-10-17/'
    path_g = '../img/good-vid/'
    path_b = '../img/bad-vid/'
    # path_cascade = '../haar-cascade-1/plate-cascade-12-stages.xml'
    # path_cascade = '../haar-cascade-2/plate-cascade-16-stages.xml'
    # path_cascade = '../haar-cascade-3/haarcascade_licence_plate_rus_16stages.xml'
    path_cascade = '../haar-cascade-9/plate-cascade-19-stages-5k-pos-2.5k-neg.xml'

    plate_cascade = cv2.CascadeClassifier(path_cascade)

    files = os.listdir(path)
    files.sort()

    files_good = os.listdir(path_g)
    files_good.sort()

    files_bad = os.listdir(path_b)
    files_bad.sort()

    if len(files_good) > 1:
        ng = int(files_good.pop().split('-')[1].split('.')[0])
    else:
        ng = 1

    if len(files_bad) > 1:
        nb = int(files_bad.pop().split('-')[1].split('.')[0])
    else:
        nb = 1

    # cv2.namedWindow('detected')
    # cv2.resizeWindow('detected', 352, 240)

    for f in files:
        full_path = path + f
        vid_cap = cv2.VideoCapture(full_path)
        print 'playing: ' + f
        actual_roi = past_roi = None

        try:
            while vid_cap.isOpened():
                _, frame = vid_cap.read()
                roi = frame[140:240, 0:200]
                gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
                # actual_roi = gray_roi
                # if past_roi is not None:
                #     mask = cv2.bitwise_xor(past_roi, actual_roi)
                #     eroded = cv2.erode(mask, (1, 1), iterations=1)
                #     past_roi = actual_roi
                #     applied_roi = cv2.bitwise_and(gray_roi, mask)
                #     copy1 = applied_roi.copy()
                #     _, contours1, _ = cv2.findContours(copy1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                #     for cnt in contours1:
                #         x, y, w, h = cv2.boundingRect(cnt)
                #         cv2.imwrite(
                #                         'C:\Users\Alexandre-Asus\Documents\projeto-graduacao\img\dectected-plates\\' + 'detected_' + str(
                #                             img_detected_num) + '.jpg',
                #                         frame)
                #         img_detected_num += 1
                # else:
                #     eroded = mask = applied_roi = past_roi = actual_roi
                # # equalized_roi = cv2.equalizeHist(gray_roi)
                # # denoised_roi = cv2.fastNlMeansDenoising(equalized_roi)

                # Area of detection
                cv2.rectangle(frame, (0, 140), (0 + 200, 140 + 100), (0, 0, 255), 2)

                detected_plates = plate_cascade.detectMultiScale(image=gray_roi,
                                                                 scaleFactor=1.3,
                                                                 minNeighbors=4,
                                                                 minSize=(40, 20),
                                                                 maxSize=(48, 24)
                                                                 )

                for (x, y, w, h) in detected_plates:
                    # detected = denoised_roi[y:y + h, x:x + w]
                    # detected = gray_roi[y:y + h, x:x + w]
                    # equalized = cv2.equalizeHist(detected)
                    # denoised = cv2.fastNlMeansDenoising(equalized)
                    # _, placa_th1 = cv2.threshold(detected, 145, 255, cv2.THRESH_BINARY)
                    # _, placa_th2 = cv2.threshold(detected, 156, 255, cv2.THRESH_BINARY_INV)
                    #
                    # copy1 = placa_th1.copy()
                    # copy2 = placa_th2.copy()
                    #
                    # _, contours1, _ = cv2.findContours(copy1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                    # _, contours2, _ = cv2.findContours(copy2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

                    cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 1)

                    # if (MAX_WIDTH_ACCEPTED > w > MIN_WIDTH_ACCEPTED) and (
                    #                 MAX_HEIGHT_ACCEPTED > h > MIN_HEIGHT_ACCEPTED):
                    #     cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 1)

                    # for cnt in contours1:
                    #     x, y, w, h = cv2.boundingRect(cnt)
                    #     if (MAX_WIDTH_ACCEPTED > w > MIN_WIDTH_ACCEPTED) and (
                    #                     MAX_HEIGHT_ACCEPTED > h > MIN_HEIGHT_ACCEPTED):
                    #         cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 1)
                            # cv2.imwrite(
                            #     'C:\Users\Alexandre-Asus\Documents\projeto-graduacao\img\dectected-plates\\' + 'detected_' + str(
                            #         img_detected_num) + '.jpg',
                            #     placa_th1)
                            # img_detected_num += 1

                cv2.imshow('video', frame)

                key = cv2.waitKey(1) & 0xFF

                if key == ord('n'):
                    break

                elif key == ord('p'):
                    raw_input('Press any key to continue...\n')
                    print 'Continuing...\n'

                elif key == ord('q'):
                    vid_cap.release()
                    cv2.destroyAllWindows()
                    exit('exit ' + str(ord('q')))

        except Exception as e:
            print str(e)
            continue

    vid_cap.release()
    cv2.destroyAllWindows()

except Exception as e:
    print str(e)
