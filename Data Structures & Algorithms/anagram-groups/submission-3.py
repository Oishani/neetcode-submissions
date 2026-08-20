class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]

        hash_to_word = defaultdict(list) # {"a1b2": [bab, abb]}
        result = []

        for st in strs:
            encoded_str = self.encode(st)
            hash_to_word[encoded_str].append(st)

        for anagram_list in hash_to_word.values():
            result.append(anagram_list)

        return result



    def encode(self, st):
        char_freq = Counter(st) # {"a": 1, "b": 2}
        sorted_freq = sorted(char_freq.items()) # [("a", 1), ("b", 2)]

        encoded_str = "".join(f"{k}{v}" for k, v in sorted_freq) # "a1b2"

        return encoded_str

# Time: O(n * m) where n is len of strs and m is avg len of a string in strs
# Space: O(n * m)