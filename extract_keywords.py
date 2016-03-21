import rake
import operator
import json

stoppath = "RAKE-tutorial/FoxStoplist.txt"

rake_obj = rake.Rake(stoppath, 5, 3, 1)

input_file = open("data/1.json", 'r')

json_decode = json.load(input_file)

text = json_decode['0'].get('comments')[0]['text']

keywords = rake_obj.run(text)

print("Keywords:", keywords)
