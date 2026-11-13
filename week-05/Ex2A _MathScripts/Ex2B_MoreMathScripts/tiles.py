import math
room_length = 10
room_width = 12
tiles_per_box = 12

tiles_needed = room_length * room_width
tiles_with_extra = math.ceil(tiles_needed * 1.10)
boxes_needed = math.ceil(tiles_with_extra / tiles_per_box)
print(f"Tiles needed with 10% extra: {tiles_with_extra}")
print(f"Boxes to buy: {boxes_needed}")
