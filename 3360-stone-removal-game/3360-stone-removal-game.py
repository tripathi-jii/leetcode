
class Solution:
    def canAliceWin(self, n: int) -> bool:
        stones = 10
        alice = True

        while stones > 0 and n >= stones:
            n -= stones
            stones -= 1
            alice = not alice

        return not alice
