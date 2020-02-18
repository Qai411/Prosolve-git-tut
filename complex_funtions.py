#simple_interest
def simple_interest(principal, rate, time):
    calculation = 0.01 * principal * rate * time
    return calculation
print(simple_interest(1500,0.2,3))

#data_transfer_speed
def calculate_speed(data_size, time):
    calculation = data_size/time
    return calculation
print(calculate_speed(150000, 120))
