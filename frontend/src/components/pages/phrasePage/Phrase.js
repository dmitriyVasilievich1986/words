import { getAdjCaseRandom, getPronRandom } from "Reducers/wordRandomizer";
import React from "react";

function Phrase(props) {
  const [reverse, setReverse] = React.useState(false);
  const [show, setShow] = React.useState(false);

  const wr = (w, r) => w.map((i) => (r ? i.translate : i.word)).join(" ");

  const ac = getAdjCaseRandom(null, props.randCase.case);
  const p = getPronRandom(props.randVerb.pron);

  return (
    <div style={{ display: "flex" }}>
      <div
        style={{
          backgroundColor: show ? "white" : "black",
          width: "fit-content",
          padding: "10px 20px",
          cursor: "pointer",
        }}
        onMouseLeave={(_) => setShow(false)}
        onMouseEnter={(_) => setShow(true)}
        onClick={props.changeRandWord}
      >
        {wr([p, props.randVerb, ac, props.randCase], reverse)}
      </div>
      <button onClick={(_) => setReverse(!reverse)}>r</button>
      <div
        style={{
          width: "fit-content",
          padding: "10px 20px",
          cursor: "pointer",
        }}
        onClick={props.changeRandWord}
      >
        {wr([p, props.randVerb, ac, props.randCase], !reverse)}
      </div>
    </div>
  );
}

export default Phrase;
