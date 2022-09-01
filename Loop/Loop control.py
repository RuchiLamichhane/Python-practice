# Loop control using Break
x="Hey there. how are you ?"
for i in x :
  if i == "." :
    break
  print(i, end="")


# Loop control using Continue
for i in [1, 13, 56, 4, 6]:
    if i > 10:
      continue
    print(i)
