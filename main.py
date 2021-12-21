low=0
medium=0
high=0
numberofbatteries=int(input("enter the number of batteries"))
for i in range(numberofbatteries):
  battery_charge_cycles = int(input("Enter the number of  charge cycles"))
  if(battery_charge_cycles<150):
    low=low+1
  elif(battery_charge_cycles > 150 && battery_charge_cycle < 649):
    medium=medium+1
  else:
    high=high+1
print("Low count"low)
print("medium count"medium)
print("high count"high)

def count_batteries_by_usage(cycles):
  return {
    "lowCount": 0,
    "mediumCount": 0,
    "highCount": 0
    
  }


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  assert(counts["lowCount"] == 1)
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 2)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
