class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def getDay(date):
            month, day = map(int, date.split('-'))
            return sum(months[:month - 1]) + day

        start = max(getDay(arriveAlice), getDay(arriveBob))
        end = min(getDay(leaveAlice), getDay(leaveBob))

        return max(0, end - start + 1)