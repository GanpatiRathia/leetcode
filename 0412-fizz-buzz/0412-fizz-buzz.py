class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer = []
        for i in range(1, n + 1):
            current_answer = ""

            # Check for divisibility by 3
            if i % 3 == 0:
                current_answer += "Fizz"

            # Check for divisibility by 5 (independent of divisibility by 3)
            if i % 5 == 0:
                current_answer += "Buzz"

            # If current_answer is still empty, it means it's not divisible by 3 or 5
            if not current_answer:
                answer.append(str(i))
            else:
                answer.append(current_answer)

        return answer