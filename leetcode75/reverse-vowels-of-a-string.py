# https://leetcode.com/problems/reverse-vowels-of-a-string/description/


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']

        new_vow = []
        v = []
        for char in s:
            if char.lower() not in vowels:
                new_vow.append(char)
            else:
                v.append(char)

        v = v[::-1]

        result = []
        v_index = 0

        for char in s:
            if char.lower() not in vowels:
                result.append(new_vow.pop(0))
            else:
                result.append(v[v_index])
                v_index += 1

        result_str = ''.join(result)
        return result_str
