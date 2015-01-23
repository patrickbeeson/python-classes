#!/usr/local/bin/python3

def description(name, instructor, *students, **staff):
    """ Print out a course description
    name: Name of the course
    instructor: Name of the instructor
    *students, ...: List of student names (positional arguments)
    **staff, ...: List of additional staff (keyword arguments)
    """
    print("=" * 40)
    print("Course Name:", name)
    print("Instructor:", instructor)
    print("-" * 40)
    for title, name in staff.items():
        print(title.capitalize(), ": ", name)
    print("{0:-^40}".format(" registered students "))
    for student in students:
        print(student)

if __name__ == "__main__":
    description(
        "Python 101",
        "Steve Holden",
        "Georgie Peorgie",
        "Mary Lamb",
        "Penny Rice",
        publisher="O'Reilly School of Technology",
        author="Python Software Foundation"
    )
    description(
        "Django 101",
        "Jacob Kaplan-Moss",
        "Baa-Baa Blacksheep",
        "Mary Contrary",
        "Missy Muffet",
        "Peter Piper",
        publisher="O'Reilly School of Technology",
        author="Django Software Foundation",
        editor="Daniel Greenfeld"
    )

    
        