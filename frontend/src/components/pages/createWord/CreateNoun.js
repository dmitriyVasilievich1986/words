import { useSelector } from "react-redux";
import className from "classnames";
import style from "./style.scss";
import React from "react";
import axios from "axios";

const cx = className.bind(style);

function CreateNoun() {
  const case_ = useSelector((s) => s.words.case);
  if (case_.length === 0) return null;

  const [newGender, setNewGender] = React.useState("f");
  const [newNoun, setNewNoun] = React.useState("");
  const divRef = React.useRef(null);

  const sendHandler = () => {
    const verbWords = newNoun.split(/ |-|\/|\,/);
    const data = {
      noun: {
        translate: verbWords?.[1] || verbWords[0],
        word: verbWords[0],
        gender: newGender,
      },
      case_noun: [],
    };
    Array.from(divRef.current.children).map((x) => {
      Array.from(x.children).map((d) => {
        if (d?.id) {
          const words = d.value.split(/ |-|\/|\,/);
          data.case_noun.push({
            translate: words?.[1] || words[0],
            gender: newGender,
            word: words[0],
            case: d.id,
          });
        }
      });
    });
    console.log("data", data);
    axios
      .post("/api/nouncase/bulk/", data)
      .then((d) => {
        console.log(d.data);
      })
      .catch((e) => console.log(e));
  };

  return (
    <div className={cx("create-card")} ref={divRef}>
      <div className={cx("create-input")}>Существительное:</div>
      <div className={cx("create-input")}>
        <select
          style={{ width: "150px", marginTop: "1rem" }}
          onChange={(e) => setNewGender(e.target.value)}
          value={newGender}
        >
          <option value="m">m</option>
          <option value="f">f</option>
          <option value="n">n</option>
        </select>
      </div>
      <div className={cx("create-input")}>
        <input
          value={newNoun}
          placeholder="дверь"
          onChange={(e) => setNewNoun(e.target.value)}
        />
      </div>
      {case_.map((p) => (
        <div key={p.id} className={cx("create-input")}>
          <input id={p.id} placeholder={p.name} />
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

export default CreateNoun;
