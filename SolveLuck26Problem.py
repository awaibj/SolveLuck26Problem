'''
    solve luck 26 problem
    luck 26 is famous as a mathematics game. 144 solutions were found in U.S mathematics competition.
    And the 145th is still a myth by now.
    Player: 1 player, above 8 years old
    Rule: Put the sticks with 1~12 on the game board, any 4 sticks on a line should be added to 26.
                    (1)
                  /     \
    (2)--------(3)----------(4)------(5)
       \    /               \   /
         (6)                  (7)
        /    \            /    \
       (8)-----(9)------(10)----(11)
                \     /
                  (12)
'''

import time

def main():
    seq_len = 12
    luck26_dict={i:0 for i in range(1,seq_len+1)}

    # enumerate all possible answers.
    start_time = time.time()
    result=[]
    for i1 in range(1,seq_len+1):
        luck26_dict[1] = i1
        for i2 in range(1, seq_len + 1):
            if i2 != i1:
                luck26_dict[2] = i2
                for i3 in range(1, seq_len + 1):
                    if i3 != i2 and i3 != i1:
                        luck26_dict[3] = i3
                        for i4 in range(1, seq_len + 1):
                            if i4 != i3 and i4 != i2 and i4 != i1:
                                luck26_dict[4] = i4
                                for i5 in range(1, seq_len + 1):
                                    if i5!=i4 and i5 != i3 and i5 != i2 and i5 != i1:
                                        luck26_dict[5] = i5
                                        for i6 in range(1, seq_len + 1):
                                            if i6!=i5 and i6 != i4 and i6 != i3 and i6 != i2 and i6 != i1:
                                                luck26_dict[6] = i6
                                                for i7 in range(1, seq_len + 1):
                                                    if i7!=i6 and i7 != i5 and i7 != i4 and i7 != i3 and i7 != i2 and i7 != i1:
                                                        luck26_dict[7] = i7
                                                        for i8 in range(1, seq_len + 1):
                                                            if i8!=i7 and i8 != i6 and i8 != i5 and i8 != i4 and i8 != i3 and i8 != i2 and i8 != i1:
                                                                luck26_dict[8] = i8
                                                                for i9 in range(1, seq_len + 1):
                                                                    if i9!=i8 and i9 != i7 and i9 != i6 and i9 != i5 and i9 != i4 and i9 != i3 and i9 != i2 and i9 != i1:
                                                                        luck26_dict[9] = i9
                                                                        for i10 in range(1, seq_len + 1):
                                                                            if i10!=i9 and i10 != i8 and i10 != i7 and i10 != i6 and i10 != i5 and i10 != i4 and i10 != i3 and i10 != i2 and i10 != i1:
                                                                                luck26_dict[10] = i10
                                                                                for i11 in range(1, seq_len + 1):
                                                                                    if i11!=i10 and i11 != i9 and i11 != i8 and i11 != i7 and i11 != i6 and i11 != i5 and i11 != i4 and i11 != i3 and i11 != i2 and i11 != i1:
                                                                                        luck26_dict[11] = i11
                                                                                        for i12 in range(1, seq_len + 1):
                                                                                            if i12!=i11 and i12 != i10 and i12 != i9 and i12 != i8 and i12 != i7 and i12 != i6 and i12 != i5 and i12 != i4 and i12 != i3 and i12 != i2 and i12 != i1:
                                                                                                luck26_dict[12] = i12
                                                                                                if CheckLuck26( luck26_dict ):
                                                                                                    end_time = time.time()
                                                                                                    print 'elapse time %d seconds.' % int(end_time-start_time)
                                                                                                    # start_time = time.time()
                                                                                                    result.append(luck26_dict)
                                                                                                    print len(result), result[-1]
        print 'it\'s %d loops.' % i1
    print result

def CheckLuck26( test_dict ):
    if ( CheckRedupliData(test_dict) == False and \
                 (test_dict[2]+test_dict[3]+test_dict[4]+test_dict[5]==26 and
                test_dict[1]+test_dict[3]+test_dict[6]+test_dict[8] == 26 and
                test_dict[1]+test_dict[4]+test_dict[7]+test_dict[11] == 26 and
                test_dict[2] + test_dict[6] + test_dict[9] + test_dict[12] == 26 and
                test_dict[8] + test_dict[9] + test_dict[10] + test_dict[11] == 26 and
                test_dict[5] + test_dict[7] + test_dict[10] + test_dict[12] == 26) ):
        return True
    else:
        return False

def CheckRedupliData( test_dict ):
    test_set = set(test_dict.values())
    if ( len(test_dict) != len(test_set) ):
        return True
    else:
        return False

if __name__ == '__main__':
    main()
