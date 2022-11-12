import { useSelector, useDispatch } from "react-redux";
import { setState } from "../../reducers/wordReducer";
import React from "react";

function Phrase() {
  const verbDeclension = useSelector((state) => state.words.verbDeclension);
  const verb = useSelector((state) => state.words.verb);
  const pron = useSelector((state) => state.words.pron);

  const [randWord, setRandWord] = React.useState(null);
  const [reverse, setReverse] = React.useState(false);

  const changeRandWord = (_) => {
    setRandWord(
      verbDeclension[Math.floor(Math.random() * verbDeclension.length)]
    );
  };

  React.useEffect(
    (_) => {
      if (pron.length > 0 && verbDeclension.length > 0) {
        changeRandWord();
      }
    },
    [pron, verbDeclension]
  );
  const dispatch = useDispatch();

  const getWordReverse = (w, r) => (r ? w.translate : w.word);

  const GetPhrase = (_) => {
    const p = pron.find((i) => i.id == randWord.pron);
    return (
      <div>
        {getWordReverse(p, reverse)} {getWordReverse(randWord, reverse)}
        <button
          style={{ margin: "0px 10px" }}
          onClick={(_) => setReverse(!reverse)}
        >
          r
        </button>
        {getWordReverse(p, !reverse)} {getWordReverse(randWord, !reverse)}
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
