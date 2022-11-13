import { getAdjCaseRandom, getPronRandom } from "Reducers/wordRandomizer";
import reverseIcon from "./actualize-arrows-couple-in-circle.png";
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
    <div style={{ display: "flex", alignItems: "center" }}>
      <div
        className={className("word", { hide: !show })}
        onMouseLeave={(_) => setShow(false)}
        onMouseEnter={(_) => setShow(true)}
        onClick={props.changeRandWord}
      >
        {wr([p, props.randVerb, ac, props.randCase], reverse)}
      </div>
      <img
        src={reverseIcon}
        onClick={(_) => setReverse(!reverse)}
        style={{ width: "25px", height: "25px", cursor: "pointer" }}
      />
      <div className={className("word")} onClick={props.changeRandWord}>
        {wr([p, props.randVerb, ac, props.randCase], !reverse)}
      </div>
    </div>
  );
}

export default Phrase;
