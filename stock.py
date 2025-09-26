# 121. Best Time to Buy and Sell Stock

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.


def maxprofit (prices):
    buy_price = prices[0]
    profit = 0 

    for p in prices [1 :]:
        if buy_price > p :
            buy_price = p 
        profit = max (profit , p - buy_price)
    return profit

prices = [7,1,5,3,6,4 ]
print(" the best time to buy sell to make profit is :", maxprofit(prices))
    