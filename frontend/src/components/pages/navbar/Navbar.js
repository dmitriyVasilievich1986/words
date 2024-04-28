import { NavLink } from "react-router-dom";
import classnames from "classnames/bind";
import style from "./style.scss";
import React from "react";

const cx = classnames.bind(style);

function Navbar() {
  return (
    <div className={cx("navbar")}>
      <div className={cx("side")} />
      <div className={cx("center")}>
        <NavLink
          className={({ isActive }) => cx("nav-link", { isActive })}
          to="/"
        >
          HOME
        </NavLink>
        {process.env.NODE_ENV === "development" && (
          <NavLink
            className={({ isActive }) => cx("nav-link", { isActive })}
            to="/create/verb"
          >
            CREATE
          </NavLink>
        )}
      </div>
      <div className={cx("side")} />
    </div>
  );
}

export default Navbar;
