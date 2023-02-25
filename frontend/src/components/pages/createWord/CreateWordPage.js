import { getInitState, InputParagraph, getRequest } from "./components";
import { connect, useDispatch } from "react-redux";
import { setState } from "Reducers/wordReducer";
import className from "classnames";
import { WORDS } from "Constants";
import style from "./style.scss";
import React from "react";
import axios from "axios";

const cx = className.bind(style);

function CreateWordPage(props) {
  const [data, setData] = React.useState(getInitState(WORDS.verbInfinitive));
  const [word, setWord] = React.useState(WORDS.verbInfinitive);
  const [selectedWord, setSelectedWord] = React.useState(
    props[WORDS.verbInfinitive][0].id
  );

  const dispatch = useDispatch();

  const changeHanler = (e) => {
    const newValue = e.target.value;
    setData(getInitState(newValue));
    setWord(newValue);
  };

  const wordSelectHandler = (e) => {
    const newID = e.target.value;
    axios
      .get(`/api/${word.toLowerCase()}/${newID}/`)
      .then((data) => {
        setData(getInitState(word, data.data));
        setSelectedWord(e.target.value);
        console.log(data.data);
      })
      .catch((e) => console.log(e));
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
    <div className={cx("create-page-card")}>
      <div className={cx("side")}>
        <div>
          <select value={word} onChange={changeHanler}>
            {Object.keys(WORDS).map((w) => (
              <option value={w} key={w}>
                {w}
              </option>
            ))}
          </select>
        </div>
      </div>
      <div className={cx("center")}>
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
          <div className={cx("button-wrapper")}>
            <button onClick={clickHandler}>send</button>
          </div>
        </div>
      </div>
      <div className={cx("side")}>
        <div>
          <select value={selectedWord} onChange={wordSelectHandler}>
            {props[word].map((w) => (
              <option value={w.id} key={w.id}>
                {w.word}
              </option>
            ))}
          </select>
        </div>
      </div>
    </div>
  );
}

const mapStateToProps = (state) => ({
  verbInfinitive: state.words.verbInfinitive,
  nounInfinitive: state.words.nounInfinitive,
});

export default connect(mapStateToProps)(CreateWordPage);
