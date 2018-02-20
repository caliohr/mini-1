from nltk import wordpunct_tokenize
from nltk.corpus import stopwords

#Insert language
def get_language(caption):
#Splitting text into lowers case words
    words = wordpunct_tokenize(caption)
    words = [word.lower() for word in words]

    languages_dict = {}
    
    for language in stopwords.fileids():
        stopwords_set = set(stopwords.words(language))
        words_set = set(words)
        common_elements = words_set.intersection(stopwords_set)
    
        languages_dict[language] = len(common_elements) # language "score"
        
    most_rated_language = str(max(languages_dict, key = languages_dict.get))
    return most_rated_language


def import_data(location):
    dir_cap = "data/" + location + "/captions.txt"
    dir_full = "data/" + location + "/full_post.txt"
    dir_hash = "data/" + location + "/hashtags.txt"
    id = 0

    d = {}
    with open(dir_full, 'r') as a, open(dir_cap, 'r') as b, open(dir_hash, 'r') as c:
        
        for line_a, line_b, line_c in zip(a, b, c):
            #print(line_a, line_b, line_c)
            line_a = line_a.strip('\n')
            line_b = line_b.strip('\n')
            line_c = line_c.strip('\n')
            lang = get_language(line_b)
            d[id] = list()
            d[id].extend((line_a,line_b,line_c, lang))
            id += 1

    
    #skal altid stå nederst
    for key in d.keys():
        print(d[key][3])

        
import_data('valby')
