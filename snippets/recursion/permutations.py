def permutations(string):
    # if the string is one character or less, then no permutations are possible
    if len(string) <= 1: 
        return [string]
    else:
        # get a list 
        result = []
        p = permutations(string[1:])
        print(p)
        for perm in p:
            for l in range(len(string)):
                # p
                result.append(perm[:l] + string[:1] + perm[l:])

        return result

perm = permutations("abc")