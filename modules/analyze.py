import json
import fkscore

try:
  paperdata = open("papers.json")
except:
  print("Please create papers.json with a dictionary of papers to process.")
  exit()
try:
  papers = json.loads(paperdata.read())
except: 
  print("Please check that papers.json is correctly written.")
  exit()

report = ""
for p in papers["papers"]:
  try: 
    paper = open(p["filename"])
  except: 
    print(f"{p['filename']} not found. Moving to the next paper.")
    report = report + p["filename"] + " not found.\n"
  else: 
    text = ""
    for line in paper:
        text = text + line.replace("\n", " ")
    
    f = fkscore.fkscore(text)
    
    report = report + "# Reading Ease Report for " + p["filename"] + "\n"
    report = report + "Number of sentences: " + str(f.stats["num_sentences"]) + "\n"
    report = report + "Number of words: " + str(f.stats["num_words"]) + "\n"
    report = report + "Flesch Kincaid reading ease: " + str(f.score["readability"]) + "\n"
    report = report + "Flesh Kincaid grade level: " + str(f.score["grade"]) + "\n\n"

stats = open("stats.txt", "w")
stats.write(str(report))
stats.close()

paper.close()
paperdata.close()

print("Report written to stats.txt.")