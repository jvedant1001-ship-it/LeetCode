class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows

        row = 0
        direction = 1

        for char in s:
            rows[row] += char

            # Change direction at top/bottom
            if row == 0:
                direction = 1
            elif row == numRows - 1:
                direction = -1

            row += direction

        return "".join(rows)
