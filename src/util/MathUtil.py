from math import *

class MathUtil:
    @staticmethod
    def isPrime(number):
        '''
        Returns whether a number is prime
        '''
        limit = int(sqrt(number))
        
        for div in range(2,limit+1):
            if number % div == 0:
                return False
            
        return True
    
    @staticmethod
    def getPrimes(number):
        '''
        Returns a list of prime numbers less than or equal to
        number
        '''
        primes = [2]
        for div in range(3, number + 1, 2):
            if MathUtil.isPrime(div):
                primes.append(div)
                
        return primes
    
    
    @staticmethod
    def isPalindrome(number):
        '''
        Returns True if the passed number is a palindrome, else returns False
        '''
        size = len(str(number))
        digits = []
        
        for pos in range (size - 1, -1, -1):
            sig = number / 10 ** pos
            digits.append(sig)
            number -= sig * (10 ** pos)
            
        for pos in range (0, size / 2):
            if digits[pos] != digits[size - 1 - pos]:
                return False
        
        return True

    @staticmethod
    def getLCM(numbers):
        '''
        Returns the lowest common multiplier of a list of numbers
        '''
        largest = max(numbers)
        primes = MathUtil.getPrimes(largest)
        #print(primes)
        divs = []
        
        for div in primes:
            changed = True
            while changed:
                changed = False
                temp = []
                for num in numbers:
                    if num % div == 0:
                        temp.append(num / div)
                        changed = True
                    else:
                        temp.append(num)
                
                numbers = temp
                if changed:
                    divs.append(div)
                #print(divs, numbers)
                
        return MathUtil.lprod(divs) * MathUtil.lprod(numbers)
    
    @staticmethod
    def lprod(l):
        ''' 
        Calculate product of list items 
        '''
        if l:
            return l.pop() * MathUtil.lprod(l)
        else:
            return 1
        
    @staticmethod
    def getSquaredSum(lst):
        sum = 0
        for sq in lst:
            sum += sq ** 2
            
        return sum
    
    @staticmethod
    def getSumSquared(lst):
        sum = 0
        for num in lst:
            sum += num
            
        return sum ** 2
        