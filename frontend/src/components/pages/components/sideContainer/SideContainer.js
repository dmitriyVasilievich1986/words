import classnames from "classnames/bind";
import style from "./style.scss";
import React from "react";

const cx = classnames.bind(style);

function SideContainer({ className = "", ...props }) {
  return (
    <div className={cx("container")}>
      <div className={cx(...className.split(" "))}>{props.children}</div>
    </div>
  );
}

export default SideContainer;
