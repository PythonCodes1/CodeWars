# I'm trying to find the difference between the oldest member to the youngest
# 8 kyu

def difference_in_ages(ages):
    return (min(ages), max(ages), max(ages) - min(ages))
