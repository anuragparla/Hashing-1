'''
Time: O(N)
Space: O(N)
'''
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        word_to_pattern_mapping = set()
        pattern_to_word_mapping = dict()

        if len(pattern) != len(words):
            return False
        '''
        Method 1: using hash map and set
        Time: O(N)
        Space: O(N)
        Note: It can also be solved using 2 hashmaps and single hashmap 
        like isomorphic strings
        '''
        for i in range(len(pattern)):
            if pattern[i] not in  pattern_to_word_mapping:
                if words[i] not in word_to_pattern_mapping:
                    pattern_to_word_mapping[pattern[i]] = words[i]
                    word_to_pattern_mapping.add(words[i])
                else:
                    return False
            else:
                if pattern_to_word_mapping[pattern[i]] != words[i]:
                    return False
        return True
                
