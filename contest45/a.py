class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        start_x = 0
        start_y = 0
        x = 0
        y = 0
        for move in moves:
            if move == 'L':
                x -= 1
            elif move == 'R':
                x += 1
            elif move == 'U':
                y += 1
            else:
                y -= 1
        return start_x == x and start_y == y