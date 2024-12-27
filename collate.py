def collatz(num):
  record = []
  while num != 1:
     if num % 2 == 0:
      record.append(num)
      num = int(num/2)
     elif num % 2 == 1:
      record.append(num)
      num = int((num*3)+1)
     else:
      print("What have you done?") 
  record.append(1)
  print(record)
x = int(input("What number would you like to see"))
collatz(x)
