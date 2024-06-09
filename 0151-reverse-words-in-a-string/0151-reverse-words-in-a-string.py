class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
    
    # Step 2: Split the string into words based on spaces
        words = s.split()
        
        # Step 3: Reverse the list of words
        reversed_words = words[::-1]
        
        # Step 4: Join the reversed list of words with a single space
        result = ' '.join(reversed_words)
    
        return result