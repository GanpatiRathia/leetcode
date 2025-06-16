class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        no_of_steps = 0

        while(num != 0):
            if num%2 == 0 :
                num /= 2
                no_of_steps +=1 
            else :
                num -= 1
                no_of_steps +=1
                
        return no_of_steps
       