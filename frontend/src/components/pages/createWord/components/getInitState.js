import store from "Reducers/store";
import { WORDS } from "Constants";

const infinitivePayload = {
  Infinitive: [
    {
      translateText: "Перевод",
      wordText: "Глагол",
      translate: "",
      word: "",
    },
  ],
};
const withBaseInfinitive = {
  Base: [
    {
      translateText: "Перевод",
      wordText: "Основа",
      translate: "",
      word: "",
    },
  ],
  ...infinitivePayload,
};

export function getInitState(word) {
  let payload = {};
  switch (word) {
    case WORDS.Verb:
      payload = { ...withBaseInfinitive };
      store.getState().words.time.map((d) => {
        const newData = store.getState().words.personalPronoun.map((pp) => ({
          translateText: pp.translate,
          wordText: pp.word,
          declention: d.id,
          pronoun: pp.id,
          translate: "",
          word: "",
        }));
        payload[d.word] = newData;
      });
      break;
    case WORDS.Noun:
      payload = { ...withBaseInfinitive };
      store.getState().words.declentions.map((d) => {
        const newData = store.getState().words.gender.map((pp) => ({
          translateText: pp.translate,
          wordText: pp.word,
          declention: d.id,
          pronoun: pp.id,
          translate: "",
          word: "",
        }));
        payload[d.word] = newData;
      });
      break;
    default:
      break;
  }
  return payload;
}
