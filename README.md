# Hacking-Lab
by @ottl-seo 

### [ [Locky 랜섬웨어 분석](./javascript-ransomware-nativeAPI) ]
Locky 랜섬웨어라고 알려져 있는 이 악성코드는 javascript 난독화를 통해 분석을 어렵게 만든 것이 특징이다.   
Python Native API를 작성해 암호화된 코드를 분석하고 원본 코드를 복원하였다. 

[BLOG](https://ottl-seo.tistory.com/45)에 분석 과정을 정리했다. 

- [Locky.vir](./javascript-ransomware-nativeAPI/Locky.vir) : Locky 랜섬웨어 코드
- [Locky_NativeAPI.py](./javascript-ransomware-nativeAPI/Locky_NativeAPI.py) : Python으로 작성한 Locky 랜섬웨어 분석용 Dummy API

### [ [Dictionary attack을 이용한 Password 크래킹](./password-cracking) ]
Dictionary 공격을 활용하여 zip 파일의 패스워드를 크래킹하는 소프트웨어이다.
잠겨있는 zip 파일 비밀번호에 대한 힌트를 바탕으로 가능한 패스워드들의 리스트를 만들고 크래킹에 성공하면 파일을 열어 내용을 확인할 수 있다.

### [ [AES 암호화 알고리즘을 이용한 txt 파일 삭제 랜섬웨어 개발](./txt-encrypt-ransomware) ]
Python script 를 통해 개발한 간단한 랜섬웨어.   
AES_CBC 암호화를 이용해 폴더 내의 모든 .txt 파일들을 .enc 파일들로 암호화한다. 
공개키 암호 알고리즘 (RSA)를 사용하여 대칭키를 암호화하여 키에 접근할 수 없도록 한다.   
마지막으로 해당 폴더 내 모든 “.txt”파일을 지우고 
“Your text files are encrypted. To
decrypt them, you need to pay me $5,000 and send key.bin in your folder to
me.”를 피해자에게 출력한다.