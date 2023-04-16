import { TextInput, BoolInput, Select, Button } from "../mainComponents";
import className from "classnames";
import style from "./style.scss";
import React from "react";
import axios from "axios";

const cx = className.bind(style);
const initialWord = { id: 0, word: "new word", translate: "", base: "" };

function CreateWordPage() {
  const [wordList, setWordList] = React.useState([initialWord]);
  const [newWord, setNewWord] = React.useState(initialWord);
  const [models, setModels] = React.useState(null);
  const [word, setWord] = React.useState(null);
  const [data, setData] = React.useState([]);

  React.useEffect(() => {
    axios
      .get("/api/model/")
      .then((data) => {
        setWord(data.data[0].id);
        setModels(data.data);
      })
      .catch((e) => console.log(e));
  }, []);

  React.useEffect(() => {
    if (word === null) return;
    setNewWord(initialWord);
    axios
      .get(`${models[word].url}model/`)
      .then((data) => {
        setData(data.data);
      })
      .catch((e) => console.log(e));
    axios
      .get(`${models[word].url}`)
      .then((data) => {
        setWordList([newWord, ...data.data]);
      })
      .catch((e) => console.log(e));
  }, [word]);

  const postData = (submitData) => {
    axios
      .post(models[word].url, submitData)
      .then((data) => {
        setWordList([...wordList, data.data]);
        setNewWord(initialWord);
      })
      .catch((e) => {
        console.log(e);
      });
  };

  const patchData = (submitData) => {
    axios
      .patch(`${models[word].url}${newWord.id}/`, submitData)
      .then((data) => {
        setWordList(wordList.map((w) => (w.id == newWord.id ? data.data : w)));
        setNewWord(initialWord);
      })
      .catch((e) => {
        console.log(e);
      });
  };

  const submitHandler = (e) => {
    const getValue = (v) => {
      if (v.includes(",")) return v.split(",").map((x) => Number(x));
      else if (["false", "true"].includes(v)) return v == "true";
      else if (!isNaN(v)) return Number(v) || [];
      return v;
    };
    e.preventDefault();
    const submitData = {};
    Array.from(e.target.getElementsByTagName("input")).map((i) => {
      submitData[i.name] = getValue(i.value);
    });
    if (newWord.id == 0) postData(submitData);
    else patchData(submitData);
  };

  const WordConstructor = (props) => {
    switch (props.component) {
      case "choiceInput":
        return <Select {...props} default={newWord[props.name]} />;
      case "boolInput":
        return <BoolInput {...props} default={newWord[props.name]} />;
      default:
        return <TextInput {...props} default={newWord[props.name]} />;
    }
  };

  if (models === null) return null;
  return (
    <div className={cx("create-word-window")}>
      <div className={cx("wrapper")}>
        <Select value={models} onChange={(e) => setWord(e[0].id)} />
        <form onSubmit={submitHandler}>
          <div style={{ textAlign: "center" }}>"{newWord.word}"</div>
          <div>
            {data.map((d, i) => (
              <WordConstructor key={i} {...d} />
            ))}
          </div>
          <Button text={newWord.id == 0 ? "Send" : "Update"} />
        </form>
        <Select value={wordList} onChange={(v) => setNewWord(v[0])} />
      </div>
    </div>
  );
}

export default CreateWordPage;
