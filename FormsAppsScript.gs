function exportScaleQuestionsFromIntelliGameForms() {
  const files = DriveApp.getFilesByType(MimeType.GOOGLE_FORMS);
  const questions = [["Nom du Formulaire", "Titre", "Type", "Label Gauche", "Label Droit"]];
  const allQuestions = [["Nom du Formulaire", "Titre", "Type"]];

  while (files.hasNext()) {
    const file = files.next();
    const fileName = file.getName();
    console.log(fileName)

    // Filtrer uniquement les formulaires contenant "IntelliGame" (insensible à la casse)
    if (fileName != "leaderboard" && fileName != "achievements" && fileName != "demographic" && fileName != "satisfaction"){
      continue;
    }

    const form = FormApp.openById(file.getId());
    const items = form.getItems();

    for (let i = 0; i < items.length; i++) {
      const item = items[i];
      const type = item.getType();

      if (type === FormApp.ItemType.SCALE) {
        const scaleItem = item.asScaleItem();
        const title = scaleItem.getTitle();
        const labelLeft = scaleItem.getLeftLabel();
        const labelRight = scaleItem.getRightLabel();

        questions.push([fileName, title, type, labelLeft, labelRight]);
      }

      allQuestions.push([fileName, title, type]);
    }
  }

  const sheet = SpreadsheetApp.create("Export IntelliGame SCALE Questions");
  const range = sheet.getActiveSheet().getRange(1, 1, questions.length, questions[0].length);
  range.setValues(questions);

  const sheetAll = SpreadsheetApp.create("Export IntelliGame Questions");
  const rangeAll = sheetAll.getActiveSheet().getRange(1, 1, allQuestions.length, allQuestions[0].length);
  rangeAll.setValues(allQuestions);
}
