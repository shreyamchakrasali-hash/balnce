import sys

if len(sys.argv)==2:
  balance=int(sys.argv[1])
  print("User provided input")
else:
  print("No Input given ,Using default")
  balance=1000

deposit=500
updated=balance+deposit

print("Updated Balance",updated)
