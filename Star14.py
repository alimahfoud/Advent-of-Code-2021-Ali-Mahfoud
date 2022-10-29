with open("/home/alimahfoud24/ALI/inputDay7.txt") as file:
    Crabs_Positions = [int(x) for x in file.readline().strip('\n').split(',')]
    average = round(sum(Crabs_Positions)//len(Crabs_Positions))
distance_to_move = 0

for i in Crabs_Positions:
    n = abs(i - average)+1
    fuel_cost = abs(n*(n-1)//2)
    distance_to_move += fuel_cost


print('The horizontal position that the crabs can align to using the least fuel possible: ',
      average, '. They will be using this amount of fuel: ', distance_to_move)
