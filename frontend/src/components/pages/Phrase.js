import { useSelector, useDispatch } from "react-redux";
import React from "react";

import {
  getVerbDeclensionRandom,
  getNounCaseRandom,
  getAdjCaseRandom,
  getCaseRandom,
  getPronRandom,
} from "../../reducers/wordRandomizer";

function Phrase() {
  const verbDeclension = useSelector((state) => state.words.verbDeclension);
  const nounCase = useSelector((state) => state.words.nounCase);

  const [randWord, setRandWord] = React.useState(null);
  const [randCase, setRandCase] = React.useState(null);
  const [reverse, setReverse] = React.useState(false);

  const changeRandWord = (_) => {
    setRandWord(getVerbDeclensionRandom());
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

  const GetPhrase = (_) => {
    const p = getPronRandom(randWord.pron);
    const ac = getAdjCaseRandom(null, randCase.case);
    const wr = (w, r) => w.map((i) => (r ? i.translate : i.word)).join(" ");
    return (
      <div>
        {wr([p, randWord, ac, randCase], reverse)}
        <button
          style={{ margin: "0px 10px" }}
          onClick={(_) => setReverse(!reverse)}
        >
          r
        </button>
        {wr([p, randWord, ac, randCase], !reverse)}
      </div>
    );
  };

  if (randWord === null) return null;
  return (
    <div>
      <div>
        <GetPhrase />
      </div>
      <button onClick={changeRandWord}>new</button>
    </div>
  );
}

export default Phrase;
