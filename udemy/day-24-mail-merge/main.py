names = []
with open(r'udemy\day-24-mail-merge\Input\Names\invited_names.txt') as names_file:
    names = names_file.readlines()

text = ''
with open(r'udemy\day-24-mail-merge\Input\Letters\starting_letter.txt') as starting_file:
    text = starting_file.read()
    for name in names:
        name = name.strip('\n')
        with open(f'udemy/day-24-mail-merge/Output/ReadyToSend/letter_for_{name}.txt', 'w') as output_file:
            output_file.write(text.replace('[name]',name))