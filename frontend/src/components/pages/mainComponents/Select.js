import className from "classnames";
import style from "./style.scss";
import picture from "./bin.png";
import React from "react";

const cx = className.bind(style);

function Select(props) {
  const [show, setShow] = React.useState(false);
  const [data, setData] = React.useState([]);
  const windowRef = React.useRef();

  React.useEffect(() => {
    if (Array.isArray(props.default) && props.default.length > 0)
      setData(props.default);
    else setData(props.multiple ? [] : [props.value[0].id]);
  }, [props.value]);

  React.useEffect(() => {
    function handleClickOutside(event) {
      if (windowRef.current && !windowRef.current.contains(event.target)) {
        setShow(false);
      }
    }
    document.addEventListener("mousedown", handleClickOutside);
    return () => {
      document.removeEventListener("mousedown", handleClickOutside);
    };
  }, [windowRef]);

  const clickHandler = (ID) => {
    let newData = [];
    if (props.multiple) {
      if (data.includes(ID)) {
        newData = data.filter((d) => d !== ID);
      } else {
        newData = [...data, ID];
      }
    } else {
      newData = [ID];
    }
    setData(newData);
    if (!props.multiple) setShow(false);
    if (props.onChange) {
      const values = props.value.filter((v) => newData.includes(v.id));
      props.onChange(values);
    }
  };

  return (
    <div className={cx("field")}>
      {props.text && <div className={cx("label")}>{props.text}</div>}
      <div className={cx("select-window", "input")} ref={windowRef}>
        <div className={cx("head")} onClick={() => setShow(!show)}>
          {props.value
            .filter((v) => data.includes(v.id))
            .map((v) => v.word)
            .join() || "empty"}
        </div>
        <div className={cx("options-window", { show })}>
          <div className={cx("innner-space")}>
            {props.value.map((d) => (
              <div
                className={cx({ active: data.includes(d.id) })}
                onClick={() => clickHandler(d.id)}
                key={d.id}
              >
                {d.word}
              </div>
            ))}
          </div>
        </div>
        <input hidden={true} name={props.name} defaultValue={data} />
      </div>
      {props.multiple && <img src={picture} onClick={() => setData([])} />}
    </div>
  );
}

export default Select;
