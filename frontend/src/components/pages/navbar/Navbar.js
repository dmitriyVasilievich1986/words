import { NavLink } from "react-router-dom";
import classnames from "classnames/bind";
import style from "./style.scss";
import PAGES from "Pages";
import React from "react";

const cx = classnames.bind(style);

function Navbar() {
  return (
    <div className={cx("navbar")}>
      <div className={cx("side")} />
      <div className={cx("center")}>
        {PAGES.filter((p) => !p.hiden).map((p) => (
          <NavLink className={cx("nav-link")} to={p.path} key={p.name}>
            {p.name}
          </NavLink>
        ))}
      </div>
      <div className={cx("side")} />
    </div>
  );
}

export default Navbar;
