
def is_palindrome(s):
    # Function to preprocess the string
    def preprocess(s):
        # Remove spaces and punctuation, convert to lowercase
        return ''.join(char.lower() for char in s if char.isalnum())

    # Preprocess the string
    s = preprocess(s)
    
    # Create a stack
    stack = []
    
    # Push half of the characters onto the stack
    for char in s[:len(s)//2]:
        stack.append(char)
    
    # Compare remaining characters with characters popped from the stack
    for char in s[len(s)//2 + len(s) % 2:]:
        if char != stack.pop():
            return False
    
    return True

# Test cases
print(is_palindrome("radar"))   # True
print(is_palindrome("A man, a plan, a canal, Panama"))  # True
print(is_palindrome("hello"))    # False
