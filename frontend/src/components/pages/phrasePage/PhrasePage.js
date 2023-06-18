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

  const [selectedTags, setSelectedTags] = React.useState([]);
  const [choices, setChoices] = React.useState([]);
  const [phrase, setPhrase] = React.useState([]);
  const [tags, setTags] = React.useState([]);

  const [show, setShow] = React.useState(false);
  const currentChoice = React.useRef(null);

  const sendAPIRequest = () => {
    if (choices.length === 0) {
      if (tags.length) {
        setSelectedTags([]);
        setTags([]);
      }
      return;
    }
    setShow(false);
    const postData = {
      random_choices: choices,
      params: {
        tags: selectedTags,
      },
    };
    axios
      .post("/api/randomchoices/", postData)
      .then((data) => {
        setPhrase(data.data.answer_list);
        setTags(data.data.tags);
      })
      .catch((e) => console.log(e));
  };

  React.useEffect(() => {
    sendAPIRequest();
  }, [randomChoices, choices, selectedTags]);

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

  if (randomChoices.length === 0) return null;
  return (
    <div className={cx("phrase-page-card")}>
      <div className={cx("side")}>
        <div>
          <Select
            onChange={(v) => setChoices(v)}
            name="Часть речи / выражение"
            options={randomChoices}
            value={choices}
            multiple={true}
          />
        </div>
        <div>
          {tags.length > 0 && (
            <Select
              onChange={(v) => setSelectedTags(v)}
              value={selectedTags}
              multiple={true}
              options={tags}
              name="Тэги"
            />
          )}
        </div>
      </div>

      <div className={cx("center")}>
        {choices.length > 0 && phrase.length > 0 && (
          <div className={cx("wrapper")} onClick={clickHandler}>
            <div>{currentChoice.current?.description || ""}</div>
            <div>"{phrase.map((w) => w.translate)}"</div>
            <div className={cx("phrase-row")} id="phrase">
              {phrase.map((w, i) => (
                <PhraseInput {...w} key={i} show={show} />
              ))}
            </div>
          </div>
        )}
      </div>

      <div className={cx("side")} />
    </div>
  );
}

export default PhrasePage;
