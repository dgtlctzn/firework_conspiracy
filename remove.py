with open('firework_locs_2.csv', 'r') as file:
    text = file.read().replace(" '", '')
    text = text.replace(', ', ',')
    text = text.replace("'", '')

with open('firework_fix.csv', 'w') as file_2:
    file_2.write(text)