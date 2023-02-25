import store from "Reducers/store";
import { WORDS } from "Constants";

const infinitivePayload = (props) => ({
  Infinitive: [
    {
      translate: props?.translate || "",
      translateText: "Перевод",
      word: props?.word || "",
      id: props?.id || null,
      wordText: "Глагол",
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
  store.getState().words.declentions.map((d) => {
    const newData = data
      .filter((nd) => nd.declention === d.id)
      .map((nd) => {
        const g = store
          .getState()
          .words.gender.find((gn) => gn.id === nd.gender);
        return {
          ...nd,
          translateText: `${g.translate} ${nd.plural ? "мн." : "ед."}`,
          wordText: `${g.word} ${nd.plural ? "plur." : "sing."}`,
        };
      });
    payload[d.word] = newData;
  });
  return payload;
};
const getNounData = (props) => {
  if (props?.noun) return props.noun;
  const payload = [];
  store.getState().words.declentions.map((d) =>
    store.getState().words.gender.map((g) =>
      [true, false].map((p) => {
        payload.push({
          declention: d.id,
          translate: "",
          gender: g.id,
          plural: p,
          word: "",
        });
      })
    )
  );
  return payload;
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
