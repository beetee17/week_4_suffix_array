# python3
import sys


def find_pattern_fast(pattern, text):
  """
  Find all the occurrences of the pattern in the text
  and return a list of all positions in the text
  where the pattern starts in the text.
  """
  
  s = pattern + '$' + text
  borders = prefix_function(s)
  matches = []

  for i in range(len(pattern) + 1, len(s)):

    if borders[i] == len(pattern):
      matches.append(i - 2*len(pattern))

  return matches



def prefix_function(text):

  # see https://www.youtube.com/watch?v=GTJr8OvyEVQ for reference

  arr = [0]
  j = 0
  i = 1

  while i < len(text):

    if text[i] == text[j]:
      arr.append(j+1)
      i += 1
      j += 1

    elif j == 0:
      arr.append(0)
      i += 1

    else:

      j = arr[i-1]

      while text[i] != text[j]:

        j = arr[j-1]
        flag = False

        if j == 0 and text[i] != text[j]:
          arr.append(0)
          i += 1
          flag = True
          break

      if not flag:
        arr.append(j+1)
        i += 1
        j += 1

  return arr



if __name__ == '__main__':
  pattern = sys.stdin.readline().strip()
  text = sys.stdin.readline().strip()
  result = find_pattern_fast(pattern, text)
  print(" ".join(map(str, result)))

