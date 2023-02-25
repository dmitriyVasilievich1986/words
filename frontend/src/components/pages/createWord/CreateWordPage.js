import { getInitState, InputParagraph, getRequest } from "./components";
import { useSelector, useDispatch } from "react-redux";
import { setState } from "Reducers/wordReducer";
import { WORDS } from "Constants";
import React from "react";
import axios from "axios";

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
    return;
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
              <InputParagraph
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
