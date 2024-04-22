import classnames from "classnames/bind";
import style from "./style.scss";
import React from "react";

const cx = classnames.bind(style);

function Card({ className = "", ...props }) {
  return (
    <div className={cx("card")}>
      <div className={cx(...className.split(" "))}>{props.children}</div>
    </div>
  );
}

export default Card;
