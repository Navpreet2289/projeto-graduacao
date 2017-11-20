import cv2
import os

PATH = '../img/placas/fotos/'
ABS_PATH = os.path.abspath(PATH) + '\\'
WIDTH = 352
HEIGHT = 240
num = 0
total = 0

try:
    with open(ABS_PATH + 'converted\\' + 'info.txt', 'w') as out:
        out.close()

    with open(ABS_PATH + 'converted\\' + 'info-full.txt', 'w') as out:
        out.close()

    if not os.path.exists(ABS_PATH + 'converted'):
        os.makedirs(ABS_PATH + 'converted')
    if not os.path.exists(ABS_PATH + 'rois'):
        os.makedirs(ABS_PATH + 'rois')

    files = os.listdir(ABS_PATH)
    files.remove('converted')
    files.remove('rois')
    files.sort()

    total = len(files)

    # mouse callback function
    def mouse_watcher(event, x, y, flags, param):
        global x1, x2, y1, y2, mouse_position
        mouse_position = {'x': x, 'y': y}

        if event == cv2.EVENT_LBUTTONDOWN:
            x1, y1 = x, y

        if event == cv2.EVENT_LBUTTONUP:
            x2, y2 = x, y

    # redimensiona a imagem
    def resize(img, width, height):
        '''Reduz o tamanho da imagem para o tamanho desejado'''
        h, w = img.shape[:2]  # Pega o tamanho atual
        pw = width / (w * 1.0)  # Porcentagem width
        ph = height / (h * 1.0)  # Porcentagem heigth
        p = min(pw, ph)  # Pega a menor porcentagem para fazer a reducao
        return cv2.resize(img, (int(w * p), int(h * p)), interpolation=cv2.INTER_AREA)

    for f in files:
        roi_num = 0
        num += 1
        print 'Marking: ' + str(num) + '/' + str(total) + '.'
        rects = []
        images = []
        mouse_position = None
        x1 = x2 = y1 = y2 = None

        image = cv2.imread(ABS_PATH + f)
        shape = image.shape[:2]
        if shape[0] > WIDTH or shape[1] > HEIGHT:
            image = resize(image, WIDTH, HEIGHT)

        cv2.imshow(f, image)
        cv2.setMouseCallback(f, mouse_watcher)

        if shape[0] < 352:
            cv2.resizeWindow(f, 352, shape[1])

        images.append(image)

        while True:
            if (x2 and y2) is not None:
                xi = min(x1, x2)
                yi = min(y1, y2)
                xf = max(x1, x2)
                yf = max(y1, y2)

                image = images[len(rects)].copy()  # exibe a imagem atual
                cv2.rectangle(image, (xi, yi), (xf, yf), (0, 255, 0), 1)  # desenha na imagem atual

                print 'Save rectangle? (y/n)'
                while True:
                    key = cv2.waitKey(1) & 0xFF
                    if key == ord('y'):
                        rects.append([{'xi': xi, 'yi': yi, 'xf': xf, 'yf': yf}])  # salva coordenadas
                        images.append(image)  # salva imagem com o novo retangulo
                        print 'Saved rectangle.'
                        x1 = x2 = y1 = y2 = None
                        break
                    elif key == ord('n'):
                        x1 = x2 = y1 = y2 = None  # descarta o retangulo
                        print 'Discarded rectangle.'
                        break

            elif (x1 and y1) is not None:
                xi = min(mouse_position['x'], x1)
                yi = min(mouse_position['y'], y1)
                xf = max(mouse_position['x'], x1)
                yf = max(mouse_position['y'], y1)
                image = images[len(rects)].copy()
                cv2.rectangle(image, (xi, yi), (xf, yf), (0, 255, 0), 1)

            else:
                image = images[len(rects)].copy()

            cv2.imshow(f, image)

            key = cv2.waitKey(1) & 0xFF

            if key == ord('c'):
                print 'Clearing saved rectangles...'
                rects = []
                while len(images) != 1:
                    images.pop(1)
                print 'Cleared.'

            if key == ord('n'):
                print 'Next...'
                cv2.destroyAllWindows()
                break

            elif key == ord('s'):
                print 'Saving...'
                image_gray = cv2.cvtColor(images[0], cv2.COLOR_BGR2GRAY)
                gray_f = f.split('.')[0] + '-gray' + '.png'
                cv2.imwrite(ABS_PATH + 'converted\\' + gray_f, image_gray)
                for r in rects:
                    roi_num += 1
                    for d in r:
                        roi = image_gray[d['yi']:d['yf'], d['xi']:d['xf']]
                        roi_gray_f = f.split('.')[0] + '-gray-roi-' + str(roi_num) + '.png'
                        cv2.imwrite(ABS_PATH + 'converted\\' + roi_gray_f, roi)
                # short path description
                with open(ABS_PATH + 'converted\\' + 'info.txt', 'a') as out:
                    line = gray_f + ' ' + str(len(rects)) + ' '
                    for r in rects:
                        for d in r:
                            w = d['xf'] - d['xi']
                            h = d['yf'] - d['yi']
                            line += str(d['xi']) + ' ' + str(d['yi']) + ' ' + str(w) + ' ' + str(h) + ' '
                    out.write(line + '\n')
                    out.close()
                # full path description
                with open(ABS_PATH + 'converted\\' + 'info-full.txt', 'a') as out:
                    line = ABS_PATH + 'converted\\' + gray_f + ' ' + str(len(rects)) + ' '
                    for r in rects:
                        for d in r:
                            w = d['xf'] - d['xi']
                            h = d['yf'] - d['yi']
                            line += str(d['xi']) + ' ' + str(d['yi']) + ' ' + str(w) + ' ' + str(h) + ' '
                    out.write(line + '\n')
                    out.close()
                print 'Saved.'
                cv2.destroyAllWindows()
                break

            elif key == ord('q'):
                cv2.destroyAllWindows()
                print 'Exiting...'
                exit('exit ' + str(ord('q')))

    print 'End.'
    raw_input('Press any key to continue...')

except Exception as e:
    print str(e)
    cv2.destroyAllWindows()
    raw_input('Press any key to continue...')
