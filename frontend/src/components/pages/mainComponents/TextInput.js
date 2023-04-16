import className from "classnames";
import style from "./style.scss";
import React from "react";

const cx = className.bind(style);

function TextInput(props) {
  const [data, setData] = React.useState("");

  React.useEffect(() => {
    setData(props.default || "");
  }, [props.value, props.data]);

  const changeHandler = (e) => {
    setData(e.target.value);
  };

  return (
    <div className={cx("field")}>
      <div className={cx("label")}>{props.text}</div>
      <div className={cx("input")}>
        <input
          onChange={changeHandler}
          placeholder={props.name}
          name={props.name}
          value={data}
          type="text"
        />
      </div>
    </div>
  );
}

export default TextInput;
