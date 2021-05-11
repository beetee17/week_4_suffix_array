# python3
import sys

def get_mapping(arr):

  mapping = dict()
  i = 0

  for item in arr:
    if not mapping.get(item, None):

      mapping.update({item : i})
      i += 1

  return mapping

def build_suffix_array(text):
  """
  Build suffix array of the string text and
  return a list result of the same length as the text
  such that the value result[i] is the index (0-based)
  in text where the i-th lexicographically smallest
  suffix of text starts.
  """
  # see https://www.youtube.com/watch?v=_TUeAdu-U_k for reference

  # convert our string to a list of unicode integers (duplicate chars have the same coding)
  arr = [ord(text[i]) for i in range(len(text))]

  l = 1
  temp = []
  # form a list of tuples for each item in arr of (item, item that is l positions in front) i.e a partial suffix of length l
  for i in range(len(arr)):

    if i + l < len(arr):

      temp.append((arr[i], arr[i+l],))
    
    else:
      temp.append((arr[i], -1,))

  # sort the list of tuples
  sorted_temp = sorted(temp)

  # give each unique item in the sorted list a coding (such that duplicates have the same coding)
  mapping = get_mapping(sorted_temp)

  # using the codings, map each item in the unsorted array to its coding
  arr = [mapping[item] for item in temp]
 
  # repeat the above until each item in the array has a unique coding
  while len(set(arr)) < len(arr):
    l *= 2
    temp = []
    for i in range(len(arr)):

      if i + l < len(arr):

        temp.append((arr[i], arr[i+l],))
      
      else:
        temp.append((arr[i], -1,))
    
    sorted_temp = sorted(temp)

    mapping = get_mapping(sorted_temp)

    arr = [mapping[item] for item in temp]

  # do one last mapping on arr to get sorted suffix array
  mapping = get_mapping(arr)
 
  arr = [mapping[i] for i in range(len(arr))]

  return arr

if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  print(" ".join(map(str, build_suffix_array(text))))
