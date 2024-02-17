from collections import defaultdict

def groupAnagrams(strs):
    anagrams = defaultdict(list)
    
    for word in strs:
        # Sort each word to obtain its sorted representation
        sorted_word = ''.join(sorted(word))
        # Add the original word to the list of anagrams for its sorted representation
        anagrams[sorted_word].append(word)
    
    # Return the values (lists of anagrams) of the defaultdict as the final result
    return list(anagrams.values())

# Example usage:
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
