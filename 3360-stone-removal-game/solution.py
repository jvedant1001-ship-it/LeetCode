class Solution:
    def canAliceWin(self, n):
        remove = 10
        alice_turn = True

        while n >= remove:
            n -= remove
            remove -= 1
            alice_turn = not alice_turn

        # Current player cannot move, so the previous player wins
        return not alice_turn
