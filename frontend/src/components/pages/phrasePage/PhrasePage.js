import { useSelector } from "react-redux";
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

  const sendAPIRequest = () => {
    axios
      .get(`/api/randomchoices/${selectValue}/`)
      .then((data) => setPhrase(data.data))
      .catch((e) => console.log(e));
  };

  React.useEffect(() => {
    sendAPIRequest();
  }, [randomChoices, selectValue]);

  if (randomChoices.length === 0 || phrase === null) return null;
  return (
    <div style={{ display: "flex", flexFlow: "row", flexWrap: "wrap" }}>
      <div style={{ flex: "1 300px" }}>
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
      <div style={{ flex: "3 700px" }}>
        <div style={{ display: "flex" }}>
          {phrase.map((w, i) => (
            <PhraseInput {...w} key={i} />
          ))}
        </div>
        <br />
        {phrase.map((w) => w.translate)}
        <br />

        <button onClick={sendAPIRequest}>next</button>
      </div>
      <div style={{ flex: "1 300px" }}>right</div>
    </div>
  );
}

export default PhrasePage;
