import { useSelector } from "react-redux";
import Phrase from "./Phrase";
import React from "react";

import {
  getVerbDeclensionRandom,
  getNounCaseRandom,
  getCaseRandom,
} from "Reducers/wordRandomizer";

function PhrasePage() {
  const verbDeclension = useSelector((state) => state.words.verbDeclension);
  const nounCase = useSelector((state) => state.words.nounCase);

  const [randVerb, setRandVerb] = React.useState(null);
  const [randCase, setRandCase] = React.useState(null);

  const changeRandWord = (_) => {
    setRandVerb(getVerbDeclensionRandom());
    setRandCase(getNounCaseRandom(null, getCaseRandom("accusative").id), null);
  };

  React.useEffect(
    (_) => {
      if (verbDeclension.length > 0 && nounCase.length > 0) {
        changeRandWord();
      }
    },
    [verbDeclension, nounCase]
  );

  if (randVerb === null) return null;
  return (
    <Phrase
      changeRandWord={changeRandWord}
      randVerb={randVerb}
      randCase={randCase}
    />
  );
}

export default PhrasePage;
