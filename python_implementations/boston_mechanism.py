"""
Implementation of the Boston Mechanism algorithm from:
https://www.bc.edu/content/dam/files/schools/cas_sites/economics/pdf/workingpapers/wp729.pdf
"""
I = (1, 2, 3, 4, 5)# Set of students
C = ('a', 'b', 'c', 'd', 'e') # Set of schools
q = [1 for x in xrange(5)] # Quota for each school

# Strict preference relation of each student
# List of school choices for each student in order of preference.
# -1 is a "null school": it means that the student would prefer to rather go to
# a school outside of the given choices.
P = ((3, 0, 4), (1, 3, 4, 2, -1, 0), (3,), (0,), (1,))

# Priority order
# List of student priorities for each school in order of preference.
# -1 is the vacant position. It means that the school would rather have a vacant
# position than a student below the ranking of the vacant position.
PO = ((0, 4, 1, 3), (0, 4, 1, 3), (4, 3, -1), (1, 2, 0), (0, 1))

def boston_mechanism(I, C, q, P, PO):
    u = [-1 for i in P] # The school each student has been admitted to.
    student_count = [0 for i in I] # The number of students each school has been admitted.

    unadmitted = [i for i in xrange(len(P)) if u[i] == -1]
    choice = 0 # The current choice level

    # While there are students left without admitted schools
    while len(unadmitted) > 0:
        print("#" * 50)
        print("Choice level: {}".format(choice+1))
        # For each school...
        for sc in xrange(len(C)):
            # ...with empty spots left
            if student_count[sc] == q[sc]:
                continue

            # Consider the students who who rather choose a null school at this
            # choice level
            null_students = [i for i in unadmitted if len(P[i]) > choice and
                    P[i][choice] == -1]
            # Assign those school to a null school
            for ns in null_students:
                u[ns] = -100
                print("Student {} gets admitted to a null school.".format(I[ns]))
            # print("Students with null choice at choice level {}: {}".format(choice+1, [I[i] for i in null_students]))

            # Consider only the students who listed the current school as their current choice
            students = [i for i in unadmitted if len(P[i]) > choice and P[i][choice] == sc]
            # print("Students with choice {} at school {}: {}".format(choice+1,
            #     C[sc], [I[i] for i in students]))

            # Assign seats to the school following the priority order of the
            # students at the school until there are no spots left at the school
            # or no students left that put the school as their top priority
            i = 0
            while not student_count[sc] == q[sc] and len(PO[sc]) > i:
                # Check if the student on the school's priority list are in the
                # group of unadmitted students
                if PO[sc][i] in students:
                    # Assign the student to the school
                    u[PO[sc][i]] = sc
                    student_count[sc] += 1
                    print("Student {} admitted to school {}.".format(I[PO[sc][i]], C[sc]))
                i += 1


        # Get the new group of unadmitted students
        unadmitted = [i for i in xrange(len(P)) if u[i] == -1]
        choice += 1
        for student, school in enumerate(u):
            print("{}:  {}.".format(I[student], C[school] if
                school > -1 else "Null school"))
    return u

u = boston_mechanism(I, C, q, P, PO)
print("*" * 50)
for student, school in enumerate(u):
    print("Student {} is admitted to school {}.".format(I[student], C[school] if
        school > -1 else "a null school"))
