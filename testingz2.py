# def song_decoder(song):
#     x = song.replace("WUB", " ")
#     x_1 = x.strip(" ")
#     val = 0
#     while val !=-1:
#         val = x_1.find("  ")
#         x_1 = x_1.replace("  ", " ", 1)
#     return x_1

def song_decoder(song):
    x_1 = song.replace('WUB', ' ')
    x_1 = x_1.split()
    return " ".join(x_1)


print(song_decoder("CDFAWUBWUBWUBWUBBWUBWUBWUBC"))
