'''
Created on Sep 24, 2011

@author: sambit
'''

from math import *
from util.MathUtil import *

class EulerProblemTo10(object):
    '''
    classdocs
    '''


    def __init__(self, problem, args):
        '''
        Constructor
        '''
        method = getattr(self, problem)
        method(args)
        
    
    def problem1(self, args):
        '''
        If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
        
        Add all the natural numbers below one thousand that are multiples of 3 or 5.
        '''
        stmt = "Add all the natural numbers below one thousand that are multiples of 3 or 5."
        sum = 0
        for num in range(1,1000):
            if (num % 3 == 0) or (num % 5 == 0):
                sum += num
                
        print(stmt)
        print("Brute force: %d" % sum)
        
        sum = 0
        for num in range(3, 1000, 3):
            sum += num
        
        for num in range (5, 1000, 5):
            if (num % 15 != 0):
                sum += num
            
        print("Better: %d" % sum)
        
    def problem2(self, args):
        '''
        Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, 
        the first 10 terms will be:

        1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

        By considering the terms in the Fibonacci sequence whose values 
        do not exceed four million, find the sum of the even-valued terms.
        '''
        stmt = "By considering the terms in the Fibonacci sequence whose \
values do not exceed four million, find the sum of the even-valued terms."
        print(stmt)
        
        fib1 = 1
        fib2 = 2
        newfib = 0
        sum = 2
        
        while newfib <= 4000000:
            newfib = fib1 + fib2
            fib1 = fib2
            fib2 = newfib
            if (newfib % 2 == 0):
                sum += newfib
                
        print(sum)
        
    def problem3(self, args):
        '''
        The prime factors of 13195 are 5, 7, 13 and 29.

        What is the largest prime factor of the number 600851475143 ?
        '''
        stmt = "What is the largest prime factor of the number 600851475143 ?"
        
        NUMBER = 600851475143
        print(stmt)
        upto = int(sqrt(NUMBER))
        maxPrime = -1
        
        for div in range (3,upto,2):
            if NUMBER % div == 0 and MathUtil.isPrime(div):
                maxPrime  = div
                
        if maxPrime == -1:
            print("NaN")
        else:
            print(maxPrime)
            
    def problem4(self, args):
        # print(MathUtil.isPalindrome(201343102))
        '''
        A palindromic number reads the same both ways. The largest palindrome made from the 
        product of two 2-digit numbers is 9009 = 91 X 99.
        
        Find the largest palindrome made from the product of two 3-digit numbers.
        '''
        
        stmt = "Find the largest palindrome made from the product of two 3-digit numbers."
        print(stmt)
        
        pals = []
        for left in range(999,100,-1):
            for right in range(999,100,-1):
                prod = left * right
                if MathUtil.isPalindrome(prod):
                    pals.append(prod)
            
        print(max(pals))
        
    def problem5(self, args):
        '''
        2520 is the smallest number that can be divided by each of the 
        numbers from 1 to 10 without any remainder.

        What is the smallest positive number that is evenly divisible by 
        all of the numbers from 1 to 20?
        '''
        stmt = "What is the smallest positive number that is evenly divisible by \
        all of the numbers from 1 to 20?"
        
        print(stmt)
        lst = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        print(MathUtil.getLCM(lst))
        
    def problem6(self, args):
        '''
        The sum of the squares of the first ten natural numbers is,
        1^2 + 2^2 + ... + 10^2 = 385

        The square of the sum of the first ten natural numbers is,
        (1 + 2 + ... + 10)^2 = 55^2 = 3025

        Hence the difference between the sum of the squares of the first ten natural 
        numbers and the square of the sum is 3025 - 385 = 2640.
        
        Find the difference between the sum of the squares of the first one hundred 
        natural numbers and the square of the sum.
        '''
        stmt = "Find the difference between the sum of the squares of the first one hundred \
        natural numbers and the square of the sum."
        
        lst = []
        for num in range(1,101):
            lst.append(num)
            
        sumSqrd = MathUtil.getSumSquared(lst)
        sqrdSum = MathUtil.getSquaredSum(lst)
        
        print("%d - %d = %d" % (sumSqrd, sqrdSum, (sumSqrd - sqrdSum)))
        
    def problem7(self, args):
            '''
            By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

            What is the 10 001st prime number?
            '''
            stmt = "What is the 10 001st prime number?"
            print(stmt)
            
            primes = []
            num = 2
            primeIdx = 10001
            
            while len(primes) < primeIdx + 1:
                if MathUtil.isPrime(num):
                    primes.append(num)
                num += 1
                
            #print(primes)
            print(primes[primeIdx - 1])
            
    def problem8(self, args):
            '''
            Find the greatest product of five consecutive digits in the 1000-digit number.

            73167176531330624919225119674426574742355349194934
            96983520312774506326239578318016984801869478851843
            85861560789112949495459501737958331952853208805511
            12540698747158523863050715693290963295227443043557
            66896648950445244523161731856403098711121722383113
            62229893423380308135336276614282806444486645238749
            30358907296290491560440772390713810515859307960866
            70172427121883998797908792274921901699720888093776
            65727333001053367881220235421809751254540594752243
            52584907711670556013604839586446706324415722155397
            53697817977846174064955149290862569321978468622482
            83972241375657056057490261407972968652414535100474
            82166370484403199890008895243450658541227588666881
            16427171479924442928230863465674813919123162824586
            17866458359124566529476545682848912883142607690042
            24219022671055626321111109370544217506941658960408
            07198403850962455444362981230987879927244284909188
            84580156166097919133875499200524063689912560717606
            05886116467109405077541002256983155200055935729725
            71636269561882670428252483600823257530420752963450
            '''
            stmt = "Find the greatest product of five consecutive digits in the 1000-digit number."
            print(stmt)
            
            ls = list("73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450")
            
            prod = 0
            sz = len(ls)
            slice = []
            lsint = []
            max = 0
            for start in range (0, sz - 4):
            #for start in range (0, 4):
                slice = ls[start:start+5]
                lsint = sum([map(int,s) for s in slice], [])
                #print(lsint)
                prod = MathUtil.lprod(lsint)
                if max < prod:
                    max = prod
                
            print(max)
            
    def problem9(self, args):
        '''
        A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
        a^2 + b^2 = c^2

        For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

        There exists exactly one Pythagorean triplet for which a + b + c = 1000.
        Find the product abc.
        '''
        stmt = "There exists exactly one Pythagorean triplet for which a + b + c = 1000. \
        Find the product abc."
        print(stmt)
        
        for a in range (1, 999):
            for b in range (1, 999):
                if a + b >= 1000:
                    continue
                if a**2 + b**2 == (1000 -a -b)**2:
                    print("%d X %d X %d = %d" % (a, b, (1000 -a -b), a*b*(1000-a-b)))
                    return
        print("No such triplet")
        
    def problem10(self, args):
        '''
        The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

        Find the sum of all the primes below two million.
        '''
        stmt = "Find the sum of all the primes below two million."
        print(stmt)
        
        primes = MathUtil.getPrimes(2000000)
        tot = sum(primes)
        
        print(tot)