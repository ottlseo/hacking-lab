import zipfile
from threading import Thread


def crackzip(zipfile, passwd):
    try:
        zfile.extractall(pwd=passwd)
        print("zip file opened by Yoonseo!! PASS= [%s]" % passwd.decode())
        return True
    except:
        pass
    return False


if __name__ == '__main__':
    dictfile = 'dict.txt'  # 딕셔너리 파일
    zipfilename = 'assignment.zip'
    zfile = zipfile.ZipFile(zipfilename, 'r')
    f = open(dictfile, 'r')  # 딕셔너리 파일을 열어서 f 에 저장

    for line in f.readlines():
        passwd = line.strip('\n')
        t = Thread(target=crackzip, args=(zfile, passwd.encode('utf-8')))
        t.start()