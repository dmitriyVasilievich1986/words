import store from "./store";

export function getRandomWords(params) {
  const pron = params?.pron || getPronRandom();
  const verb = params?.verb || getVerbRandom();
  const verbPron = getVerbDeclensionRandom(pron.id, verb.id);

  const gender = params?.gender || getGenderRandom();
  const case_ = params?.case || getCaseRandom();

  const adjective =
    params?.adjective || getAdjectiveRandom(null, gender?.id || gender);
  const noun = params?.noun || getNounRandom(null, gender?.id || gender);
  const pronoun =
    params?.pronoun || getPronounRandom(null, gender?.id || gender);

  const adjCase = getAdjCaseRandom(
    adjective?.id || adjective,
    case_?.id || case_,
    gender
  );
  const nounCase = getNounCaseRandom(
    noun.id || noun,
    case_?.id || case_,
    gender
  );

  return {
    verbPron,
    verb,
    pron,
    adjective,
    gender,
    case_,
    noun,
    nounCase,
    adjCase,
    pronoun,
  };
}

export function getVerbDeclensionRandom(pron = null, verb = null) {
  let vd = store
    .getState()
    .words.verbDeclension.filter(
      (i) =>
        (pron === null || i.pron == pron) && (verb === null || i.verb == verb)
    );
  if (vd.length == 0) {
    console.log("getVerbDeclensionRandom", pron, verb);
  }
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
  if (vd.length == 0) {
    console.log("getAdjCaseRandom", adjective, wordCase, gender);
  }
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
  if (vd.length == 0) {
    console.log("getNounCaseRandom", noun, wordCase, gender);
  }
  return vd[Math.floor(Math.random() * vd.length)];
}

export function getNounRandom(word = null, gender = null) {
  let vd = store
    .getState()
    .words.noun.filter(
      (i) =>
        (gender === null || i.gender == gender) &&
        (word === null || i.word == word)
    );
  return vd[Math.floor(Math.random() * vd.length)];
}

export function getAdjectiveRandom(word = null, gender = null) {
  let vd = store
    .getState()
    .words.adjective.filter(
      (i) =>
        (gender === null || i.gender == gender) &&
        (word === null || i.word == word)
    );
  return vd[Math.floor(Math.random() * vd.length)];
}

export function getPronounRandom(word = null, gender = null) {
  let vd = store
    .getState()
    .words.pronoun.filter(
      (i) =>
        (gender === null || i.gender == gender) &&
        (word === null || i.word == word)
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

export function getGenderRandom(name = null) {
  let vd = ["f", "m"];
  // let vd = ["f", "m", "n"];
  return name
    ? vd.find((i) => i == name)
    : vd[Math.floor(Math.random() * vd.length)];
}
