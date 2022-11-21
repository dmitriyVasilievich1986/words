import { useSelector } from "react-redux";
import className from "classnames";
import style from "./style.scss";
import React from "react";
import axios from "axios";

const cx = className.bind(style);

function CreateVerb() {
  const pron = useSelector((s) => s.words.pron);
  if (pron.length === 0) return null;

  const [newVerb, setNewVerb] = React.useState("");
  const divRef = React.useRef(null);

  const sendHandler = () => {
    const verbWords = newVerb.split(/ |-|\/|\,/);
    const data = {
      verb: { word: verbWords[0], translate: verbWords?.[1] || verbWords[0] },
      verb_pron: [],
    };
    Array.from(divRef.current.children).map((x) => {
      Array.from(x.children).map((d) => {
        if (d?.id) {
          const words = d.value.split(/ |-|\/|\,/);
          data.verb_pron.push({
            pron: d.id,
            word: words[0],
            translate: words?.[1] || words[0],
          });
        }
      });
    });
    console.log("data", data);
    axios
      .post("/api/verbdeclension/bulk/", data)
      .then((d) => {
        console.log(d.data);
      })
      .catch((e) => console.log(e));
  };

  return (
    <div className={cx("create-card")} ref={divRef}>
      <div className={cx("create-input")}>Глагол со спряжениями:</div>
      <div className={cx("create-input")}>
        <input
          value={newVerb}
          placeholder="делать"
          onChange={(e) => setNewVerb(e.target.value)}
        />
      </div>
      {pron.map((p) => (
        <div key={p.id} className={cx("create-input")}>
          <input id={p.id} placeholder={p.word} />
        </div>
      ))}
      <div className={cx("create-input")}>
        <button className={cx("create-button")} onClick={sendHandler}>
          сохранить
        </button>
      </div>
    </div>
  );
}

export default CreateVerb;
