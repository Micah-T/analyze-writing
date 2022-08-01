import fkscore
import json

def analyze(content, sitename):
  report = ""
# The BeautifulSoup output doesn't need this.
#   text = "" 
#  for line in content:
#    text = text + line.replace("\n", " ")
      
  f = fkscore.fkscore(content)
  
  fkdata = {
    "sitename": sitename,
    "number of sentences": str(f.stats["num_sentences"]),
    "number of words": str(f.stats["num_words"]),
    "Flesch Kincaid reading ease": str(f.score["readability"]),
    "Flesch Kincaid grade level": str(f.score["grade"])
  }
  
  report = report + "# Reading Ease Report for " + sitename + "\n"
  report = report + "Number of sentences: " + str(f.stats["num_sentences"]) + "\n"
  report = report + "Number of words: " + str(f.stats["num_words"]) + "\n"
  report = report + "Flesch Kincaid reading ease: " + str(f.score["readability"]) + "\n"
  report = report + "Flesch Kincaid grade level: " + str(f.score["grade"]) + "\n\n"

  stats = open(f"_output/{sitename}-stats.txt", "w")
  stats.write(str(report))
  stats.close()
  print(f"Report for {sitename} written to _output/{sitename}-stats.txt.")

  stats = open(f"_output/{sitename}-stats.json", "w")
  jsonreport = json.dumps(fkdata, indent=4)
  stats.write(jsonreport)
  stats.close()
  print(f"Report for {sitename} written to _output/{sitename}-stats.json.")

  return fkdata