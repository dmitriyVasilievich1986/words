import { getAdjCaseRandom, getPronRandom } from "Reducers/wordRandomizer";
import className from "classnames";
import style from "./style.scss";
import React from "react";

const cx = className.bind(style);

function Phrase(props) {
  const [reverse, setReverse] = React.useState(false);
  const [show, setShow] = React.useState(false);

  const wr = (w, r) => w.map((i) => (r ? i.translate : i.word)).join(" ");

  const ac = getAdjCaseRandom(null, props.randCase.case);
  const p = getPronRandom(props.randVerb.pron);

  return (
    <div style={{ display: "flex" }}>
      <div
        className={className("word", { hide: !show })}
        onMouseLeave={(_) => setShow(false)}
        onMouseEnter={(_) => setShow(true)}
        onClick={props.changeRandWord}
      >
        {wr([p, props.randVerb, ac, props.randCase], reverse)}
      </div>
      <button onClick={(_) => setReverse(!reverse)}>r</button>
      <div className={className("word")} onClick={props.changeRandWord}>
        {wr([p, props.randVerb, ac, props.randCase], !reverse)}
      </div>
    </div>
  );
}

export default Phrase;
