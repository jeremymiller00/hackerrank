def countingValleys(n, s):
    level = 0
    levels = [0]
    valleys = 0
    for step in s:
        if step == 'U':
            level += 1
        elif step == 'D':
            level -= 1
        else:
            print("Invalid Input")
            break
        levels.append(level)

    for i in range(len(levels)-1):
        if levels[i]==0 and levels[i+1]==-1:
            valleys += 1
    return valleys