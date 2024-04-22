import classnames from "classnames/bind";
import style from "./style.scss";
import React from "react";

const cx = classnames.bind(style);

function Delimiter({ className = "" }) {
  return (
    <div className={cx("delimiter")}>
      <div className={cx(...className.split(" "))} />
    </div>
  );
}

export default Delimiter;
