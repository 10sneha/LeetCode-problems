class Solution:
    def intToRoman(self, num: int) -> str:
        d = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M',
        4:'IV',9:'IX',40:'XL',90:'XC',400:'CD',900:'CM'}

        result =''

        for n in sorted(d.keys(),reverse=True):
            while n <= num:
                result += d[n]
                num -= n
        
        return result


        