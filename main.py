try:
    import simpleaudio as sa
    import random
    import os
except ModuleNotFoundError as err:
    print(err)

OPTIONS = '''
1.Enter a song
2.Suffle
3.List all songs
0.Exit
'''


def player(song):
    wave_obj = sa.WaveObject.from_wave_file(
        f"./songs/{song}")
    play_obj = wave_obj.play()
    print(f'Currently Playing: {song}')
    while True:
        if(play_obj.is_playing()):
            pass
        else:
            print('Ended')
            break
    play_obj.wait_done()


def greetings():
    print('*' * 35)
    print('Welcome To The Python Music Player')
    print('*' * 35)


def get_list_of_songs():
    song_list = dict()
    for key, value in enumerate(os.listdir('./songs')):
        song_list[key+1] = value
    return song_list


def main(choice):
    list_of_songs = os.listdir(
        "./songs")
    song_list = get_list_of_songs()

    if option == 1:
        for id_, song in song_list.items():
            print(f"{id_}. {song}")
        song = int(input('Enter a song id to play: '))
        if bool(song_list.get(song, 0)):
            player(song_list[song])
        else:
            print("Song with the given id was not found.")
    elif option == 2:
        song = random.choice(list_of_songs)
        player(song)
    elif option == 3:
        for id_, song in song_list.items():
            print(f"{id_}. {song}")
    elif option == 0:
        exit()
    else:
        print('Something went wrong!')


if __name__ == '__main__':
    greetings()
    while True:
        option = int(input(OPTIONS))
        main(option)
