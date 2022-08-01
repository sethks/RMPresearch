import requests
import json

f = open("listOfBUProfessors.txt", 'r')
myfile = open("newFile.txt", 'w')
count = 1

# function to retireve an array of dictionaries that contains information about each professor at BU
def get_num_of_professors():  
        page = requests.get("http://www.ratemyprofessors.com/filter/professor/?&page=1&filter=teacherlastname_sort_s+asc&query=*%3A*&queryoption=TEACHER&queryBy=schoolId&sid=124")
        temp_jsonpage = json.loads(page.content)
        num_of_prof = (temp_jsonpage["remaining"] + 20)  # get the number of professors if needed
        print(temp_jsonpage)

# for loop to clean up the textfile to make it easier for MySQL to read
for x in f:
    new_line = ""
    temp = x.strip()
    temp = str(count) + ', ' + temp + '\n'
    #myfile.write(temp)
    print(temp)
    count += 1

f.close()
myfile.close()

#credit to tisuela on github for the help on json requests 