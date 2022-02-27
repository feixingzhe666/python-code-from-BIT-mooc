def mean(numbers):  #计算平均值
    s = 0.0
    for num in numbers:
        s += num
        return s / len(numbers)
