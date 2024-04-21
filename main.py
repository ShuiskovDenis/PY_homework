data_1 = ['Hello\n' 'World\n', 'save\n', 'my\n', 'data\n']
data = open('data_1.txt', 'w')
data.writelines(data_1)
data.close()

data_2 = []
data = open("data_2.txt",'a')
data.close()

with open ("data_2.txt") as data_2:
    print("data_2 befolre add words -> ",f'[{data_2.read()}]')

user_input = int(input("Enter your line to copy -> "))

with open('data_1.txt', 'r') as copy_word_data_1:
    line = copy_word_data_1.readlines()
    save_word = (line[user_input])
    
print("Saved word is -> ", save_word)

with open("data_2.txt", 'a') as add_word:
    add_word.write(save_word)

with open('data_2.txt', 'r') as read_data_2:
    print("New lile add",f'({save_word})',"\n",read_data_2.read())

user_clear = int(input("Select 1 to clear data , or 0 to exit -> "))

if user_clear == 1:
    with open ('data_2.txt', 'w') as clear:
        clear = []
else:
    exit