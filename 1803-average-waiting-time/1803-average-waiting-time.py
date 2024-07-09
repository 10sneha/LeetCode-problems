class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        wait = 0
        time = 0
        for cust in customers:
            if time < cust[0]:
                time = cust[0] 
            wait += (time + cust[1] - cust[0])
            time += cust[1]
        return wait / len(customers)
         