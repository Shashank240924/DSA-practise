# 25% Beats
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1]

        for i in range(1, rowIndex + 1):
            prevElement = result[i - 1]
            # Use the formula C(r, i) = C(r, i-1) * (r - i + 1) / i
            currentElement = prevElement * (rowIndex - i + 1) // i
            result.append(currentElement)

        return result
        