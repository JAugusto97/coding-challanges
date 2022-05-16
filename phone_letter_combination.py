"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
Difficulty: Medium

Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number could represent.
Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""

from typing import List


class Solution:
    def get_combinations(self, t1, t2):
        """
        this operation is cumulative. combination(combination(a, b), c) = combination(a, b, c)
        combination([a,b], [d, e]) == [ad, ae, bd, be].
        combination([ad,ae,bd,be], [f, g]) = [adf, adg, aef, aeg, bdf, bdg, bef, beg]
        """
        r = []

        for c1 in t1:
            for c2 in t2:
                r.append((c1 + c2))

        return set(r)

    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": set(["a", "b", "c"]),
            "3": set(["d", "e", "f"]),
            "4": set(["g", "h", "i"]),
            "5": set(["j", "k", "l"]),
            "6": set(["m", "n", "o"]),
            "7": set(["p", "q", "r", "s"]),
            "8": set(["t", "u", "v"]),
            "9": set(["w", "x", "y", "z"]),
        }

        possibilities = [mapping[c] for c in digits]
        if len(possibilities) > 1:  # at least two combinations
            r = self.get_combinations(possibilities[0], possibilities[1])
            for i in range(2, len(possibilities)):
                r = self.get_combinations(r, possibilities[i])

        elif len(possibilities) == 1:  # one combination is just its mapping
            return possibilities[0]

        else:
            r = []

        return r
