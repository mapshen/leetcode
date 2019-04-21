class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        mapping = {"A": 0, "C": 1, "G": 2, "T": 3}
        mask = (1 << 20) - 1

        seen, output = set(), set()
        code = 0

        for i in range(len(s)):
            code = (code << 2) | mapping[s[i]]

            if i >= 9:
                code = code & mask
                if code in seen and s[i - 9:i + 1] not in output:
                    output.add(s[i - 9:i + 1])

                if code not in seen:
                    seen.add(code)

        return list(output)
