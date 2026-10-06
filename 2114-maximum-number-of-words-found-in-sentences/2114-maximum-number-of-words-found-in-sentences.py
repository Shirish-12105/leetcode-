class Solution(object):
    def mostWordsFound(self, sentences):
        max_words = 0
        
        for sentence in sentences:
            # Every sentence starts with at least 1 word
            current_words = 1
            
            for char in sentence:
                if char == ' ':
                    current_words += 1
            
            if current_words > max_words:
                max_words = current_words
                
        return max_words


        
        