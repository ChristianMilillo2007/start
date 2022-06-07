import os

if __name__ == '__main__':
  print('start')

text = str(input(''))
qt = len(text)

for letter in text:
  if qt == 0:
    quit()
  else:
    print('Hello everybody ;)')
    
os.system('PAUSE')
