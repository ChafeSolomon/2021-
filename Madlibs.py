q1 = input('Color ')
q2 = input('Verb ')
q3 = input('Planet ')
q4 = input('Adjetive ')
q5 = input('Adjetive ')

not_allowed = ['1','2','3','4','5','6','7','8','9','0']
if not_allowed in q1 or q2 or q3 or q4 or q5:
    phrase = f"{q1} foxes {q2} over the {q3} {q4} {q5}"
    print(phrase)

else:
    print('Variable uses intger')