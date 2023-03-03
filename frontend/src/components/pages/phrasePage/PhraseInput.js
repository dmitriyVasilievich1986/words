import React from "react";

function PhraseInput(props) {
  const [value, setValue] = React.useState("");

  React.useEffect(() => {
    setValue("");
  }, [props.word]);

  React.useEffect(() => {
    if (props.show) setValue(props.word);
  }, [props.show]);

  const changeHandler = (e) => {
    const v = e.target.value.toLocaleLowerCase();
    if (v.length >= props.word.length + 1) {
      return;
    }
    setValue(v);
  };

  if (!props.hiden) {
    return <div>{props.word}</div>;
  }
  return (
    <input
      style={{ width: `${props.word.length * 13}px` }}
      disabled={value === props.word}
      onChange={changeHandler}
      value={value}
      type="text"
    />
  );
}

export default PhraseInput;
