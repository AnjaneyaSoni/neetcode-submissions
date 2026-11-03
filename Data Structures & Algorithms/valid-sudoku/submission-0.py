class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        my_dict = {
    '1': [[], [], []],
    '2': [[], [], []],
    '3': [[], [], []],
    '4': [[], [], []],
    '5': [[], [], []],
    '6': [[], [], []],
    '7': [[], [], []],
    '8': [[], [], []],
    '9': [[], [], []]
}
        for r in range(9):
            for c in range(9):
                
                val=board[r][c]

                if val==".":
                    continue

                if r in my_dict[val][0]:
                    return False
                my_dict[val][0].append(r)

                if c in my_dict[val][1]:
                    return False
                my_dict[val][1].append(c)

                box = (r // 3) * 3 + (c // 3) + 1

                if box in my_dict[val][2]:
                    return False
                my_dict[val][2].append(box)
        return True













