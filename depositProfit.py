# https://app.codesignal.com/arcade/intro/level-7/8PxjMSncp9ApA4DAb
def depositProfit(deposit, rate, threshold):
    year_count = 0
    while deposit < threshold:
        deposit = deposit + (deposit * (rate/100))
        year_count += 1
    return year_count

    # def depositProfit(deposit, rate, threshold):

    # return math.ceil(math.log(threshold/deposit, 1+rate/100))