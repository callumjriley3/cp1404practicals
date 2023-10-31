"""
Languages
Estimated: 30 minutes
Actual: 24 minutes
"""

from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

programming_languages = [ProgrammingLanguage("Python", "Dynamic", True, 1991),
                         ProgrammingLanguage("Ruby", "Dynamic", True, 1995),
                         ProgrammingLanguage("Visual Basic", "Static", False, 1991)]

print("The dynamically typed languages are:")
dynamic_languages = [programming_language for programming_language in programming_languages
                     if programming_language.is_dynamic()]
for language in dynamic_languages:
    print(language.name)
