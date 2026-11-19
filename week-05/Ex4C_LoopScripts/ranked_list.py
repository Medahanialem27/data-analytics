favorite_things =["strawberry", "mango", " watermelon", "injera", "jerk chicken" ]

for number, item in enumerate(reversed(favorite_things), start=1):

    if number ==1:
        print(number, item, "<- top pick!")
    else:
        print(number, item)
