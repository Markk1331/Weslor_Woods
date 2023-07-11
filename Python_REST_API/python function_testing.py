student = {"name":"Rolf","grades":(89,90,93,78,90)}

def average(sequence):
    sequence = sequence['grades']
    return sum(sequence) / len(sequence)

print(average(student))