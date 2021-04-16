# Tuple
# Tuple adalah struktur data kolektif sekuensial yang tidak dapat diubah bawaan python

# Tuple juga bisa menyimpan banyak tipe data yang berbeda dan mengizinkan duplikasi data
this_is_tuple = ("oke", 100, 9.0, "oke") #immutable
print(this_is_tuple)

#yang termasuk data tuple
this_is_not_tuple_1 = (2)
#print(type(this_is_not_tuple_1))

this_is_not_tuple_2 = ("Borobudur")
#print(type(this_is_not_tuple_2)) 

tup = (2,)
#print(type(tup))
tup1 = ("Borobudur",)
#print(type(tup1))

#membuat tupple
x = tuple("abc")
#print(x) # ('a', 'b', 'c')

y = tuple([2, 1, 2, 1])
#print(y) # (2, 1, 2, 1)

z = tuple(range(3))
#print(z) # (0, 1, 2)

w = tuple()
#print(w) # ()

#operasi pada tupple
# print("oke" in this_is_tuple)
# print(len(this_is_tuple))

#Tuple Method
int_tuple = (1,5,2,4,3,7,6)
# print(min(int_tuple))
# print(max(int_tuple))
# print(sum(int_tuple))

# Akses data di Tuple
# print("First index is ", this_is_tuple[0])
# print("Last index is ", this_is_tuple[-1])
# print("Data after index 0 is ", this_is_tuple[1:])
# print("Data from index 3 is ", this_is_tuple[:3])
# print("Data between index 0 and 3 is ", this_is_tuple[1:3])

# Mengubah data di dalam tuple
# this_is_tuple[2] = 10
# this_is_listed_tuple = list(this_is_tuple)
# this_is_listed_tuple[2] = 10
# this_is_tuple = tuple(this_is_listed_tuple)
# print(this_is_tuple)

#List vs Tuple

#1.Apppend
# num_list = [3, 1, 2]
# num_list.append(5)
# print(num_list)


# num_tuple = (3, 1, 2)
# #num_tuple.append(5)
# print(num_tuple)


#2.Del
# num_list = [3, 1, 2]
# del num_list[0]
# print(num_list)


# num_tuple = (3, 1, 2)
# del num_tuple[0]
#print(num_tuple)