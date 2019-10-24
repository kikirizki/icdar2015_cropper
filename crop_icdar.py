import os
import cv2


class IcdarCropper():
    def __init__(self, years, image_source_path, label_source_path, image_dest_path, label_dest_path):
        img_names = os.listdir(image_source_path)
        self.images_path = [os.path.join(image_source_path, img) for img in img_names]
        self.labels_path = [os.path.join(label_source_path, img.replace("jpg", "txt")) for img in img_names]
        self.years = years
        self.image_dest_path = image_dest_path
        self.label_dest_path = label_dest_path

    def _string2rect(self, line):
        line = line.split(',')
        poly = [int(float(p)) for p in line[:4]]

        name = line[-1].replace("\n", "")
        return poly, name

    def _string2polygon(self, line):
        line = line.split(',')
        poly = [int(float(p)) for p in line[:8]]
        poly = [(poly[i], poly[i + 1]) for i in range(0, 8, 2)]
        name = line[-1].replace("\n", "")
        return poly, name

    def _label2polygon(self, labels_path):
        polygon = []
        f = open(labels_path)
        lines = f.readlines()
        for line in lines:
            if self.years == '2015':
                poly = self._string2rect(line)
            else:
                print("Error : does not support other than 2015")
                exit(0)
                poly = self._string2polygon(line)
            polygon.append(poly)
        f.close()
        return polygon

    def _crop_icdar(self, img_path, labels_path):
        [(poly, name)] = self._label2polygon(labels_path)
        img = cv2.imread(img_path)
        x1, y1, x2, y2 = poly
        img = img[y1:y2, x1:x2]

        return img, name

    def crop(self):
        for i_path, l_path in zip(self.images_path, self.labels_path):
            img, name = self._crop_icdar(i_path, l_path)
            img_path = os.path.join(self.image_dest_path, name + ".jpg")
            lbl_path = os.path.join(self.label_dest_path, name + ".txt")
            cv2.imwrite(img_path,img)
            print("Cropping image and save at {}".format(img_path))
            f_l = open(lbl_path,"w")
            print("Writting label and save at {}".format(lbl_path))
            f_l.write(name)
            f_l.close()
