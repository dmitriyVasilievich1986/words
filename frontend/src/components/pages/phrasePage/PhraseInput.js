import classnames from "classnames/bind";
import style from "./style.scss";
import React from "react";

const cx = classnames.bind(style);

function PhraseInput({ base, word }) {
  const [value, setValue] = React.useState(base);

  const changeHandler = (e) => {
    const v = e.target.value.toLocaleLowerCase();
    if (v.length >= word.length + 3 || value === word || !v.startsWith(base)) {
      return;
    }
    setValue(v);
  };

  if (word === base) return <span>{word}</span>;
  return (
    <input
      className={cx({ isCorrect: value === word })}
      style={{ width: `${word.length * 10}px` }}
      onChange={changeHandler}
      autoCapitalize="none"
      autoComplete="off"
      autoCorrect="off"
      value={value}
      type="text"
    />
  );
}

export default PhraseInput;
