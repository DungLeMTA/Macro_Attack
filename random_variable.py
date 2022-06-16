import random
import string

f = open('dictionary_Eng.txt','r',encoding='utf-8')
data = f.read().split('\n')
f.close()

def generate_random_string(low, high):
    length = random.randint(low, high)
    # letters = string.ascii_letters  # + string.digits
    return '_'.join([random.choice(data) for _ in range(length)])

if __name__ == '__main__':
    for i in range(0,6):
        a = generate_random_string(2,3)
        print(a)

# f = open('dictionary_Eng.txt','r',encoding='utf-8')
#
# data = f.read()
#
# f.close()
#
# data = data.replace(" ","")
# f = open('dictionary_Eng.txt','w',encoding='utf-8')
# f.write(data)
#
# f.close()