class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        zigzag = [''] * numRows
        step = 1 # 다음 행으로 움직일때는 1 아니면 -1
        index = 0 # 현재 지시된 행의 번호
        for character in s:
            zigzag[index] += character
            if index == numRows - 1:
                step = -1
            elif index == 0:
                step = 1

            index += step

        return ''.join(zigzag)
