class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans=[]
        for i in range(1,1+n):
            if i%3==0 and i%5==0 :
               ans.append("FizzBuzz")
            elif i%3==0 : 
                ans.append("Fizz")
            elif i%5==0:
                ans.append("Buzz")    
            else:
                ans.append(str(i))

        return ans          
