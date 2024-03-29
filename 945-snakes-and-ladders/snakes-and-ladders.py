class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        """
        Finds the minimum number of moves required to reach the last square on a snakes and ladders board.

        Args:
            board (List[List[int]]): The board configuration where -1 represents empty squares.

        Returns:
            int: The minimum number of moves to reach the last square. Returns -1 if not possible.
        """
        n = len(board)
        jumps, target = {}, n * n

        board.reverse()
        for i in range(n): board[i].reverse() if i % 2 else None

        c = 0
        for i in board:
            for j in i:
                c += 1
                if j == -1: continue
                jumps[c] = j
        
        q, seen = deque([(1, 0)]), set([1])

        while q:
            i, moves = q.popleft()
            if i == target: return moves
            for j in range(i+1, i+7):
                if j > target: break
                if j in seen: continue
                seen.add(j)
                if j in jumps: j = jumps[j]
                q.append((j, moves + 1))

        return -1