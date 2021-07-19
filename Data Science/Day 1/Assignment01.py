import numpy as np

#Initialize of random array(A, B)
random_array_one = np.random.randint(20, 40, size=(2, 4))
random_array_two = np.random.randint(20, 40, size=(4, 2))

#Calcultation of dot product of A and B --> C
random_dot_product = np.dot(random_array_one, random_array_two)

#Calculation of sum of elements to array A and B
random_array_one_sum_of_element = np.sum(random_array_one)
random_array_two_sum_of_element = np.sum(random_array_two)


if random_array_one_sum_of_element >= random_array_two_sum_of_element:
    #Calculating transpose
    print("Transpose")
    result = np.transpose(random_dot_product)
else:
    #Calculating array C * 9
    print("Multiply array C by 9")
    result = random_dot_product * 9

#Display the result
print(result)