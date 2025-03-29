# caesar_cipher
Caesar cipher
The code above implements a simple Caesar cipher encryption and decryption system using a shift value and a specified alphabet. The program allows users to either encrypt or decrypt a message using the following steps:

Initial Prompt: The user is prompted to choose between encryption or decryption by typing "encrypt" or "decrypt".

Encryption:

If "encrypt" is selected, the user is asked to input the message they want to encrypt and the shift value (how many positions each character in the message will be moved).

The function encrypt() then loops through each character of the message:

If the character is a space, it is left unchanged.

For each letter in the message, it finds its position in the alphabet, shifts it by the specified value (circularly, so it wraps around), and then adds the new letter to the result.

Decryption:

If "decrypt" is selected, the user is prompted to enter the encrypted message and the same shift value used for encryption.

The decrypt() function works similarly to encryption but in reverse: it shifts each letter backward in the alphabet by the shift value.

If a shift would move the character outside of the alphabet, it wraps around from the other end.

Repetition: After each operation, the user is asked if they want to continue. If they type "yes", they are prompted again to either encrypt or decrypt. If they type "no", the program ends with a "Goodbye!" message.

The code uses Python’s string module to create an alphabet (lowercase English letters). It handles spaces in the message by leaving them unchanged and performs the shift operation modulo 26 to ensure that the alphabet wraps around correctly.

Key Points:
Encrypting and decrypting messages using a Caesar cipher.

Modular arithmetic ensures that the letters wrap around the alphabet (e.g., 'z' becomes 'a' after a shift of 1).

Users can repeatedly encrypt or decrypt messages by inputting "yes" to continue, or "no" to exit.



