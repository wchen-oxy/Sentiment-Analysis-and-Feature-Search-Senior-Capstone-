
array = []
correct = 0
total = 0
sent_correct = 0
feat_correct = 0
wrong = 0


with open("cleaned/correct_copy1.txt", "r") as file:
    for x in file.readlines():
        if x == "11\n":
            correct += 1
        if x == "10\n":
            feat_correct += 1

        if x == "01\n":
            sent_correct += 1
        if x == "00\n":
            wrong += 1
        total += 1

print("Correct: " + str(correct))
print("wrong: " + str(wrong))
print("# features correct: " + str(feat_correct))
print("# of sent correct: " + str(sent_correct))
print("Total: " + str(total))
percent = correct / total
print("percent" + str(percent))
