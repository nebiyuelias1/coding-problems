from typing import Dict, List


class Solution:
    def buildAdjacencyList(self, wordList: List[str], m: int) -> Dict:
        adj_list = {}
        for word in wordList:
            for i in range(m):
                possible_word = word[:i] + '*' + word[i+1:]
                if possible_word in adj_list:
                    adj_list[possible_word].add(word)
                else:
                    adj_list[possible_word] = set([word])
                    
        return adj_list

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        m = len(beginWord)
        
        adj_list = self.buildAdjacencyList(wordList, m)
        
        words_queue = [(beginWord, 1)]
        visited = set([beginWord])
        
        while words_queue:
            current_word, current_level = words_queue.pop(0)

            for i in range(m):
                intermediate_word = current_word[:i] + '*' + current_word[i+1:]
                if intermediate_word in adj_list:
                    for word in adj_list[intermediate_word]:
                        if word == endWord:
                            return current_level + 1
                        
                        if word not in visited:
                            visited.add(word)
                            words_queue.append([word, current_level + 1])
                
        return 0
    
    
sol = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

print(sol.ladderLength(beginWord=beginWord, endWord=endWord, wordList=wordList))
            
