class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while n not in visited:
            visited.add(n)

            sum=0

            while n > 0:
                mod = n%10
                n = n//10
                sum += (mod*mod)

            print(sum)
            n=sum

            if n==1:
                return True

        return False    
