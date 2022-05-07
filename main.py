import cv2
import pytesseract


def main():
    image_path = "tests/artifacts/image.jpg"
    img = cv2.imread(image_path)

    # Adding custom options
    custom_config = r"--oem 3 --psm 6"
    output = pytesseract.image_to_string(img, config=custom_config)
    print("output: \n {}".format(output))


if __name__ == "__main__":
    main()
