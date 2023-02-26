import store from "Reducers/store";
import { WORDS } from "Constants";

const infinitivePayload = (props) => ({
  Infinitive: [
    {
      translate: props?.translate || "",
      translateText: "Перевод",
      word: props?.word || "",
      id: props?.id || null,
      wordText: "Слово",
    },
  ],
});
const basePayload = (props) => ({
  Base: [
    {
      translate: props?.translate || "",
      translateText: "Перевод",
      word: props?.base || "",
      wordText: "Основа",
    },
  ],
});
const verbPayload = (data) => {
  const payload = {};
  store.getState().words.time.map((t) => {
    const newData = data
      .filter((d) => d.time === t.id)
      .map((d) => {
        const p = store
          .getState()
          .words.personalPronoun.find((pp) => pp.id === d.pronoun);
        return {
          ...d,
          translateText: p.translate,
          wordText: p.word,
        };
      });
    payload[t.word] = newData;
  });
  return payload;
};
const getVerbData = (props) => {
  if (props?.verb) return props.verb;
  return store
    .getState()
    .words.time.map((t) =>
      store.getState().words.personalPronoun.map((pp) => ({
        pronoun: pp.id,
        translate: "",
        time: t.id,
        word: "",
      }))
    )
    .flat();
};
const nounPayload = (data) => {
  const payload = {};
  store.getState().words.declentions.map((decl) => {
    const newData = data
      .filter((d) => d.declention == decl.id)
      .map((d) => ({
        ...d,
        translateText: d.plural ? "мн." : "ед.",
        wordText: d.plural ? "plur." : "sing.",
      }));
    payload[decl.word] = newData;
  });
  return payload;
};
const getNounData = (props) => {
  if (props?.noun) return props.noun;
  return store
    .getState()
    .words.declentions.map((d) => {
      return [false, true].map((p) => ({
        declention: d.id,
        translate: "",
        plural: p,
        word: "",
      }));
    })
    .flat();
};

export function getInitState(word, props) {
  switch (word) {
    case WORDS.verbInfinitive:
      return {
        ...basePayload(props),
        ...infinitivePayload(props),
        ...verbPayload(getVerbData(props)),
      };
    case WORDS.nounInfinitive:
      return {
        ...basePayload(props),
        ...infinitivePayload(props),
        ...nounPayload(getNounData(props)),
      };
    default:
      return {};
  }
}
