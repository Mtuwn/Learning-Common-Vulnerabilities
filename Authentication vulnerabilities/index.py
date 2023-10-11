new_lines = []
try:
    with open('user.txt','r') as file:
        contents = file.readlines()
except Exception as e:
    print(e)
finally:
    file.close()

for content in contents:
    new_lines.append(content.strip())

    
try:
    with open('Lab.txt','w') as file:
        for line in new_lines:
            file.write((line+'\n')*10)
except Exception as e:
    print(e)
finally:
    file.close()