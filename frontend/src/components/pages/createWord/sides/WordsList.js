import classnames from "classnames/bind";
import { NavLink } from "react-router-dom";
import style from "./style.scss";
import React from "react";

const cx = classnames.bind(style);

function WordsList({ infinitives }) {
  const [search, setSearch] = React.useState("");

  return (
    <div className={cx("list")}>
      <div className={cx("search")}>
        <input
          type="text"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />
      </div>
      <div className={cx("wrapper")}>
        {infinitives
          .filter(
            (i) =>
              search === "" ||
              i.word.toLowerCase().includes(search.toLowerCase()) ||
              i.translate.toLowerCase().includes(search.toLowerCase())
          )
          .map((infinitive) => (
            <div key={infinitive.id}>
              <NavLink
                className={({ isActive }) => cx({ isActive })}
                to={`/create/update/${infinitive.id}`}
              >
                {infinitive.word} / {infinitive.translate}
              </NavLink>
            </div>
          ))}
      </div>
    </div>
  );
}

export default WordsList;
