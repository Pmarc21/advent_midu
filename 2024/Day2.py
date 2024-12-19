# Santa Claus 🎅 wants to frame the names of the good children to decorate his workshop 🖼️, but the frame must follow specific rules. Your task is to help the elves generate this magical frame.

# Rules:

# Given an array of names, you must create a rectangular frame that contains all of them.
# Each name must be on a line, aligned to the left.
# The frame is built with * and has a border one line thick.
# The width of the frame automatically adapts to the longest name plus a margin of 1 space on each side.

names = ['midu', 'madeval', 'educalvolpz']
asterisk_init = '* '
asterisk_end = ' *'
asterisk = '*'
max_word = 0

def createFrame(names):
  max_word = max(len(name) for name in names)
  border = asterisk * (max_word + 4)
  frames = [border]
  for name in names:
    name = asterisk_init + name
    while len(name) < max_word + 2:
      name = name + ' '
    name = name + asterisk_end
    frames.append(name)
  frames.append(border)
  return "\n".join(frames)

print(createFrame(names))