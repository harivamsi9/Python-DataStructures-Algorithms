class Solution:
    def calculateScore(self, s: str) -> int:
        # Create reverse mapping for letters
        mirror = {chr(ord('a') + i): chr(ord('z') - i) for i in range(26)}
        unmarked_indices = {}
        score = 0
        
        for i, char in enumerate(s):
            mirrored_char = mirror[char]
            if mirrored_char in unmarked_indices and unmarked_indices[mirrored_char]:
                j = unmarked_indices[mirrored_char].pop()  # Get the last inserted index
                score += (i - j)
            else:
                if char not in unmarked_indices:
                    unmarked_indices[char] = []
                unmarked_indices[char].append(i)
        
        return score


s = Solution()
input_string1 = input()
input_string2 = input()
t3 = input()
print(s.calculateScore(input_string1))  # Output: 5
print(s.calculateScore(input_string2))  # Output: 0
print(s.calculateScore(t3))  # Output: 18
