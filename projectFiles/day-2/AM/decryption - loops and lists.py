import time

def pause(tics):
    numDots = 0
    while numDots < tics:
        numDots += 1
        time.sleep(0.6)
        print(".", end = "")

def encrypt(msg):
    return msg

def decrypt(msg):
    return msg

def print_message(msg):
    print("\n\n-------------------------------------------")
    print(msg)
    print("-------------------------------------------\n")

while True:
    choice = input("[E]ncrypt, [D]ecrypt, or [Q]uit: ").upper()
    
    while choice != "E" and choice != "D" and choice != "Q":
        choice = input("Enter E to encrypt, D to decrypt, or Q to quit: ").upper()

    if choice == "D":
        message = input("\nEnter encrypted message: ")
        print("\nDecrypting message is", end = "")
        pause(4)
        print("\n\nDecrypted message:")
        print_message(decrypt(message))
    elif choice == "E":
        message = input("\nEnter decrypted message: ")
        print("\nEncrypting message is", end = "")
        pause(4)
        print("\n\nEncrypted message:")
        print_message(encrypt(message))
    else: # choice is "Q"
        quit()
        
    


        
        
