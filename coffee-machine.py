# Calculate sufficiency or availability
print('Write how many ml of water the coffee machine has:')
av_water = int(input())
print('Write how many ml of milk the coffee machine has:')
av_milk = int(input())
print('Write how many grams of coffee beans the coffee machine has:')
av_beans = int(input())
print('Write how many cups of coffee you will need:')
cups = int(input())
waterCups = av_water // 200
milkCups = av_milk // 50
beansCups = av_beans // 15
leastCups = min(waterCups,min(milkCups,beansCups))
if cups > leastCups:
    print('No, I can make only ' + str(leastCups) + ' cups of coffee.')
elif cups == leastCups:
    print('Yes, I can make that amount of coffee.')
else:
    extraCups = leastCups - cups
    print('Yes, I can make that amount of coffee (and even ' + str(extraCups) + ' more than that)')
