class Solution(object):
    def recoverOrder(self, order, friends):
        
        friend_set = set(friends)
        return [x for x in order if x in friend_set]
