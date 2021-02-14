# In this program the user enters a starting
# value, stopping value, and step
# The program then counts up

# Get inputs from user
start_num = int(input("Start?"))
stop_num = int(input("Stop?"))
step = int(input("Change each time?"))
# Print the numbers
for num in range(start_num, stop_num+1, step):
    print(num)