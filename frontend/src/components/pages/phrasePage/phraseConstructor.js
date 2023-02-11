import { getRandomWords } from "Reducers/wordRandomizer";

export const PHRASE_NAME = {
  hslr: "я вижу красивую реку",
  bt: "красивый стол",
  hs: "его сестра",
  ys: "я вижу",
  ja: "я",
};

export function getAllWords(phrase) {
  switch (phrase) {
    case PHRASE_NAME.hslr:
      return getRandomWords({ case: 2 });
    case PHRASE_NAME.bt:
      return getRandomWords({ case: 1 });
    case PHRASE_NAME.ja:
    case PHRASE_NAME.ys:
    case PHRASE_NAME.hs:
    default:
      return getRandomWords();
  }
}

export function phraseConstructor(words, phrase, reverse) {
  const ph = (wordsArray) =>
    wordsArray.map((w) => (reverse ? w?.translate : w?.word) || w).join(" ");

  switch (phrase) {
    case PHRASE_NAME.ja:
      return ph([words.pron]);
    case PHRASE_NAME.hs:
      return ph([words.pronoun, words.noun]);
    case PHRASE_NAME.ys:
      return ph([words.pron, words.verbPron]);
    case PHRASE_NAME.bt:
      return ph([words.adjCase, words.nounCase]);
    case PHRASE_NAME.hslr:
    default:
      return ph([words.pron, words.verbPron, words.adjCase, words.nounCase]);
  }
}
