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
        f.write(str(len(libs)) + "\n")
        for lib in libs:
            if lib["keep"]:
                f.write("{} {}\n".format(lib["id"], lib["nb_books"]))
                f.write(" ".join(lib["books"]) + "\n")


# def cut_out_of_day_lib(libs, nb_days):
#     total = 0
#     for idx, lib in enumerate(libs):
#         total += lib["signup"]
#         if total >= nb_days:
#             return libs[0:idx + 1]
#     return libs


def remove_duplicate(libs, nb_days):
    books = []
    for lib in libs:
        new_books = []
        for book in lib["books"]:
            if book not in books:
                books.append(book)
                new_books.append(book)
        if len(new_books) > 0:
            lib["books"] = new_books
            lib["nb_books"] = len(new_books)
            lib["keep"] = True
        else:
            lib["keep"] = False,
            lib["books_score"] = 0
            lib["nb_books"] = 0
            lib["signup"] = nb_days
            lib["b_p_day"] = nb_days
    return libs


def calculate_books_score(books, books_score):
    score = 0
    for book_id in books:
        score += int(books_score[int(book_id)])
    return score


def algo(file_name):
    with open(file_name, 'r') as file:
        content = file.readlines()
    # print(content)

    params = content[0].replace('\n', '').split(' ')
    # print(params)
    nb_books = int(params[0])
    nb_lib = int(params[1])
    nb_days = int(params[2])
    books_score = content[1].replace('\n', '').split(' ')

    content = content[2:]
    # print(content)
    libs = []
    books = []
    for idx, ligne in enumerate(content):
        params = ligne.replace('\n', '').split(' ')
        id = idx // 2
        if idx % 2 == 0:
            libs.append({
                "nb_books": int(params[0]),
                "signup": int(params[1]),
                "b_p_day": int(params[2]),
                "books": [],
                "id": id,
                "books_score": 0,
            })
        else:
            libs[id]["books"] = params
            libs[id]["books_score"] = calculate_books_score(
                params, books_score)

    sorted_lib = sorted(libs, key=lambda lib:
                        (-lib["books_score"], -lib["nb_books"], lib["signup"], -lib["b_p_day"]))
    no_duplicate = remove_duplicate(sorted_lib, nb_days)
    output_result(no_duplicate, file_name)

    sorted_lib_bis = sorted(no_duplicate, key=lambda lib:
                            (-lib["books_score"], -lib["nb_books"], lib["signup"], -lib["b_p_day"]))
    output_result(sorted_lib_bis, file_name + ".bis")


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
