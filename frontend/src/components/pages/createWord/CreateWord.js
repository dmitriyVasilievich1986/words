import { useSearchParams } from "react-router-dom";
import { Select } from "../mainComponents";
import classnames from "classnames/bind";
import { Card } from "../components";
import style from "./style.scss";
import React from "react";
import axios from "axios";

const cx = classnames.bind(style);

function CreateWord(props) {
  const [selectedPartOfSpeech, setSelectedPartOfSpeech] = React.useState(null);
  const [partsOfSpeech, setPartsOfSpeech] = React.useState([]);
  const [searchParams, setSearchParams] = useSearchParams();
  const [translate, setTranslate] = React.useState("");
  const [word, setWord] = React.useState("");

  React.useEffect(() => {
    props.setTags([]);
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
      part_of_speech: selectedPartOfSpeech.id,
      tags: props.tags,
      translate,
      word,
    };
    axios
      .post("/api/infinitive/", data)
      .then((response) => {
        props.setInfinitives((prev) => [...prev, response.data]);
        setTranslate("");
        setWord("");
        setSearchParams({ infinitive: response.data.id });
      })
      .catch((error) => {
        console.log(error);
      });
    event.target.reset();
  };

  if (partsOfSpeech.length === 0) return <div>loading...</div>;
  return (
    <div>
      <form onSubmit={submitHandler}>
        <div className={cx("send-button")} style={{ marginBottom: "2rem" }}>
          <Select
            options={partsOfSpeech.map((p) => ({ ...p, word: p.translate }))}
            onChange={setSelectedPartOfSpeech}
            value={selectedPartOfSpeech.id}
            isNullable={false}
          />
        </div>
        <Card>
          <div className={cx("input-wrapper")}>
            <div className={cx("input-row")}>
              <label>Слово:</label>
              <input
                type="text"
                value={word}
                autoCorrect="off"
                placeholder="Слово"
                autoCapitalize="none"
                onChange={(e) => setWord(e.target.value.toLowerCase())}
              />
            </div>
            <div className={cx("input-row")}>
              <label>Перевод:</label>
              <input
                type="text"
                value={translate}
                autoCorrect="off"
                autoCapitalize="none"
                placeholder="Перевод"
                onChange={(e) => setTranslate(e.target.value.toLowerCase())}
              />
            </div>
          </div>
        </Card>
        <div className={cx("send-button")}>
          <button>сохранить</button>
        </div>
      </form>
    </div>
  );
}

export default CreateWord;
