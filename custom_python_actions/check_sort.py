def check_sort() -> None:
    with open("open-repositories.txt") as my_file:
        data = my_file.read()
        repo_list = data.split("\n")
        repo_list.remove("")
        if repo_list != sorted(repo_list):
            raise Exception("open-repositories.txt is not correctly sorted")


if __name__ == "__main__":
    check_sort()
