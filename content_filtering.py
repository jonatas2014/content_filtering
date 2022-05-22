from math import sqrt

# sample data
musics = {"Dr Dog/Fate": {"piano": 2.5, "vocals": 4, "beat": 3.5, "blues": 3, "guitar": 5, "backup vocals": 4, "rap": 1},
         "Phoenix/Lisztomania": {"piano": 2, "vocals": 5, "beat": 5, "blues": 3, "guitar": 2, "backup vocals": 1, "rap": 1},
         "Heartless Bastards/Out at Sea": {"piano": 1, "vocals": 5, "beat": 4, "blues": 2, "guitar": 4, "backup vocals": 1, "rap": 1},
         "Todd Snider/Don't Tempt Me": {"piano": 4, "vocals": 5, "beat": 4, "blues": 4, "guitar": 1, "backup vocals": 5, "rap": 1},
         "The Black Keys/Magic Potion": {"piano": 1, "vocals": 4, "beat": 5, "blues": 3.5, "guitar": 5, "backup vocals": 1, "rap": 1},
         "Glee Cast/Jessie's Girl": {"piano": 1, "vocals": 5, "beat": 3.5, "blues": 3, "guitar":4, "backup vocals": 5, "rap": 1},
         "La Roux/Bulletproof": {"piano": 5, "vocals": 5, "beat": 4, "blues": 2, "guitar": 1, "backup vocals": 1, "rap": 1},
         "Mike Posner": {"piano": 2.5, "vocals": 4, "beat": 4, "blues": 1, "guitar": 1, "backup vocals": 1, "rap": 1},
         "Black Eyed Peas/Rock That Body": {"piano": 2, "vocals": 5, "beat": 5, "blues": 1, "guitar": 2, "backup vocals": 2, "rap": 4},
         "Lady Gaga/Alejandro": {"piano": 1, "vocals": 5, "beat": 3, "blues": 2, "guitar": 1, "backup vocals": 2, "rap": 1}}


def cosseno(music_features_values_1, music_features_values_2):

    ''' 
        This return the cosseno distance between two rows 
        based on their feature values. 
        The returned value is a value from the interval [-1,1],
        the nearest from 1 indicate the greater similarity between two
        rows, the nearest to -1 the poorest their similarity 
    '''

    numerador = 0
    for key in music_features_values_1:
        if key in music_features_values_2:
            numerador += (music_features_values_1[key] * music_features_values_2[key])

    comp_x, comp_y = 0, 0

    for key in music_features_values_1:
        comp_x += (music_features_values_1[key])**2

    for key in music_features_values_2:
        comp_y += (music_features_values_2[key])**2

    denominador = sqrt(comp_x) * sqrt(comp_y)

    return numerador/denominador

def recomender(music_profile, musics):
    """creates a sorted list of musics based on their similarity distance to musicname"""
    distances = []
    for music in musics:
            distance = cosseno(musics[music], music_profile)
            distances.append((distance, music))
    # sort based on distance -- closest first
    return sorted(distances, 
                  key=lambda bandtuple : bandtuple[0], 
                  reverse=True)



'''#Tests 

profile = {"piano": 2.5, "vocals": 4, "beat": 1, "blues": 3, "guitar": 1, "backup vocals": 4, "rap": 1}

print(recomender(profile, musics))'''
