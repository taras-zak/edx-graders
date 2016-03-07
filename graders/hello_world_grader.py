import subprocess
from xqueue_watcher import grader

class HelloGrader(grader.Grader):
    def grade(self, grader_path, grader_config, student_response):
        tests = []
        errors = []
        correct = 0
        score = 0
        print grader_path
        print grader_config
        print student_response

        p = subprocess.Popen(["python", "-c {0}".format(student_response)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()

        if (err != ""):
            errors.append(err)
        else:
            if str(out) == "Hello world":
                correct = 1
                score = 1
            else:
                errors.append("One more time. Just print 'Hello world'")

        results = {
                'correct': correct,
                'score': score,
                'tests': tests,
                'errors': errors,
            }
        return results

