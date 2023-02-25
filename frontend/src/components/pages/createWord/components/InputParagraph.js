import InputFields from "./InputFields";
import React from "react";

function InputParagraph(params) {
  const [show, setShow] = React.useState(true);

  return (
    <div>
      <div style={{ display: "flex", width: "100%" }}>
        <div style={{ textAlign: "center", width: "100%" }}>{params.name}</div>
        <button
          style={{ width: "25px", cursor: "pointer" }}
          tabIndex="-1"
          onClick={() => setShow(!show)}
        >
          {show ? "-" : "+"}
        </button>
      </div>
      <div style={{ display: show ? "block" : "none" }}>
        {params.list.map((l, i) => (
          <InputFields {...params} {...l} key={i} i={i} />
        ))}
      </div>
    </div>
  );
}

export default InputParagraph;
