import chardet

detect = chardet.detect(b'Hello, world!')
print(detect)