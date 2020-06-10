#Author - Jonathan Wong, jfw5328@psu.edu

#inputs
people = int(input('How many people are sharing pizza? '))
pizza = int(input('How many pizzas will be ordered? '))
two_slice_people = int(input('How many will limit themselves to two slices? '))

#calculating total amount of slices two_slice_people will consume
two_slice_amount = two_slice_people * 2

#8 slices per pizza
total_pizza_slices = pizza * 8

#calculating total slices after subtracting slices consumed by two_slice_people
total_after = total_pizza_slices - two_slice_amount

#calculating people left after two_slice_people consume their share 
people_after = people - two_slice_people

#slices if divided equally among people
slices_per_person = total_after // people_after

#adding 1 slice to people who get remaining slices
remaining_slices = slices_per_person + 1

#calculating slices one would get if the total could be divided equally
equal_slices = total_after % people_after

#calculating people who will get remaining slice amount
remaining_slices_people = equal_slices

#calculating who will get equal slice amount
equal_slices_people = people_after - equal_slices

##print('You will divide ', total_pizza_slices, 'slices -- ', equal_slices_people, 'will have', slices_per_person,
##      'slices,', remaining_slices_people, 'will have', remaining_slices, 'slices, and', two_slice_people, 'will have 2.' )

print('You will divide ', total_pizza_slices, 'slices -- ', two_slice_people, 'will have 2 slices,', equal_slices_people,
      'will have', slices_per_person, 'slices, and', remaining_slices_people, 'will have', remaining_slices, 'slices.')
