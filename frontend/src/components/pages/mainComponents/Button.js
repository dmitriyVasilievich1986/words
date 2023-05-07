import className from "classnames";
import style from "./style.scss";
import React from "react";

const cx = className.bind(style);

function Button(props) {
  const [disabled, setDisabled] = React.useState(false);
  const clickHandler = (e) => {
    if (disabled) {
      e.preventDefault();
    } else {
      setDisabled(true);
      setTimeout(() => setDisabled(false), 1000);
    }
    if (props?.clickHandler) props.clickHandler();
  };

  return (
    <button
      className={cx("button", { disabled })}
      disabled={props?.disabled}
      onClick={clickHandler}
    >
      {props.text}
    </button>
  );
}

export default Button;
