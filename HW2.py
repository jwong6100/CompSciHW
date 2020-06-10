#Author - Jonathan Wong, jfw5328@psu.edu

#populating dictionaries and lists
property_groups_size = {'purple':2, 'light blue':3, 'maroon':3, 'orange':3, 'red':3, 'yellow':3, 'green':3,
                        'dark blue':2}
property_groups_size_words = {'purple':'two', 'light blue':'three', 'maroon':'three', 'orange':'three',
                              'red':'three', 'yellow':'three', 'green':'three', 'dark blue':'two'}
property_groups_cost = {'purple':50, 'light blue':50, 'maroon':100, 'orange':100, 'red':150, 'yellow':150,
                        'green':200, 'dark blue':200}
number_of_houses = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
                    'eleven', 'twelve']
size_of_property_group = ['none', 'one', 'two']

#user inputs
color = input('Which color block will you be building on? ')
money = int(input('How much money do you have to spend? '))

print('There are ' + property_groups_size_words[color] + ' properties and each house costs ' +
      str(property_groups_cost[color]))

#converting values to integers
int_size = int(property_groups_size[color])
int_cost = int(property_groups_cost[color])

#calculations for total houses and the divisions between the size of the property group
total_houses = money // int_cost
divided_total_houses = total_houses // int_size
remaining_total_houses = divided_total_houses + 1

#calculating who will get x number of houses
equal_houses = total_houses % int_size
remaining_size = equal_houses
other_int_size = int_size - equal_houses

print('You can build ' + str(number_of_houses[total_houses]) + ' house(s) -- ' +
      str(size_of_property_group[other_int_size]) + ' will have ' + str(number_of_houses[divided_total_houses]) +
      ' and ' + str(size_of_property_group[remaining_size]) + ' will have ' + str(number_of_houses[remaining_total_houses]))

###test
##print(divided_total_houses)
##print(remaining_total_houses)
##print(equal_houses)
##print(other_int_size)
