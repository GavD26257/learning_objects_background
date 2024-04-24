import json

# Text
text = '{"type":"text",\
    "title":"Lesson 1",\
    "content":"The universe\'s average color is called Cosmic Latte"}'

text_dict = json.loads(text)
# print("\ntext_dict =", text_dict)

# Multiple Choice
mc_question = '{"type":"multiple-choice",\
    "title":"Question 1",\
    "question":"What relational SQL DBMS did we use in this class",\
    "options":["MySQL", "PostgreSQL", "MongoDB"], \
    "answer":"PostreSQL", \
    "explanations":[\
        "MySQL is a commonly-used relational DBMS, but it is not the one we used in this class", \
        "although we used MongoDB in this class, it is a non-relational SQL DBMS"\
    ]}' 

mc_dict = json.loads(mc_question)
# print("\nmc_dict =", mc_dict)

# Fill in the black
fill_in_the_blank = '{"type":"fill-in-the-blank", \
    "title":"Question 2", \
    "question":"The course number for this class is _blank_ (enter answer without any spaces)", \
    "answer":["cs3960", "Cs3960", "CS3960"]}'

fitb_dict = json.loads(fill_in_the_blank)
# print("\nfitb_dict =", fitb_dict)

ser_text = json.dumps(text_dict, indent=4)
ser_mc = json.dumps(mc_dict, indent=4)
ser_fitb = json.dumps(fitb_dict, indent=4)

print("\nser_text =", ser_text)
print("\nser_mc =", ser_mc)
print("\nser_fitb =", ser_fitb)
