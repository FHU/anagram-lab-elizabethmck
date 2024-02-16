#REMOVE PASS AND FIX THIS FUNCTION
def anagram(list1, list2):
    if list1 == " ":
        return False
    else:
        list1 = list1.upper()
        list1 = list1.replace(" ","")
        list2 = list2.upper()
        list2 = list2.replace(" ","")
        
        word = []
        
        for i in list1:
            word.append(i)
            
        for i in word:
            if i in list2:
                continue
            else:
                return False
        return True


if __name__ == '__main__':
    #REMOVE PASS YOUR CODE GOES HERE
    list1 = input()
    list2 = input()
    print(anagram(list1, list2))