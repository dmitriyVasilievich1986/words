import { Select } from "../mainComponents";
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
  const [choices, setChoices] = React.useState([{ id: 0 }]);
  const [phrase, setPhrase] = React.useState(null);
  const [show, setShow] = React.useState(false);

  const sendAPIRequest = () => {
    setShow(false);
    const id = choices[Math.floor(Math.random() * choices.length)].id;
    axios
      .get(`/api/randomchoices/${id}/`)
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
        <Select
          multiple={true}
          alwaysFilled={true}
          value={randomChoices}
          onChange={setChoices}
        />
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
