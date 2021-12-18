salary_list = [7.3, 8.5, 11, 12.7, 15.2, 21.12, 27.35]
afterIndex = list(map(lambda x: round(1.3*x, 2), salary_list)) #[1.3, 2.6, 3.9, ...]
sumIndex = list(map(lambda x: round(0.3*x, 2), salary_list)) #[0.3, 2*0.3, ...]
print ("Salary table: ")
print (" ".join(map(str, afterIndex)))
print (" ".join(map(str, sumIndex)))