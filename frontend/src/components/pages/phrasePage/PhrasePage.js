import { Select } from "../mainComponents";
import { useSelector } from "react-redux";
import PhraseInput from "./PhraseInput";
import className from "classnames";
import style from "./style.scss";
import React from "react";
import axios from "axios";

const cx = className.bind(style);

function PhrasePage() {
  const randomChoices = useSelector((state) => state.words.randomChoices);
  const [selectedChoice, setSelectedChoice] = React.useState(null);
  const [choices, setChoices] = React.useState([{ id: 0 }]);
  const [phrase, setPhrase] = React.useState(null);
  const [show, setShow] = React.useState(false);

  const sendAPIRequest = () => {
    setShow(false);
    const newChoice = choices[Math.floor(Math.random() * choices.length)];
    setSelectedChoice(newChoice);
    axios
      .get(`/api/randomchoices/${newChoice.id}/`)
      .then((data) => setPhrase(data.data))
      .catch((e) => console.log(e));
  };

  React.useEffect(() => {
    sendAPIRequest();
  }, [choices]);

  const clickHandler = (e) => {
    if (e.target.type === "text") return;
    const allInputs = Array.from(
      document.getElementById("phrase").getElementsByTagName("input")
    ).map((i) => i.disabled);
    if (show || !allInputs.includes(false)) {
      setShow(false);
      sendAPIRequest();
    } else {
      setShow(true);
    }
  };

  if (randomChoices.length === 0 || phrase === null) return null;
  return (
    <div className={cx("phrase-page-card")}>
      <div className={cx("side")}>
        <div>
          <Select
            multiple={true}
            alwaysFilled={true}
            value={randomChoices}
            onChange={setChoices}
          />
        </div>
      </div>

      <div className={cx("center")}>
        <div className={cx("wrapper")} onClick={clickHandler}>
          <div>{selectedChoice?.description || ""}</div>
          <div>"{phrase.map((w) => w.translate)}"</div>
          <div className={cx("phrase-row")} id="phrase">
            {phrase.map((w, i) => (
              <PhraseInput {...w} key={i} show={show} />
            ))}
          </div>
        </div>
      </div>

      <div className={cx("side")} />
    </div>
  );
}

export default PhrasePage;
