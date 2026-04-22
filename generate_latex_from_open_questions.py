import pandas as pd

questions = [
    "S-Donner 3 points positifs du plugin",
    "S-Donner 3 points négatifs du plugin",
    "S-Donner 3 améliorations à apporter au plugin"
]

input_path = "generated/forms/data.csv"
output_path = "generated/forms/open-questions.tex"

df = pd.read_csv(input_path)
print(df)
data = df[questions]

def process_text(text):
    if "\n" not in text:
        return text

    return text.replace("\n", " \\newline ")


with open(output_path, "w", encoding="utf-8") as f:
    f.write("\\begin{center}\n")
    f.write("\t\\begin{longtable}{|p{5.1cm}|p{5.1cm}|p{5.1cm}|}\n")
    f.write("\t\t\\hline\n")

    f.write("\t\t\\textbf{" + questions[0][2:] + "}")
    for question in questions[1:]:
        f.write(" & \\textbf{" + question[2:] + "}")

    f.write(" \\\\\n\t\t\hline\n")

    for idx, row in data.iterrows():
        # if idx > 2: break
        f.write("\t\t" + process_text(str(row[questions[0]])))
        for question in questions[1:]:
            f.write(" & " + process_text(str(row[question])))
        f.write(" \\\\\n\t\t\hline\n")

    f.write("\t\\end{longtable}\n")
    f.write("\t\\label{table:open-questions-answers}\n")
    f.write("\\end{center}")