
coins = [25, 10, 5, 1]
coins_1 = coins[-3:0, -1]

def num_coins(cents):
    if cents < 1:
        return 0

    coins = [25, 10, 1]
    coins_1 = coins[-3:0]
    num_of_coins = 0

# plus 7 min to timer
#minimizing coins: create recursive function to loop through all possible combinations of coins for given amount of coins
# eg. 25 > 1q, 2d 1n, 5n, 25c, 2d 5c, 4n 5c, 3n 10c, 2n 15c, 1n 20c,
# eg. 31 > 1q 6c, 3d 1c, 
# 
#
# 
#  iterate over each starting postition of list(coins)
#  find solution for number of coins and append to list coins
#  return lowest number in list coins
#0:1, 1:
# for coin in coins[0:4]
    for coin in coins:
        for coin in coins:
            num_of_coins += cents // coin
            cents = cents - ((cents//coin)*coin)
            if cents == 0:
                break
        return num_of_coins


#99> 3q, 2d, 4c
print (num_coins(31))
print (coins_1)




