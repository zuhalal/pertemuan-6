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
# print("Data between index 0 and 3 is ", this_is_list[1:3])

# Mengubah data yang ada di dalam list
this_is_list[2] = 4j+1
# print("List setelah diubah", this_is_list)

# Menambah data ke dalam list
this_is_list.append(9.0)
# print("List setelah ditambahkan", this_is_list)

# Menghapus data dari list
this_is_list.pop(2)
# print("List setelah dihapus", this_is_list)

# Akses list dengan loop
# for data in this_is_list:
#     print(data)

# [print(data) for data in this_is_list]

this_is_new_list = [data for data in this_is_list]
# print(this_is_new_list)

# Mengurutkan list
this_is_string_list = ["uwu", "owo", "owi"]
this_is_string_list.sort()
# print(this_is_string_list)

# Menggabungkan 2 List
this_is_list.extend(this_is_string_list)
# print(this_is_list)

