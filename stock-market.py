# [4, 5, 2, 3, 4, 12, 1] <- value of a stock at day i
# buy once, sell once
# maximize your profit

# input: array of stock prices
# output: tuple: (day to buy, day to sell)


def stock_market(prices):
    min_index = 0
    buy = 0
    sell = 0
    diff = 0 
    for i in range(len(prices)):
        if prices[i] < prices[min_index]:
            min_index = i
        
        
        temp = prices[i] - prices[min_index]
        if temp > diff:
            buy = min_index
            sell = i
            diff = temp

    return buy, sell

def st_mrkt_brute(prices):
    min_index = 0
    max_index = 0
    diff = 0 
    
    for i in range(len(prices)):
        for j in range(i, len(prices)):
            temp = prices[j] - prices[i]
            if temp > diff:
                diff = tempu
                max_index = j
                min_index = i
                
    return min_index, max_index


prices = [4, 5, 2, 3, 4, 12, 1]
print stock_market(prices)
print st_mrkt_brute(prices)
    
# http://articles.leetcode.com/best-time-to-buy-and-sell-stock/