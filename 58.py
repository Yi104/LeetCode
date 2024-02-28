def lengthOfLastWord(s: str) -> int:
    # Remove trailing spaces
    s = s.rstrip()
    
    # Iterate from the end to find the last word length
    length = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] == ' ':
            break
        length += 1
    
    return length

# Test the function
print(lengthOfLastWord("Hello World"))  # Output: 5
