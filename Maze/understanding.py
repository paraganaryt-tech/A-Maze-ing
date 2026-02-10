from enum import Enum


class Season(Enum):
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4


print(Season.SPRING)
raise ValueError('Test')
print(Season.SUMMER.name)
#  print(Season.AUTUMN.name)
print(Season.SUMMER.value)
