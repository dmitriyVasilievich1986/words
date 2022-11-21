import { useSelector } from "react-redux";
import className from "classnames";
import style from "./style.scss";
import React from "react";
import axios from "axios";

const cx = className.bind(style);
// const genders = ["m", "f"];
const genders = ["m", "f", "n"];

function CreateAdj() {
  const case_ = useSelector((s) => s.words.case);
  if (case_.length === 0) return null;

  const [newGender, setNewGender] = React.useState("f");
  const [newAdj, setNewAdj] = React.useState("");
  const divRef = React.useRef(null);

  const sendHandler = () => {
    const adjWords = newAdj.split(/ |-|\/|\,/);
    const data = {
      adjective: {
        translate: adjWords?.[1] || adjWords[0],
        word: adjWords[0],
        gender: newGender,
      },
      case_adj: [],
    };
    Array.from(divRef.current.children).map((x) => {
      Array.from(x.children).map((d) => {
        if (d?.id) {
          const words = d.value.split(/ |-|\/|\,/);
          const ids = d.id.split("_");
          data.case_adj.push({
            translate: words?.[1] || words[0],
            word: words[0],
            gender: ids[0],
            case: ids[1],
          });
        }
      });
    });
    console.log("data", data);
    axios
      .post("/api/adjcase/bulk/", data)
      .then((d) => {
        console.log(d.data);
      })
      .catch((e) => console.log(e));
  };

  return (
    <div className={cx("create-card")} ref={divRef}>
      <div className={cx("create-input")}>Прилагательное:</div>
      <div className={cx("create-input")}>
        <select
          style={{ width: "150px", marginTop: "1rem" }}
          onChange={(e) => setNewGender(e.target.value)}
          value={newGender}
        >
          {genders.map((g) => (
            <option key={g} value={g}>
              {g}
            </option>
          ))}
        </select>
      </div>
      <div className={cx("create-input")}>
        <input
          value={newAdj}
          placeholder="красивый"
          onChange={(e) => setNewAdj(e.target.value)}
        />
      </div>
      {genders.map((g) =>
        case_.map((p) => (
          <div key={`${g}_${p.id}`} className={cx("create-input")}>
            <input id={`${g}_${p.id}`} placeholder={`${g} ${p.name}`} />
          </div>
        ))
      )}
      <div className={cx("create-input")}>
        <button className={cx("create-button")} onClick={sendHandler}>
          сохранить
        </button>
      </div>
    </div>
  );
}

export default CreateAdj;
