from numpy import dot
from numpy.linalg import norm
import numpy as np


class Music:
    title = []
    genre = []
    artist = []
    lang = []
    def setTitle(self, title):
        self.title.append(title)
    def setGenre(self, genre):
        self.genre.append(genre)
    def setArtist(self, artist):
        self.artist.append(artist)
    def setLang(self, lang):
        self.lang.append(lang)

def musicSave():

    print('제목을 입력해주세요 >> ',end='')
    title = input()

    check = True
    while check:
        print('장르를 입력해주세요 >> ', end='')
        genre = input()
        try:
            if genre in ["발라드", "댄스", "힙합", "록", "트로트"]:
                 check = False
            else:
                raise Exception("장르는 발라드, 댄스, 힙합, 록, 트로트 중에서 해주세요")
        except Exception as err:
            print(err)

    print('가수 이름을 입력해주세요 >> ', end='')
    artist = input()

    check = True
    while check:
        print('언어를 입력해주세요 >> ', end='')
        lang = input()
        try:
            if lang in ["한국어", "영어", "일본어"]:
                check = False
            else:
                raise Exception("언어는 한국어, 영어, 일본어 중에서 해주세요")
        except Exception as err:
            print(err)


    song = Music()
    song.setTitle(title)
    song.setGenre(genre)
    song.setArtist(artist)
    song.setLang(lang)

    song_list = []
    song_list.append(title)
    song_list.append(genre)
    song_list.append(artist)
    song_list.append(lang)

    f.write(str(song_list))

def search():
    playlist = Music()

    print('음원 제목, 장르, 가수, 언어 중에 조회하실 것을 한 개만 골라주세요 >> ',end='')
    text = input()

    if text == "음원 제목":
        cnt = 1
        for i in playlist.title:
            print(cnt ,'. ',i)
            cnt += 1
    elif text == "장르":
        cnt = 1
        for i in playlist.genre:
            print(cnt ,'. ',i)
            cnt += 1
    elif text == "가수":
        cnt = 1
        for i in playlist.artist:
            print(cnt ,'. ',i)
            cnt += 1
    elif text == "언어":
        cnt = 1
        for i in playlist.lang:
            print(cnt ,'. ',i)
            cnt += 1

def edit():
    print('수정하실 음원의 제목을 입력해주세요 >> ',end='')
    text = input()

    song = Music()
    cnt = -1
    for i in song.title:
        cnt += 1
        if text == i:
            break

    print('수정하실 항목을 골라주세요')
    print('1: 음원 제목, 2: 장르, 3: 가수, 4: 언어 >> ',end='')
    num = int(input())

    print('수정하실 내용을 입력해주세요 >> ',end='')
    editText = input()

    if num == 1:
        song.title[cnt] = editText
    elif num == 2:
        if not editText in ["발라드", "댄스", "힙합", "록", "트로트"]:
            print('장르는 발라드, 댄스, 힙합, 록, 트로트 중에서만 입력해주세요')
            check = True
            while check:
                print('수정하실 내용을 입력해주세요 >> ',end='')
                editText = input()
                try:
                    if editText in ["발라드", "댄스", "힙합", "록", "트로트"]:
                        check = False
                    else:
                        raise Exception("장르는 발라드, 댄스, 힙합, 록, 트로트 중에서만 입력해주세요")
                except Exception as err:
                    print(err)
        song.genre[cnt] = editText
    elif num == 3:
        song.artist[cnt] = editText
    elif num == 4:
        if not editText in ["한국어", "영어", "일본어"]:
            print('언어는 한국어, 영어, 일본어 중에서만 입력해주세요')
            check = True
            while check:
                print('수정하실 내용을 입력해주세요 >> ',end='')
                editText = input()
                try:
                    if editText in ["한국어", "영어", "일본어"]:
                        check = False
                    else:
                        raise Exception("언어는 한국어, 영어, 일본어 중에서만 입력해주세요")
                except Exception as err:
                    print(err)
        song.lang[cnt] = editText

def delete():
    print('삭제하실 음원의 제목을 입력해주세요 >> ', end='')
    text = input()

    song = Music()
    cnt = -1
    for i in song.title:
        cnt += 1
        if text == i:
            break

    del song.artist[cnt]
    del song.title[cnt]
    del song.lang[cnt]
    del song.genre[cnt]

def cos_sim(a, b):
    return dot(a, b)/(norm(a)*norm(b))

def make_matrix(feats, list_data):
    freq_list = []
    for feat in feats:
        freq = 0
        for word in list_data:
            if feat == word:
                freq += 1
        freq_list.append(freq)
    return freq_list

def recommend():
    song = Music()
    history_list = []

    f = open("history.dat", 'r', encoding='utf-8')

    while True:
        line = f.readline()
        if not line: break
        line = line.strip('\n') #읽어올때 개행문자 제거
        history_song = line.split(', ')
        del history_song[0]
        history_list += history_song

    history_list = set(history_list)

    num = []
    for i in range(len(song.title)):
        music = []
        music.append(song.artist[i])
        music.append(song.genre[i])
        music.append(song.lang[i])

        num.append(np.array(make_matrix(history_list, music)))

    cos_list = []

    num_11 = [1,1,1,1,1,1,1,1]
    num_11 = np.array(num_11)

    for i in range(len(song.title)):
        cos_list.append(cos_sim(num_11, num[i]))

    temp = 0
    for i in cos_list:
        if temp < i:
            temp = i

    song_idx = -1
    for i in cos_list:
        song_idx += 1
        if i == temp:
            break

    print('{} 가수의 {} 장르, {} 언어 음악을 추천드립니다'.format(song.artist[song_idx], song.genre[song_idx], song.lang[song_idx]))

while(True):
    f = open("play_list.dat", 'r', encoding='utf-8')

    song = Music()

    print('1: 음원 저장, 2: 음원 조회, 3: 음원 수정, 4: 음원 삭제, 5: 음원 추천')
    choice = int(input())
    if choice == 1:
        musicSave()
    elif choice == 2:
        search()
    elif choice == 3:
        edit()
    elif choice == 4:
        delete()
    elif choice == 5:
        recommend()
