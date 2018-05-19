"""
Implementation of the Boston Mechanism algorithm from:
https://www.bc.edu/content/dam/files/schools/cas_sites/economics/pdf/workingpapers/wp729.pdf
"""
# I = ('Pete Michelin', 'Mpilo Kwathwane', 'Prince Sibanda') # Set of students
I = (1,2,3,4,5)
# C = ('Huguenot High School', 'Virginia Tech') # Set of schools
C = ('a', 'b', 'c', 'd', 'e')
# q = (2, 1) # Quota for each school
q = [1 for x in xrange(5)]

# Strict preference relation of each student
# First index is student, second is school's ranking
# P = ((1, 2), (2, 1), (1, 2))
# P = ((2, 100, 100, 1, 3), (6, 1, 4, 2, 3), (100, 100, 100, 1, 100), (1, 100,
#     100, 100, 100), (100, 1, 100, 100, 100))
P = ((3, 0, 4), (1, 3, 4, 2, -1, 0), (3,), (0,), (1,))

# Priority order
# First index is student, second is the school and the priority of the student
# at that school
# Note: I'm assuming each student get a unique priority order at each school
# PO = ((3, 1), (0, 2), (5, 0))
# PO = ((5, 5, 0, 3, 5), (3, 3, 0, 5, 4), (0, 0, 0, 4, 0), (2, 2, 4, 0, 0), (4, 4,
#    5, 0, 0))
PO = ((0, 4, 1, 3), (0, 4, 1, 3), (4, 3, -1), (1, 2, 0), (0, 1))


u = [0, 1, 0] # School match for each student

def boston_mechanism(I, C, q, P, PO):
    u = [-1 for i in P]
    uc = [0 for i in I]

    # While there are students left without assigned schools
    unassigned = [i for i in xrange(len(P)) if u[i] == -1]
    print("unassigned: {}".format(unassigned))
    choice = 0 # The current choice level
    iteration = 0
    while len(unassigned) > 0:
        # For each school with empty seats left
        for sc in xrange(len(C)):
            if uc[sc] == q[sc]:
                continue

            # Consider the students who who rather choose a null school at this
            # choice level
            null_students = [i for i in unassigned if len(P[i]) > choice and
                    P[i][choice] == -1]
            for ns in null_students:
                u[ns] = 1000000

            # Consider only the students who listed the school as their current choice
            students = [i for i in unassigned if len(P[i]) > choice and P[i][choice] == sc]
            print("students with choice {} at school {}: {}".format(choice, C[sc], students))

            # Assign seats to the school following the priority order of the
            # students at the school
            # PO = ((0, 4, 1, 3), (0, 4, 1, 3), (4, 3, -1), (1, 2, 0), (0, 1))
            # st_po = [(i, PO[i][sc]) for i in students]
            # st_po.sort(key=lambda x: x[1], reverse=True)

            # Assign seats until there are no seats left or no students left that
            # put the school as their top priority
            i = 0
            while not uc[sc] == q[sc] and len(PO[sc]) > i:
                if PO[sc][i] in students:
                    uc[sc] += 1
                    u[PO[sc][i]] = sc
                i += 1


        unassigned = [i for i in xrange(len(P)) if u[i] == -1]
        choice += 1
        print(u)
        iteration += 1
        if iteration > 5:
            break
    return u
