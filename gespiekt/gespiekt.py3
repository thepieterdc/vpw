for e in range(int(input())):
    students, points = str(input()+" 999").split(' ', 1)
    if int(students) < 2:
        print("spieken kon niet")
    else:
        points = points.split(' ')
        diff, diffp = 101, 0
        for i in range(1, int(students)):
            pts = abs(int(points[i]) - int(points[i - 1]))
            if pts < diff:
                diff = pts
                diffp = i - 1

                if diff == 0:
                    break

        print("{} en {} zijn{} verdacht".format(diffp + 1, diffp + 2, " zwaar" if diff == 0 else ""))
