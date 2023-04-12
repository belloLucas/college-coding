#Merge Sort

lista = [10, 9, 5, 8, 11, 3]
def merge_sort(lista):
    if len(lista) <= 1: return lista
    else:
        half = len(lista) // 2
        left = merge_sort(lista[:half])
        right = merge_sort(lista[half:])
        return merge_exec(left, right)

def merge_exec(left, right):
    sub_list_ordered = []
    top_left, top_right = 0, 0
    while top_left < len(left) and top_right < len(right):
        if left[top_left] <= right[top_right]:
            sub_list_ordered.append(left[top_left])
            top_left += 1
        else:
            sub_list_ordered.append(right[top_right])
            top_right += 1
    sub_list_ordered += left[top_left:]
    sub_list_ordered += right[top_right:]
    return sub_list_ordered

print(merge_sort(lista))