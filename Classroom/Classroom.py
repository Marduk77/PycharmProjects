__author__ = 'jason allen'
boxes = 1
sum = 0
print ('The Girl Scout Cookie Program.')
print ('Enter 0 to Quit')
while boxes != 0:
    print ('Current Sum:', sum)
    boxes = input('Number of Boxes Sold: ')
    boxes = int(boxes)
    sum = sum + boxes
print('Total sum:',sum)