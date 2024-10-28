# https://www.notion.so/ALGORITHMIQUE-NOTES-a4320aa5c16444c3b3d5a2d311f149d3
def bubble_sort(tab):
    n = len(tab)

    for i in range(n):
        for j in range(0, n - 1 - i):
            if tab[j] > tab[j + 1]:
                tab[j], tab[j + 1] = tab[j + 1], tab[j]
    return tab


# if __name__ == "__main__":
#     print("hello")
