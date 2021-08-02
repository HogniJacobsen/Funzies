import re

def palindrome(text):
    text = str(text)
    text = re.sub(r'[^\w\s]', '', text)
    text = text.replace(' ', '')
    text = text.lower()
    len_text = len(text)

    for i in range(len_text//2):
        if text[i] != text[-i-1]:
            return False
    return True

if __name__ == '__main__':
    palindrome_list = ["Don't nod." , "I did, did I?", 
    "My gym", "Red rum, sir, is murder",
    "Step on no pets", "Top spot",
    "Was it a cat I saw?", "Eva, can I see bees in a cave?",
    "No lemon, no melon", "test", 1234, 121]

    for i in palindrome_list:
        print(f'Text: {i} \nPalindrome: {palindrome(i)}\n')