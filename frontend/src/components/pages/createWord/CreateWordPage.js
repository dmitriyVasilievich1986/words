import { useSelector, useDispatch } from "react-redux";
import { setState } from "Reducers/wordReducer";
import store from "Reducers/store";
import { WORDS } from "Constants";
import React from "react";
import axios from "axios";

function InputFields(params) {
  const changeHandler = (e) => {
    if (params.name === "Base") {
      const newData = {};
      Object.keys(params.data).map((k) => {
        newData[k] = params.data[k].map((d) => ({
          ...d,
          [e.target.name]: e.target.value,
        }));
      });
      params.setData(newData);
    } else {
      const newList = params.data[params.name].map((d, i) => {
        if (i === params.i) return { ...d, [e.target.name]: e.target.value };
        return d;
      });
      params.setData({ ...params.data, [params.name]: newList });
    }
  };

  return (
    <div
      style={{
        display: "flex",
        width: "100%",
        justifyContent: "space-evenly",
        margin: "10px 0",
      }}
    >
      <div
        style={{
          width: "40%",
          display: "flex",
          justifyContent: "space-between",
        }}
      >
        {params.wordText}
        <input
          value={params.word}
          style={{ width: "150px" }}
          name="word"
          onChange={changeHandler}
        />
      </div>
      <div
        style={{
          width: "40%",
          display: "flex",
          justifyContent: "space-between",
        }}
      >
        {params.translateText}
        <input
          style={{ width: "150px" }}
          value={params.translate}
          onChange={changeHandler}
          name="translate"
        />
      </div>
    </div>
  );
}

function MyInput(params) {
  const [show, setShow] = React.useState(true);

  return (
    <div>
      <div style={{ display: "flex", width: "100%" }}>
        <div style={{ textAlign: "center", width: "100%" }}>{params.name}</div>
        <button
          style={{ width: "25px", cursor: "pointer" }}
          tabIndex="-1"
          onClick={() => setShow(!show)}
        >
          {show ? "-" : "+"}
        </button>
      </div>
      <div style={{ display: show ? "block" : "none" }}>
        {params.list.map((l, i) => (
          <InputFields {...params} {...l} key={i} i={i} />
        ))}
      </div>
    </div>
  );
}

function getInitState(word) {
  const infinitivePayload = {
    Infinitive: [
      {
        translateText: "Перевод",
        wordText: "Глагол",
        translate: "",
        word: "",
      },
    ],
  };
  const withBaseInfinitive = {
    Base: [
      {
        translateText: "Перевод",
        wordText: "Основа",
        translate: "",
        word: "",
      },
    ],
    ...infinitivePayload,
  };
  let payload = {};
  switch (word) {
    case WORDS.Verb:
      payload = { ...withBaseInfinitive };
      store.getState().words.time.map((d) => {
        const newData = store.getState().words.personalPronoun.map((pp) => ({
          translateText: pp.translate,
          wordText: pp.word,
          declention: d.id,
          pronoun: pp.id,
          translate: "",
          word: "",
        }));
        payload[d.word] = newData;
      });
      return payload;
    case WORDS.Noun:
      payload = { ...withBaseInfinitive };
      store.getState().words.declentions.map((d) => {
        const newData = store.getState().words.gender.map((pp) => ({
          translateText: pp.translate,
          wordText: pp.word,
          declention: d.id,
          pronoun: pp.id,
          translate: "",
          word: "",
        }));
        payload[d.word] = newData;
      });
      return payload;
    default:
      return payload;
  }
}

function getRequest(word, data) {
  switch (word) {
    case WORDS.Verb:
      const verbsKeys = Object.keys(data).filter((k) => k !== "Infinitive");
      const verbs = [];
      verbsKeys.map((k) => {
        data[k].map((d) => {
          verbs.push({
            declention: d.declention,
            translate: d.translate,
            pronoun: d.pronoun,
            word: d.word,
          });
        });
      });
      return {
        translate: data.Infinitive[0].translate,
        word: data.Infinitive[0].word,
        base: data.Infinitive[1].word,
        verb: verbs,
      };
    default:
      break;
  }
}

function CreateWordPage() {
  const verbInfinitive = useSelector((state) => state.words.verbInfinitive);
  const dispatch = useDispatch();

  const [data, setData] = React.useState(getInitState(WORDS.Verb));
  const [word, setWord] = React.useState(WORDS.Verb);

  const changeHanler = (e) => {
    const newValue = e.target.value;
    setData(getInitState(newValue));
    setWord(newValue);
  };

  const clickHandler = (_) => {
    const payload = getRequest(word, data);
    console.log(payload);
    axios
      .post("/api/verbinfinitive/", payload)
      .then((data) => {
        dispatch(setState({ verbInfinitive: [...verbInfinitive, data.data] }));
        console.log(data.data);
      })
      .catch((e) => console.log(e));
  };

  return (
    <div style={{ display: "flex", flexWrap: "wrap" }}>
      <div
        style={{
          flex: "1 300px",
          display: "flex",
          justifyContent: "center",
          margin: "2rem 0",
        }}
      >
        <div style={{ width: "250px" }}>
          <select
            value={word}
            onChange={changeHanler}
            style={{ width: "100%" }}
          >
            {Object.keys(WORDS).map((w) => (
              <option value={w} key={w}>
                {w}
              </option>
            ))}
          </select>
        </div>
      </div>
      <div
        style={{
          flex: "3 700px",
          display: "flex",
          justifyContent: "center",
        }}
      >
        <div style={{ width: "100vw", maxWidth: "700px" }}>
          <div>
            {Object.keys(data).map((k) => (
              <MyInput
                setData={setData}
                list={data[k]}
                data={data}
                name={k}
                key={k}
              />
            ))}
          </div>
          <div style={{ display: "flex", justifyContent: "center" }}>
            <button
              onClick={clickHandler}
              style={{
                border: "none",
                cursor: "pointer",
                width: "150px",
                marginTop: "2rem",
                padding: "10px 1rem",
                borderRadius: "10px",
              }}
            >
              send
            </button>
          </div>
        </div>
      </div>
      <div style={{ flex: "1 300px" }} />
    </div>
  );
}

export default CreateWordPage;
