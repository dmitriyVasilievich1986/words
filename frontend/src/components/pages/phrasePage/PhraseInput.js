import React from "react";

function PhraseInput(props) {
  const [value, setValue] = React.useState("");

  React.useEffect(() => {
    setValue("");
  }, [props.word]);

  const changeHandler = (e) => {
    const v = e.target.value;
    if (v.length >= props.word.length + 1) {
      return;
    }
    setValue(v);
    setFinish(v === props.word);
  };

  if (!props.hiden) {
    return (
      <div style={{ width: "fit-content", minWidth: "1rem" }}>{props.word}</div>
    );
  }
  return (
    <input
      style={{ width: `${props.word.length * 10}px` }}
      disabled={value === props.word}
      onChange={changeHandler}
      value={value}
      type="text"
    />
  );
}

export default PhraseInput;
