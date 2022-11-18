import reverseIcon from "./actualize-arrows-couple-in-circle.png";
import phraseConstructor, { PHRASES } from "./phraseConstructor";
import { getRandomWords } from "Reducers/wordRandomizer";
import className from "classnames";
import style from "./style.scss";
import React from "react";

const cx = className.bind(style);
const ph = "he see beuty river";

function PhrasePage() {
  const [reverse, setReverse] = React.useState(false);
  const [words, setWords] = React.useState(null);
  const [show, setShow] = React.useState(false);

  React.useEffect((_) => {
    setWords(getRandomWords(PHRASES[ph].params));
  }, []);

  if (words === null) return null;
  return (
    <div style={{ display: "flex", alignItems: "center" }}>
      <div
        onClick={(_) => setWords(getRandomWords(PHRASES[ph].params))}
        className={cx("word", { hide: !show })}
        onMouseLeave={(_) => setShow(false)}
        onMouseEnter={(_) => setShow(true)}
      >
        {phraseConstructor(words, PHRASES[ph].caseNumber, reverse)}
      </div>
      <img
        src={reverseIcon}
        onClick={(_) => setReverse(!reverse)}
        className={cx("icon")}
      />
      <div
        className={cx("word")}
        onClick={(_) => setWords(getRandomWords(PHRASES[ph].params))}
      >
        {phraseConstructor(words, PHRASES[ph].caseNumber, !reverse)}
      </div>
    </div>
  );
}

export default PhrasePage;
