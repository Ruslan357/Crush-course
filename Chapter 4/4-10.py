numbers = list('0123456789')

message1 = 'The first three item in the list are:'
message2 = 'The items from the middle of the list are:'
message3 = 'The last three items in the list are:'

print(message1, numbers[:3])
print(message2, numbers[int(len(numbers) / 2) - 1:int(len(numbers) / 2) + 2])
print(message1, numbers[-3:])
