f = open('django.txt', 'r', encoding='utf-8')
i = 0
test = False
for line in f:
    i+=1
    if "Manzil:" in line:
        print(i,".",line)
        test=True

if not test:
    print("Bunday so'z yo'q de karoche")