import React from "react";
import axios from "axios";

const WordConstructor = (props) => {
  const [data, setData] = props.dataHandler;
  const changeHandler = (e) => {
    setData(
      data.map((d) => {
        if (d.name === props.name) {
          return { ...d, data: e.target.value };
        } else {
          return d;
        }
      })
    );
  };
  if (props.component === "textInput") {
    return (
      <React.Fragment>
        <p>{props.text}</p>
        <input type="text" onChange={changeHandler} value={props.data} />
      </React.Fragment>
    );
  } else if (props.component === "choiceInput") {
    return (
      <React.Fragment>
        <p>{props.text}</p>
        <select onChange={changeHandler} value={props.data}>
          {props.value.map((v) => (
            <option key={v.id} value={v.id}>
              {v.word}
            </option>
          ))}
        </select>
      </React.Fragment>
    );
  }
};

function CreateWordPage() {
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
    axios
      .get(models[word].url)
      .then((data) => {
        setData(data.data);
      })
      .catch((e) => console.log(e));
  }, [word]);

  const clickHandler = (e) => {
    const payload = {};
    data.map((d) => {
      payload[d.name] = d.data;
    });
    console.log(payload);
  };

  if (models === null) return null;
  return (
    <div>
      <select value={word} onChange={(e) => setWord(e.target.value)}>
        {models.map((m) => (
          <option key={m.id} value={m.id}>
            {m.name}
          </option>
        ))}
      </select>
      <div>New word:</div>
      <div>
        {data.map((d, i) => (
          <WordConstructor key={i} {...d} dataHandler={[data, setData]} />
        ))}
      </div>
      <button onClick={clickHandler}>send</button>
    </div>
  );
}

export default CreateWordPage;
