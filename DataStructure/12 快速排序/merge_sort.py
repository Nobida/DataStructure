def merge_sort(seq):
    if len(seq) <= 1:
        #print(seq)
        return seq
    else:
        mid = len(seq) // 2
        sort1 = merge_sort(seq[:mid])
        sort2 = merge_sort(seq[mid:])
        seq = merge(sort1,sort2)
        return seq

def merge(sort1,sort2):
    len1,len2 = len(sort1), len(sort2)
    a = b = 0
    new_seq = []
    while a < len1 and b < len2:
        if sort1[a] < sort2[b]:
            new_seq.append(sort1[a])
            a += 1
        else:
            new_seq.append(sort2[b])
            b += 1
    while a < len1:
        new_seq.append(sort1[a])
        a += 1

    while b < len2:
        new_seq.append(sort2[b])
        b += 1
    return new_seq

