import { WORDS } from "Constants";

export function getRequest(word, data) {
  switch (word) {
    case WORDS.Verb:
      const verbsKeys = Object.keys(data).filter(
        (k) => k !== "Infinitive" && k !== "Base"
      );
      const verbs = [];
      verbsKeys.map((k) => {
        data[k].map((d) => {
          verbs.push({
            translate: d.translate,
            pronoun: d.pronoun,
            word: d.word,
            time: d.time,
          });
        });
      });
      return {
        translate: data.Infinitive[0].translate,
        word: data.Infinitive[0].word,
        base: data.Base[0].word,
        verb: verbs,
      };
    default:
      break;
  }
}
