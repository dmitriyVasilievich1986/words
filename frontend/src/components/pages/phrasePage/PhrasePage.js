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

function PhrasePage() {
  const [phrase, setPhrase] = React.useState(PHRASE_NAME.hslr);
  const [reverse, setReverse] = React.useState(false);
  const [words, setWords] = React.useState(null);
  const [show, setShow] = React.useState(false);

  React.useEffect(() => {
    setWords(getAllWords(phrase));
  }, [phrase]);

  if (words === null) return null;
  return (
    <div className={cx("phrase-main")}>
      <div className={cx("phrase-side")}>
        <select
          className={cx("phrase-select")}
          value={phrase}
          onChange={(e) => setPhrase(e.target.value)}
        >
          {Object.values(PHRASE_NAME).map((k) => (
            <option value={k} key={k}>
              {k}
            </option>
          ))}
        </select>
      </div>
      <div className={cx("phrase-center")}>
        <div className={cx("empty")} />
        <div className={cx("phrase-card")}>
          <div
            onClick={() => setWords(getAllWords(phrase))}
            onMouseLeave={() => setShow(false)}
            onMouseEnter={() => setShow(true)}
            className={cx("word")}
          >
            {show ? phraseConstructor(words, phrase, reverse) : "xxxxxxxxxx"}
          </div>
          <img
            src={reverseIcon}
            onClick={() => setReverse(!reverse)}
            className={cx("icon")}
          />
          <div
            className={cx("word")}
            onClick={() => setWords(getAllWords(phrase))}
          >
            {phraseConstructor(words, phrase, !reverse)}
          </div>
        </div>
      </div>
      <div className={cx("phrase-side")} />
    </div>
  );
}

export default PhrasePage;
