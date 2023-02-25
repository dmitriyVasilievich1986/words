import className from "classnames";
import style from "./style.scss";
import React from "react";

const cx = className.bind(style);

function InputFields(params) {
  const changeHandler = (e) => {
    if (params.name === "Base") {
      const newData = {};
      Object.keys(params.data).map((k) => {
        newData[k] = params.data[k].map((d) => ({
          ...d,
          [e.target.name]: e.target.value,
        }));
      });
      params.setData(newData);
    } else {
      const newList = params.data[params.name].map((d, i) => {
        if (i === params.i) return { ...d, [e.target.name]: e.target.value };
        return d;
      });
      params.setData({ ...params.data, [params.name]: newList });
    }
  };

  return (
    <div className={cx("input-field-card")}>
      <div>
        {params.wordText}
        <input onChange={changeHandler} value={params.word} name="word" />
      </div>
      <div>
        {params.translateText}
        <input
          value={params.translate}
          onChange={changeHandler}
          name="translate"
        />
      </div>
    </div>
  );
}

export default InputFields;
