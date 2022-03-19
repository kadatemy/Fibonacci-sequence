nth_term = int(input("How many terms? "))

n1, n2 = 0, 1
count = 0

# Check for valid terms
if nth_term <= 0:
  print("Please enter a positive integer")

# Return n1 if only one term is present
elif nth_term == 1:
  print("Sequence upto", nth_term, ":")
  print(n1)

# If more than one, generate sequence.
else:
  print("Fibonnaci sequence:")
  while count < nth_term:
    print(n1)
    nth = n1 + n2
  # Update values
    n1 = n2
    n2 = nth
    count += 1
