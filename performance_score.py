#!/usr/bin/env python
# -*- coding:utf-8 -*-

# The total person of your department.
PERSON = 13

# The ratio of levels.
SCORE_A = 1.5
SCORE_B = 1.1
SCORE_C = 0.9
SCORE_D = 0.5

# The minimum department goal avarage ratio.
GOAL_UPPER = 1.0
# The maximum department goal avarage ratio.
GOAL_LOWER = 0.99

# Allow no person in such level?
ALLOW_NO_A = False
ALLOW_NO_B = False
ALLOW_NO_C = False
ALLOW_NO_D = False


count = 1

if ALLOW_NO_A:
    a = 0
else:
    a = 1

while a <= PERSON:
    if ALLOW_NO_B:
        b = 0
    else:
        b = 1

    while b <= PERSON:
        if ALLOW_NO_C:
            c = 0
        else:
            c = 1

        while c <= PERSON:
            if ALLOW_NO_D:
                d = 0
            else:
                d = 1

            while d <= PERSON:
                condition_person = a + b + c + d
                tot_score = SCORE_A * a + SCORE_B * b + SCORE_C * c + SCORE_D * d
                avg_score = tot_score / PERSON
                if avg_score > GOAL_LOWER and avg_score <= GOAL_UPPER and condition_person == PERSON: 
                    print '=== %d ===' % count
                    print 'AVG: %f' % avg_score
                    print 'A: %d' % a
                    print 'B: %d' % b
                    print 'C: %d' % c
                    print 'D: %d\n' % d

                    count += 1

                d += 1

            c += 1

        b += 1

    a += 1
