ipstring= input('Please enter a string : ')
def most_frequent(string):
    d = {}
    for letter in string:
        d[letter] = string.count(letter)
    d = sorted(d.items(), key=lambda item: item[1],reverse=True)
    for i in range(len(d)):
        print(d[i][0],'=',d[i][1])
        
most_frequent(ipstring)
