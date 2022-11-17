import store from "./store";

export function getVerbDeclensionRandom(pron = null, verb = null) {
  let vd = store
    .getState()
    .words.verbDeclension.filter(
      (i) =>
        (pron === null || i.pron == pron) && (verb === null || i.verb == verb)
    );
  return vd[Math.floor(Math.random() * vd.length)];
}

export function getAdjCaseRandom(
  adjective = null,
  wordCase = null,
  gender = null
) {
  let vd = store
    .getState()
    .words.adjCase.filter(
      (i) =>
        (adjective === null || i.adjective == adjective) &&
        (wordCase === null || i.case == wordCase) &&
        (gender === null || i.gender == gender)
    );
  return vd[Math.floor(Math.random() * vd.length)];
}

export function getNounCaseRandom(noun = null, wordCase = null, gender = null) {
  let vd = store
    .getState()
    .words.nounCase.filter(
      (i) =>
        (wordCase === null || i.case == wordCase) &&
        (gender === null || i.gender == gender) &&
        (noun === null || i.noun == noun)
    );
  return vd[Math.floor(Math.random() * vd.length)];
}

export function getPronRandom(id_ = null) {
  const vd = store.getState().words.pron;
  return id_
    ? vd.find((i) => i.id == id_)
    : vd[Math.floor(Math.random() * vd.length)];
}

export function getVerbRandom(id_ = null) {
  const vd = store.getState().words.verb;
  return id_
    ? vd.find((i) => i.id == id_)
    : vd[Math.floor(Math.random() * vd.length)];
}

export function getCaseRandom(name = null) {
  let vd = store.getState().words.case;
  return name
    ? vd.find((i) => i.name == name)
    : vd[Math.floor(Math.random() * vd.length)];
}
