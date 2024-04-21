import classnames from "classnames/bind";
import style from "./style.scss";
import React from "react";

const cx = classnames.bind(style);

function PhraseInput({ base, word, error }) {
  const [value, setValue] = React.useState(base);

  const changeHandler = (e) => {
    const v = e.target.value.toLocaleLowerCase();
    if (v.length >= word.length + 3 || value === word || !v.startsWith(base)) {
      return;
    }
    setValue(v);
  };

  if (word === base) return <span style={{ margin: "0 5px" }}>{word}</span>;
  return (
    <React.Fragment>
      <input
        className={cx({ isCorrect: value === word, error })}
        style={{ width: `${word.length * 10}px` }}
        value={error ? word : value}
        onChange={changeHandler}
        autoCapitalize="none"
        autoComplete="off"
        autoCorrect="off"
        autoFocus={true}
        type="text"
      />
      {!error && value !== word && (
        <input type="hidden" name="isNotComplited" />
      )}
    </React.Fragment>
  );
}

export default PhraseInput;
