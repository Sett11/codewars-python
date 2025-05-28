def decompose_single_strand(s):
    result = []
    for i in range(3):
        result.append(f"Frame {i+1}: {s[:i]+(' ' if i else '')+' '.join([''.join(s[j:j+3]) for j in range(i, len(s), 3)])}")
    return "\n".join(result)

print(decompose_single_strand("AGGTGACACCGCAAGCCTTATATTAGC"))