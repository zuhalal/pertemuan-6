# List
# List adalah struktur data kolektif sekuensial yang dapat diubah bawaan python
# Sekuensial berarti adalah data yang ada di dalam list memiliki index sehingga dapat diakses satu persatu

# List dapat menyimpan berbagai macam tipe data dan mengizinkan duplikasi data di dalamnya
this_is_list = [1, "oke", 9.0, "oke"]
# print(this_is_list, " is type of ", type(this_is_list))

# Akses data yang ada di dalam list
# print("First index is ", this_is_list[0])
# print("Last index is ", this_is_list[-1])
# print("Data after index 0 is ", this_is_list[1:])
# print("Data from index 3 is ", this_is_list[:3])
# print("Data from index 1 until 3-1 is ", this_is_list[1:3])

#indexing with step
nums = [5, 1, 9, 7, 6, 13, 1000]

# print(nums[::2]) # [5, 9, 6, 1000]
# print(nums[::-1]) # [1000, 13, 6, 7, 9, 1, 5]
# print(nums[5::-2]) # [13, 7, 1]

#List Function
nums = [1, 2, 4, 3]
# print(min(nums)) # 1
# print(max(nums)) # 4
# print(sum(nums)) # 10

# Mengubah data yang ada di dalam list
this_is_list[2] = 4j+1
# print("List setelah diubah", this_is_list)

# Menambah data ke dalam list
this_is_list.append(9.0)
# print("List setelah ditambahkan", this_is_list)

# Menghapus data dari list
this_is_list.pop(2)
# print("List setelah dihapus", this_is_list)

#Menghapus data dengan remove
nums = [4, 3, 2, 1, 0]
nums.remove(3) # angka / huruf apa yang mau dihapus
#print(nums)

# Akses list dengan loop
# for data in this_is_list:
#     print(data)

#List Comprehension
# [print(data) for data in this_is_list]
list_comprehension = [i*2 for i in [0,1,2,3,4] if i%2 == 0]
#print(list_comprehension)

this_is_new_list = [data for data in this_is_list]
# print(this_is_new_list)

# Mengurutkan list
this_is_string_list = ["uwu", "owo", "owi"]
this_is_string_list.sort()
# print(this_is_string_list)

#sort vs sorted
nums = [4, 1, 2, 3]
# print(nums.sort()) # None
# print(nums) # [1, 2, 3, 4]
nums = [4, 1, 2, 3]
# print(sorted(nums)) # [1, 2, 3, 4]
# print(nums) # [4, 1, 2, 3]

#split and join
x = "good luck for quiz and exam"
l = x.split()
# print(l)
# print("###".join(l))

# Menggabungkan 2 List
this_is_list.extend(this_is_string_list)
# print(this_is_list)

#list with same reference
x = [3, 1]
y = x
y.append(2)
#print(x) # [3, 1, 2]

#copying list with different reference
x = [3, 1]
y = x[:] # copy list object
y.append(2)
#print(x) # [3, 1]
#print(y)

