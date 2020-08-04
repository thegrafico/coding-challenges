from typing import List

class Solution:
    def is_palindrome(self, x: int) -> bool:

        if x < 0:
            return False
        elif 0 < x < 10:
            return True

        # Create a copy of our value
        mod = 0
        org = int(x)
        temp = 0

        tam = self.get_len_(x)
        units = self.get_units(tam)[::-1]

        for i in range(tam):
            mod = x % 10
            x = int(x/10)

            temp += mod * units[i]

        return True if temp == org else False


    def get_len_(self, x: int) -> int:
        times = 1

        # if the number is negative, convert into positive
        if x < 0:
            x = x * - 1

        if 0 < x < 10:
            return times

        x = int(x/10)
        while x != 0:
            times += 1
            x = int(x/10)

        return times

    def get_units(self, tam: int) -> List:
        units = []
        n = 1

        for i in range(tam):
            units.append(n)
            n *= 10

        return units


if __name__ == "__main__":
    s = Solution()
    n = 121
    print("ORIGINAL: ", n)
    print(s.is_palindrome(n))
