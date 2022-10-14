def make_album(musician_name, album_name, number_of_songs=None):
    '''add values and returns as a list'''
    if number_of_songs:
        temp = {album_name: musician_name, 'number of songs': number_of_songs}
    else:
        temp = {album_name: musician_name}
    return temp


album = make_album('Michael Kenji Shinoda', 'Meteora', 13)
print(album)

album = make_album('Jared Leto', '30 Seconds to Mars ')
print(album)

album = make_album('Isaac Edward Slade', 'The Fray')
print(album)
