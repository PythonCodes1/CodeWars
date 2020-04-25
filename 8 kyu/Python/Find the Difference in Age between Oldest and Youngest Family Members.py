# Finding the difference between the oldest and youngest member
# 8 kyu

def difference_in_ages(ages):
    return (min(ages), max(ages), max(ages) - min(ages))
