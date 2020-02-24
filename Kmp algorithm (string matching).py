# -*- coding: utf-8 -*-

"""

Created on Mon Feb 24 21:10:32 2020

@author: Shouzeb

"""

#Knuth–Morris–Pratt algorithm or KMP algorithm
def testing_Data():
    p1 = "aa"
    t1 = "aaaaaaaa"

    kmp = KMP()
    assert(kmp.searching(t1, p1) == [0, 1, 2, 3, 4, 5, 6])
    print("test 1 pass")
    
    p2 = "abc"
    t2 = "abdabeabfabca"
    print("test 2 pass")


    assert(kmp.searching(t2, p2) == [9])

    p3 = "aab"
    t3 = "aaabaacbaab"

    assert(kmp.searching(t3, p3) == [1, 8])
    print("test 3 pass")
    print("all test pass")
    
class KMP:
    def partial(self, pattern):
        """ Calculate partial match table: String -> [Int]"""
        ret = [0]
        
        for i in range(1, len(pattern)):
            j = ret[i - 1]
            while j > 0 and pattern[j] != pattern[i]:
                j = ret[j - 1]
            ret.append(j + 1 if pattern[j] == pattern[i] else j)
        return ret
        
    def searching(self, T, P):
        
        """ 
        KMP search main algorithm: String -> String -> [Int] 
        Return all the matching position of pattern string P in T
        """
        partial, ret, j = self.partial(P), [], 0
        
        for i in range(len(T)):
            while j > 0 and T[i] != P[j]:
                j = partial[j - 1]
            if T[i] == P[j]: j += 1
            if j == len(P): 
                ret.append(i - (j - 1))
                j = partial[j - 1]
            
        return ret

  
testing_Data();