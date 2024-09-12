class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for i in range(len(words)):
            if sorted(set(list(words[i] + allowed))) == list(sorted(allowed)): count += 1
        return count
        