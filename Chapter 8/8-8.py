def make_album(musician_name, album_name, number_of_songs=None):
    '''add values and returns as a list'''
    if number_of_songs:
        temp = {album_name: musician_name, 'number of songs': number_of_songs}
    else:
        temp = {album_name: musician_name}
    return temp


run = True
while run:
    musician_name = input('Enter the name of the musician ')
    album_name = input('Enter the name of the album ')
    if not musician_name or not album_name:
        run = False
    else:
        album = make_album(musician_name, album_name)
        print(album)
