
def yield_reverse(number):
    reversed = str(number)[::-1]
    return int(reversed)

def test_palindromic(number):
    if str(number)[::-1] == str(number):
        return True
    else:
        return False

def palindromic_sum(input,depth = 0):
    recur_depth = depth
    result = yield_reverse(input)+input
    if test_palindromic(result) == True:
        return True
    elif test_palindromic(result) == False and recur_depth<50:
        return palindromic_sum(result,depth = recur_depth + 1)
    else:
        return False
    
build_arr = [palindromic_sum(a) for a in xrange(1,10000)]
print sum(1 if a==False else 0 for a in build_arr )



    

