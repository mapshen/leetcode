class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0

        if len(s) == 1:
            if s[0] == "0":
                return 0
            elif s[0] == "*":
                return 9
            else:
                return 1

        a = 1
        if s[0] == "*" and s[1] == "0":
            b = 2
        elif s[0] == "*":
            b = 9
        else:
            b = 1

        for i in range(1, len(s)):
            if s[i - 1] not in "12*" and s[i] == "0":
                return 0

            if s[i - 1] == "*" and s[i] == "*":
                if s[i + 1:i + 2] == "0":
                    a, b = b, 2 * b
                else:
                    a, b = b, 9 * b + 15 * a
            elif s[i - 1] == "*":
                if s[i] == "0" or s[i + 1:i + 2] == "0":
                    a, b = b, b
                elif s[i] < "7":
                    a, b = b, b + 2 * a
                else:
                    a, b = b, b + a
            elif s[i] == "*":
                if s[i + 1:i + 2] == "0":
                    a, b = b, 2 * b
                elif s[i - 1] == "0":
                    a, b = b, 9 * b
                elif s[i - 1] == "1":
                    a, b = b, a * 9 + b * 9
                elif s[i - 1] == "2":
                    a, b = b, a * 6 + b * 9
                else:
                    a, b = b, b * 9
            elif (s[i - 1] > "2" or (s[i - 1] == "2" and s[i] > "6")) or "0" in s[i - 1: i + 2]:
                a, b = b, b
            else:
                a, b = b, b + a

        return b % (10 ** 9 + 7)
