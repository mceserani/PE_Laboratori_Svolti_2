""" Student score management tool """

class StudentsDataException(Exception):
    """ Base class for all exceptions in this task """
    def __init__(self, msg):
        self.msg = msg

class EmptyFileError(StudentsDataException):
    """ Raised when the file is empty """
    def __init__(self, msg="File is empty."):
        super().__init__(msg)

class BadLineError(StudentsDataException):
    """ Raised when the line has invalid format """
    def __init__(self, msg="Bad line format."):
        super().__init__(msg)

def process_file(filename):
    """ Process the given file """
    student_scores = {}

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            if not lines:
                raise EmptyFileError("File is empty.")

            for line in lines:
                line = line.strip()
                if line:
                    parts = line.split()
                    if len(parts) == 3:
                        first_name, last_name, score = parts
                        score = float(score)
                        student = f"{first_name} {last_name}"

                        if student in student_scores:
                            student_scores[student] += score
                        else:
                            student_scores[student] = score
                    else:
                        raise BadLineError(f"Bad line format: {line}")
                else:
                    raise BadLineError("Empty line detected.")

        sorted_report = sorted(student_scores.items(), key=lambda x: x[0])

        for student, score in sorted_report:
            print(f"{student}\t{score}")
    except FileNotFoundError as e:
        print(str(e))
    except EmptyFileError as e:
        print(str(e))
    except BadLineError as e:
        print(str(e))

# Ask the user for Prof. Jekyll's file name
filename = input("Enter Prof. Jekyll's file name: ")

# Call the function to process the file and print the report
process_file(filename)
