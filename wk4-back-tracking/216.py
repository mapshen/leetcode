class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.results = []
        self.temp = []

        def backtrack(idx):
            for i in range(idx, 10):
                self.temp.append(i)
                print(self.temp)

                # TODO: this is terrible
                #   You can tric more agressively
                if len(self.temp) == k:
                    if sum(self.temp) == n:
                        self.results.append(self.temp[:])
                else:
                    backtrack(i + 1)

                self.temp.pop()

        backtrack(1)

        return self.results
