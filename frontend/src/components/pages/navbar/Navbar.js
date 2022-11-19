import { NavLink } from "react-router-dom";
import className from "classnames";
import style from "./style.scss";
import React from "react";

const cx = className.bind(style);

function Navbar() {
  return (
    <div className={cx("navbar")}>
      <div className={cx("side")} />
      <div className={cx("center")}>
        <NavLink className={cx("nav-link")} to="/">
          Home
        </NavLink>
        <NavLink className={cx("nav-link")} to="create">
          Create
        </NavLink>
      </div>
      <div className={cx("side")} />
    </div>
  );
}

export default Navbar;
