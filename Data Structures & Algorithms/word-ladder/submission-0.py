class Node:
    def __init__(self, val = "", neighbors = []):
        self.val = val
        self.neighbors = [nbr for nbr in neighbors]

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        found = {}
        for word in wordList:
            found[word] = Node(word)
        
        def isValid(word1, word2):
            nr = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    nr += 1
            return False if nr != 1 else True

        for word in wordList:
            for word2 in wordList:
                if word != word2 and isValid(word, word2):
                    found[word].neighbors.append(found[word2])
        
        from collections import deque

        que = deque()
        que.append(found[beginWord])
        wordList.pop()
        nr = 0
        seen = set()
        seen.add(beginWord)

        while que:
            dim = len(que)
            nr += 1
            for _ in range(dim):
                curr = deque.popleft(que)
                if curr.val == endWord:
                    return nr
                for nbr in curr.neighbors:
                    if nbr.val not in seen:
                        seen.add(nbr.val)
                        que.append(nbr)
        return 0

                
                
        
