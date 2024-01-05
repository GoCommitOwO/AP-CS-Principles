def bubbleSort(list):
    for lcv in range(len(list)-1,0,-1):
        for lcv2 in range(lcv):
            if list[lcv2]>list[lcv2+1]:
                temp = list[lcv2]
                list[lcv2] = list[lcv2+1]
                list[lcv2+1] = temp

def selectionSort(list):
    for lcv in range(len(list)-1,0,-1):
        maxPos = 0
        for lcv2 in range(1,lcv+1):
            if list[lcv2]>list[maxPos]:
                maxPos = lcv2
        temp = list[lcv]
        list[lcv] = list[maxPos]
        list[maxPos] = temp

def insertionSort(list):
    for lcv in range(1,len(list)):
        currentVal = list[lcv]
        position = lcv
        while position>0 and list[position-1]>currentVal:
            list[position]=list[position-1]
            position = position-1
        list[position]=currentVal

def pythonSort(list):
    list.sort()

def print_sort_time(sort_name, time):
    print(f"\n{sort_name} sort time: {time:.7f} seconds")