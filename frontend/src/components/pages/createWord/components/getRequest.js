import { WORDS } from "Constants";

const getFlatenData = (data) => {
  return Object.keys(data)
    .map((k) => (["Infinitive", "Base"].includes(k) ? [] : data[k]))
    .flat();
};

export function getRequest(word, data) {
  const base = {
    ...data.Infinitive[0],
    base: data.Base[0].word,
  };
  switch (word) {
    case WORDS.verbInfinitive:
      return { ...base, verb: getFlatenData(data) };
    case WORDS.nounInfinitive:
      return { ...base, noun: getFlatenData(data) };
    default:
      break;
  }
}
