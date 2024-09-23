import statistics

heights: list[float] = []
heights_counter: int = 0
player_counter: int = 0
while True:
    height: float = float(input(" enter player's height: "))
    if height == -999:
        break
    elif height < 1.6 or height > 3:
        continue
    else:
        heights.append(height)
        if height > 2.0:
            heights_counter += 1
print(heights)
# exc 1
print(f'there were a total of {len(heights)} valid heights')
# exc 2
print(f"the tallest player height is {max(heights)}")
# exc 3
print(f"the shortest player height is {min(heights)}")
# exc 4
print(f"the players average height is {statistics.mean(heights)}")
# exc 5
print(f"there were a total of {heights_counter} players higher than 2 meters")
# exc 6
print(heights)
for i in range(len(heights)):
    if i > statistics.mean(heights):
        player_counter += 1
    else:
        continue
print(f"there were a total of {player_counter} player higher than the average")
