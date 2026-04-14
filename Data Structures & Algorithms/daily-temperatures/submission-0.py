class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = [0] * len(temperatures)
        for i in range(len(temperatures)):
            for j in range(i, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    diff = j - i
                    days[i] = diff
                    break
        return days