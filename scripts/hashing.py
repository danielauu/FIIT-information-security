
import hashlib

def hashing(path, salt):
    with open(path, "w") as file_out:
        for line in data:
            password = line.replace('\n', '')
            dataBase_password = password+salt   # Adding salt at the last of the password
            hashed = hashlib.sha1(dataBase_password.encode())    # Encoding the password
            file_out.write(hashed.hexdigest()+'\n')

if __name__ == '__main__':
    salt = ""
    with open("../test-passwords/PAO.txt", 'r') as data:
        path = "../test-passwords-hashed/PAO_hash_"+salt+".txt"
        hashing(path, salt)

    with open("../test-passwords/Bruce_Schneier.txt", 'r') as data:
        path = "../test-passwords-hashed/Bruce_Schneier_hash_"+salt+".txt"
        hashing(path, salt)

    with open("../test-passwords/word_translation.txt", 'r') as data:
        path = "../test-passwords-hashed/word_translation_hash_"+salt+".txt"
        hashing(path, salt)