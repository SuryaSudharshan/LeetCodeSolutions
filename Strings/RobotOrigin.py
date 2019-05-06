class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if(len(moves) == 2):
            if moves[0] == 'U' and moves [1] == 'D':
                return True
            if moves[0] == 'D' and moves [1] == 'U':
                return True
            if moves[0] == 'L' and moves [1] == 'R':
                return True
            if moves[0] == 'R' and moves [1] == 'L':
                return True
            else:
                return False
        elif(len(moves)%2 == 0 and len(moves)>2):
            lcount=rcount=ucount=dcount=0
            for i in moves:
                if( i == 'L'):
                    lcount+=1
                elif(i == 'R'):
                    rcount+=1
                elif(i == 'U'):
                    ucount+=1
                else:
                    dcount+=1
            if lcount == rcount and ucount == dcount:
                return True
            else:
                return False
        else:
            return False
#Leetcode solution
#         x = y = 0
#         for move in moves:
#             if move == 'U': y += 1
#             elif move == 'D': y -= 1
#             elif move == 'L': x -= 1
#             elif move == 'R': x += 1

#         return x == y == 0
        