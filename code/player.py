import cv2
import os

path = '../vid/02-10-17/'
path_g = path + 'good-vid/'
path_b = path + 'bad-vid/'

files = os.listdir(path)
files.sort()

files_good = os.listdir(path_g)
files_good.sort()

files_bad = os.listdir(path_b)
files_bad.sort()

if len(files_good) > 0:
    ng = files_good.pop().split('-')[1].split('.')[0]
else:
    ng = 1

if len(files_bad) > 0:
    nb = files_bad.pop().split('-')[1].split('.')[0]
else:
    nb = 1

with open(path_g + 'controle-good.txt', 'a') as txt_good:
    with open(path_b + 'controle-bad.txt', 'a') as txt_bad:
        for f in files:
            full_path = path + f
            vid_cap = cv2.VideoCapture(full_path)
            print 'playing: ' + f

            try:
                while vid_cap.isOpened():
                    _, frame = vid_cap.read()
                    cv2.imshow('video', frame)

                    key = cv2.waitKey(1) & 0xFF

                    if key == ord('g'):
                        cv2.imwrite(path + '/good-vid/pic-' + str(ng) + '.jpg', frame)
                        txt_good.write(f + ' - ' + str(ng) + '.jpg\n')
                        ng += 1

                    elif key == ord('b'):
                        cv2.imwrite(path + '/bad-vid/pic-' + str(nb) + '.jpg', frame)
                        txt_bad.write(f + ' - ' + str(nb) + '.jpg\n')
                        nb += 1

                    elif key == ord('n'):
                        break

                    elif key == ord('p'):
                        raw_input('Press any key to continue...')

                    elif key == ord('q'):
                        vid_cap.release()
                        cv2.destroyAllWindows()
                        exit('exit ' + str(ord('q')))

            except Exception as e:
                print str(e)
                continue


vid_cap.release()
cv2.destroyAllWindows()
