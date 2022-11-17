export const PHRASES = {
  "he see beuty river": {
    params: { case: 2 },
    caseNumber: 1,
  },
};

export default function (words, phrase, reverse) {
  const ph = (wordsArray) =>
    wordsArray.map((w) => (reverse ? w?.translate : w?.word) || w).join(" ");
  switch (phrase) {
    case PHRASES["he see beuty river"].caseNumber:
    default:
      return ph([words.pron, words.verbPron, words.adjCase, words.nounCase]);
  }
}
