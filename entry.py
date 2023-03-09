# import aristhmetics_module
# import statistics_module

# print (aristhmetics_module.sum(1,2))
# print (statistics_module.sum(1,2))

# from aristhmetics_module import sum as asum
# print(asum(1,2))
# from statistics_module import sum as ssum
# print(ssum(1,2))

from number_package.aristhmetics_module import sum as asum
print(asum(1,2))
from number_package.statistics_module import sum as ssum
print(ssum(1,2))