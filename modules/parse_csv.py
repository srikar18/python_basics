# https://youtu.be/q5uM4VKywbA
import csv

# if delimiter being used is a part of CSV, csv writer wraps it around double quotes
# to indicate that it is content and not a delimiter

# using csv reader and writer
with open('names.csv') as rf, open('names_copy.csv', 'w') as wf:
    # default delimiter for read and write is a comma
    # if different delimiter is used and is not speciifed, each line is represented as a single item in list

    csv_contents = csv.reader(rf)
    csv_writer = csv.writer(wf, delimiter="\t")
    for line in csv_contents:
        csv_writer.writerow(line)

# using dictonary reader and writer
with open('names.csv') as rf, open('names_copy_dict.csv', 'w') as wf:
    csv_contents = csv.DictReader(rf, delimiter=',')
    csv_writer = csv.DictWriter(
        wf, fieldnames=csv_contents.fieldnames, delimiter=":")
    # writes the header
    csv_writer.writeheader()
    for line in csv_contents:
        csv_writer.writerow(line)


# CONTRIBUTORS EXERCISE

names = []

with open('contributors.csv', 'r') as rf:
    csv_reader = csv.reader(rf)

    # skip first two lines of the file
    next(csv_reader)
    next(csv_reader)

    for line in csv_reader:
        if line[0] == 'No Reward':
            break
        names.append(f'{line[0]} {line[1]}')

html_output = f'<p>There are currently {len(names)} public contributors. Thank you!</p>'
html_output += '\n<ul>'

for name in names:
    html_output += '\n\t<li>{0}</li>'.format(name)

html_output += '\n</ul>'
print(html_output)

# USING DICT READER

names = []

with open('contributors.csv') as rf:
    csv_reader = csv.DictReader(rf)
    # skip first line
    # headers are part of csv_reader.fieldnames
    next(csv_reader)
    for line in csv_reader:
        if line["FirstName"] == "No Reward":
            break
        names.append(f'{line["FirstName"]} {line["LastName"]}')

html_output = f'<p>There are currently {len(names)} public contributors. Thank you!</p>'
html_output += '\n<ul>'

for name in names:
    html_output += '\n\t<li>{0}</li>'.format(name)

html_output += '\n</ul>'
print(html_output)
print(names)