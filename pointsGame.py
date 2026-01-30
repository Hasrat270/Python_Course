initialPoints = 50
earnedPoints = input("Enter earned points: ")
losedPoints = input("Enter lost points: ")
initialPoints += int(earnedPoints)
initialPoints -= int(losedPoints)
print("Total points:", initialPoints)