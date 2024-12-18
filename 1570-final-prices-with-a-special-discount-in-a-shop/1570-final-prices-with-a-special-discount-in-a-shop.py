class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        #THE INTUITION OF USING 2 POINTERS COME FROM THE FACT THAT FOR ANY ITH VALUE IN ANSWER WE NEED TO ACCESS TWO VALUES IN INPUT ARRAY
        i = 0 
        j = i +1
        
        while i <j and j < len(prices) :
            #STEP 1: INCREASE I TO  NEXT INDEX AND J NEXT TO I IF ITH ELEMENT GREATER THAN JTH AFTER PERFORMING THE OPERATION
            if prices[i] >= prices[j]:
                
                prices[i] = prices[i] - prices[j]
                i = i +1
                j = i+1
            
            else:
                
            #STEP2:  IF THERE IS NO JTH ELEMENT WHICHH IS SMALLER THAN ITH AND YOU REACH END OF ARRAY THEN INCREMENT i and shift back j to i+1
            
                if (j == len(prices)-1):
                    i = i +1
                    j = i +1
                    
            # STEP3 :ELSE INCREASE j by 1 and re enter in to step 1 if condition satisfies
                else:
                    j = j +1
        return prices
            
            
            
        