
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        len_of_word = len(word)
        rows, columns = len(board), len(board[0])
        set_of_word = set()

        def helperFunction(i, j, tempA, visited):
            if len(tempA) == len_of_word:
                set_of_word.add(''.join(tempA))
                return

            if i < 0 or i >= rows or j < 0 or j >= columns:
                return
            if (i, j) in visited:
                return
            if board[i][j] != word[len(tempA)]:
                return

            tempA.append(board[i][j])
            visited.add((i, j))

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                helperFunction(i + dr, j + dc, tempA, visited)

            tempA.pop()
            visited.remove((i, j))

        for i in range(rows):
            for j in range(columns):
                helperFunction(i, j, [], set())
                if word in set_of_word:
                    return True

        return False
