import { Select, Button } from "../mainComponents";
import className from "classnames";
import style from "./style.scss";
import React from "react";
import axios from "axios";

const cx = className.bind(style);
const initialWord = { id: 0, word: "new word", translate: "", base: "" };

function CreateWordPage() {
  const [selectedPartOfSpeech, setSelectedPartOfSpeech] = React.useState(null);
  const [wordsList, setWordsList] = React.useState([initialWord]);
  const [partsOfSpeech, setPartsOfSpeech] = React.useState(null);
  const [selectedWord, setSelectedWord] = React.useState(null);
  const [wordModel, setWordModel] = React.useState([]);

  const [postData, dispatch] = React.useReducer(function (state, action) {
    return { ...state, ...action };
  }, {});

  React.useEffect(() => {
    axios
      .get("/api/model/")
      .then((data) => {
        setPartsOfSpeech(data.data);
        setSelectedPartOfSpeech(data.data[0]);
      })
      .catch((e) => console.log(e));
  }, []);

  React.useEffect(() => {
    if (selectedPartOfSpeech === null) return;
    axios
      .get(`${selectedPartOfSpeech.url}model/`)
      .then((data) => {
        dispatch(Object.fromEntries(data.data.map((v) => [v.name, v.data])));
        setWordModel(data.data);
      })
      .catch((e) => console.log(e));
    axios
      .get(`${selectedPartOfSpeech.url}`)
      .then((data) => {
        setWordsList(data.data);
      })
      .catch((e) => console.log(e));
  }, [selectedPartOfSpeech]);

  const dispatchWord = (word) => {
    dispatch(
      Object.fromEntries(
        Object.keys(word)
          .filter((k) => k !== "id")
          .map((k) => [k, word[k]])
      )
    );
  };

  const sendPostRequest = () => {
    axios
      .post(selectedPartOfSpeech.url, postData)
      .then((data) => {
        setWordsList([...wordsList, data.data]);
        dispatchWord(data.data);
        setSelectedWord(data.data);
      })
      .catch((e) => {
        console.log(e);
      });
  };

  const sendPatchRequest = () => {
    axios
      .patch(`${selectedPartOfSpeech.url}${selectedWord.id}/`, postData)
      .then((data) => {
        setWordsList(
          wordsList.map((w) => (w.id == selectedWord.id ? data.data : w))
        );
        dispatchWord(data.data);
      })
      .catch((e) => {
        console.log(e);
      });
  };

  const submitHandler = (e) => {
    e.preventDefault();
  };

  if (!selectedPartOfSpeech) return null;
  return (
    <div className={cx("create-word-window")}>
      <div className={cx("wrapper")}>
        <div
          style={{ width: "100%", display: "flex", justifyContent: "center" }}
        >
          <Select
            onChange={(p) => {
              if (p !== null) {
                setSelectedWord(null);
                setSelectedPartOfSpeech(
                  partsOfSpeech.find((ps) => ps.id === p)
                );
              }
            }}
            value={selectedPartOfSpeech.id}
            options={partsOfSpeech}
          />
        </div>
        <form onSubmit={submitHandler}>
          <div style={{ textAlign: "center" }}>
            "{selectedWord?.word || "New Word"}"
          </div>
          <div>
            {wordModel.map((d, i) => {
              switch (d.component) {
                case "textInput":
                  return (
                    <div
                      className={cx("field-row")}
                      key={`${selectedPartOfSpeech.word}_${d.name}`}
                    >
                      <span>{d.name}:</span>
                      <input
                        type="text"
                        key={d.name}
                        className={cx("input")}
                        value={postData[d.name]}
                        onChange={(e) => dispatch({ [d.name]: e.target.value })}
                      />
                    </div>
                  );
                case "boolInput":
                  return (
                    <div
                      className={cx("field-row")}
                      key={`${selectedPartOfSpeech.word}_${d.name}`}
                    >
                      <span>{d.name}:</span>
                      <div
                        style={{
                          width: "70%",
                          display: "flex",
                          justifyContent: "center",
                        }}
                      >
                        <input
                          key={d.name}
                          type="checkbox"
                          value={postData[d.name]}
                          onChange={(e) =>
                            dispatch({ [d.name]: e.target.value })
                          }
                        />
                      </div>
                    </div>
                  );
                case "choiceInput":
                  return (
                    <div
                      className={cx("field-row")}
                      key={`${selectedPartOfSpeech.word}_${d.name}`}
                    >
                      <span>{d.name}:</span>
                      <Select
                        options={d.value}
                        multiple={d?.multiple}
                        value={postData[d.name]}
                        onChange={(v) => dispatch({ [d.name]: v })}
                      />
                    </div>
                  );
                default:
                  return null;
              }
            })}
          </div>
          <div style={{ display: "flex", justifyContent: "center" }}>
            <Button text={"Send"} clickHandler={sendPostRequest} />
            <Button
              text={"Update"}
              clickHandler={sendPatchRequest}
              disabled={selectedWord?.id === undefined}
            />
          </div>
        </form>
        <div style={{ display: "flex", justifyContent: "center" }}>
          <Select
            options={wordsList}
            value={selectedWord?.id}
            onChange={(v) => {
              const newValue = v && wordsList.find((wl) => wl.id === v);
              setSelectedWord(newValue);
              if (v === null) {
                dispatch(
                  Object.fromEntries(wordModel.map((wm) => [wm.name, wm.data]))
                );
              } else {
                dispatchWord(newValue);
              }
            }}
          />
        </div>
      </div>
    </div>
  );
}

export default CreateWordPage;
