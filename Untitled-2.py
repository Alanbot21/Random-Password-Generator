
def work(work_progress):
 if salary >= 10000:
  work_progress = 100
 else:
  work_progress = work_progress
  return work_progress  
salary = int(input("What will you pay: "))
result = work(50)
print(f"Work progress: {result}")
print("BYE",work)