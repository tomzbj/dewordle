f = open("wordle.txt")
words = f.readlines()

while True:
    cmd = input()
    if cmd[0] not in "+-":
        continue
    if not cmd[1:].isalpha():
        continue

    if cmd[0] == "+":
        for c in cmd[1:]:
            tmp = set()
            for w in words:
                if c in w:
                    tmp.add(w)
            words = tmp
    elif cmd[0] == "-":
        tmp = set()
        for w in words:
            flag = False
            for c in cmd[1:]:
                if c in w:
                    flag = True
            if flag == False:
                tmp.add(w)
        words = tmp
    if len(words) < 100:
        count = 0
        for w in words:
            w = w[:-1]
            print(w, end="  ")
            if count % 10 == 9:
                print()
            count += 1
    print()
    print(len(words))
    print("Total: ", len(words))
