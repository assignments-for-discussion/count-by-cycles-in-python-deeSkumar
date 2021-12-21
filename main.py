
def count_batteries_by_usage(cycles):
  count1={'lowCount':0,'mediumCount':0,'highCount':0}
  for cycle in cycles:
    if (cycle<50):
      counts1['lowCount']+=1
    elif (cycle>=150 and cycle<650):
      counts1['mediumCount']+=1
    else:
      counts1['highCount']+=1
  return {
    'lowCount':counts1['lowCount'],
    'mediumCount':counts1['mediumCount'],
    'highCount': counts1['highCount']
    
  }


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  assert(counts["lowCount"] == 1)
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 2)
  print(counts)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
