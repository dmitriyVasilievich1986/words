import className from "classnames";
import style from "./style.scss";
import picture from "./bin.png";
import React from "react";

const cx = className.bind(style);

function Select(props) {
  const [show, setShow] = React.useState(false);
  const [data, setData] = React.useState(null);
  const windowRef = React.useRef();

  const setDataToDefault = () => {
    if (Array.isArray(props.default) && props.default.length > 0)
      setData(props.default);
    else if (props.default === null) setData([-1]);
    else if (!isNaN(props.default)) setData([Number(props.default)]);
    else if (props.multiple && !props.alwaysFilled) setData([]);
    else setData([props.value[0].id]);
  };

  React.useEffect(() => {
    if (props.value.length > 0) setDataToDefault();
  }, [props.value, props.default]);

  React.useEffect(() => {
    if (props.onChange && data !== null) {
      const values = props.value.filter((v) => data.includes(v.id));
      props.onChange(values);
    }
  }, [data]);

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
        newData =
          props.alwaysFilled && data.length == 1
            ? data
            : data.filter((d) => d !== ID);
      } else {
        newData = [...data, ID];
      }
    } else {
      newData = [ID];
    }
    setData(newData);
    if (!props.multiple) setShow(false);
  };

  if (data === null) return null;
  return (
    <div className={cx("field")}>
      {props.text && <div className={cx("label")}>{props.text}</div>}
      <div className={cx("select-window", "input")} ref={windowRef}>
        <div className={cx("head")} onClick={() => setShow(!show)}>
          {props.value
            .filter((v) => data.includes(v.id))
            .map((v) => v.word)
            .join(", ") || "empty"}
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
      {props.multiple && <img src={picture} onClick={setDataToDefault} />}
    </div>
  );
}

export default Select;
