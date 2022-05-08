# ocr-app
Extracting text from Images using OCR technology

[![Python 3.10 OCR application Github workflow](https://github.com/JeremyCurmi/ocr-app/actions/workflows/main.yml/badge.svg)](https://github.com/JeremyCurmi/ocr-app/actions/workflows/main.yml)

To solve the following lint error ([Link](https://stackoverflow.com/questions/50612169/pylint-not-recognizing-cv2-members)):
Module 'cv2' has no 'imread' member (no-member)

Run: 
pylint --generate-rcfile > .pylintrc
and then add: extension-pkg-whitelist=cv2

