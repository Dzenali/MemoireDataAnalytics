import pandas as pd

questions = [
    "Pouvez-vous citer trois points positifs du plugin ? ",
    "Pouvez-vous citer trois points negatifs du plugin ? ",
    "Quels succès auriez-vous souhaité voir dans le plugin ?"
]

input_path_solo = "data/forms/SOLO.csv"
input_path_team = "data/forms/TEAM.csv"
output_path = "generated/forms/open-questions.tex"

df_solo = pd.read_csv(input_path_solo)
df_team = pd.read_csv(input_path_team)
df = pd.concat([df_solo, df_team], ignore_index=True)
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

    f.write("\t\t\\textbf{" + questions[0] + "}")
    for question in questions[1:]:
        f.write(" & \\textbf{" + question + "}")

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