import time
import random

def selection_sort(arr):
    for k in range (0, len(arr)-1): #check each cell
        min=k
        n=k+1
        while (n < len(arr)):
            if arr[n] < arr[min]:#check if cell j is less than cell j+n
                min = n
            n+=1
        temp = arr[min] # may need to fix this swap
        arr[min] = arr[k]
        arr[k] = temp
    return arr #dont know if we need but it helps to debug

def insertion_sort(arr):
    for k in range(1, len(arr)):
        cur = arr[k]
        j = k
        while j > 0 and arr[j-1] > cur:
            arr[j] = arr[j-1]
            j = j - 1
        arr[j] = cur
    return arr ###possible debug

if __name__ == '__main__':
    # Initializing variables and selecting length

    minVal = 0 #for random array
    maxVal = 100
    start = 0.0
    end = 0.0
    averageTimes = [0] * 6
    length = int(input('How many values should be generated? '))

    arr_sel_inc = [0] * length
    arr_sel_dec = [0] * length
    arr_sel_ran = [0] * length
    arr_ins_inc = [0] * length
    arr_ins_dec = [0] * length
    arr_ins_ran = [0] * length
    tempArray = [0] * length

    times_sel_inc = [0] * 5
    times_sel_dec = [0] * 5
    times_sel_ran = [0] * 5
    times_ins_inc = [0] * 5
    times_ins_dec = [0] * 5
    times_ins_ran = [0] * 5
    tempTimes = [0] * 5

    # Generating 3 sets of 2 identical arrays
    for x in range(0,length):
        arr_sel_inc[x] = x + 1
    arr_ins_inc = arr_sel_inc
    #print("arr_ins_inc is " + str(arr_ins_inc))
    #print("arr_sel_inc is " + str(arr_sel_inc))

    for x in range(0,length):
        arr_sel_dec[x] = length - x
    arr_ins_dec = arr_sel_dec
    #print("arr_sel_dec is " + str(arr_sel_dec))
    #print("arr_ins_dec is " + str(arr_ins_dec))

    for x in range(0, length):
        arr_sel_ran[x] = random.randint(minVal, maxVal)
    arr_ins_ran = arr_sel_ran
    #print("arr_sel_ran is " + str(arr_sel_ran))
    #print("arr_ins_ran is " + str(arr_ins_ran))

    # Creating arrays of arrays
    # Indexing key:
    # Selection Sorting: Increasing = 0, Decreasing = 1, Random = 2
    # Insertion Sorting: Increasing = 3, Decreasing = 4, Random = 5
    array_Arrays = [arr_sel_inc, arr_sel_dec, arr_sel_ran, \
    arr_ins_inc, arr_ins_dec, arr_ins_ran]
    array_Times = [times_sel_inc, times_sel_dec, times_sel_ran, \
    times_ins_inc, times_ins_dec, times_ins_ran]

    # Looping through Selection and then Insertion
    for index in range(0, 3):   # Looping through selection_sort
        for count in range(0,5): #
            #print("count is " + str(count)) ### DEBUG
            #print("index is " + str(index)) ### DEBUG
            #print(str(array_Arrays[index])) ### DEBUG
            #print(type(array_Arrays[index])) ### DEBUG
            tempArray = array_Arrays[index][:]
            #print("temparray before is " + str(tempArray)) ### DEBUG
            start = time.clock()
            selection_sort(tempArray)
            #print("temparray after is " + str(tempArray)) ### DEBUG
            end = time.clock()
            tempTimes[count] = end - start
            #print("time was " + '{:.20f}'.format(end - start)) ### DEBUG
            #print("mainarray is " + str(array_Arrays[index])) ### DEBUG
        array_Times[index] = tempTimes[:]

    for index in range(3, 6):   # Looping through insertion_sort
        for count in range(0,5):
            tempArray = array_Arrays[index][:]
            #print("count is " + str(count)) ### DEBUG
            #print("index is " + str(index)) ### DEBUG
            #print(str(array_Arrays[index])) ### DEBUG
            #print(type(array_Arrays[index])) ### DEBUG
            #print("temparray before is " + str(tempArray))
            start = time.clock()
            insertion_sort(tempArray)
            end = time.clock()
            #print("temparray after is " + str(tempArray))
            tempTimes[count] = end - start
        array_Times[index] = tempTimes[:]

    # Computing average times:
    # Indexing key:
    # Selection Sorting: Increasing = 0, Decreasing = 1, Random = 2
    # Insertion Sorting: Increasing = 3, Decreasing = 4, Random = 5
    #print(str(array_Times))
    for index in range(0,6):
        tempVal = 0
        tempTimes = array_Times[index][:]
        #print(str(tempTimes))
        for count in range(0,5):
            tempVal = tempVal + tempTimes[count]
        #print(str(tempVal))
        averageTimes[index] = tempVal / 5
        #print(str(averageTimes))
    # Printing results:
    print(str(length) + '-Val Increasing Selection: ' + '{:.20f}'.format(averageTimes[0]))
    print(str(length) + '-Val Decreasing Selection: ' + '{:.20f}'.format(averageTimes[1]))
    print(str(length) + '-Val Random Selection:     ' + '{:.20f}'.format(averageTimes[2]))
    print(str(length) + '-Val Increasing Insertion: ' + '{:.20f}'.format(averageTimes[3]))
    print(str(length) + '-Val Decreasing Insertion: ' + '{:.20f}'.format(averageTimes[4]))
    print(str(length) + '-Val Random Insertion:     ' + '{:.20f}'.format(averageTimes[5]))
