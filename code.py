
my_dict = {}
lst = []

def number_of_occurances(input_line = "")

  for word in input_line.split():

    if word not in my_dict:

      my_dict[word] = 0

    else:

      my_dict[word] += 1

    lst.append(my_dict[word])

  return ' '.join(list(map(str, lst)))
  
