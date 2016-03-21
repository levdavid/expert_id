import rake
import operator
import json
import csv

stoppath = "RAKE-tutorial/FoxStoplist.txt"

rake_obj = rake.Rake(stoppath, 4, 4, 1)

input_file = open("data/1.json", 'r')

output_file = open("data/1.csv", 'wb')

json_decode = json.load(input_file)

comments = json_decode['0'].get('comments')

writer = csv.writer(output_file, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)

for comment in comments:
	print comment['text']
	keywords = rake_obj.run(comment['text'])
	print("Keywords:", keywords[0:10])
	writer.writerow([comment['text'],keywords[0:10]])