import classnames from "classnames/bind";
import PhraseInput from "./PhraseInput";
import style from "./style.scss";
import React from "react";
import axios from "axios";
import { Delimiter } from "../components";

const cx = classnames.bind(style);

function PhraseForm(props) {
  const formRef = React.useRef(null);

  const [pk, setPk] = React.useState(null);
  const [words, setWords] = React.useState([]);
  const [error, setError] = React.useState(false);

  React.useEffect(() => {
    if (props.selectedRules.length === 0) {
      setWords([]);
    } else {
      getWords();
    }
  }, [props.selectedRules]);

  const getWords = () => {
    const newPk =
      props.selectedRules[
        Math.floor(Math.random() * props.selectedRules.length)
      ];
    setPk(newPk);
    setError(false);
    axios
      .get(`api/rulesrandom/${newPk}/`)
      .then((data) => {
        setWords(data.data);
      })
      .catch((e) => console.log(e));
  };

  const submitHandler = (e) => {
    e.preventDefault();
    if (
      Array.from(formRef.current.getElementsByTagName("input")).find(
        (i) => i.name === "isNotComplited"
      )
    ) {
      setError(true);
    } else {
      getWords();
    }
  };

  if (words.length === 0)
    return (
      <div className={cx("container")}>
        <div style={{ textAlign: "center" }}>
          Выберите одно или несколько правил.
        </div>
      </div>
    );
  const description = props.rules.find((r) => r.id === pk)?.description;
  return (
    <div className={cx("container")}>
      <form onSubmit={submitHandler} ref={formRef}>
        <div className={cx("row")} style={{ marginBottom: "2rem" }}>
          <div className={cx("description")}>{description}</div>
        </div>
        <div className={cx("row")}>
          <div>{words.map((w) => w.translate).join(" ")}</div>
        </div>
        <Delimiter />
        <div className={cx("row")}>
          <div className={cx("problem")}>
            {words.map((w) => (
              <PhraseInput key={w.word} {...w} error={error} />
            ))}
          </div>
        </div>
      </form>
    </div>
  );
}

export default PhraseForm;
