# 90. Subsets II
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [[]] if len(nums) == 0 else [[], nums]
        nums.sort()
        subsets = [[], [nums[0]]]
        prev = 1
        last = 1
        
        for i in range(1, len(nums)):
            prev = len(subsets)
            if nums[i] == nums[i - 1]:
                start = prev - last
            else:
                start = 0
            tmp = []
            for j in subsets[start:]:
                new_list = j.copy()
                new_list.append(nums[i])
                tmp.append(new_list)
            subsets.extend(tmp)
            last = len(subsets) - prev
        return subsets

# 52. N-Queens II
    def totalNQueens(self, n: int) -> int:
        if n <= 3:
            return 1 if n == 1 else 0 
        loc = [0]*n
        res = []
                
        def validLoc(tmp, k):
            valid = set(range(n))
            invalid = set([])
            for i, j in enumerate(tmp):
                invalid.add(j)
                if j + k - i < n:
                    invalid.add(j + k - i)
                if j - k + i >= 0:
                    invalid.add(j - k + i)
            return valid - invalid
                
        
        def helper(tmp, index):
            if len(tmp) == n:
                res.append(tmp)
            else:
                for i in range(index, n):
                    if len(tmp) < i:
                        break
                    thislayer = validLoc(tmp, i)
                    if not thislayer:
                        break
                    for j in thislayer:
                        tmp.append(j)
                        helper(tmp, i + 1)
                        tmp.pop()
        
        helper([], 0)
        return len(res)

# 216. Combination Sum III
    def combinationSum3(self, n, k):
        nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        res = []
    
        def helper(n, k, tmp, index):
            if k == 0:
                if n == 0:
                    res.append(tmp)
            else:
                for i in range(index, 9):
                    if k >= nums[i]:
                        helper(n - 1, k - nums[i], tmp + [nums[i]], i)
        helper(n, k, [], 0)
        return res

# 37. Sodoku Solver
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        x = {i:0 for i in range(1, 10)}
        checkRow = [x.copy() for i in range(9)]
        checkColumn = [x.copy() for i in range(9)]
        checkSquare = [[x.copy() for i in range(3)] for i in range(3)]
        blankLoc = []
        
        # initialize
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    val = int(board[i][j])
                    checkRow[i][val] = 1
                    checkColumn[j][val] = 1
                    checkSquare[i//3][j//3][val] = 1
                else:
                    blankLoc.append((i, j))
                    
                    
        def backtrack(index):
            if index == len(blankLoc):
                return True
            for a in blankLoc[index:]:
                i, j = a                    
                for val in range(1, 10):
                    if checkRow[i][val] == 0 and checkColumn[j][val] == 0 and checkSquare[i//3][j//3][val] == 0:
                        board[i][j] = str(val)
                        checkRow[i][val] = checkColumn[j][val] = checkSquare[i//3][j//3][val] = 1
                        if backtrack(index + 1):
                            return True
                        checkRow[i][val] = checkColumn[j][val] = checkSquare[i//3][j//3][val] = 0
                return False
        
        backtrack(0)
                
        
        

# 47. Permutations II
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [[]] if len(nums) == 0 else [nums]
        
        res = []
        visited = [0]*len(nums)
        
        def helper(tmp):
            if len(tmp) == len(nums) and tmp not in res:
                res.append(tmp.copy())
            else:
                prev = -1
                for i in range(len(nums)):
                    if prev >= 0 and nums[i] == nums[prev]:
                        continue
                    if not visited[i]:
                        visited[i] = 1
                        tmp.append(nums[i])
                        helper(tmp)
                        tmp.pop()
                        visited[i] = 0
                        prev = i
        helper([])       
        return res

# 131. Palindrome Partitioning
    def partition(self, s: str) -> List[List[str]]:
        if len(s) <= 1:
            return [[]] if len(s) == 0 else [[s]]
        res = []
        def helper(s, tmp):
            if len(s) == 0:
                res.append(tmp)
            else:
                for i in range(0, len(s)):
                    if self.isPalindrome(s[:i+1]):
                        helper(s[i + 1:], tmp + [s[:i+1]])
        helper(s, [])
        return res
        
        
    def isPalindrome(self, n):
        return n == n[::-1]
