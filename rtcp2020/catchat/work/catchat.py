CAT_CHAT_DICT = { 'A':'nyameow', 'B':'meownyanyanya', 
                    'C':'meownyameownya', 'D':'meownyanya', 'E':'nya', 
                    'F':'nyanyameownya', 'G':'meowmeownya', 'H':'nyanyanyanya', 
                    'I':'nyanya', 'J':'nyameowmeowmeow', 'K':'meownyameow', 
                    'L':'nyameownyanya', 'M':'meowmeow', 'N':'meownya', 
                    'O':'meowmeowmeow', 'P':'nyameowmeownya', 'Q':'meowmeownyameow', 
                    'R':'nyameownya', 'S':'nyanyanya', 'T':'meow', 
                    'U':'nyanyameow', 'V':'nyanyanyameow', 'W':'nyameowmeow', 
                    'X':'meownyanyameow', 'Y':'meownyameowmeow', 'Z':'meowmeownyanya',
                    '0':'meowmeowmeowmeowmeow','1':'nyameowmeowmeowmeow','2':'nyanyameowmeowmeow',
                    '3':'nyanyanyameowmeow','4':'nyanyanyanyameow','5':'nyanyanyanyanya',
                    '6':'meownyanyanyanya','7':'meowmeownyanyanya','8':'meowmeowmeownyanya',
                    '9':'meowmeowmeowmeownya','.':'nyameownyameownyameow',',':'meowmeownyanyameowmeow',
                    ':':'meowmeowmeownyanyanya','?':'nyanyameowmeownyanya','-':'meownyanyanyanyameow',
                    '/':'meownyanyameownya','(':'meownyameowmeownya',')':'meownyameowmeownyameow',
                    '"':'nyameownyanyameownya', "'":"nyameowmeowmeowmeownya", '+':'nyameownyameownya',
                    '@':'nyameowmeownyameownya','=':'meownyanyanyameow','_':'nyanyameowmeownyameow',' ':'purr'} 
  
def encrypt(message): 
    cipher = '' 
    for letter in message: 
        if letter != ' ':  
            cipher += CAT_CHAT_DICT[letter] + ' '
        else: 
            cipher += ' '
  
    return cipher 
  
def decrypt(message): 
  
    message += ' '
  
    decipher = '' 
    citext = '' 
    for letter in message: 
        if (letter != ' '): 
            i = 0
            citext += letter 
  
        else: 
            i += 1
            if i == 2 : 
  
                decipher += ' '
            else: 
                decipher += list(CAT_CHAT_DICT.keys())[list(CAT_CHAT_DICT 
                .values()).index(citext)] 
                citext = '' 
    return decipher 

def main():
    beg = input("Do you want to ENCRYPT or DECRYPT?\n> ").lower()
    if beg == "decrypt":
        message = input("What do you want to decrypt?\n> ")
        result = decrypt(message) 
        print(result)
    else:
        message = input("What do you want to encrypt?\n> ")
        result = encrypt(message.upper()) 
        print(result)
        
if __name__ == '__main__': 
    main() 
