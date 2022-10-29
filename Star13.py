with open("/home/alimahfoud24/ALI/inputDay7.txt") as file:
    Crabs_Positions = [int(x) for x in file.readline().strip('\n').split(',')]
    Sorted_Crabs_Positions = sorted(Crabs_Positions)
    median = Sorted_Crabs_Positions[len(Crabs_Positions)//2]

distance_to_move = 0
for i in Crabs_Positions:
    distance_to_move += abs(median-i)


print('The horizontal position that the crabs can align to using the least fuel possible: ',
      median, '. They will be using this amount of fuel: ', distance_to_move)
