import { useSelector, useDispatch } from "react-redux";
import React from "react";

function Phrase() {
  const verbDeclension = useSelector((state) => state.words.verbDeclension);
  const nounCase = useSelector((state) => state.words.nounCase);
  const wordCase = useSelector((state) => state.words.case);
  const pron = useSelector((state) => state.words.pron);

  const [randWord, setRandWord] = React.useState(null);
  const [randCase, setRandCase] = React.useState(null);
  const [reverse, setReverse] = React.useState(false);

  const changeRandWord = (_) => {
    setRandWord(
      verbDeclension[Math.floor(Math.random() * verbDeclension.length)]
    );
    const a = wordCase.find((i) => i.name == "accusative");
    const l = nounCase.filter((i) => i.case == a.id);
    setRandCase(l[Math.floor(Math.random() * l.length)]);
  };

  React.useEffect(
    (_) => {
      if (verbDeclension.length > 0 && nounCase.length > 0) {
        changeRandWord();
      }
    },
    [verbDeclension, nounCase]
  );

  const getWordReverse = (w, r) => (r ? w.translate : w.word);

  const GetPhrase = (_) => {
    const p = pron.find((i) => i.id == randWord.pron);
    return (
      <div>
        {getWordReverse(p, reverse)} {getWordReverse(randWord, reverse)}{" "}
        {getWordReverse(randCase, reverse)}
        <button
          style={{ margin: "0px 10px" }}
          onClick={(_) => setReverse(!reverse)}
        >
          r
        </button>
        {getWordReverse(p, !reverse)} {getWordReverse(randWord, !reverse)}{" "}
        {getWordReverse(randCase, !reverse)}
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
