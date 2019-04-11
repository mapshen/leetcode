class Solution:
    def partition(self, s: str) -> List[List[str]]:
        string_size = len(s)
        self.temp = []
        self.results = []

        def helper(idx, temp_size):
            # Can do better by caching the results
            partition = ""
            for i in range(idx, string_size):
                partition += s[i]
                if not self.is_palindrome(partition):
                    continue

                self.temp.append(partition)
                temp_size += len(partition)

                if temp_size == string_size:
                    self.results.append(self.temp[:])
                else:
                    helper(i + 1, temp_size)

                self.temp.pop()
                temp_size -= len(partition)

        helper(0, 0)

        return self.results

    def is_palindrome(self, s):
        for i in range(len(s) // 2):
            if not s[i] == s[-i - 1]:
                return False

        return True
