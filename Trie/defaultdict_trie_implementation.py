from collections import defaultdict

class Solution:
    def longestCommonPrefix(self, words: List[str], k: int) -> List[int]:
        #ok
        def factory():
            return defaultdict(factory, {"count" : 0})  # Ensures every node has a "count" key with default 0

        #ok
        def insert_trie(trie, word, index):
            if index >= len(word):
                return
            trie[word[index]]["count"] += 1  # No need to manually initialize "count"
            insert_trie(trie[word[index]], word, index + 1)

        
        #ok
        def remove_trie(trie, word, index):
            if index >= len(word):
                return
            trie[word[index]]["count"] -= 1
            remove_trie(trie[word[index]], word, index+1)
            
        #ok
        def max_depth(trie, d):
            depth = d
            for child in trie:
                if child != "count" and trie[child]["count"] >= k:
                    depth = max(depth, max_depth(trie[child], d+1)) 
            return depth


        trie = factory()

        for word in words:
            insert_trie(trie, word, 0)

        max_depth_ans = []

        for word in words:
            remove_trie(trie, word, 0)
            max_depth_ans.append(max_depth(trie, 0))
            insert_trie(trie, word, 0)

        return max_depth_ans
