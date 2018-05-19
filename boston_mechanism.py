"""
Implementation of the Boston Mechanism algorithm from:
https://www.bc.edu/content/dam/files/schools/cas_sites/economics/pdf/workingpapers/wp729.pdf
"""
I = ('Pete Michelin', 'Mpilo Kwathwane', 'Prince Sibanda') # Set of students
C = ('Huguenot High School', 'Virginia Tech') # Set of schools
q = (2, 1) # Quota for each school

# Strict preference relation of each student
# First index is student, second is school's ranking
P = ((1, 2), (2, 1), (1, 2))

# Priority order
# First index is student, second is the school and the priority of the student
# at that school
# Note: I'm assuming each student get a unique priority order at each school
PO = ((3, 1), (0, 2), (5, 0))

u = [0, 1, 0] # School match for each student

def boston_mechanism(I, c, q, P, PO):
    u = [-1 for i in P]
    uc = [0 for i in I]

    # While there are students left without assigned schools
    u = [i for i in xrange(len(P)) if u[i] == -1]
    while len(u) > 0:
        # For each school with empty seats left
        for sc in len(C):
            if uc[sc] == a[sc]:
                continue
            # Consider only the students who listed the school as their top choice
            students = [i for i in xrange(len(P)) if P[i][sc] == 1]

            # Assign seats to the school following the priority order of the
            # students at the school
            st_po = [(i, PO[i][sc]) for i in students]
            st_po.sort(key lamdba x: x[1], reverse=True)

            # Assign seats until there are no seats left or no students left that
            # put the school as their top priority
            i = 0
            while not uc[sc] > q[sc] and len(st_po) > 0 and st_po[i][0] > 0:
                uc[sc] += 1
                u[st_po[i][1]] = sc
                i += 1


        u = [i for i in xrange(len(P)) if u[i] == -1]
