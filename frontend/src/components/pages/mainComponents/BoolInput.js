import className from "classnames";
import style from "./style.scss";
import React from "react";

const cx = className.bind(style);

function BoolInput(props) {
  const [data, setData] = React.useState(false);

  React.useEffect(() => {
    setData(props.default || false);
  }, [props.value, props.data]);

  const changeHandler = (e) => {
    setData(e.target.value);
  };

  return (
    <div className={cx("field")}>
      <div className={cx("label")}>{props.text}</div>
      <div
        className={cx("check", { checked: data })}
        onClick={() => setData(!data)}
      />
      <input hidden={true} name={props.name} defaultValue={data} />
    </div>
  );
}

export default BoolInput;
