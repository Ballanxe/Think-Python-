def nested_sum(nestedList, newList = [0]):
        '''
        nestedList: list composed of nested lists containing int.
        newList: list. The flat list composed of all the items present
        in the nested lists.
        Returns the sum of all the int in the nested list
        '''
        #Helper function to flatten the list
        def flatlist(nestedList):
                '''
                Returns a flat list
                '''
                for i in range(len(nestedList)):
                        if type(nestedList[i]) == int:
                                newList.append(nestedList[i])
                        else:
                                flatlist(nestedList[i])
                return newList

        flatlist(nestedList)
        print sum(newList)
        
nested_sum(nestedList)
# l = ['perro','gato', [5,3,6,7],'leon',[54,6,35,8]]

# def lista_nueva(lista,nueva = [0]):
#         for i in range(len(lista)):
#                 if type(lista[i]) == list:
#                        nueva = nueva + lista[i]

#         print sum(nueva)

# def suma_nested(lista,nueva = [0]):
        
#         lista_nueva(lista)
#         print sum(nueva)

# lista_nueva(l)

#Write a function named "capitalize_nested" that takes a nested list of strings and returns a new nested list with all strings capitalized.

l = [['perro','gato','leon'],[5,3,6,7],[54,6,35,8]]

def capitalize_nested(l): 

        def capitalize(s):
            return s.capitalize()
        for n, i in enumerate(l):       
            if type(i) is list:
                l[n] = capitalize_nested(l[n])
            elif type(i) is str:
                l[n] = capitalize(i)
        print l

def mayusculas(l, n = []):
        for i in range(len(l)):
                if type(l[i]) == list and type(l[i][0] == str):
                        l[i].capitalize()


# l[0][0].upper()

#cumulative sume


# def cumulative(l,cumulative_sum=0,new_list = []):
#     for i in l:
#         cumulative_sum += i
#         new_list.append(cumulative_sum)
#     return new_list

# l = [1,2,3,4,5,6]

# print cumulative(l)

# #middle

def anagram(word1,word2):
        t = list(word1)
        m = list(word2)
        if sorted(t) == sorted(m):
                return True
        else:
                return False


print anagram('avion','oivon')