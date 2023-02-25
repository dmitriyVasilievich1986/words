import InputFields from "./InputFields";
import className from "classnames";
import style from "./style.scss";
import React from "react";

const cx = className.bind(style);

function InputParagraph(params) {
  const [show, setShow] = React.useState(true);

  return (
    <div className={cx("input-paragraph-card")}>
      <div className={cx("head")}>
        <div>{params.name}</div>
        <button tabIndex="-1" onClick={() => setShow(!show)}>
          {show ? "-" : "+"}
        </button>
      </div>
      <div className={cx("body", { show })}>
        {params.list.map((l, i) => (
          <InputFields {...params} {...l} key={i} i={i} />
        ))}
      </div>
    </div>
  );
}

export default InputParagraph;
