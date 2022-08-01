import fkscore

def analyze(content):
  report = ""
# The BeautifulSoup output doesn't need this.
#   text = "" 
#  for line in content:
#    text = text + line.replace("\n", " ")
      
  f = fkscore.fkscore(content)
    
 # report = report + "# Reading Ease Report for " + p["filename"] + "\n"
  report = report + "Number of sentences: " + str(f.stats["num_sentences"]) + "\n"
  report = report + "Number of words: " + str(f.stats["num_words"]) + "\n"
  report = report + "Flesch Kincaid reading ease: " + str(f.score["readability"]) + "\n"
  report = report + "Flesh Kincaid grade level: " + str(f.score["grade"]) + "\n\n"

  stats = open("stats.txt", "w")
  stats.write(str(report))
  stats.close()

  print("Report written to stats.txt.")