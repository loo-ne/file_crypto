from cryptography.fernet import Fernet

def gen_key():
    return Fernet.generate_key()

def encr(key, data):
    mkey = Fernet(key)
    if binary == 0:
        return mkey.encrypt(data.encode())
    else:
        return mkey.encrypt(data)

def decode(key, data):
    mkey = Fernet(key)
    return mkey.decrypt(data)

print('파일 경로와 파일명(확장자까지)를 입력해주십시오')
fild = input('ㄴ')

try:
    with open(fild, 'rb') as file:
        text = file.read()
        binary = 1
except:
    with open(fild, 'r', encoding='utf-8') as file:
        text = file.read()
        binary = 0

print('암호화 혹은 복호화(1/2)')
yn = input('ㄴ')

if yn == '1':
    key = gen_key()
    print(f'키를 저장하십시오.\n키 : {key}')
    print('키를 파일로 저장할까요?(y/n)')
    yn = input('ㄴ')
    if yn.lower() == 'y':
        print('원하는 세이브 경로와 파일명을 입력해주십시오.')
        save = input('ㄴ') + '.txt'
        with open(save, 'wb') as file:
            file.write(key)
            print(f'키 파일 위치 : {save}')
    encrypto_data = encr(key, text)
    with open(fild, 'wb') as file:
        file.write(encrypto_data)
    print('done')
    exit()

if yn == '2':
    print('키 파일이 있으십니까?(y/n)')
    yn = input('ㄴ')
    if yn.lower() == 'y':
        print('키 파일의 경로와 파일명(확장자 포함)를 입력해주십시오')
        link = input('ㄴ')
        try:
            with open(link, 'rb') as file:
                key = file.read()
        except:
            print('키 파일이 존재하지 않거나 경로가 잘못되었습니다.')
            exit()
    elif yn.lower() == 'n':
        print('키가 있으십니까?(y/n)')
        yn = input('ㄴ')
        if yn.lower() == 'y':
            print('키를 입력해주십시오')
            key = input('ㄴ').encode()
        else:
            print('복호화할 수 없습니다. 키가 필요합니다.')
            exit()

    try:
        decode_data = decode(key, text)
    except:
        print('복호화 실패: 키가 잘못되었거나 데이터가 손상되었습니다.')
        exit()

    try:
        with open(fild, 'wb') as file:
            file.write(decode_data)
    except:
        with open(fild, 'w', encoding='utf-8') as file:
            file.write(decode_data.decode())