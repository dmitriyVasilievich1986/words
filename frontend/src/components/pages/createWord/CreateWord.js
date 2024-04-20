import { Select } from "../mainComponents";
import className from "classnames";
import style from "./style.scss";
import React from "react";
import axios from "axios";

const cx = className.bind(style);

function CreateWord(params) {
  const [selectedPartOfSpeech, setSelectedPartOfSpeech] = React.useState(null);
  const [partsOfSpeech, setPartsOfSpeech] = React.useState([]);

  React.useEffect(() => {
    axios
      .get("/api/partsofspeech/")
      .then((response) => {
        setSelectedPartOfSpeech(response.data[0]);
        setPartsOfSpeech(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  const submitHandler = (event) => {
    event.preventDefault();
    const data = {
      word: event.target.word.value,
      translate: event.target.translate.value,
      part_of_speech: selectedPartOfSpeech.id,
    };
    axios
      .post("/api/infinitive/", data)
      .then((response) => {
        params.setInfinitives((prev) => [...prev, response.data]);
      })
      .catch((error) => {
        console.log(error);
      });
    event.target.reset();
  };

  if (partsOfSpeech.length === 0) return <div>loading...</div>;
  return (
    <div className={cx("container")}>
      <form onSubmit={submitHandler}>
        <div className={cx("send-button")} style={{ marginBottom: "2rem" }}>
          <Select
            options={partsOfSpeech}
            value={selectedPartOfSpeech.id}
            onChange={setSelectedPartOfSpeech}
          />
        </div>
        <div className={cx("input-wrapper")}>
          <div className={cx("input-row")}>
            <label>word</label>
            <input type="text" name="word" placeholder="word" />
          </div>
          <div className={cx("input-row")}>
            <label>translate</label>
            <input type="text" name="translate" placeholder="translate" />
          </div>
        </div>
        <div className={cx("send-button")}>
          <button>send</button>
        </div>
      </form>
    </div>
  );
}

export default CreateWord;
