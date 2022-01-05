
def count_batteries_by_usage(cycles):
  return {
    "lowCount": 0,
    "mediumCount": 0,
    "highCount": 0
  }


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  if charge < 400:
    assert(counts["lowCount"] == 2)
  if (charge < 400 && charge < 999):
    assert(counts["mediumCount"] == 3)
  else:
    assert(counts["highCount"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()

  charged less than 400 times: classified as low
charged between 400 and 919 times: classified as medium
charged 920 times or more: classified as high
