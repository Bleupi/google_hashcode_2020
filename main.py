FILE = "./exemple"
FILE_1 = "a_example.in"
FILE_2 = "b_read_on.in"
FILE_3 = "c_incunabula.in"
FILE_4 = "d_tough_choices.in"
FILE_5 = "e_so_many_books.in"
FILE_6 = "f_libraries_of_the_world.in"


def output_result(libs, file_name):
    output_file = file_name.replace('.in', '.out')
    with open(output_file, 'w+') as f:
        # print(len(libs))
        f.write(str(len(libs)) + "\n")
        for idx, lib in enumerate(libs):
            # print("{} {}".format(idx, lib["nb_books"]))
            f.write("{} {}\n".format(lib["id"], lib["nb_books"]))
            f.write(" ".join(lib["books"]) + "\n")
            # print(" ".join(lib["books"]))


def cut_out_of_day_lib(libs, nb_days):
    total = 0
    for idx, lib in enumerate(libs):
        total += lib["signup"]
        if total >= nb_days:
            return libs[0:idx + 1]
    return libs


def remove_duplicate(libs):
    books = []
    for lib in libs:
        new_books = []
        for book in lib["books"]:
            if book not in books:
                books.append(book)
                new_books.append(book)
        lib["books"] = new_books
        lib["nb_books"] = len(new_books)
    return libs


def algo(file_name):
    with open(file_name, 'r') as file:
        content = file.readlines()
    # print(content)

    params = content[0].replace('\n', '').split(' ')
    # print(params)
    nb_books = int(params[0])
    nb_lib = int(params[1])
    nb_days = int(params[2])

    content = content[2:]
    # print(content)
    libs = []
    books = []
    for idx, ligne in enumerate(content):
        params = ligne.replace('\n', '').split(' ')
        if idx % 2 == 0:
            libs.append({
                "nb_books": int(params[0]),
                "signup": int(params[1]),
                "b_p_day": int(params[2]),
                "books": [],
                "id": idx // 2
            })

        else:
            # print(idx // 2, libs)
            libs[idx // 2]["books"] = params

    sorted_lib = sorted(libs, key=lambda lib:
                        (-lib["nb_books"], lib["signup"], -lib["b_p_day"]))
    # sorted_lib = sorted(libs, key=lambda lib: lib["nb_books"])
    # print(sorted_lib)
    #max_day_lib = cut_out_of_day_lib(sorted_lib, nb_days)
    no_duplicate = remove_duplicate(sorted_lib)
    # print(max_day_lib)
    output_result(no_duplicate, file_name)


def main():
    algo(FILE_1)
    algo(FILE_2)
    algo(FILE_3)
    algo(FILE_4)
    algo(FILE_5)
    algo(FILE_6)


main()


# // ligne 1 B(int) nb books, L(int) nbr lib D(int) nbr of Days
# // score of books int, int, int

# 2lignes for each lib:
# - N nbr of book, T nbr of days for suignup, M nbr book by day
# - it, int, int(ids of books)

# file format:
# nbr of lib to sign up
# - id of lib nbr of books to scan from this lib
# - id of the books to scan in oder of scan

# lib ...
