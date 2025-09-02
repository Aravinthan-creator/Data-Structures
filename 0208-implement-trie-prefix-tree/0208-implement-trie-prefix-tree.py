class TrieNode:
    def __init__(self):
        self.child = {}
        self.end= False
     

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            if c not in current.child:
                current.child[c] = TrieNode()
            current = current.child[c]

        current.end =True
        

    def search(self, word: str) -> bool:
        current = self.root
        for c in word:
            if c not in current.child:
                return False
            current = current.child[c]

        return current.end
       
        
 

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for c in prefix:
            if c not in current.child:
                return False
            current = current.child[c]

        return True
    


