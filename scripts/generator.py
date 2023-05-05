## Implementation of Daniel Acuña Ureta
## email: doacuna@uc.cl
## 2023
from text2int import text2int
from random import randint, sample
import string

def PAO(sentence):
    # Person-Action-Object System
    password = ''
    sentence = sentence.split()
    for word in sentence:
        password += word[randint(0, min(5, len(word)-1))]
    return password

def Bruce_Schneier(sentence):
    password = ''
    sentence = sentence.split()
    for word in sentence:
        try:
            word = str(text2int(word))
            password += str(word)
        except:
            if len(word) >= 2:
                password += word[:randint(1, len(word)-1)]
            if word.endswith(','):
                password += ','
    return password

def word_translation(sentence):
    chars = string.ascii_letters + string.digits + string.punctuation
    d = dict(zip(chars, [*''.join(sample(chars, len(chars)))]))
    password = ''
    sentence = sentence.split()
    for word in sentence:
        password += ''.join(d[i] for i in [*word[randint(0, len(word)-1)]])
    return password

if __name__ == '__main__':
    i=0
    with open("./sentiment labelled sentences/sentiment labelled sentences/amazon_cells_labelled.txt", 'r') as data:
        with open("../test-passwords/PAO.txt", "w") as PAO_file:
            for line in data:
                i+=1
                if i == 100: break
                else:
                    PAO_file.write(PAO(line)+'\n')
    i=0
    with open("./sentiment labelled sentences/sentiment labelled sentences/amazon_cells_labelled.txt", 'r') as data:
        with open("../test-passwords/Bruce_Schneier.txt", "w") as BS_file:
            for line in data:
                i+=1
                if i == 100: break
                else:
                    BS_file.write(Bruce_Schneier(line)+'\n')
    i=0
    with open("./sentiment labelled sentences/sentiment labelled sentences/amazon_cells_labelled.txt", 'r') as data:
        with open("../test-passwords/word_translation.txt", "w") as WT_file:
            for line in data:
                i+=1
                if i == 100: break
                else:
                    WT_file.write(word_translation(line)+'\n')
