num = int(input())
gifts = []
boxes = []

for a in range(num):
    gift = int(input())
    gifts.append(gift)

for b in range(num):
    box = int(input())
    boxes.append(box)
    
for i in gifts:
    for j in boxes:
        if(j >= i):
            boxes.remove(j)
            break

print(len(boxes))