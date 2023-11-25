"""Quiz03 practice: function edition."""

from __future__ import annotations

class Course:
    """Models the idea of a UNC course."""
    name: str
    level: int
    prereqs: list[str]

    def find_courses(self, list_courses: list[Course], search_word: str) -> list[str]:
        """Finds 400+ level courses with the given prereq."""
        course_names: list[str] = []

        for course in list_courses: 
            if course.level >= 400:
                for prereq in course.prereqs:
                    if prereq == search_word:
                        course_names.append(course.name)
        return course_names

    def is_valid_course (self, prereq: str) -> bool:
        if self.level < 400:
            return False
        else: 
            for p in self.prereqs:
                if p == prereq:
                    return True
        return False
