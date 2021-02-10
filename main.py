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
    while True:
        if(play_obj.is_playing()):
            print('')
        else:
            print('Ended')
            break
    play_obj.wait_done()


def greetings():
    print('*' * 35)
    print('Welcome To The Python Music Player')
    print('*' * 35)


def main(choice):
    list_of_songs = os.listdir(
        "./songs")
    if option == 1:
        for i in list_of_songs:
            print(i)
        song = input('Enter song to play:')
        if song in list_of_songs:
            player(song)
        else:
            print('Song not found!(Please type in the full name and the extension!!)')
    elif option == 2:
        song = random.choice(list_of_songs)
        player(song)
    elif option == 3:
        for i in list_of_songs:
            print(i)
    elif option == 0:
        exit()
    else:
        print('Something went wrong!')


if __name__ == '__main__':
    greetings()
    while True:
        option = int(input(OPTIONS))
        main(option)
