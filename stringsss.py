def reverse(x):
        """
        :type x: int
        :rtype: int
        """
        digit=str(x)
        
        if(digit[0] == '-'):
            rev = digit[1:][::-1]
            rev = "-"+rev
        else:
            rev = digit[::-1]
        
        n=int(rev)

        if n > 2 ** 31 -1 or n < -2 ** 31:
            return 0
        return n

print(reverse(-12345))