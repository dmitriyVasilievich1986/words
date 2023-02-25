import React from "react";

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
    <div
      style={{
        display: "flex",
        width: "100%",
        justifyContent: "space-evenly",
        margin: "10px 0",
      }}
    >
      <div
        style={{
          width: "40%",
          display: "flex",
          justifyContent: "space-between",
        }}
      >
        {params.wordText}
        <input
          value={params.word}
          style={{ width: "150px" }}
          name="word"
          onChange={changeHandler}
        />
      </div>
      <div
        style={{
          width: "40%",
          display: "flex",
          justifyContent: "space-between",
        }}
      >
        {params.translateText}
        <input
          style={{ width: "150px" }}
          value={params.translate}
          onChange={changeHandler}
          name="translate"
        />
      </div>
    </div>
  );
}

export default InputFields;
