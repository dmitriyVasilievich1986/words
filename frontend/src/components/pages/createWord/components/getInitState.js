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
const basePayload = {
  Base: [
    {
      translateText: "Перевод",
      wordText: "Основа",
      translate: "",
      word: "",
    },
  ],
};

export function getInitState(word) {
  let payload = {};
  switch (word) {
    case WORDS.Verb:
      payload = { ...basePayload, ...infinitivePayload };
      store.getState().words.time.map((d) => {
        const newData = store.getState().words.personalPronoun.map((pp) => ({
          translateText: pp.translate,
          wordText: pp.word,
          pronoun: pp.id,
          translate: "",
          time: d.id,
          word: "",
        }));
        payload[d.word] = newData;
      });
      break;
    case WORDS.Noun:
      payload = { ...basePayload, ...infinitivePayload };
      store.getState().words.declentions.map((d) => {
        const newData = [
          ...store.getState().words.gender.map((pp) => ({
            translateText: `${pp.translate} ед.`,
            wordText: `${pp.word} sing.`,
            declention: d.id,
            gender: pp.id,
            plural: false,
            translate: "",
            word: "",
          })),
          ...store.getState().words.gender.map((pp) => ({
            translateText: `${pp.translate} мн.`,
            wordText: `${pp.word} plur.`,
            declention: d.id,
            gender: pp.id,
            translate: "",
            plural: true,
            word: "",
          })),
        ];
        payload[d.word] = newData;
      });
      break;
    default:
      break;
  }
  return payload;
}
