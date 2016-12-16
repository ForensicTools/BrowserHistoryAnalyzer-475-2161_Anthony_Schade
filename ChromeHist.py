import AppTest, History_Pull

print("############################")
print("Welcome to Chrome Analyzer!!")
print("############################")
print("")

print("Options are: history, apps, bookmarks")
print("")
print("Enter the information you would like: ")
choice = input()

if choice == "bookmarks":
    AppTest.books()

if choice == "apps":
    AppTest.go()

if choice == "history":
    History_Pull.do()

