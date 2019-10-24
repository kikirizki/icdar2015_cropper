from crop_icdar import IcdarCropper

cropper = IcdarCropper(
    "2015",
    "/home/robert/DATASET/license_plate_dataset_13_sep_2019/images/val",
    "/home/robert/DATASET/license_plate_dataset_13_sep_2019/labels/val",
    "/home/robert/DATASET/licenseplate_recognition_dataset/images/val",
    "/home/robert/DATASET/licenseplate_recognition_dataset/labels/val"
)
cropper.crop()
