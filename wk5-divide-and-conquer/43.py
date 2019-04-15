class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        k1, k2 = len(num1), len(num2)

        product = [0] * (k1 + k2)

        for i in range(k1 - 1, -1, -1):
            for j in range(k2 - 1, -1, -1):
                p1, p2 = i + j, i + j + 1
                temp = int(num1[i]) * int(num2[j]) + product[p2]

                product[p1] += temp // 10
                product[p2] = temp % 10

        result = "".join(map(str, product)).lstrip("0")
        if result:
            return result
        else:
            return "0"
