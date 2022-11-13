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
    setRandCase(getNounCaseRandom(null, getCaseRandom("accusative").id));
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
    <div>
      <div>
        <Phrase randVerb={randVerb} randCase={randCase} />
      </div>
      <button onClick={changeRandWord}>new</button>
    </div>
  );
}

export default PhrasePage;
