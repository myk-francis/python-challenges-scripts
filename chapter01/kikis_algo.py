# Caesar cipher 

def caesar_cipher_encrypt(text, shift):
    """
    Encrypts a given text using the Caesar cipher with the given shift.

    Args:
        text (str): The text to be encrypted.
        shift (int): The number of positions to shift each character.

    Returns:
        str: The encrypted text.
    """
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted_char = chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                encrypted_char = chr((ord(char) - 97 + shift) % 26 + 97)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(encrypted_text, shift):
    """
    Decrypts a given encrypted text using the Caesar cipher with the given shift.

    Args:
        encrypted_text (str): The text to be decrypted.
        shift (int): The number of positions to shift each character.

    Returns:
        str: The decrypted text.
    """
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            if char.isupper():
                decrypted_char = chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                decrypted_char = chr((ord(char) - 97 - shift) % 26 + 97)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

# Example usage:
text = "Hello, World!"
shift = 4
encrypted_text = caesar_cipher_encrypt(text, shift)
print("Encrypted text:", encrypted_text)
decrypted_text = caesar_cipher_decrypt(encrypted_text, shift)
print("Decrypted text:", decrypted_text)