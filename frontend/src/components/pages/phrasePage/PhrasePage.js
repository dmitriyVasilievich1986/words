import { useSelector } from "react-redux";
import arrowPNG from "./circleArrow.png";
import PhraseInput from "./PhraseInput";
import className from "classnames";
import style from "./style.scss";
import React from "react";
import axios from "axios";

const cx = className.bind(style);

function PhrasePage() {
  const randomChoices = useSelector((state) => state.words.randomChoices);
  const [selectValue, setSelectValue] = React.useState(0);
  const [phrase, setPhrase] = React.useState(null);
  const [show, setShow] = React.useState(false);

  const sendAPIRequest = () => {
    axios
      .get(`/api/randomchoices/${selectValue}/`)
      .then((data) => setPhrase(data.data))
      .catch((e) => console.log(e));
  };

  React.useEffect(() => {
    sendAPIRequest();
  }, [randomChoices, selectValue]);

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
          <select
            value={selectValue}
            onChange={(e) => setSelectValue(e.target.value)}
          >
            {randomChoices.map((p, i) => (
              <option value={i} key={i}>
                {p.name}
              </option>
            ))}
          </select>
        </div>
      </div>
      <div className={cx("center")}>
        <div className={cx("phrase-row")} onClick={clickHandler} id="phrase">
          {phrase.map((w, i) => (
            <PhraseInput {...w} key={i} show={show} />
          ))}
          <img src={arrowPNG} />
          {phrase.map((w) => w.translate)}
        </div>
      </div>
      <div className={cx("side")} />
    </div>
  );
}

export default PhrasePage;
