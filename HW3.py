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

x = 0

#user inputs
while x == 0:
    color = input('Which color block will you be building on? ')
    if color in property_groups_size:    
        print('There are ' + property_groups_size_words[color] + ' properties and each house costs ' +
              str(property_groups_cost[color]))
        money = int(input('How much money do you have to spend? '))
        x = 1
    else:
        print('Sorry, that is not a color on the list')

#converting values to integers
int_size = int(property_groups_size[color])
int_cost = int(property_groups_cost[color])

#calculations for total houses and the divisions between the size of the property group
total_houses = money // int_cost
divided_total_houses = total_houses // int_size
more_total_houses = divided_total_houses + 1

#calculating which properties will get x number of houses
equal_houses = total_houses % int_size
remaining_props = equal_houses
other_props = int_size - equal_houses

#outputs
if money < int_cost:
    print('You cannot afford even one house.')
elif divided_total_houses > 5:
    print('You can build ' + str(total_houses) + ' house(s) -- ' + str(other_props) + ' will have a hotel.')
elif more_total_houses == 5:
    print('You can build ' + str(total_houses) + ' house(s) -- ' + str(other_props) + ' will have ' +
          str(divided_total_houses) + ' and ' + str(remaining_props) + ' will have a hotel')
elif remaining_props > 0:
    print('You can build ' + str(total_houses) + ' house(s) -- ' +
      str(other_props) + ' will have ' + str(divided_total_houses) +
      ' and ' + str(remaining_props) + ' will have ' + str(more_total_houses))
elif remaining_props == 0:
    print('You can build ' + str(total_houses) + ' house(s) -- ' +
      str(other_props) + ' will have ' + str(divided_total_houses))

###test
##print(divided_total_houses)
##print(equal_houses)
##print(other_int_size)
