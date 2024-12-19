# It's time to select the fastest reindeer for Santa's journeys! 🦌🎄
# Santa Claus has organized exciting reindeer races to determine which ones are in the best shape.

# Your task is to display each reindeer's progress on a snow track in isometric format.

# The information you receive:

# indices: An array of integers representing each reindeer's progress on the track:
# 0: The lane is empty.
# Positive number: The reindeer's current position from the beginning of the track.
# Negative number: The reindeer's current position from the end of the track.
# length: The length of each lane.
# Return a string representing the race track:

# Each lane has exactly length positions filled with snow (~).
# Each reindeer is represented with the letter r.
# Lanes are numbered at the end with /1, /2, etc.
# The view is isometric, so the lower lanes are shifted to the right.

def draw_race(indices, length):
  snow = '~'
  race = []
  space = ' '

  for i,j in enumerate(indices):
      lines = space * (len(indices) - i-1)
      track = list(snow * length)

      if j == 0:
        track[0] = '~'
      elif j > 0:
        track[j] = 'r'
      else:
        track[length + j] = 'r'

      lines += ''.join(track) + f" /{i + 1}"
      race.append(lines)
  return '\n'.join(race)

indices = [0, 5, -3]
length = 10
print(draw_race(indices, length))


# def draw_race(indices, length):
#   snow = '~'
#   race = []
#   space = ' '

#   for i,j in enumerate(indices):
#       lines = space * (len(indices) - i-1)
#       if j == 0:
#         lines += snow * length + ' /'+str(i+1)
#       elif j > 0:
#         k = 0
#         for k in range(length):
#           if k == j:
#             lines += 'r'
#           else:
#             lines += snow
#         lines += ' /'+str(i+1)
#       else:
#         k = 0
#         for k in range(length):
#           if k == length+j:
#             lines += 'r'
#           else:
#             lines += snow
#         lines += ' /'+str(i+1)
#       race.append(lines)
#   return '\n'.join(race)