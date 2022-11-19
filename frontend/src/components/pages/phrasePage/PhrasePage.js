import reverseIcon from "./actualize-arrows-couple-in-circle.png";
import className from "classnames";
import style from "./style.scss";
import React from "react";

import {
  phraseConstructor,
  getAllWords,
  PHRASE_NAME,
} from "./phraseConstructor";

const cx = className.bind(style);
const ph = PHRASE_NAME.ja;

function PhrasePage() {
  const [reverse, setReverse] = React.useState(false);
  const [words, setWords] = React.useState(null);
  const [show, setShow] = React.useState(false);

  React.useEffect(() => {
    setWords(getAllWords(ph));
  }, []);

  if (words === null) return null;
  return (
    <div>
      <div className={cx("empty")} />
      <div className={cx("main-module")}>
        <div
          onClick={() => setWords(getAllWords(ph))}
          onMouseLeave={() => setShow(false)}
          onMouseEnter={() => setShow(true)}
          className={cx("word")}
        >
          {show ? phraseConstructor(words, ph, reverse) : "xxxxxxxxxx"}
        </div>
        <img
          src={reverseIcon}
          onClick={() => setReverse(!reverse)}
          className={cx("icon")}
        />
        <div className={cx("word")} onClick={() => setWords(getAllWords(ph))}>
          {phraseConstructor(words, ph, !reverse)}
        </div>
      </div>
    </div>
  );
}

export default PhrasePage;
