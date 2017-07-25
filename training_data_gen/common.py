import numpy as np


def wind_to_dvorak(wind):
    arr = np.zeros(16)

    if wind <= 15:
        # too weak
        arr[0] = 1
    elif wind == 20:
        # T1.0 -> tropical depression
        arr[1] = 1
    elif wind == 25:
        # T1.5
        arr[2] = 1
    elif wind == 30:
        # T2.0
        arr[3] = 1
    elif wind == 35 or wind == 40:
        # T2.5 -> tropical storm
        arr[4] = 1
    elif wind == 45 or wind == 50:
        # T3.0
        arr[5] = 1
    elif wind == 55 or wind == 60:
        # T3.5
        arr[6] = 1
    elif wind == 65 or wind == 70:
        # T4.0 -> category 1
        arr[7] = 1
    elif wind == 75 or wind == 80:
        # T4.5
        arr[8] = 1
    elif 85 <= wind <= 95:
        # T5.0 -> category 2
        arr[9] = 1
    elif 100 <= wind <= 110:
        # T5.5 -> category 3
        arr[10] = 1
    elif wind == 115 or wind == 120:
        # T6.0 -> category 4
        arr[11] = 1
    elif 125 <= wind <= 135:
        # T6.5
        arr[12] = 1
    elif wind == 140 or wind == 145:
        # T7.0 -> category 5
        arr[13] = 1
    elif wind == 150 or wind == 155:
        # T7.5
        arr[14] = 1
    elif wind >= 160:
        # T8.0
        arr[15] = 1

    return arr

if __name__ == '__main__':
    for i in range(5, 175, 5):
        print(str(i) + " is " + str(wind_to_dvorak(i)))
